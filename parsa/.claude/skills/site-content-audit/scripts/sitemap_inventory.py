#!/usr/bin/env python3
import argparse
import csv
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


def read_source(source, timeout):
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        req = urllib.request.Request(source, headers={"User-Agent": "CodexSiteContentAudit/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()
    return Path(source).read_bytes()


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def text_of(parent, name):
    for child in parent:
        if local_name(child.tag) == name:
            return (child.text or "").strip()
    return ""


def parse_sitemap(xml_bytes):
    root = ET.fromstring(xml_bytes)
    kind = local_name(root.tag)
    rows = []
    child_sitemaps = []

    if kind == "sitemapindex":
        for item in root:
            if local_name(item.tag) != "sitemap":
                continue
            loc = text_of(item, "loc")
            if loc:
                child_sitemaps.append(loc)
        return rows, child_sitemaps

    if kind == "urlset":
        for item in root:
            if local_name(item.tag) != "url":
                continue
            loc = text_of(item, "loc")
            if loc:
                rows.append({
                    "url": loc,
                    "lastmod": text_of(item, "lastmod"),
                    "changefreq": text_of(item, "changefreq"),
                    "priority": text_of(item, "priority"),
                })
    return rows, child_sitemaps


def write_rows(rows, output, fmt):
    if fmt == "json":
        Path(output).write_text(json.dumps(rows, indent=2) + "\n")
        return
    with Path(output).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["url", "lastmod", "changefreq", "priority", "source_sitemap"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Parse sitemap XML into URL inventory CSV/JSON.")
    parser.add_argument("--input", required=True, help="Sitemap XML file or URL.")
    parser.add_argument("--output", required=True, help="Output CSV or JSON path.")
    parser.add_argument("--format", choices=["csv", "json"], default="csv")
    parser.add_argument("--follow-index", action="store_true", help="Fetch child sitemaps from a sitemap index.")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    pending = [args.input]
    seen = set()
    all_rows = []

    while pending:
        source = pending.pop(0)
        if source in seen:
            continue
        seen.add(source)
        xml_bytes = read_source(source, args.timeout)
        rows, children = parse_sitemap(xml_bytes)
        for row in rows:
            row["source_sitemap"] = source
            all_rows.append(row)
        if args.follow_index:
            pending.extend(children)

    write_rows(all_rows, args.output, args.format)
    print(f"Wrote {len(all_rows)} URLs to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
