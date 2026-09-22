# Timeline and Gates — Lease #4593311

NOT LEGAL ADVICE — SELF-PREPARED DRAFT. Verify all research items in the spec §14 before filing.

**Purpose.** The phase sequencing for the case, the live operational clocks that actually govern what can be
done when, the §6.2 trigger checklist, and the two open decision gates. This is the document to check before
taking any action in the case — it says what phase we are in and what clock is running.

---

## Phase table

| Phase | Window | Actions | Status | Date completed |
|---|---|---|---|---|
| **0** | Week 1 | Serve `02` and `03`. Both cost nothing, start two independent clocks, and preserve every option including Count 7. Do this before relocating. | `[STATUS]` | `[DATE]` |
| **1** | Weeks 0–3 | Evidence items 1–4 (E1–E4) in parallel — the long poles. Land records and the refinance file may need in-person or notarised requests, so front-load them while in the US. | `[STATUS]` | `[DATE]` |
| **2** | ~Week 4 | 20-day tender window under § 42-139(a) closes; the title argument crystallises. | `[STATUS]` | `[DATE]` |
| **3** | Weeks 4–6 | File `04` with JAMS; pay $125; mail copies to the CT AG and DCP. | `[STATUS]` | `[DATE]` |
| **3a** | Not scheduled | Contingent only. `09` is built and filed if and only if a §6.2 trigger condition fires. No action unless triggered. | `[STATUS]` | `[DATE]` |
| **4** | Months 2–4 | Arbitrator selection (§19: agreed or selected under the Rules within 30 days); preliminary conference; request remote hearing under Rule 17(g). | `[STATUS]` | `[DATE]` |
| **5** | Months 3–8 | Rule 13 exchange within 14 days of claims, then targeted requests. | `[STATUS]` | `[DATE]` |
| **6** | ~Month 4 | §16(b) 90 days expire — amend to assert Count 7 as ripe if uncured. | `[STATUS]` | `[DATE]` |
| **7** | Months 8–14 | Remote hearing; written award with essential findings of fact and conclusions of law (§19). | `[STATUS]` | `[DATE]` |

---

## Live clocks — the operational heart of this document

Update this table every time a notice is served or a document is received. Do not rely on memory for any
deadline in this table.

| Clock | Authority | Starts | Length | Expires | Status |
|---|---|---|---|---|---|
| §16(b) cure period | Lease §16(b) | Service of `03` | 90 days | `[DATE — 90 days from 03 service date]` | `[not yet started / running / expired]` |
| § 42-139(a) tender window | § 42-139(a) | Service of `02` | 20 days | `[DATE — 20 days from 02 service date]` | `[not yet started / running / expired]` |
| § 42-138(a) refund period | § 42-138(a) | SunPower's receipt of `02` | 10 business days | `[DATE — 10 business days from receipt]` | `[not yet started / running / expired]` |
| JAMS Rule 13 exchange | JAMS Rule 13 | Receipt of claims (i.e., SunPower's receipt of `04`) | 14 calendar days | `[DATE — 14 calendar days from receipt of 04]` | `[not yet started / running / expired]` |
| CUTPA window | § 42-110g(f) | Rolling, 3 years from each act | 3 years | Acts before 2023-09-21 already barred | **closed** (for pre-2023-09-21 acts only; post-2023-09-21 acts remain live) |
| §11(a)(i) purchase option | Lease §11(a)(i) | Lease Term Start Date (April 2023) | 5 years | **April 2028** | pending |
| §11(b) recapture adder | Lease §11(b) | In-service date (~May 2023) | 5 years | **April 2028**, 0% thereafter | currently stepping 40%→20% |

Notes:
- The §16(b) and § 42-139(a)/§ 42-138(a) clocks do not start until `02` and `03` are actually served — see Phase
  0. Until service, all three read "not yet started."
- The Rule 13 clock does not start until the Demand (`04`) is filed and received by SunPower — it belongs to
  Phase 5, not Phase 0.
- The CUTPA window is not a single deadline; it is a rolling three-year bar applied act-by-act. It is marked
  "closed" only in the narrow sense that every act before 2023-09-21 is already time-barred (see
  `04-JAMS-DEMAND.md` Count 6). Acts on or after that date remain within the window on a rolling basis.
- The §11(a)(i) option and §11(b) recapture adder both resolve on the same date, April 2028, because both are
  keyed to five-year periods that started within weeks of each other (Lease Term Start Date vs. in-service
  date). The recapture adder is not a deadline to act by — it is a cost that shrinks the later the purchase
  option is exercised, reaching 0% exactly when the option's five-year window also closes.

---

## §6.2 trigger checklist — when to build and file `09`

`09-SPOUSE-QUIET-TITLE.md` does not exist and must not be drafted absent one of the following. Check this list
before any decision to build it:

- [ ] The arbitrator declines to grant equitable relief clearing the land records (e.g., accepts a SunPower
      argument, grounded in Lease §19's limits on the arbitrator's authority to alter the Lease's terms, as a
      bar to that relief).
- [ ] Counts 1–2 fail on the HSSA threshold **and** Count 7 (the §16(b) default / purchase-option floor) also
      fails, **and** SunPower refuses to release or subordinate its filing.
- [ ] SunPower asserts the §1(c)/§5(a)(xii) counterclaim addressed in `10-SECTION-1c-DEFENCE.md`. At that point
      deploy the prepared defence; her filing becomes comparatively low-risk because the exposure has already
      materialised.
- [ ] SunPower records any new or broader filing against the Real Property beyond what is currently of record.

If none of these are checked, `09` stays unwritten and unfiled, and the co-owner's non-signature stays
unpleaded everywhere except this checklist, `10-SECTION-1c-DEFENCE.md`, and the "Do not" list in
`00-CASE-STRATEGY.md`.

---

## Open decision gates

1. **Whether to serve `02` early.** Serving `02` alone (without `03`) starts the § 42-139(a)/§ 42-138(a) clocks
   but leaves Count 7's §16(b) predicate unstarted. The case strategy (see `00-CASE-STRATEGY.md` "Do not" list)
   is to serve `02` and `03` together in Phase 0, not `02` alone — this gate exists to record that the question
   has been considered and decided, not to reopen it without a reason to.
2. **Whether SAVKAT stays named.** SAVKAT, Inc. (the soliciting dealer) is currently named defensively only; it
   is not a party to the §19 arbitration agreement and any damages claim against it is time-barred (see
   CONTEXT.md Parties). Revisit only if new facts change either conclusion.
