#!/usr/bin/env python3
import argparse
import csv
import sys
from pathlib import Path


def as_float(value, default=0.0):
    try:
        return float(str(value or "").replace(",", "").strip())
    except ValueError:
        return default


def pick(row, names):
    lowered = {key.lower().strip(): key for key in row.keys()}
    for name in names:
        if name in lowered:
            return row.get(lowered[name], "")
    return ""


def classify(row):
    clicks = as_float(pick(row, ["clicks", "organic traffic", "traffic", "sessions"]))
    impressions = as_float(pick(row, ["impressions"]))
    position = as_float(pick(row, ["position", "avg position", "rank"]), 999)
    product_fit = pick(row, ["product fit", "product_fit", "fit"]).lower()
    intent = pick(row, ["intent", "search intent"]).lower()
    backlinks = as_float(pick(row, ["backlinks", "referring domains", "ref domains"]))
    lastmod = pick(row, ["lastmod", "last updated", "updated"])

    if product_fit in {"forced", "deceptive", "none"} and clicks < 10:
        return "prune", "low traffic and weak product fit"
    if product_fit in {"forced", "deceptive"} and clicks >= 10:
        return "rewrite", "traffic exists but product fit distorts intent"
    if clicks == 0 and impressions == 0 and backlinks == 0:
        return "prune", "no visible demand or authority signals"
    if impressions > 500 and position > 10:
        return "rewrite", "demand exists but rankings are weak"
    if clicks > 0 and not lastmod:
        return "refresh", "traffic exists but freshness is unknown"
    if "duplicate" in intent or "overlap" in intent:
        return "merge", "overlapping intent"
    return "manual-review", "insufficient signals for automatic action"


def main():
    parser = argparse.ArgumentParser(description="Classify URL portfolio rows into action buckets.")
    parser.add_argument("--input", required=True, help="Input CSV.")
    parser.add_argument("--output", required=True, help="Output CSV.")
    args = parser.parse_args()

    with Path(args.input).open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Input CSV is empty")

    fieldnames = list(rows[0].keys()) + ["recommended_action", "action_reason"]
    output_rows = []
    for row in rows:
        action, reason = classify(row)
        row = dict(row)
        row["recommended_action"] = action
        row["action_reason"] = reason
        output_rows.append(row)

    with Path(args.output).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Wrote {len(output_rows)} triage rows to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
