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
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a - not effective against buyer",
        "source": "ct740-home-solicitation.txt",
        "quote": "No agreement in a home solicitation sale shall be effective against the buyer",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(1) - fully completed copy",
        "source": "ct740-home-solicitation.txt",
        "quote": "Fail to furnish the buyer with a fully completed receipt or copy of all contracts",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(1) - immediate proximity to signature",
        "source": "ct740-home-solicitation.txt",
        "quote": "in immediate proximity to the space reserved in the contract for the signature of the buyer",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(2) - easily detachable notice",
        "source": "ct740-home-solicitation.txt",
        "quote": "easily detachable",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-137(a) - three business days from buyer signing",
        "source": "ct740-home-solicitation.txt",
        "quote": "until midnight of the third business day after the day on which the buyer signs",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-139(a) - goods become buyer's property",
        "source": "ct740-home-solicitation.txt",
        "quote": "the goods shall become the property of the buyer without obligation to pay for them",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-138(a) - tender payments",
        "source": "ct740-home-solicitation.txt",
        "quote": "the seller shall tender to the buyer any payments made by the buyer",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-139(c) - no compensation for services",
        "source": "ct740-home-solicitation.txt",
        "quote": "the seller is entitled to no compensation",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "Lease 28 - seven calendar day cancellation",
        "source": "lease.txt",
        "quote": "PRIOR TO MIDNIGHT OF THE SEVENTH (7TH) CALENDAR DAY AFTER THE DATE YOU SIGN THIS LEASE",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "5(c)(xiv) - not put a lien on your Home or Property",
        "source": "lease.txt",
        "quote": "not put a lien on your Home or Property",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "Exhibit E - no lien on the Real Property",
        "source": "lease.txt",
        "quote": "We do not have a lien on the Real Property",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "Exhibit E - will not impede any sale",
        "source": "lease.txt",
        "quote": "We will not impede any sale of the Real Property",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "Exhibit E - subordination to Security Instrument",
        "source": "lease.txt",
        "quote": "subject and subordinate in all respects to the Security Instrument",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "4(b)(i) - refinance cooperation",
        "source": "lease.txt",
        "quote": "We are asked or required to provide any cooperation",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "5(c)(xiii) - ensure repair under Limited Warranty",
        "source": "lease.txt",
        "quote": "ensure that the System will be repaired pursuant to the Limited Warranty",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "Exhibit A 2(a)(iii) - at no cost or expense",
        "source": "lease.txt",
        "quote": "at no cost or expense to you",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "16(b) - ninety days to initiate a remedy",
        "source": "lease.txt",
        "quote": "do not initiate a remedy of such failure within a period of ninety (90) days",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "11(c) - lease terminated, bill of sale",
        "source": "lease.txt",
        "quote": "the Lease will be terminated and neither You nor SunPower will have any remaining obligations",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-141(b) - HSSA violation is unfair or deceptive",
        "source": "ct740-home-solicitation.txt",
        "quote": "Violation of any of the provisions of sections 42-135a",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-110g(a) - punitive damages and equitable relief",
        "source": "ct735a-cutpa.txt",
        "quote": "The court may, in its discretion, award punitive damages and may provide such equitable relief",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-110g(d) - injunctive or other equitable relief",
        "source": "ct735a-cutpa.txt",
        "quote": "injunctive or other equitable relief",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-110g(f) - three years after occurrence",
        "source": "ct735a-cutpa.txt",
        "quote": "may not be brought more than three years after the occurrence of a violation",
    },
    {
        "doc": "10-SECTION-1c-DEFENCE.md",
        "note": "1(c) - other owners have acknowledged by execution",
        "source": "lease.txt",
        "quote": "any other owners of the Property have acknowledged this Lease by execution hereof",
    },
    {
        "doc": "10-SECTION-1c-DEFENCE.md",
        "note": "5(a)(xii) - have owners sign",
        "source": "lease.txt",
        "quote": "have anyone who has an ownership interest in your Home sign this Lease",
    },
    {
        "doc": "10-SECTION-1c-DEFENCE.md",
        "note": "8(a)(i) - real estate due diligence condition precedent",
        "source": "lease.txt",
        "quote": "real estate due diligence to confirm the suitability of the Property",
    },
    {
        "doc": "10-SECTION-1c-DEFENCE.md",
        "note": "16(a)(ii) - fifteen days after written notice",
        "source": "lease.txt",
        "quote": "such failure continues for a period of fifteen (15) days after",
    },
    {
        "doc": "07-FILING-LOGISTICS.md",
        "note": "19 - fallback to another accredited provider if no JAMS office in county",
        "source": "lease.txt",
        "quote": "If a JAMS office does not exist in the county where you live, then we will use another accredited arbitration provider with offices close to your Home",
    },
    {
        "doc": "07-FILING-LOGISTICS.md",
        "note": "19 - claimant pays first $125",
        "source": "lease.txt",
        "quote": "you will be required to pay the first $125 of any filing fee",
    },
    {
        "doc": "07-FILING-LOGISTICS.md",
        "note": "JAMS Consumer Minimum Standard 7 - $250 consumer fee cap",
        "source": "jams-consumer-minimum-standards.txt",
        "quote": "the only fee required to be paid by the consumer is $250",
    },
    {
        "doc": "07-FILING-LOGISTICS.md",
        "note": "JAMS Streamlined Rule 17(g) - remote hearing authority",
        "source": "jams-streamlined-rules.txt",
        "quote": "conducted in person or virtually by conference call, videoconference or using other communications technology",
    },
    {
        "doc": "07-FILING-LOGISTICS.md",
        "note": "JAMS Streamlined Rule 13 - fourteen calendar day exchange",
        "source": "jams-streamlined-rules.txt",
        "quote": "conclude the document and information exchange process within fourteen (14) calendar days after all pleadings or notices of claims have been received",
    },
    {
        "doc": "00-CASE-STRATEGY.md",
        "note": "IRS Section 25D - credit unavailable for property placed in service after 2025-12-31",
        "source": "irs-25d-residential-clean-energy.txt",
        "quote": "The credit is not available for any property placed in service after December 31, 2025",
    },
    {
        "doc": "00-CASE-STRATEGY.md",
        "note": "IRS Section 25D - used property ineligible",
        "source": "irs-25d-residential-clean-energy.txt",
        "quote": "Used (previously owned) clean energy property is not eligible",
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
