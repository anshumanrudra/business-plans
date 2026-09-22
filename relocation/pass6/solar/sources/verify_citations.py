#!/usr/bin/env python3
"""Verify every legal quotation in the deliverables appears verbatim in a pinned source.

Usage:
    python3 sources/verify_citations.py            # check all
    python3 sources/verify_citations.py 03-SECTION-16b-NOTICE.md
"""
import re
import sys
from pathlib import Path

SOLAR = Path(__file__).resolve().parent.parent
SOURCES = SOLAR / "sources"

# Each later task appends to this list. Keep grouped by `doc`, ordered as the doc reads.
CITATIONS = [
    {
        "doc": "03-SECTION-16b-NOTICE.md",
        "note": "Lease 16(b) - lessor default, 90 days",
        "source": "lease.txt",
        "quote": "do not initiate a remedy of such failure within a period of ninety (90) days",
    },
    {
        "doc": "03-SECTION-16b-NOTICE.md",
        "note": "Lease 5(c)(xiii) - lessor must ensure repair",
        "source": "lease.txt",
        "quote": "ensure that the System will be repaired pursuant to the Limited Warranty",
    },
    {
        "doc": "03-SECTION-16b-NOTICE.md",
        "note": "Exhibit A 2(a)(iii) - repair at no cost",
        "source": "lease.txt",
        "quote": "at no cost or expense to you",
    },
]


def normalize(text):
    """Collapse whitespace so PDF line wrapping and markdown reflow do not cause false failures."""
    return re.sub(r"\s+", " ", text).strip()


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    cache = {}
    failures = []
    checked = 0

    for entry in CITATIONS:
        if only and entry["doc"] != only:
            continue
        needle = normalize(entry["quote"])
        for kind, path in (
            ("source", SOURCES / entry["source"]),
            ("deliverable", SOLAR / entry["doc"]),
        ):
            if path not in cache:
                cache[path] = normalize(path.read_text(encoding="utf-8")) if path.exists() else None
            haystack = cache[path]
            if haystack is None:
                failures.append(f"{entry['doc']} [{entry['note']}]: missing {kind} file {path.name}")
            elif needle not in haystack:
                failures.append(
                    f"{entry['doc']} [{entry['note']}]: quote absent from {kind} "
                    f"{path.name}\n    wanted: {needle[:100]}"
                )
        checked += 1

    if failures:
        print(f"FAIL — {len(failures)} problem(s) across {checked} citation(s):\n")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"PASS — {checked} citation(s) verified verbatim against pinned sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
