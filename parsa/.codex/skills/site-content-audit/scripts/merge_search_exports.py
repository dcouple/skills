#!/usr/bin/env python3
import argparse
import csv
import sys
from pathlib import Path


URL_ALIASES = {"url", "page", "landing page", "address", "loc"}
QUERY_ALIASES = {"query", "keyword", "search term", "term"}


def read_csv(path):
    with Path(path).open(newline="") as handle:
        return list(csv.DictReader(handle))


def find_column(fieldnames, aliases):
    normalized = {name.strip().lower(): name for name in fieldnames or []}
    for alias in aliases:
        if alias in normalized:
            return normalized[alias]
    return None


def normalize_url(url):
    return (url or "").strip().rstrip("/")


def main():
    parser = argparse.ArgumentParser(description="Merge URL inventory with one or more search export CSVs.")
    parser.add_argument("--urls", required=True, help="Base URL inventory CSV.")
    parser.add_argument("--exports", required=True, nargs="+", help="Search export CSV(s).")
    parser.add_argument("--output", required=True, help="Merged output CSV.")
    args = parser.parse_args()

    base_rows = read_csv(args.urls)
    if not base_rows:
        raise ValueError("URL inventory is empty")
    base_url_col = find_column(base_rows[0].keys(), URL_ALIASES)
    if not base_url_col:
        raise ValueError("Could not find URL column in base inventory")

    by_url = {normalize_url(row.get(base_url_col)): dict(row) for row in base_rows}
    extra_fields = []

    for export_path in args.exports:
        rows = read_csv(export_path)
        if not rows:
            continue
        url_col = find_column(rows[0].keys(), URL_ALIASES)
        query_col = find_column(rows[0].keys(), QUERY_ALIASES)
        if not url_col:
            raise ValueError(f"Could not find URL column in {export_path}")
        prefix = Path(export_path).stem
        for field in rows[0].keys():
            out_field = f"{prefix}_{field}"
            if out_field not in extra_fields:
                extra_fields.append(out_field)
        if query_col:
            query_field = f"{prefix}_queries"
            if query_field not in extra_fields:
                extra_fields.append(query_field)

        grouped = {}
        for row in rows:
            key = normalize_url(row.get(url_col))
            grouped.setdefault(key, []).append(row)
        for key, export_rows in grouped.items():
            target = by_url.setdefault(key, {base_url_col: key})
            first = export_rows[0]
            for field, value in first.items():
                target[f"{prefix}_{field}"] = value
            if query_col:
                target[f"{prefix}_queries"] = "; ".join(sorted({r.get(query_col, "").strip() for r in export_rows if r.get(query_col)}))

    fields = list(base_rows[0].keys()) + [field for field in extra_fields if field not in base_rows[0].keys()]
    with Path(args.output).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(by_url.values())
    print(f"Wrote {len(by_url)} merged rows to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
