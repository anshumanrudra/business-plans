# Solar Lease Arbitration Document Set — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for
> tracking.

> **SUPERSEDED IN PART — 2026-09-23.** This plan's Global Constraints state the Lease Term Start Date as **April
> 2023** and payments to date as **41, ≈$3,740.98**. Both are withdrawn: interconnection is **May 2023** and the
> first payment fell due **1 June 2023** (evidence items E13/E14). See the full supersession banner in
> `2026-09-21-solar-arbitration-design.md` and the corrected figures in `06-DAMAGES-SCHEDULE.md` D1. The
> deliverables `00`–`10` govern over this plan wherever they disagree. The task structure and architecture below are
> unaffected.

**Goal:** Produce the nine documents Anshuman Rudra needs to self-file and prosecute a JAMS arbitration against
SunPower Capital, LLC seeking cancellation of Lease #4593311, discharge of the UCC/fixture filing, and title to
the solar System — with every legal quotation verified verbatim against a pinned primary source.

**Architecture:** A pinned source corpus plus a citation-verification harness comes first, so every later
document is written against sources that can be mechanically checked. Documents are then built in urgency order:
the zero-risk §16(b) breach notice before anything else (it starts a 90-day clock at no cost), then evidence and
damages scaffolding, then the Demand itself in three passes, then supporting and reserve documents. The harness
is the test cycle: each document task begins by asserting its quotations, watches the assertion fail, writes the
document, and watches it pass.

**Tech Stack:** Markdown deliverables; Python 3 (stdlib only) for the verification harness; `pdftotext` for PDF
extraction; `curl` for pinning statutes from the Connecticut General Assembly.

**Spec:** `relocation/pass6/solar/2026-09-21-solar-arbitration-design.md`

**Plan location note:** The writing-plans skill defaults to `docs/superpowers/plans/`. This repo keeps all
relocation work under `relocation/pass6/`, and the spec was written there, so the plan lives beside it.

## Global Constraints

Values copied verbatim from the spec. Every task's requirements implicitly include this section.

- **Claimant:** Anshuman Rudra. **Property:** 498 Plainville Ave, Unionville (Town of Farmington), CT 06085.
- **Lease #:** 4593311. **DocuSign Envelope ID:** `3A20E4A8-02E4-4424-A69E-69C610492E40`.
- **Claimant signed:** 2023-01-16. **Lessor countersigned:** 2023-01-19 (Sherilyn M. Cano).
- **Exhibit C states:** "(Date of Lease) 1/19/2023", cancel by "1/26/2023".
- **Lease Term Start Date (§2, = interconnection approval):** **April 2023**. **Energized:** May 2023.
- **Actual installation:** ~Feb–Mar 2023 (inferred). **Lease states:** "Approximate Start Date: 7/18/2023",
  "Approximate Completion Date: 7/23/2023".
- **System:** 5.46 kW DC, 14 × Canadian Solar 390W (Model SPR-U-390-BLK-C-DC), inverter Type H / SPWR-A4
  (IQ 7HS)(14), racking InvisiMount, PVS6 Monitoring Kit.
- **Payments:** Yr1 $88.02, Yr2 $90.57, Yr3 $93.20, Yr4 $95.90 (current). Disclosed total $28,094.36.
- **Payments to date:** 41 payments, **≈ $3,740.98** (estimate; confirm against ledger).
- **Production Guarantee Period 1:** 10,465 kWh @ $0.187/kWh, true-up came due **~May 2025**.
- **§11(a)(i) purchase option opens:** **April 2028**, which is also when the §11(b) recapture adder reaches 0%.
- **CUTPA live window:** acts **on or after 2023-09-21** only. **Contract window:** to ~2029-01.
- **Respondents:** SunPower Capital, LLC (primary); SunStrong entity (once confirmed); SAVKAT, Inc. (defensively).
  **Never name** SunPower Corporation, Systems (Chapter 11).
- **Spouse:** confirmed record co-owner, did not sign. **Reserved — never pleaded.** Evidence and prepared
  defence only.
- **Forum:** JAMS Streamlined Rules, Hartford County, remote hearing. Claimant pays **$125**.
- **Scope:** deliverables `01`–`08` and `10`. **`09` is contingent and excluded from this plan.**

**Standing drafting rules for every deliverable:**

1. Never quote a statute or lease clause that is not in `sources/` and registered in the harness.
2. Never plead the spouse's non-signature, her interest, or trespass.
3. Never plead the January 2023 sales conduct as a CUTPA or tort damages claim (time-barred).
4. Never plead Guarantee Period 2 as a present breach (not due until ~May 2027).
5. Never plead Regulation M as a standalone count (one-year limit expired January 2024) — evidence only.
6. Every deliverable carries the header: `NOT LEGAL ADVICE — SELF-PREPARED DRAFT. Verify all research items in
   the spec §14 before filing.`

---

## File Structure

```
relocation/pass6/solar/
├── 2026-09-21-solar-arbitration-design.md   spec (exists)
├── 2026-09-21-solar-arbitration-plan.md     this plan
├── sources/                                  pinned primary sources + harness
│   ├── lease.txt                             extracted lease text (exists at ../lease.txt, move here)
│   ├── case_accept.txt                       Covar report text (exists at ../, move here)
│   ├── ct740-home-solicitation.txt           Ch. 740 HSSA
│   ├── ct735a-cutpa.txt                      Ch. 735a CUTPA
│   ├── ct926-limitations.txt                 Ch. 926 §§52-576, 52-577
│   ├── SOURCES.md                            provenance: URL, fetch date, sha256
│   └── verify_citations.py                   the test harness
├── 00-CASE-STRATEGY.md        index + operative summary (points at spec, no duplication)
├── 01-EVIDENCE-CHECKLIST.md   12 items, request templates
├── 02-NOTICE-OF-CANCELLATION.md
├── 03-SECTION-16b-NOTICE.md
├── 04-JAMS-DEMAND.md
├── 05-DOCUMENT-REQUESTS.md
├── 06-DAMAGES-SCHEDULE.md
├── 07-FILING-LOGISTICS.md
├── 08-TIMELINE-AND-GATES.md
└── 10-SECTION-1c-DEFENCE.md   reserved, not filed
```

Responsibilities: `sources/` is the only place raw authority lives — deliverables quote it, never restate it
from memory. `02`/`03` are operative instruments that get served, so they are self-contained and carry no
analysis. `04` is the pleading. `01`/`05`/`06` are working documents Claimant updates as evidence arrives.
`07`/`08` are procedural. `00` is navigation. `10` is a drawer document.

---

## Task 1: Source corpus and citation-verification harness

**Files:**
- Create: `relocation/pass6/solar/sources/SOURCES.md`
- Create: `relocation/pass6/solar/sources/verify_citations.py`
- Move: `relocation/pass6/solar/lease.txt` → `sources/lease.txt`
- Move: `relocation/pass6/solar/case_accept.txt` → `sources/case_accept.txt`
- Create: `sources/ct740-home-solicitation.txt`, `sources/ct735a-cutpa.txt`, `sources/ct926-limitations.txt`

**Interfaces:**
- Consumes: nothing.
- Produces: `sources/verify_citations.py` exposing a module-level `CITATIONS` list of dicts with keys
  `doc` (str, deliverable filename relative to `solar/`), `quote` (str, verbatim text), `source` (str, filename
  relative to `sources/`), and `note` (str, the citation label such as `"§ 42-139(a)"`). Every later task appends
  entries to this list. Running `python3 sources/verify_citations.py` exits 0 when every quote appears verbatim
  in both its `doc` and its `source`, and exits 1 with a report otherwise. Optional first argument filters to
  one `doc`.

- [ ] **Step 1: Pin the statute sources and record provenance**

```bash
cd relocation/pass6/solar && mkdir -p sources && git mv lease.txt sources/lease.txt 2>/dev/null || mv lease.txt sources/lease.txt
mv case_accept.txt sources/case_accept.txt
for pair in "chap_740:ct740-home-solicitation" "chap_735a:ct735a-cutpa" "chap_926:ct926-limitations"; do
  chap="${pair%%:*}"; out="${pair##*:}"
  curl -sL --max-time 60 "https://www.cga.ct.gov/current/pub/${chap}.htm" -o "/tmp/${chap}.html"
  python3 -c "
import re,html,sys
t=open('/tmp/${chap}.html',encoding='utf-8',errors='replace').read()
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r' ?\n ?','\n',t); t=re.sub(r'\n{3,}','\n\n',t)
open('sources/${out}.txt','w',encoding='utf-8').write(t)
"
done
shasum -a 256 sources/*.txt > /tmp/hashes.txt && cat /tmp/hashes.txt
```

- [ ] **Step 2: Write `sources/SOURCES.md`**

Record for each file: the exact URL, the fetch date (2026-09-21), the sha256 from Step 1, and for the PDF-derived
files the extraction command. Include this table, filling the hashes from `/tmp/hashes.txt`:

```markdown
# Pinned Primary Sources

Fetched 2026-09-21. Re-verify hashes before filing; CGA publishes supplements each January.

| File | Source | sha256 |
|---|---|---|
| `lease.txt` | `pdftotext -layout sunpower_lease_oct_2022.pdf` | <hash> |
| `case_accept.txt` | `pdftotext -layout Anshuman_20Rudra_20Case_20Acceptance_20Report.pdf` | <hash> |
| `ct740-home-solicitation.txt` | https://www.cga.ct.gov/current/pub/chap_740.htm | <hash> |
| `ct735a-cutpa.txt` | https://www.cga.ct.gov/current/pub/chap_735a.htm | <hash> |
| `ct926-limitations.txt` | https://www.cga.ct.gov/current/pub/chap_926.htm | <hash> |

**Not yet pinned — pin before filing:**
- IRS Residential Clean Energy Credit page (§25D termination after 2025-12-31; used property ineligible).
  Used only in `00`/spec §10.
- JAMS Consumer Arbitration Minimum Standards (Standard 3 remedies; Standard 7 $250 cap).
- JAMS Streamlined Arbitration Rules (Rule 13 exchange; Rule 17(g) remote hearings).

**CGA caveat:** `www.cga.ct.gov` presents an incomplete TLS chain; `curl` succeeds where strict verifiers fail.
Confirm any quotation against the printed General Statutes before filing.
```

- [ ] **Step 3: Write the failing harness with the first three assertions**

Create `sources/verify_citations.py`:

```python
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
```

- [ ] **Step 4: Run the harness and verify it fails for the right reason**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py`
Expected: `FAIL` — three failures, each reporting `missing deliverable file 03-SECTION-16b-NOTICE.md`. The
`source` half of each check must **not** fail; if a quote is reported absent from `lease.txt`, the quote is wrong
— fix the quote, not the source.

- [ ] **Step 5: Commit**

```bash
git add relocation/pass6/solar/sources/
git commit -m "chore(solar): pin primary sources and add citation verification harness"
```

---

## Task 2: `01-EVIDENCE-CHECKLIST.md`

Built second because every other document has blanks only this fills.

**Files:**
- Create: `relocation/pass6/solar/01-EVIDENCE-CHECKLIST.md`

**Interfaces:**
- Consumes: spec §8 (12 evidence items).
- Produces: stable item numbers **E1–E12** matching spec §8's numbering, referenced by `04`, `05`, and `06`.

- [ ] **Step 1: Write the document**

Twelve sections, one per spec §8 item, each with: what to request, who from, the exact wording to send, what it
proves, and which count it serves. Priority order E1 (DocuSign certificate), E2 (fixture filing / UCC search),
E3 (refinance file), E4 (deed), then the rest.

Include these four ready-to-send request bodies verbatim.

**E1 — DocuSign Certificate of Completion:**

> I am requesting the Certificate of Completion and full audit trail for DocuSign Envelope ID
> 3A20E4A8-02E4-4424-A69E-69C610492E40, executed 16 January 2023, in which I was a signer. Please provide the
> complete envelope history including all sent, viewed, and signed timestamps for every recipient, and the
> signer's IP address and authentication method. I am the signer and am entitled to a copy of the completed
> envelope and its audit trail.

**E2 — Land records and UCC search:**

> I request certified copies of any UCC-1 financing statement, fixture filing, notice of lease, or other
> instrument recorded against 498 Plainville Ave, Unionville/Farmington, CT 06085, or indexed against Anshuman
> Rudra, in which SunPower Capital, LLC, SunPower Corporation, SunStrong, or SAVKAT, Inc. appears as secured
> party or claimant. Please also confirm the recording date, volume and page, and whether the instrument is
> indexed against the real property or against personal property only.

**E3 — Refinance file (to the lender):**

> I am requesting my complete loan file for the refinance application I submitted on [DATE], including: the
> adverse action or denial notice and all stated reasons; the title commitment or preliminary title report and
> every exception listed; all internal and external correspondence referencing a solar lease, UCC filing, or
> fixture filing; the rate lock or rate quote in effect; and all documents relating to the mortgage recast I
> completed instead, including the recast agreement and any fees charged.

**E7 — Interconnection date (to Eversource):**

> Please provide written confirmation of the date Eversource approved interconnection and granted permission to
> operate for the photovoltaic system at 498 Plainville Ave, Unionville, CT 06085, together with any
> interconnection agreement, net metering agreement, and the date the system was authorized to energize.

Each item ends with a status line: `Requested: ___  Received: ___  Location: ___`.

Add a header block flagging: **E7 is currently on recollection only** (April 2023 interconnection, May 2023
energization) and the entire date structure in the Global Constraints depends on it — get it in writing first.
Note that **E4 is obtained but never pleaded** (spec §6.2).

- [ ] **Step 2: Verify the document covers every spec item**

Run:
```bash
cd relocation/pass6/solar && for n in $(seq 1 12); do grep -q "^## E${n} " 01-EVIDENCE-CHECKLIST.md \
  && echo "E${n} ok" || echo "E${n} MISSING"; done
```
Expected: `E1 ok` through `E12 ok`, no `MISSING`.

- [ ] **Step 3: Verify the reserved-fact rule is honoured**

Run: `grep -in "trespass\|void as to her\|her interest" 01-EVIDENCE-CHECKLIST.md`
Expected: no output. E4 may mention co-ownership as a fact to document; it must not frame a claim.

- [ ] **Step 4: Commit**

```bash
git add relocation/pass6/solar/01-EVIDENCE-CHECKLIST.md
git commit -m "docs(solar): add evidence checklist E1-E12 with request templates"
```

---

## Task 3: `03-SECTION-16b-NOTICE.md` — serve immediately

Zero downside: it starts the §16(b) 90-day clock, preserves Count 7, and does not invite removal of the System.

**Files:**
- Create: `relocation/pass6/solar/03-SECTION-16b-NOTICE.md`
- Modify: `relocation/pass6/solar/sources/verify_citations.py` (entries already present from Task 1)

**Interfaces:**
- Consumes: Task 1 harness entries for `03-SECTION-16b-NOTICE.md`.
- Produces: a served date, recorded in `08`, from which the 90-day clock runs.

- [ ] **Step 1: Run the harness to confirm the failing baseline**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 03-SECTION-16b-NOTICE.md`
Expected: `FAIL` — 3 failures, all `missing deliverable file`.

- [ ] **Step 2: Write the notice**

A letter, not a brief. No HSSA, no CUTPA, no rescission — this document exists solely to start a contractual
clock, and mentioning cancellation here would muddy it.

Structure:
1. Addressed to SunPower Capital, LLC per §21 (personal delivery, electronic mail, overnight courier, or
   certified/registered mail, return receipt requested) at 8900 Amberglen Boulevard, Suite 325, Austin, TX 78729,
   Attn: SunPower Financing, and `SunPowerFinancing@sunpower.com`. Copy the current servicer.
2. Subject: `NOTICE OF FAILURE TO PERFORM MATERIAL OBLIGATIONS UNDER SECTION 16(b) — Lease #4593311`.
3. Opening: identifies Claimant, Property, Lease #4593311, and states the notice is given under §16(b).
4. **Failure 1 — repair and maintenance.** Recite that §5(c)(xiii) obliges Lessor to "ensure that the System
   will be repaired pursuant to the Limited Warranty", and that Exhibit A §2(a)(iii) promises repair
   "at no cost or expense to you", then state that Claimant was directed to outside service providers at his own
   expense on [DATES], and itemise amounts paid.
5. **Failure 2 — Production Guarantee.** Guarantee Period 1 ended ~May 2025 with a guarantee of 10,465 kWh at
   $0.187/kWh; no Payment Amount was remitted; demand the biennial reconciliation and supporting production data.
6. **Failure 3 — real property / refinance cooperation.** Recite §5(c)(xiv) and the Exhibit E representations,
   state that a filing appears against the Property, and demand a subordination or estoppel letter and
   confirmation the filing does not encumber the real property.
7. **Demand:** initiate a remedy within ninety (90) days of receipt, and state that failure will constitute
   default under §16(b), entitling Claimant to the purchase option under §11(a)(iv).
8. **Reservation:** all rights reserved; no waiver; payments continue under protest and without prejudice.
9. Signature block, date, and a service record table (method, address, tracking number, date sent, date
   received).

Use the exact quoted fragments registered in the harness: `do not initiate a remedy of such failure within a
period of ninety (90) days`, `ensure that the System will be repaired pursuant to the Limited Warranty`, and
`at no cost or expense to you`.

- [ ] **Step 3: Run the harness and verify it passes**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 03-SECTION-16b-NOTICE.md`
Expected: `PASS — 3 citation(s) verified verbatim against pinned sources.`

- [ ] **Step 4: Verify scope discipline**

Run: `grep -in "42-13\|42-110\|cancel\|rescind\|rescission\|trespass" 03-SECTION-16b-NOTICE.md`
Expected: no output. Statutory theories belong in `02` and `04`, not here.

- [ ] **Step 5: Commit**

```bash
git add relocation/pass6/solar/03-SECTION-16b-NOTICE.md
git commit -m "docs(solar): add Section 16(b) material-breach notice starting the 90-day clock"
```

---

## Task 4: `02-NOTICE-OF-CANCELLATION.md` — draft now, serve with the Demand

**Files:**
- Create: `relocation/pass6/solar/02-NOTICE-OF-CANCELLATION.md`
- Modify: `relocation/pass6/solar/sources/verify_citations.py`

**Interfaces:**
- Consumes: Task 1 harness.
- Produces: the cancellation date that Count 2 in `04` pleads, and the start of the § 42-139(a) 20-day clock.

- [ ] **Step 1: Add the failing citation assertions**

Append to `CITATIONS` in `sources/verify_citations.py`:

```python
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
```

- [ ] **Step 2: Run the harness and verify the new assertions fail**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 02-NOTICE-OF-CANCELLATION.md`
Expected: `FAIL` — 11 failures, all `missing deliverable file`. Any quote reported absent from
`ct740-home-solicitation.txt` or `lease.txt` means the quote is mis-transcribed; fix the quote.

- [ ] **Step 3: Write the notice**

Structure:
1. Same §21 service block as Task 3, plus SAVKAT, Inc.
2. Subject: `NOTICE OF CANCELLATION OF HOME SOLICITATION SALE — Lease #4593311`.
3. **Operative sentence first**, tracking § 42-137(c) so effectiveness does not depend on form: a plain
   statement that Claimant hereby cancels the transaction and does not intend to be bound.
4. **Why the right is still available.** The transaction is a home solicitation sale under § 42-134a(a) (a lease
   of consumer goods, personally solicited, signed away from the seller's place of business). The agreement is
   not effective against Claimant under § 42-135a because the copy furnished was not a "fully completed" copy —
   the Federal Consumer Leasing Act Disclosures page bears three blank dollar fields in the "Other Charges"
   column including the Total; because the cancellation statement was not in immediate proximity to the
   signature; and because the notice understated the refund period as ten calendar rather than ten business
   days. No compliant notice having been furnished, the cancellation period never began to run.
5. **What SunPower must now do:** tender all payments made (§ 42-138(a), figure from `06`); claim no compensation
   for services (§ 42-139(c)); and cancel any security interest — quoting SunPower's own Exhibit C, "any
   security interest arising out of the transaction will be canceled."
6. **Tender.** The System is made available at 498 Plainville Ave and nowhere else (§ 42-139(a)). Twenty days
   are stated expressly, with the § 42-139(a) consequence quoted, alongside Exhibit C's matching promise.
7. **Anticipate the §4(e) waiver** in one sentence, quoting its own carve-out `EXCEPT AS REQUIRED BY APPLICABLE
   LAW`.
8. **Status quo request:** because the parties dispute the effect of cancellation and arbitration is being
   commenced concurrently, request written notice at least ten days before any attempt to enter the Property or
   remove the System, and state that Claimant will seek interim relief preserving the System in place.
9. Reservation of rights; payments continue under protest. Signature, date, service record.

- [ ] **Step 4: Run the harness and verify it passes**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 02-NOTICE-OF-CANCELLATION.md`
Expected: `PASS — 11 citation(s) verified verbatim against pinned sources.`

- [ ] **Step 5: Add the serving decision gate at the top of the document**

Insert a fenced warning block before the letter:

```markdown
> ## DO NOT SERVE THIS ALONE — READ FIRST
>
> § 42-139(a) vests title in Claimant only if SunPower **fails** to take possession within twenty days.
> Serving this notice therefore invites removal of the System. If they remove it, Claimant obtains
> cancellation and restitution but **loses the panels** — objective 3 of three.
>
> **Default: serve concurrently with `04-JAMS-DEMAND.md`**, and include in the Demand a request for interim
> relief preserving the System in place pending the award. That runs the twenty-day clock with an arbitrator
> available to restrain removal.
>
> Serving earlier is a deliberate trade of objective 3 for a faster, cleaner Count 2. Claimant's call — do not
> make it by default.
```

- [ ] **Step 6: Verify the reserved-fact rule and the gate**

Run: `grep -c "DO NOT SERVE THIS ALONE" 02-NOTICE-OF-CANCELLATION.md && grep -in "trespass\|co-owner\|my wife\|spouse" 02-NOTICE-OF-CANCELLATION.md`
Expected: `1`, then no further output.

- [ ] **Step 7: Commit**

```bash
git add relocation/pass6/solar/02-NOTICE-OF-CANCELLATION.md relocation/pass6/solar/sources/verify_citations.py
git commit -m "docs(solar): add HSSA cancellation notice with serve-timing gate"
```

---

## Task 5: `06-DAMAGES-SCHEDULE.md`

**Files:**
- Create: `relocation/pass6/solar/06-DAMAGES-SCHEDULE.md`

**Interfaces:**
- Consumes: E3, E5, E6, E8 from `01`.
- Produces: named totals `D1`–`D4` and `D_TOTAL`, quoted by `02` §5 and by `04`'s prayer.

- [ ] **Step 1: Write the schedule**

Four heads, each with a worked table, a stated source, and a confidence label.

**D1 — Restitution of payments (§ 42-138(a)).** Reproduce the Global Constraints table:

| Contract year | Period | Rate | Payments | Subtotal |
|---|---|---|---|---|
| 1 | May 2023 – Apr 2024 | $88.02 | 12 | $1,056.24 |
| 2 | May 2024 – Apr 2025 | $90.57 | 12 | $1,086.84 |
| 3 | May 2025 – Apr 2026 | $93.20 | 12 | $1,118.40 |
| 4 | May 2026 – Sep 2026 | $95.90 | 5 | $479.50 |
| | | | **41** | **$3,740.98** |

Label ESTIMATED; add a row for sales/use tax actually charged; supersede from the E5 ledger.

**D2 — Refinance damages (Count 3).** Formula: `(recast rate − refinance rate quoted) × principal × remaining
term`, plus recast fees, plus any §4(b)(i) charges. Provide a worked illustration clearly marked
`ILLUSTRATIVE — REPLACE WITH E3 FIGURES`: $400,000 principal, 1.00 point differential, 27 years ⇒ ~$4,000/yr
before discounting. State that the figure must be computed from the actual rate lock and that §15(a) will be
invoked to recharacterise it as consequential — so plead it as direct loss flowing from breach of the specific
cooperation covenant.

**D3 — Out-of-pocket repairs (Count 4).** Itemisation table: date, provider, work, amount, invoice reference.
Populate from E8. Each line must be one the Repair Promise covered.

**D4 — Production Guarantee shortfall (Count 5).** `(10,465 − Actual Biennial kWh) × $0.187`, Guarantee Period 1
only, ending ~May 2025. Worked example: an actual of 9,900 kWh yields `565 × $0.187 = $105.66`. State the
$5.00 Minimum Payment Amount threshold and that Guarantee Period 2 is **not** pleaded.

**Non-monetary relief** noted separately as not reducible to a figure: lease termination, UCC-3 termination and
recorded release, title to the System, and punitive damages under § 42-110g(a) (discretionary, unquantified).

- [ ] **Step 2: Verify every figure is labelled and arithmetic is right**

Run:
```bash
cd relocation/pass6/solar && python3 -c "
vals=[(88.02,12),(90.57,12),(93.20,12),(95.90,5)]
print('D1 total', round(sum(r*n for r,n in vals),2), 'payments', sum(n for _,n in vals))
print('D4 example', round((10465-9900)*0.187,2))
"
grep -c "ESTIMATED\|ILLUSTRATIVE" 06-DAMAGES-SCHEDULE.md
```
Expected: `D1 total 3740.98 payments 41`, `D4 example 105.66`, and a count of at least 2.

- [ ] **Step 3: Commit**

```bash
git add relocation/pass6/solar/06-DAMAGES-SCHEDULE.md
git commit -m "docs(solar): add damages schedule D1-D4 with sources and confidence labels"
```

---

## Task 6: `04-JAMS-DEMAND.md` — parties, forum, statement of facts

Split across three tasks because a reviewer can meaningfully reject the facts while approving the counts.

**Files:**
- Create: `relocation/pass6/solar/04-JAMS-DEMAND.md`
- Modify: `relocation/pass6/solar/sources/verify_citations.py`

**Interfaces:**
- Consumes: Global Constraints; `01` item numbers; `06` totals.
- Produces: numbered fact paragraphs **¶1–¶40** that Tasks 7–8 cite by number rather than restating.

- [ ] **Step 1: Add the failing citation assertions**

```python
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
```

- [ ] **Step 2: Run the harness and verify the new assertions fail**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 04-JAMS-DEMAND.md`
Expected: `FAIL` — 7 failures, all `missing deliverable file`.

- [ ] **Step 3: Write sections I–IV**

**I. Caption.** `JAMS Demand for Arbitration` — Anshuman Rudra, Claimant, v. SunPower Capital, LLC; [SunStrong
entity]; and SAVKAT, Inc., Respondents. Lease #4593311. Streamlined Rules. Hartford County, CT. Remote hearing
requested under Rule 17(g).

**II. Parties.** One paragraph each, per spec §5. For SAVKAT add a footnote preserving the position that it is
named to avoid claim-splitting and that Claimant does not concede it is a party to §19. State affirmatively that
**SunPower Corporation, Systems is not named** because it is a Chapter 11 debtor, and that its non-performance is
asserted against Lessor through §5(c)(xiii).

**III. Jurisdiction, forum, and fees.** Quote §19's JAMS designation, the `$125` allocation, and the
`authority to award any legal or equitable remedy or relief that a court could order or grant` grant — the last
is load-bearing for the UCC-3 relief, so foreground it here rather than burying it in the prayer. Add that JAMS
Consumer Minimum Standard 3 preserves remedies otherwise available under state law.

**IV. Statement of facts, ¶1–¶40.** Chronological, one fact per paragraph, each tied to an evidence item:

- ¶1–¶6: parties, Property, Claimant's occupancy, the System description.
- ¶7–¶12: the January 2023 solicitation — a live one-to-one video presentation, DocuSign delivery, signature
  2023-01-16, countersignature 2023-01-19 (cite E1). **State the facts of the presentation without pleading
  fraud or misrepresentation** — they establish the § 42-134a(a) elements only.
- ¶13–¶16: the documents furnished, including the three blank dollar fields on the Federal Consumer Leasing Act
  Disclosures page and the placement of the cancellation statement.
- ¶17–¶20: installation ~Feb–Mar 2023 against the stated 7/18–7/23/2023, the §8(a)(i) site audit, interconnection
  April 2023, energization May 2023 (cite E7, E12).
- ¶21–¶25: the payment history and the current $95.90 rate (cite E5).
- ¶26–¶30: the filing against the Property and the failed refinance and recast (cite E2, E3). Facts only — the
  co-ownership appears nowhere.
- ¶31–¶35: service and maintenance history, including direction to outside providers at Claimant's expense
  (cite E8).
- ¶36–¶38: Guarantee Period 1 ending ~May 2025 and the absence of any Payment Amount (cite E6).
- ¶39–¶40: the SunPower bankruptcy and the servicing transfer (cite E9).

- [ ] **Step 4: Run the harness and verify it passes**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 04-JAMS-DEMAND.md`
Expected: `PASS — 7 citation(s) verified verbatim against pinned sources.`

- [ ] **Step 5: Verify paragraph numbering and prohibited content**

Run:
```bash
cd relocation/pass6/solar && grep -c "^¶" 04-JAMS-DEMAND.md
grep -in "fraud\|misrepresent\|trespass\|co-owner\|spouse\|did not sign" 04-JAMS-DEMAND.md
```
Expected: `40`, then no output.

- [ ] **Step 6: Commit**

```bash
git add relocation/pass6/solar/04-JAMS-DEMAND.md relocation/pass6/solar/sources/verify_citations.py
git commit -m "docs(solar): add JAMS Demand sections I-IV (parties, forum, facts)"
```

---

## Task 7: `04-JAMS-DEMAND.md` — Counts 1 and 2 (the HSSA counts)

**Files:**
- Modify: `relocation/pass6/solar/04-JAMS-DEMAND.md`
- Modify: `relocation/pass6/solar/sources/verify_citations.py`

**Interfaces:**
- Consumes: ¶1–¶40 from Task 6; the § 42-13x quotes already registered for `02`.
- Produces: Counts 1–2, cited by the prayer in Task 8.

- [ ] **Step 1: Add the failing citation assertions**

```python
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
```

- [ ] **Step 2: Run the harness and verify the new assertions fail**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 04-JAMS-DEMAND.md`
Expected: `FAIL` — 9 new failures reporting the quotes absent from the **deliverable** (the file now exists, and
the 7 Task 6 citations still pass).

- [ ] **Step 3: Write Count 1**

Sub-headed to mirror spec §6, in the spec's order of strength — defect 1 leads:

1. **Elements.** § 42-134a(a) includes a "lease" of "consumer goods"; §5(a)(ix)'s
   `use the System primarily for personal, family or household purposes` supplies the consumer-goods element;
   personally solicited by live video; signed at the Property.
2. **Defect A — not "fully completed."** Quote `Fail to furnish the buyer with a fully completed receipt or copy
   of all contracts`; plead ¶13–¶16; identify the three blank "Other Charges" dollar fields including the Total.
   Add that the same blanks independently violate Regulation M, 12 CFR 1013.4, **pleaded as evidence of the
   § 42-135a(1) violation and not as a count**.
3. **Defect B — a deviation shortening Claimant's rights.** The prescribed form provides for return within ten
   **business** days; Exhibit C states ten **calendar** days. Plead expressly that this deviation reduces the
   statutory entitlement, distinguishing it from defect D.
4. **Defect C — placement.** Quote `in immediate proximity to the space reserved in the contract for the
   signature of the buyer` and `easily detachable`; plead the page separation from ¶13–¶16.
5. **Defect D — period and prescribed text.** Quote Lease §28's
   `PRIOR TO MIDNIGHT OF THE SEVENTH (7TH) CALENDAR DAY AFTER THE DATE YOU SIGN THIS LEASE` against the
   statutory third-business-day form. Plead for completeness and say so.
6. **Defect E — wrong trigger date.** Quote § 42-137(a)'s
   `until midnight of the third business day after the day on which the buyer signs`; Exhibit C runs from
   1/19/2023, the countersignature.
7. **Meet the (a)(3) exclusion head-on.** Both rebuttals: the transaction was conducted by videoconference and
   electronic signature, neither of which is mail or telephone; and there was other contact before delivery of
   the goods — the §8(a)(i) `a thorough physical inspection of the Property` and the installation crew, all
   before the April 2023 interconnection (¶17–¶20).
8. **Meet §4(e)** using its own `EXCEPT AS REQUIRED BY APPLICABLE LAW` carve-out.
9. **Relief:** declaration the Lease is not effective against Claimant.

- [ ] **Step 4: Write Count 2**

Pleaded in the alternative and as consequential on Count 1: no compliant notice having been furnished, the period
never began; cancellation was effected by `02` on [DATE]; therefore § 42-138(a) restitution of D1, § 42-139(c) no
compensation for services, and § 42-139(a) title on failure to take possession within twenty days. Quote each.
Add that SunPower's own Exhibit C promises the same two consequences. Include a short paragraph requesting
**interim relief preserving the System in place** pending the award, cross-referencing the `02` gate.

- [ ] **Step 5: Run the harness and verify it passes**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 04-JAMS-DEMAND.md`
Expected: `PASS — 16 citation(s) verified verbatim against pinned sources.`

- [ ] **Step 6: Commit**

```bash
git add relocation/pass6/solar/04-JAMS-DEMAND.md relocation/pass6/solar/sources/verify_citations.py
git commit -m "docs(solar): add Demand Counts 1-2 (HSSA voidness and cancellation)"
```

---

## Task 8: `04-JAMS-DEMAND.md` — Counts 3–7, defences, and prayer

**Files:**
- Modify: `relocation/pass6/solar/04-JAMS-DEMAND.md`
- Modify: `relocation/pass6/solar/sources/verify_citations.py`

**Interfaces:**
- Consumes: ¶1–¶40; Counts 1–2; `06` totals D1–D4.
- Produces: the complete pleading, consumed by `05` and `07`.

- [ ] **Step 1: Add the failing citation assertions**

```python
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
```

- [ ] **Step 2: Run the harness and verify the new assertions fail**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 04-JAMS-DEMAND.md`
Expected: `FAIL` — 13 new failures against the deliverable; the 16 existing citations still pass.

- [ ] **Step 3: Write Counts 3, 4 and 5**

**Count 3 — breach, no-lien and cooperation.** Quote `not put a lien on your Home or Property`,
`We do not have a lien on the Real Property`, `We will not impede any sale of the Real Property`,
`subject and subordinate in all respects to the Security Instrument`, and §4(b)(i)'s
`We are asked or required to provide any cooperation`. Plead ¶26–¶30 and damages D2. **Concede §10's
`right to file any UCC-1 financing statement or fixture filing` expressly** and frame the breach as the filing
encumbering the *Real Property* and the failure to cooperate — per spec §6, framing decides this count. **No
reference to the co-owner.**

**Count 4 — breach, repair and maintenance.** Quote `ensure that the System will be repaired pursuant to the
Limited Warranty` and `at no cost or expense to you`. Plead ¶31–¶35, damages D3.

**Count 5 — breach, Production Guarantee.** Guarantee Period 1 only; 10,465 kWh at $0.187; plead ¶36–¶38,
damages D4. Pre-empt the Communication Requirements defence with Exhibit A §2(c)(iv)'s lost-data reconstruction.
State expressly that Guarantee Period 2 is not yet due and is not pleaded.

- [ ] **Step 4: Write Count 6 (CUTPA) with the limitations fence built in**

Two routes: per se under § 42-141(b) (quote `Violation of any of the provisions of sections 42-135a`), and
independent unfair acts. Then a paragraph headed **Limitations** that quotes
`may not be brought more than three years after the occurrence of a violation` and states that Claimant pleads
**only** acts on or after 2023-09-21 and **does not** plead the January 2023 sales conduct as a CUTPA violation.
Enumerate the in-window acts: refusal to furnish subordination or estoppel documentation; charging Claimant for
covered repairs; failure to remit the Guarantee Period 1 Payment Amount; failure to give §21 notice of the
servicing transfer. Remedies: quote § 42-110g(a) and `injunctive or other equitable relief` from (d). Note the
copies to the Attorney General and the Commissioner of Consumer Protection.

- [ ] **Step 5: Write Count 7 (alternative) and the defences section**

**Count 7.** Pleaded expressly in the alternative to Counts 1–2. Quote §16(b)'s
`do not initiate a remedy of such failure within a period of ninety (90) days`; recite the `03` notice and its
service date; predicate on Counts 3–5. Relief: declaration of default, purchase at FMV set by a **mutually
agreed** appraiser (arguing from §18's independent-appraiser-agreed-by-both mechanism), **without** the §11(b)
tax-credit-recapture adder because the early purchase is compelled by Lessor's own default, plus
`the Lease will be terminated and neither You nor SunPower will have any remaining obligations` and a bill of
sale. Acknowledge §11(a)(i) opens the option unconditionally in April 2028 so the count is not overstated.

**Defences to anticipated shields**, per spec §6.1 — §4(e), §15(a)/(b) with JAMS Standard 3, §19's
"not authorized to change or alter the terms", §23, and §6.

- [ ] **Step 6: Write the prayer for relief**

Twelve numbered items exactly as spec §7, with D1–D4 substituted for the money items and the alternative Count 7
relief as item 11. Include the pro se fee limitation as a footnote: fees are requested under § 42-110g(d) but
Claimant acknowledges a pro se party generally cannot recover attorney's fees and seeks costs.

- [ ] **Step 7: Run the harness and verify it passes**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 04-JAMS-DEMAND.md`
Expected: `PASS — 29 citation(s) verified verbatim against pinned sources.`

- [ ] **Step 8: Verify the count structure and prohibited content**

Run:
```bash
cd relocation/pass6/solar && for n in 1 2 3 4 5 6 7; do grep -q "^## COUNT ${n}" 04-JAMS-DEMAND.md \
  && echo "Count ${n} ok" || echo "Count ${n} MISSING"; done
grep -in "trespass\|co-owner\|spouse\|did not sign\|47-31" 04-JAMS-DEMAND.md
grep -c "Guarantee Period 2 is not" 04-JAMS-DEMAND.md
```
Expected: `Count 1 ok` … `Count 7 ok`; no output from the second command; `1` from the third.

- [ ] **Step 9: Commit**

```bash
git add relocation/pass6/solar/04-JAMS-DEMAND.md relocation/pass6/solar/sources/verify_citations.py
git commit -m "docs(solar): complete JAMS Demand with Counts 3-7, defences and prayer"
```

---

## Task 9: `05-DOCUMENT-REQUESTS.md`

**Files:**
- Create: `relocation/pass6/solar/05-DOCUMENT-REQUESTS.md`

**Interfaces:**
- Consumes: `01` items E1–E12; `04` counts.
- Produces: numbered requests R1–R20.

- [ ] **Step 1: Write the requests**

Open by stating the Rule 13 baseline: parties must cooperate in sharing all non-privileged documents and
information including electronically stored information within fourteen calendar days after claims are received,
so R1–R20 are framed as what that obligation already requires rather than as a discovery motion.

Twenty numbered requests, each naming the count it serves:

- R1–R3: the complete DocuSign envelope, audit trail, and every version of the document set sent (Count 1).
- R4–R5: all sales training materials, scripts, and dealer agreements with SAVKAT concerning cancellation-rights
  disclosure and discount expiry representations (Count 1).
- R6–R8: every UCC-1, UCC-3, fixture filing, or recorded instrument touching the Property; the filing
  instructions; and all title work performed under §8(a)(i) (Counts 3, 6). **Request the title work without
  arguing the co-ownership point** — if their title report shows the co-owner, that surfaces on its own.
- R9–R11: all communications with Claimant's lender or any title company; all subordination, estoppel, or
  payoff requests received and the responses (Count 3).
- R12–R13: the complete payment ledger and all assignment and servicing-transfer notices (Counts 2, 6).
- R14–R16: all PVS6 production data; every Guarantee Period calculation; and all Payment Amount determinations
  (Count 5).
- R17–R18: all service tickets, dispatch records, and any policy directing customers to third-party providers at
  their own expense (Count 4).
- R19–R20: any appraisal or FMV determination for the System, and any document concerning federal tax credits
  claimed and recapture exposure (Count 7).

Close with a preservation demand covering ESI, the DocuSign envelope, and monitoring telemetry.

- [ ] **Step 2: Verify coverage**

Run:
```bash
cd relocation/pass6/solar && for n in $(seq 1 20); do grep -q "^### R${n}\b" 05-DOCUMENT-REQUESTS.md \
  || echo "R${n} MISSING"; done; echo "coverage check done"
grep -in "trespass\|spouse\|co-owner" 05-DOCUMENT-REQUESTS.md
```
Expected: `coverage check done` with no `MISSING`, and no output from the second command.

- [ ] **Step 3: Commit**

```bash
git add relocation/pass6/solar/05-DOCUMENT-REQUESTS.md
git commit -m "docs(solar): add Rule 13 document requests R1-R20"
```

---

## Task 10: `10-SECTION-1c-DEFENCE.md` — reserved, not filed

**Files:**
- Create: `relocation/pass6/solar/10-SECTION-1c-DEFENCE.md`
- Modify: `relocation/pass6/solar/sources/verify_citations.py`

**Interfaces:**
- Consumes: spec §6.2.
- Produces: a drawer document; nothing else depends on it.

- [ ] **Step 1: Add the failing citation assertions**

```python
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
```

- [ ] **Step 2: Run the harness and verify the new assertions fail**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 10-SECTION-1c-DEFENCE.md`
Expected: `FAIL` — 4 failures, all `missing deliverable file`.

- [ ] **Step 3: Write the defence**

Open with a prominent use-restriction block: this document is **not filed and never volunteered**; it is used
only if SunPower asserts the §1(c)/§5(a)(xii) point first.

Then: the exposure (quote `any other owners of the Property have acknowledged this Lease by execution hereof`,
`have anyone who has an ownership interest in your Home sign this Lease`, and §16(a)(ii)'s
`such failure continues for a period of fifteen (15) days after`, routing through §17 to §18); followed by the
three answers from spec §6.2 in order of strength, led by §8(a)(i)'s
`real estate due diligence to confirm the suitability of the Property`; then waiver and estoppel from 41
accepted payments; then the illusory-cure point. Close with the §6.2 trigger table, noting that once SunPower
raises the point the exposure has already materialised and filing `09` becomes comparatively low-risk.

- [ ] **Step 4: Run the harness and verify it passes**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py 10-SECTION-1c-DEFENCE.md`
Expected: `PASS — 4 citation(s) verified verbatim against pinned sources.`

- [ ] **Step 5: Commit**

```bash
git add relocation/pass6/solar/10-SECTION-1c-DEFENCE.md relocation/pass6/solar/sources/verify_citations.py
git commit -m "docs(solar): add reserved Section 1(c) defence brief"
```

---

## Task 11: `07-FILING-LOGISTICS.md`

**Files:**
- Create: `relocation/pass6/solar/07-FILING-LOGISTICS.md`

**Interfaces:**
- Consumes: `04`.
- Produces: the filing runbook.

- [ ] **Step 1: Write the runbook**

1. **What to file:** the Demand, the Lease as an exhibit, the `02` and `03` notices with proof of service, and
   the $125.
2. **Where:** JAMS intake, Streamlined Rules, Hartford County venue. Record the §19 fallback verbatim — if no
   JAMS office exists in the county, another accredited provider is used — and the standing decision **not** to
   litigate the forum, per spec §3.
3. **Fees:** the $125 under §19, with JAMS Consumer Minimum Standard 7's $250 cap noted as the alternative
   ceiling and all remaining fees on Respondents.
4. **Service:** §21 methods and the Exhibit A §7 notice addresses, verbatim. Certified mail **and** email;
   retain return receipts.
5. **Statutory copies:** the Attorney General and the Commissioner of Consumer Protection, per § 42-110g(c)
   practice, noting the subsection is framed for court actions and the copies are prophylactic.
6. **Remote hearing:** request under Rule 17(g) at the preliminary conference, citing the arbitrator's full
   authority to conduct proceedings virtually.
7. **From India:** designate a US mailing address and a person authorised to receive certified mail; calendar
   in IST with a US-Eastern column; keep scanned originals in `sources/`; expect to appear by videoconference.
8. **Keep paying.** A standing block reciting §16(a)(i)'s thirty days, §18's Early Termination Liability, and
   Exhibit D's statement that terminating the ACH authorisation does not terminate the Lease or the payment
   obligation. Payments continue under protest and without prejudice.
9. A pre-filing checklist gating on spec §14 research items 1, 1a, 1b, 2, 9, 10 and 11.

- [ ] **Step 2: Verify the keep-paying warning and research gate are present**

Run:
```bash
cd relocation/pass6/solar && grep -c "under protest" 07-FILING-LOGISTICS.md
grep -q "Early Termination Liability" 07-FILING-LOGISTICS.md && echo "ETL warning ok"
grep -q "14" 07-FILING-LOGISTICS.md && echo "research gate ok"
```
Expected: at least `1`, then `ETL warning ok`, then `research gate ok`.

- [ ] **Step 3: Commit**

```bash
git add relocation/pass6/solar/07-FILING-LOGISTICS.md
git commit -m "docs(solar): add JAMS filing logistics runbook"
```

---

## Task 12: `08-TIMELINE-AND-GATES.md` and `00-CASE-STRATEGY.md`

**Files:**
- Create: `relocation/pass6/solar/08-TIMELINE-AND-GATES.md`
- Create: `relocation/pass6/solar/00-CASE-STRATEGY.md`

**Interfaces:**
- Consumes: every prior deliverable.
- Produces: navigation and the live tracker.

- [ ] **Step 1: Write `08-TIMELINE-AND-GATES.md`**

Reproduce spec §12's phase table with a `Status` and `Date completed` column. Then a **live clocks** table, the
operational heart of the document:

| Clock | Authority | Starts | Length | Expires | Status |
|---|---|---|---|---|---|
| §16(b) cure period | Lease §16(b) | service of `03` | 90 days | | |
| § 42-139(a) tender | § 42-139(a) | service of `02` | 20 days | | |
| § 42-138(a) refund | § 42-138(a) | SunPower's receipt of `02` | 10 business days | | |
| Rule 13 exchange | JAMS Rule 13 | receipt of claims | 14 calendar days | | |
| CUTPA window | § 42-110g(f) | rolling | 3 years | acts before 2023-09-21 already barred | closed |
| §11(a)(i) option | Lease §11(a)(i) | Lease Term Start Date | 5 years | **April 2028** | pending |
| §11(b) recapture | Lease §11(b) | in-service date | 5 years | **April 2028**, 0% thereafter | 40%→20% |

Then the four §6.2 trigger conditions as a checklist, and the two decision gates: whether to serve `02` early
(Task 4's block) and whether SAVKAT stays named.

- [ ] **Step 2: Write `00-CASE-STRATEGY.md` as an index, not a duplicate**

One page. Objectives, the three-line theory (HSSA voidness for the upside, breach for the durable claims, §16(b)
default as the floor), a table of the nine documents with one-line purposes and read order, and a **Read the spec
first** pointer to `2026-09-21-solar-arbitration-design.md` for all analysis. Then a short **Do not** list:
do not stop paying; do not plead the co-owner, trespass, or the January 2023 sales conduct as a damages claim; do
not serve `02` alone; do not file `09` absent a trigger. Close with the §25D correction from spec §10 and a
pointer to fix `SOLAR-BUYOUT-RESEARCH.md`.

Keep it under 100 lines — its job is routing, and analysis duplicated here will drift from the spec.

- [ ] **Step 3: Verify no duplication and correct linkage**

Run:
```bash
cd relocation/pass6/solar && wc -l 00-CASE-STRATEGY.md
grep -c "2026-09-21-solar-arbitration-design.md" 00-CASE-STRATEGY.md
for f in 01 02 03 04 05 06 07 08 10; do grep -q "${f}-" 00-CASE-STRATEGY.md || echo "missing link ${f}"; done
echo "link check done"
```
Expected: under 100 lines; at least `1`; `link check done` with no `missing link`.

- [ ] **Step 4: Commit**

```bash
git add relocation/pass6/solar/08-TIMELINE-AND-GATES.md relocation/pass6/solar/00-CASE-STRATEGY.md
git commit -m "docs(solar): add timeline with live clocks and case strategy index"
```

---

## Task 13: Correct `SOLAR-BUYOUT-RESEARCH.md`

Spec §10. The document currently drives decisions off a tax credit that no longer exists.

**Files:**
- Modify: `relocation/pass6/SOLAR-BUYOUT-RESEARCH.md`

**Interfaces:**
- Consumes: spec §10.
- Produces: nothing; terminal correction.

- [ ] **Step 1: Add a correction banner at the top of the file**

```markdown
> # ⚠️ SUPERSEDED IN PART — READ THIS FIRST (2026-09-21)
>
> **The 30% federal ITC premise in this document is wrong, on two independent grounds.** Per the IRS
> Residential Clean Energy Credit guidance: "The credit is not available for any property placed in service
> after December 31, 2025," and separately "Used (previously owned) clean energy property is not eligible."
>
> A 2026-or-later buyout of this previously leased system therefore receives **no § 25D credit at all**.
>
> Consequences:
> - Every "net cost after ITC" figure below is understated by the assumed credit.
> - The decision thresholds (≤$10k buy / ≥$15k keep) are invalid as written.
> - "Bottom Line: The 30% ITC Changes Everything" is withdrawn.
>
> Also superseded: this document guessed ~$115/mo with a 3% escalator. The actual lease is **$88.02 year 1,
> 2.9% annual, $95.90 currently**, with a disclosed total of **$28,094.36**. Lease Term Start Date is
> **April 2023**; the §11(a)(i) purchase option opens **April 2028**, when the §11(b) recapture adder also
> reaches 0%.
>
> Current strategy: `solar/2026-09-21-solar-arbitration-design.md`.
```

- [ ] **Step 2: Strike the ITC rows in the three scenario tables**

For each of Scenario 1, 2 and 3, leave the gross figures and mark each ITC line
`~~30% federal ITC: −$X~~ **(NOT AVAILABLE — see banner)**`, and restate each net cost as equal to the gross.
Do not delete the tables — the buyout-versus-lease comparison is still useful once the credit is removed.

- [ ] **Step 3: Verify the corrections landed**

Run:
```bash
cd relocation/pass6 && grep -c "NOT AVAILABLE" SOLAR-BUYOUT-RESEARCH.md
grep -c "SUPERSEDED IN PART" SOLAR-BUYOUT-RESEARCH.md
```
Expected: at least `3`, then `1`.

- [ ] **Step 4: Commit**

```bash
git add relocation/pass6/SOLAR-BUYOUT-RESEARCH.md
git commit -m "docs(solar): correct dead 25D credit premise in buyout research"
```

---

## Final verification

- [ ] **Step 1: Full harness run**

Run: `cd relocation/pass6/solar && python3 sources/verify_citations.py`
Expected: `PASS — 47 citation(s) verified verbatim against pinned sources.`

Breakdown: 3 (Task 1) + 11 (Task 4) + 7 (Task 6) + 9 (Task 7) + 13 (Task 8) + 4 (Task 10) = 47, of which 29
belong to `04-JAMS-DEMAND.md`.

- [ ] **Step 2: Every deliverable exists and carries the disclaimer**

```bash
cd relocation/pass6/solar && for f in 00-CASE-STRATEGY 01-EVIDENCE-CHECKLIST 02-NOTICE-OF-CANCELLATION \
  03-SECTION-16b-NOTICE 04-JAMS-DEMAND 05-DOCUMENT-REQUESTS 06-DAMAGES-SCHEDULE 07-FILING-LOGISTICS \
  08-TIMELINE-AND-GATES 10-SECTION-1c-DEFENCE; do
  [ -f "${f}.md" ] || echo "MISSING ${f}.md"
  grep -q "NOT LEGAL ADVICE" "${f}.md" 2>/dev/null || echo "NO DISCLAIMER ${f}.md"
done; echo "done"; [ -f 09-SPOUSE-QUIET-TITLE.md ] && echo "ERROR: 09 must not exist yet"
```
Expected: `done`, with no `MISSING`, no `NO DISCLAIMER`, and no `ERROR`.

- [ ] **Step 3: Global prohibited-content sweep**

```bash
cd relocation/pass6/solar && grep -rin "trespass\|47-31\|quiet title" --include="0*.md" --include="1*.md" . \
  | grep -v "10-SECTION-1c-DEFENCE\|08-TIMELINE\|00-CASE-STRATEGY"
echo "sweep done"
```
Expected: `sweep done` with no hits. Mentions are permitted only in the reserve document, the trigger table, and
the index's "do not" list — never in an operative filing.

---

## Self-Review

**1. Spec coverage.** Spec §1 objectives → `00`. §2 decisions and timeline → Global Constraints, `08`. §3 forum →
Task 11. §4 limitations → Task 8 Step 4's Limitations paragraph. §5 parties → Task 6 Step 3. §6 Counts 1–7 →
Tasks 7–8. §6.1 defences → Task 8 Step 5. §6.2 reserved co-owner → Task 10, plus the prohibition rules and
sweeps. §7 relief → Task 8 Step 6. §8 evidence → Task 2. §9 deliverables → Tasks 2–12; `09` correctly excluded
and asserted absent. §10 correction → Task 13. §11 open items → SAVKAT footnote (Task 6) and `08` gate. §12
sequencing → Task 12. §13 risks → risk 3 in Task 11 Step 1.8, risk 11 in Task 10, risk 14 in Task 7 Step 4.
§14 research → Task 11's pre-filing gate. **No gaps.**

**2. Placeholder scan.** The only bracketed values are facts that genuinely do not exist yet — `[DATE]` for
service dates, `[SunStrong entity]` pending E9, and the `ILLUSTRATIVE` D2 figures — each labelled and each with a
named evidence item that supplies it. No "TBD", no "add error handling", no "similar to Task N".

**3. Type consistency.** `CITATIONS` entry keys (`doc`, `note`, `source`, `quote`) are identical across Tasks 1,
4, 6, 7, 8 and 10. Citation totals reconcile: cumulative 3 → 14 → 21 → 30 → 43 → 47, and the per-document
expectations match (Task 7 expects 16 for `04`, Task 8 expects 29 for `04`, Final Verification expects 47
overall). Identifier schemes are stable and non-overlapping: E1–E12 (evidence), R1–R20 (requests), D1–D4
(damages), ¶1–¶40 (facts), Counts 1–7.

Three quotes are deliberately registered against two documents each — § 42-135a's "not effective against the
buyer", § 42-138(a)'s tender language, and § 42-139(a)'s vesting language appear in both `02` and `04`. That is
intentional, not duplication: the notice and the pleading must say the same thing, and the harness checking both
is what guarantees they do not drift apart.

---

**Plan complete and saved to `relocation/pass6/solar/2026-09-21-solar-arbitration-plan.md`. Two execution
options:**

**1. Subagent-Driven (recommended)** — a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — execute tasks in this session using executing-plans, batch execution with checkpoints.

**Which approach?**
