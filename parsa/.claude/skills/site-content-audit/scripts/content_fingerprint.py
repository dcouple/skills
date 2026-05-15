#!/usr/bin/env python3
import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


CTA_PATTERNS = [
    r"\btry\b",
    r"\bget started\b",
    r"\bsign up\b",
    r"\bbook a demo\b",
    r"\bdownload\b",
    r"\bstart free\b",
    r"\bfree trial\b",
    r"\bpricing\b",
]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.headings = []
        self.links = []
        self.schema_scripts = []
        self._tag = None
        self._buffer = []
        self._script_type = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"title", "h1", "h2", "h3", "script", "a"}:
            self._tag = tag
            self._buffer = []
            self._script_type = attrs.get("type", "")
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_data(self, data):
        if self._tag:
            self._buffer.append(data)

    def handle_endtag(self, tag):
        if tag != self._tag:
            return
        text = " ".join(" ".join(self._buffer).split())
        if tag == "title":
            self.title = text
        elif tag in {"h1", "h2", "h3"}:
            self.headings.append({"level": tag, "text": text})
        elif tag == "script" and self._script_type == "application/ld+json":
            self.schema_scripts.append(text)
        self._tag = None
        self._buffer = []
        self._script_type = ""


def read_source(source, timeout):
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        req = urllib.request.Request(source, headers={"User-Agent": "CodexSiteContentAudit/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    return Path(source).read_text(errors="replace")


def count_patterns(text, patterns):
    lowered = text.lower()
    return {pattern: len(re.findall(pattern, lowered)) for pattern in patterns}


def analyze(source, html, product_terms):
    parser = PageParser()
    parser.feed(html)
    visible_text = re.sub(r"<[^>]+>", " ", html)
    visible_text = " ".join(visible_text.split())
    heading_texts = [h["text"] for h in parser.headings]
    repeated_headings = sorted({h for h in heading_texts if heading_texts.count(h) > 1 and h})
    schema_text = "\n".join(parser.schema_scripts)
    unresolved_schema_tokens = sorted(set(re.findall(r"\{[^{}]{1,40}\}|\bYEAR\b|\byear\b", schema_text)))
    product_counts = count_patterns(visible_text, [re.escape(term.lower()) for term in product_terms])

    return {
        "source": source,
        "title": parser.title,
        "h1_count": sum(1 for h in parser.headings if h["level"] == "h1"),
        "h2_count": sum(1 for h in parser.headings if h["level"] == "h2"),
        "h3_count": sum(1 for h in parser.headings if h["level"] == "h3"),
        "repeated_headings": repeated_headings,
        "cta_counts": count_patterns(visible_text, CTA_PATTERNS),
        "product_term_counts": product_counts,
        "schema_script_count": len(parser.schema_scripts),
        "unresolved_schema_tokens": unresolved_schema_tokens,
        "internal_link_like_count": sum(1 for href in parser.links if href.startswith("/") or "#" not in href),
        "word_count_estimate": len(re.findall(r"\w+", visible_text)),
    }


def main():
    parser = argparse.ArgumentParser(description="Fingerprint HTML for editorial, CTA, and template signals.")
    parser.add_argument("--input", required=True, nargs="+", help="HTML file(s) or URL(s).")
    parser.add_argument("--output", required=True, help="Output JSON path.")
    parser.add_argument("--product-term", action="append", default=[], help="Product or brand term to count. Repeatable.")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    rows = []
    for source in args.input:
        html = read_source(source, args.timeout)
        rows.append(analyze(source, html, args.product_term))
    Path(args.output).write_text(json.dumps(rows, indent=2) + "\n")
    print(f"Wrote {len(rows)} fingerprints to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
