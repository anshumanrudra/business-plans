# Pinned Primary Sources

Fetched 2026-09-21 unless noted. Re-verify hashes before filing; CGA publishes supplements each January.

| File | Source | sha256 |
|---|---|---|
| `lease.txt` | `pdftotext -layout sunpower_lease_oct_2022.pdf` | 5f3ce2d8418ae3bba3381dd4bd819429b3919b4a3eebf0c3f927f6ddaa32e9f7 |
| `case_accept.txt` | `pdftotext -layout Anshuman_20Rudra_20Case_20Acceptance_20Report.pdf` | c245f8cfd4d2362c01a1ac71d0f518a7c30b2304ddfc3b5ad988fa68d9eda986 |
| `ct740-home-solicitation.txt` | https://www.cga.ct.gov/current/pub/chap_740.htm | e7c981f76369cece961895bb4c0874fa270381c1c88f326c77c610723d556657 |
| `ct735a-cutpa.txt` | https://www.cga.ct.gov/current/pub/chap_735a.htm | 398c7b39a689e79df04e92ba7cea701076af42cfd754fa499bbdcddcfb24232d |
| `ct926-limitations.txt` | https://www.cga.ct.gov/current/pub/chap_926.htm | 799b1e02c117f41ee951284e3fa26390cebb10645df9060aa0d4620666e41cf1 |
| `jams-consumer-minimum-standards.txt` | https://www.jamsadr.com/consumer-minimum-standards/ (fetched 2026-09-22) | f80288c135c99c029999bb5d5981226d8b942ded41c62ebbe38af91283400931 |
| `jams-streamlined-rules.txt` | https://www.jamsadr.com/rules-streamlined-arbitration/ (fetched 2026-09-22) | aab119170be386c3cfb71ccb1b80f1b11809154dbadc76f5cb40bf9d88b8e4dd |
| `irs-25d-residential-clean-energy.txt` | https://www.irs.gov/credits-deductions/residential-clean-energy-credit (fetched 2026-09-22) | e75f5a0af8d6edb7a59bc31b6bda5fb354e8e1d011850c978c723d3b46a05e8d |

## Claimant's own documents (added 2026-09-23)

These four are E13 and E14 in `01-EVIDENCE-CHECKLIST.md`. They are **Claimant's own copies of documents the
seller's agent prepared**, not third-party-certified records; the certified originals are still to be requested
from Eversource under E7 and E13.

| File | Source | sha256 |
|---|---|---|
| `pura-ic-packet.txt` | `pdftotext -layout "ANSHUMAN RUDRA IC PACKET LEASE.pdf"` (10 pp., Eversource/PURA interconnection + RES packet, executed 2023-02-23) | 53d7e99cb51d33b94d63333cdd8c1eaf0c4fc613978b1a190b225e6621519a7a |
| `pura-res-revised.txt` | `pdftotext -layout "ANSHUMAN RUDRA  RES REVISED.pdf"` (2 pp., revised RES application, executed 2023-03-07) | 0d281dde3c8e6f4bcd30133a1b2efd23dba134b5936d466426f48e07351842cb |
| `savkat-pto-2023-05-12.txt` | `pdftotext -layout "SAVKAT SOLAR - TIME TO TURN ON YOUR SYSTEM!.pdf"` (SAVKAT email, 2023-05-12) | 39c1f87ceeee2d3d1ef76e2b41c93fb904fdb86a66cd10d7352ae830438abeeb |
| `sunpower-system-on-2023-05-15.txt` | `pdftotext -layout "SunPower Installation Update.pdf"` (SunPower Customer Service email, 2023-05-15) | e0d5b8f09a4ec1253808ed72ffcdbe794b88327ef46f8a2839a7a42d9888580d |

**Checkbox caveat — read before quoting any Yes/No answer from `pura-ic-packet.txt`.** The Eversource forms use
`☐`/`☒` glyphs that `pdftotext` renders with the mark adjacent to, and sometimes on the line below, the box it
belongs to. Every Yes/No answer relied on in the deliverables was read from a **rendered page image**
(`pdftoppm -r 130 -png`) and not from the text layer. Re-render before relying on any answer not already cited.

## Harness-unverifiable evidence — page 9 of the IC packet is a scan

**Read this before relying on any certification from E13 at a hearing.** Page 9 of
`ANSHUMAN RUDRA IC PACKET LEASE.pdf` is a **scanned raster page with no usable text layer**: it yields 119
characters against ~1,355 on page 8 and ~2,044 on page 10. No OCR tool is available in this environment. Its
content is perfectly legible in a rendered image, and was read that way, but it **cannot be matched by
`verify_citations.py`** and therefore carries none of the mechanical assurance every other quotation in this
document set carries.

Three of the most consequential certifications in the case sit on that page, and only on that page:

| Certification (page 9, image only) | Answer | Relied on in |
|---|---|---|
| "Will a filing be recorded in the land records of the customer's municipality pursuant to the contract for this system?" | **Yes** | `04` ¶ 28 and Count 3; `05` R7; `01` E2 |
| "Must the customer continue to make payments in the event of an extended system shutdown?" | **No** | `04` Count 4; `01` E13 |
| "Does the system installation contract conform to the requirements of the Connecticut Home Improvement Contractor Law?" | **Yes** | `08` decision gate 3; `01` E13 |

Also image-only on page 9: the **$0.314/kWh** starting utility rate and **4%** escalator behind the savings
estimate, contract and warranty transferability, and the Key Responsibilities Checklist.

**Why the asymmetry matters.** Pages 8 and 10 of the same document are digital pages with text layers — page 10
even carries the handwritten signature images over live text. Page 9 alone is a scan, and renders visibly rotated
and speckled. That is probably nothing more than one page having been printed, signed and rescanned, but it is an
obvious thing for a respondent to probe, and it should be closed rather than explained.

**Close it two ways before filing:** (1) obtain Eversource's or PURA's **certified copy** of the Third Party
Ownership Customer Disclosure — this is folded into the E7 request wording and into `05` R21; and (2) run an OCR
pass over page 9 and add the resulting text as a pinned source, at which point the three citations above can be
added to `verify_citations.py` (the entries are pre-written as comments in that file). Recorded as a pre-filing item
in `07-FILING-LOGISTICS.md` § 9.

**Non-rendering field data.** `pura-ic-packet.txt` also contains a block of bare numbers (twelve monthly values
and a set of per-kWh rates around $0.237–$0.315, dated 1/3/23) that does **not** appear on any rendered page. It
is unverified form-field residue, likely the twelve-month usage history behind the savings estimate. It is not
cited anywhere and must not be pleaded until its provenance is established.

**CGA caveat:** `www.cga.ct.gov` presents an incomplete TLS chain; `curl` succeeds where strict verifiers fail.
Confirm any quotation against the printed General Statutes before filing.
