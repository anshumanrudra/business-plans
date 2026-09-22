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
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a - agreement not effective, fully completed",
        "source": "ct740-home-solicitation.txt",
        "quote": "No agreement in a home solicitation sale shall be effective against the buyer",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(1) - fully completed receipt",
        "source": "ct740-home-solicitation.txt",
        "quote": "Fail to furnish the buyer with a fully completed receipt or copy of all contracts",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-134a(a) - lease of consumer goods, personally solicits",
        "source": "ct740-home-solicitation.txt",
        "quote": "means a sale, lease, or rental of consumer goods or services",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-137(c) - effective if indicates intention not to be bound",
        "source": "ct740-home-solicitation.txt",
        "quote": "it indicates the intention on the part of the buyer not to be bound",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-138(a) - tender payments within ten business days",
        "source": "ct740-home-solicitation.txt",
        "quote": "the seller shall tender to the buyer any payments made by the buyer",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-139(a) - goods become property of buyer after twenty days",
        "source": "ct740-home-solicitation.txt",
        "quote": "the goods shall become the property of the buyer without obligation to pay for them",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-139(a) - tender at own address only",
        "source": "ct740-home-solicitation.txt",
        "quote": "he is not obligated to tender at any place other than his own address",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-139(c) - seller entitled to no compensation for services",
        "source": "ct740-home-solicitation.txt",
        "quote": "the seller is entitled to no compensation",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "Exhibit C - security interest will be canceled",
        "source": "lease.txt",
        "quote": "any security interest arising out of the transaction will be canceled",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "Exhibit C - retain goods if not picked up in twenty days",
        "source": "lease.txt",
        "quote": "you may retain or dispose of the goods without any further obligation",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "4(e) carve-out for applicable law and Section 28",
        "source": "lease.txt",
        "quote": "EXCEPT AS REQUIRED BY APPLICABLE LAW",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "19 - JAMS, Streamlined Rules, governing law",
        "source": "lease.txt",
        "quote": "administered by JAMS, under its Streamlined Arbitration Rules",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "19 - claimant pays first $125",
        "source": "lease.txt",
        "quote": "you will be required to pay the first $125 of any filing fee",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "19 - arbitrator may award any legal or equitable remedy",
        "source": "lease.txt",
        "quote": "authority to award any legal or equitable remedy or relief that a court could order or grant",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "2 - Lease Term Start Date is interconnection approval",
        "source": "lease.txt",
        "quote": "is the date upon which your utility approves interconnection of the System",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "5(a)(ix) - personal family household purposes",
        "source": "lease.txt",
        "quote": "use the System primarily for personal, family or household purposes",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "8(a)(i) - engineering site audit condition precedent",
        "source": "lease.txt",
        "quote": "a thorough physical inspection of the Property",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "10 - personal property, right to file UCC-1 or fixture filing",
        "source": "lease.txt",
        "quote": "right to file any UCC-1 financing statement or fixture filing",
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
