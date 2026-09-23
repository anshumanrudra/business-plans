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
        "doc": "03-SECTION-16b-NOTICE.md",
        "note": "4(b)(i) - refinance cooperation (Failure 3)",
        "source": "lease.txt",
        "quote": "We are asked or required to provide any cooperation",
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
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(1) - ten point boldface, substantially the following form",
        "source": "ct740-home-solicitation.txt",
        "quote": "in boldface type of a minimum size of ten points, a statement in substantially the following form",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(1) - the prescribed statement itself",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "YOU, THE BUYER, MAY CANCEL THIS TRANSACTION AT ANY TIME PRIOR TO MIDNIGHT OF THE THIRD "
            "BUSINESS DAY AFTER THE DATE OF THIS TRANSACTION. SEE THE ATTACHED NOTICE OF CANCELLATION "
            "FORM FOR AN EXPLANATION OF THIS RIGHT."
        ),
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(2) - duplicate form",
        "source": "ct740-home-solicitation.txt",
        "quote": "a completed form in duplicate",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(2) - easily detachable",
        "source": "ct740-home-solicitation.txt",
        "quote": "easily detachable",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(2) - ten-point boldface type",
        "source": "ct740-home-solicitation.txt",
        "quote": "in ten-point boldface type",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-135a(3) - cancellation date not earlier than third business day",
        "source": "ct740-home-solicitation.txt",
        "quote": "not earlier than the third business day following the date of the transaction",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "52-576 - six years on a contract in writing",
        "source": "ct926-limitations.txt",
        "quote": (
            "No action for an account, or on any simple or implied contract, or on any contract in "
            "writing, shall be brought but within six years after the right of action accrues"
        ),
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "Exhibit C - buyer must make goods available at residence",
        "source": "lease.txt",
        "quote": (
            "you must make available to the seller at your residence, in substantially as good "
            "condition as when received, any goods delivered to you under this contract or sale"
        ),
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-137(b) - cancellation occurs on giving notice or deposit in a mail box",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "Cancellation shall occur when the buyer gives written notice of cancellation to the "
            "seller at the address specified for notice of cancellation provided by the seller or "
            "when such written notice bearing such address is deposited in a mail box"
        ),
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-139(a) - twenty days after cancellation",
        "source": "ct740-home-solicitation.txt",
        "quote": "within twenty days after a home solicitation sale has been cancelled",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "42-139(a) - seller fails to take possession within twenty days",
        "source": "ct740-home-solicitation.txt",
        "quote": "If the seller fails to take possession of such goods within twenty days after cancellation",
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
        "doc": "04-JAMS-DEMAND.md",
        "note": "52-576 - six years on a contract in writing (Count 1 limitation answer)",
        "source": "ct926-limitations.txt",
        "quote": (
            "No action for an account, or on any simple or implied contract, or on any contract in "
            "writing, shall be brought but within six years after the right of action accrues"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(2) - refund within ten business days (prescribed form text)",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "WILL BE RETURNED WITHIN TEN BUSINESS DAYS FOLLOWING RECEIPT BY THE SELLER OF YOUR "
            "CANCELLATION NOTICE"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(2) - duplicate form (Defect C)",
        "source": "ct740-home-solicitation.txt",
        "quote": "a completed form in duplicate",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(1) - ten point boldface, substantially the following form (Defect D)",
        "source": "ct740-home-solicitation.txt",
        "quote": "in boldface type of a minimum size of ten points, a statement in substantially the following form",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(1) - the prescribed statement itself (Defect D)",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "YOU, THE BUYER, MAY CANCEL THIS TRANSACTION AT ANY TIME PRIOR TO MIDNIGHT OF THE THIRD "
            "BUSINESS DAY AFTER THE DATE OF THIS TRANSACTION. SEE THE ATTACHED NOTICE OF CANCELLATION "
            "FORM FOR AN EXPLANATION OF THIS RIGHT."
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(2) - ten-point boldface type (Defect D)",
        "source": "ct740-home-solicitation.txt",
        "quote": "in ten-point boldface type",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(3) - cancellation date not earlier than third business day (Defect E)",
        "source": "ct740-home-solicitation.txt",
        "quote": "not earlier than the third business day following the date of the transaction",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-134a(a)(5) - real property exclusion",
        "source": "ct740-home-solicitation.txt",
        "quote": "pertaining to the sale or rental of real property",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-134a(a)(5) annotation 340 C. 711 - exception not strictly limited",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "The real property exception to definition of “home solicitation sale” is not "
            "strictly limited to the sale or rental or real property"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "10 - System is personal property and not a fixture",
        "source": "lease.txt",
        "quote": (
            "is Our personal property under the Uniform Commercial Code and not a fixture (or real "
            "property) regardless of whether it is attached to real property"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-137(b) - cancellation occurs on giving notice or deposit in a mail box",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "Cancellation shall occur when the buyer gives written notice of cancellation to the "
            "seller at the address specified for notice of cancellation provided by the seller or "
            "when such written notice bearing such address is deposited in a mail box"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-139(a) - seller fails to take possession within twenty days",
        "source": "ct740-home-solicitation.txt",
        "quote": "If the seller fails to take possession of such goods within twenty days after cancellation",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-141(b) - failure to honor the notice of cancellation",
        "source": "ct740-home-solicitation.txt",
        "quote": "failure to honor any provisions of the notice of cancellation required by this chapter",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(7) - fail or refuse to honor a valid notice of cancellation",
        "source": "ct740-home-solicitation.txt",
        "quote": "Fail or refuse to honor any valid notice of cancellation by a buyer",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(7)(C) - terminate promptly any security interest",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "take any action necessary or appropriate to terminate promptly any security interest "
            "created in the transaction"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-135a(9) - notify whether seller will repossess or abandon",
        "source": "ct740-home-solicitation.txt",
        "quote": (
            "to notify such buyer whether the seller intends to repossess or to abandon any shipped "
            "or delivered goods"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "11(b) - prices only (i), (ii) and (iii)",
        "source": "lease.txt",
        "quote": "In each of (i), (ii) and (iii) above, the price you pay for the System will be the fair market value",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "11(b) - recapture included if purchased before fifth anniversary of In-Service Date",
        "source": "lease.txt",
        "quote": (
            "If the System is purchased prior to the fifth (5th) anniversary of the In-Service Date, "
            "the Fair Market Value will include the recapture of any federal tax credits"
        ),
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "11(a)(iv) - purchase option on Our default under Section 16(b)",
        "source": "lease.txt",
        "quote": "In the event of Our default pursuant to Section 16(b)",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "19 - only disputes involving you and Us",
        "source": "lease.txt",
        "quote": "Only Disputes involving you and Us may be addressed in the arbitration",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "19 - no relief for or against a non-party",
        "source": "lease.txt",
        "quote": "award relief for or against anyone who is not a party",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "42-136(a) - assignee subject to all claims and defenses of the buyer",
        "source": "ct740-home-solicitation.txt",
        "quote": "subject to all claims and defenses of the buyer against the seller",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "19 - fee shifting if award exceeds last written settlement offer",
        "source": "lease.txt",
        "quote": "the award you receive from the arbitrator is higher than Our last written settlement offer",
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
        "doc": "05-DOCUMENT-REQUESTS.md",
        "note": "8(a)(i) - real estate due diligence condition precedent (R8)",
        "source": "lease.txt",
        "quote": "real estate due diligence to confirm the suitability of the Property",
    },
    {
        "doc": "05-DOCUMENT-REQUESTS.md",
        "note": "11(b) - recapture included if purchased before fifth anniversary (R20)",
        "source": "lease.txt",
        "quote": (
            "If the System is purchased prior to the fifth (5th) anniversary of the In-Service Date, "
            "the Fair Market Value will include the recapture of any federal tax credits"
        ),
    },
    {
        "doc": "08-TIMELINE-AND-GATES.md",
        "note": "11(b) - binary recapture rule, no step-down",
        "source": "lease.txt",
        "quote": (
            "If the System is purchased prior to the fifth (5th) anniversary of the In-Service Date, "
            "the Fair Market Value will include the recapture of any federal tax credits"
        ),
    },
    {
        "doc": "08-TIMELINE-AND-GATES.md",
        "note": "42-138(a) - ten business days after cancellation",
        "source": "ct740-home-solicitation.txt",
        "quote": "within ten business days after a home solicitation sale has been cancelled",
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
    # --- E13 / E14: Claimant's own documents, added 2026-09-23 -------------------
    # Sub-spans are chosen to start mid-sentence where the source capitalises a
    # sentence-initial word that the deliverables quote in lower case. The matcher is
    # case-sensitive, so "utility has given you..." matches both "The utility has given
    # you..." (source) and "the utility has given you..." (pleading).
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "E14 - SAVKAT relays permission to operate, 2023-05-12",
        "source": "savkat-pto-2023-05-12.txt",
        "quote": "utility has given you permission to operate your system",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "E14 - SunPower confirms energization, 2023-05-15",
        "source": "sunpower-system-on-2023-05-15.txt",
        "quote": "YOUR SYSTEM IS ON!",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "E14 - SunPower billing rule, anchors first payment to 2023-06-01 (D1)",
        "source": "sunpower-system-on-2023-05-15.txt",
        "quote": "payments will be due on the first day of the month beginning the month after your system is interconnected",
    },
    {
        "doc": "02-NOTICE-OF-CANCELLATION.md",
        "note": "E14 - same billing rule, quoted in the cancellation notice",
        "source": "sunpower-system-on-2023-05-15.txt",
        "quote": "payments will be due on the first day of the month beginning the month after your system is interconnected",
    },
    # NOT VERIFIABLE BY THIS HARNESS — page 9 of the IC packet is a scanned raster page.
    #
    # Page 9 of "ANSHUMAN RUDRA IC PACKET LEASE.pdf" yields 119 characters of text against
    # ~1,355 on page 8 and ~2,044 on page 10: it is an image, not text. No OCR tool is
    # available in this environment. Three certifications live only on that page and are
    # therefore quoted in the deliverables from a RENDERED IMAGE, not from a pinned text
    # source, and cannot be added here:
    #
    #   - "Will a filing be recorded in the land records of the customer's municipality
    #      pursuant to the contract for this system?" -> Yes        (04 P28, Count 3; 05 R7)
    #   - "Must the customer continue to make payments in the event of an extended system
    #      shutdown?" -> No                                          (04 Count 4)
    #   - "Does the system installation contract conform to the requirements of the
    #      Connecticut Home Improvement Contractor Law?" -> Yes      (08 decision gate 3)
    #
    # Also image-only on that page: the $.314/kWh starting utility rate, the 4% savings
    # escalator, contract/warranty transferability, and the Key Responsibilities Checklist.
    #
    # See the "Harness-unverifiable evidence" register in sources/SOURCES.md and the
    # pre-filing item in 07-FILING-LOGISTICS.md section 9. Do not add these as citations
    # unless an OCR pass or a certified copy from Eversource makes the text layer real.
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "E13 - PURA misrepresentation penalty (page 10, text layer present)",
        "source": "pura-ic-packet.txt",
        "quote": "may be grounds for enforcement action by the",
    },
    {
        "doc": "04-JAMS-DEMAND.md",
        "note": "E13 - installer's year-one production estimate, 5516 kWh (Count 5, D4)",
        "source": "pura-ic-packet.txt",
        "quote": "Estimated Year One Production (kWh): 5516",
    },
    {
        "doc": "08-TIMELINE-AND-GATES.md",
        "note": "E13 - Home Improvement Contractor Law, footnote on p.10 (the question itself is image-only on p.9)",
        "source": "pura-ic-packet.txt",
        "quote": "rights and protections under the Connecticut Home Improvement Contractor Law",
    },
    {
        "doc": "05-DOCUMENT-REQUESTS.md",
        "note": "E13 - net savings line item sought in R21",
        "source": "pura-ic-packet.txt",
        "quote": "Estimated Year One Customer Net Savings",
    },
    {
        "doc": "01-EVIDENCE-CHECKLIST.md",
        "note": "Lease cover page - year 1 production estimate, 5,821 kWh (E6 comparison)",
        "source": "lease.txt",
        "quote": "Estimated year 1 production",
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
