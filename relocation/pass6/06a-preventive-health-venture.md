# The Venture: South Asian Preventive Health Intelligence

*Created 2026-09-06. **This is the business.** The immigration track it carries is specified separately in `01e-wife-l1a-eb1c-track.md` — that file is what counsel reads; this one is what she executes. Read `01e §8` (the firewall) before anything here.*

*⚠️ Competitive funding figures and regulatory rule status below are current to ~mid-2026 and this category moves fast. Treat named companies as real and verify current numbers before relying on them.*

---

## §0 — One page

| | |
|---|---|
| **What it sells** | Quarterly detection of **metabolic and renal drift** in South Asians, against ancestry-calibrated reference bands, with every interpretation signed by a licensed clinician. |
| **Why it exists** | Every consumer biomarker platform runs Western reference ranges and sells **snapshots against thresholds**. South Asians are systematically under-scored, and nobody sells **slope**. |
| **The founder story** | Under-detected chronic kidney disease. Her father's dialysis at ₹2.3–4.7L/yr (`05-parents-healthcare.md`) is the cost this product exists to prevent. **Hers, not yours** — which is why it survives `01e §8`. |
| **Structure** | Delaware C-corp (parent, MA-registered, US-citizen technical co-founder as CTO) + India Pvt Ltd (wholly-owned delivery subsidiary, Bengaluru). See `01e §1`. |
| **Pricing** | India **₹24,000/yr** · US/NRI **$1,200/yr** |
| **Capital** | **$50–150k**, no equity round in year one |
| **⚠️ The load-bearing number** | **~₹1.6–1.7Cr annualized revenue by month 15–18** (~150 India + ~125 US members) — because that is what funds the org chart the petition needs (`01e §2`). |
| **⚠️ The structural constraint** | Clinician review is legally required, so **gross margin is capped near 50%** until the B2B motion arrives. This is not a software-margin business yet. |

---

## §1 — The gap

Function Health, Superpower, InsideTracker, Whoop's labs product, and Bengaluru-based **Ultrahuman Blood Vision** all share two blind spots:

**1. Reference ranges built on predominantly Western cohorts.** South Asians cross into pathological risk at **lower BMI and lower waist circumference**, carry **elevated Lp(a)**, and develop coronary disease **earlier**. US cardiology guidelines handle this by *flagging South Asian ancestry as a risk-enhancing factor* — an admission that the models don't fit rather than a fix. The **MASALA** cohort exists precisely because of this mismatch; **ICMR-INDIAB** gives the Indian denominator (~100M diabetics, a larger prediabetic population).

**2. Thresholds instead of slope.** A UACR of 24 mg/g reads "normal" because the cutoff is 30. **A tripling from 8 to 24 is the actual signal.** Nobody sells slope.

**So the software is drift detection against ancestry-calibrated bands.** A data-and-modeling product, not a UI product — which is why it is defensible.

⚠️ **Explicitly dropped:** gut microbiome. The science does not yet support actionable advice and it invites credibility attacks on a product whose entire pitch is rigour.

⚠️ **Ultrahuman is the competitive fact to respect.** Bengaluru-based, already shipping ring + CGM + blood biomarkers, recruiting from the same talent pool in the same city. The wedge is not "do what they do" — it is calibration and slope, which they do not sell.

---

## §2 — The product

### The drift panel — deliberately small

| Domain | Markers |
|---|---|
| Glycemic | HbA1c, fasting insulin → **HOMA-IR** |
| Atherogenic | **ApoB**, **Lp(a)** (once — largely genetic), lipid panel, TG:HDL ratio |
| **Renal** | creatinine → eGFR, **cystatin C** as confirmatory, **urine albumin-to-creatinine ratio (UACR)** |
| Metabolic adjuncts | uric acid, ALT/GGT (MASLD — high South Asian prevalence), ferritin, vitamin D, TSH |
| Anthropometric | **waist circumference against South Asian thresholds**, not BMI |

> **Build the brand on UACR.** Earliest signal of diabetic and hypertensive kidney damage, costs almost nothing, and is **chronically under-ordered** in this population. It is the test that, ordered five years earlier, changes stories like her father's.

### The continuous layer

- **CGM: intermittent 14-day, not always-on** — cheaper and clinically sufficient for drift.
- **Home BP cuff** — morning/evening.
- **Sleep, HRV, resting HR** from whichever ring or watch the member already owns.

⚠️ **The proprietary asset hiding here:** glycemic response to **Indian carbohydrate loads** — idli, dosa, rice, roti. No Western dataset contains it.

### Cadence — the differentiator is trajectory, not snapshot

- Baseline: **full panel + 14-day CGM + 30-day wearable baseline**
- Quarterly: **narrow repeat** (HbA1c, UACR, eGFR, ApoB, ALT) — this is where the COGS discipline lives
- Annual: full panel

---

## §3 — The regulatory boundary IS the product spec

These are product rules, not disclaimers.

### FDA — the crux

- ✅ The software **displays and trends** values against South-Asian reference bands. *"Your UACR moved 8 → 24 mg/g across three quarters"* is data presentation.
- ❌ The software **never** issues a diagnosis, an unattended clinical risk determination, or a treatment recommendation. **FDA's 2022 clinical-decision-support guidance narrowed the enforcement-discretion safe harbour sharply**; crossing it makes this **Software as a Medical Device requiring a 510(k)** — unfundable at this capital level.
- ✅ Therefore **every interpretation is signed by a licensed clinician**: MBBS/MD under India's **Telemedicine Practice Guidelines 2020**; a physician licensed in the member's state in the US.

> ⚠️ **This is not a compliance tax — it is the business model.** The human review is what justifies $1,200/yr instead of $9/mo, and it is what a well-funded pure-software competitor cannot cheaply copy. It is also what caps gross margin near 50% (§5).

### Privacy — four regimes, all cheap now and expensive to retrofit

| Regime | What it means here |
|---|---|
| ⚠️ **FTC Health Breach Notification Rule** | Applies to non-HIPAA wellness apps. **No ad-tech on any authenticated page. Ever.** No Meta pixel, no ad-network SDK. Sharing health data with advertisers is exactly what GoodRx, Premom and BetterHelp were fined for. |
| ⚠️ **Washington My Health My Data Act** | **Private right of action.** Requires a separate *Consumer Health Data Privacy Policy* and separate consent. Reaches her customers regardless of where she incorporates. Build to it. |
| **HIPAA** | Probably **does not** apply to a direct-to-consumer service — but **will** the moment she contracts with US clinicians or labs as a business associate. Build HIPAA-grade controls from the start; it is table stakes for the B2B motion anyway. |
| **India DPDP Act 2023** | Data-fiduciary duties, consent notices, breach notification. ⚠️ Verify rule-notification status with Indian counsel. |
| **MA 201 CMR 17.00** | Triggered by the co-founder's location: a documented **Written Information Security Program**. |

Cross-border: Indian staff processing US consumer health data is normal and lawful, but needs a documented data-processing architecture. It becomes a diligence item for every B2B customer later — build it right once.

### Never touch

- ❌ **CLIA** — she will never run a lab.
- ❌ **Direct-to-consumer lab ordering in restricted states** — use an ordering-physician network.

---

## §4 — Build vs buy: the sync layer is a commodity

⚠️ **"Sync all wearables" is not a moat.** Terra, Vital, Rook, Spike and Metriport already sell unified wearable APIs to anyone. Rent it for ~$1–5/user/month and spend nothing building it.

That matters because the raw integrations are genuinely hard to obtain:

| Source | Reality |
|---|---|
| Apple HealthKit | **On-device only**, requires an app on the user's phone; forbids using the data for advertising |
| Google | Fit APIs retiring in favour of **on-device Health Connect** |
| Dexcom | Public API **delayed ~3 hours**; real-time behind a partnership |
| Abbott Libre | LibreView API effectively closed |
| Oura, Fitbit, Withings, Garmin, Omron | Cloud APIs available, aggregator-brokered |

**Year-one scoping decision: cloud-API devices only.** No native app in year one → no App Store review, no iOS/Android duplication, consumer view is responsive web. **Apple Health arrives in year two** with a mobile wrapper.

**Use Vital** rather than stitching vendors — it covers wearables **and** lab ordering on one contract.

**Labs:** India via NABL-accredited chains with home phlebotomy (Thyrocare, Redcliffe, Orange Health, 1mg) at ₹500–2,000 a panel versus $100–400 in the US. US via an ordering-physician network (Vital, Rupa, Evexia).

### ⚠️ Build the clinician console before the consumer app

Not a compromise — the correct order:

1. It is the **regulatory-safe surface**: clinician-in-the-loop is mandatory, so the primary UI should serve the person who signs.
2. It costs roughly **a third** of a polished consumer mobile app.
3. **It is the B2B asset.** Building it first makes the physician-practice motion available in year two rather than year four — and that is where software margins actually live (§5).

---

## §5 — Pricing and the honest margin story

| | India | US / NRI |
|---|---|---|
| **Price** | **₹24,000/yr** | **$1,200/yr** |
| COGS: annual full panel | ₹2,000 | ~$180 |
| COGS: 3 narrow quarterly panels | ₹3,000 | ~$240 |
| COGS: 1 CGM sensor | ₹4,000 | ~$120 |
| COGS: clinician review (2/yr + async) | ₹3,000 | ~$100 |
| **COGS total** | **~₹12,000** | **~$640** |
| **Gross margin** | **~50%** | **~48%** |

⚠️ **The US tier is $1,200, not $800.** At $800 the model does not close: 120 US members at $800 with $640 COGS yields too little gross profit to carry an India payroll. $1,200 is also defensible — it sits at the Superpower tier and includes quarterly trajectory plus clinician review, where Function Health's ~$499 buys an annual snapshot.

### ⚠️ The structural constraint, stated plainly

**Regulatory-mandated clinician review structurally caps gross margin near 50–60%.** This is a services-inflected business, not a software business, at consumer scale. Software margins arrive only with the **B2B motion** — selling the console to physician practices whose *own* clinicians do the review. That is the real reason to build the console first, and it validates the "eventually B2B" instinct.

### The commercial logic mirrors the immigration logic

Engineering, data analysis, care coordination and coaching sit at **Indian cost** while the price is **American**. ⚠️ One precision: the **physician signature must be US-licensed and cannot be arbitraged.** The labor around it can. This is why the petition in `01e` reads as honest — the corporate structure exists for a real commercial reason.

---

## §6 — Year-one budget and the revenue gate

**Year 1 = Nov 2026 → Oct 2027.** The co-founder as CTO of record removes a ₹32–38L Bengaluru CTO — the single largest line — and that capital goes into India engineering headcount instead, because the org chart in `01e §2` needs professional subordinates at the entity that employs her.

| Line | Timing | Cost |
|---|---|---|
| Clinical Data Scientist (₹16L) — owns the calibration engine | month 1 | ~$19k |
| Engineer #1 (₹16L) | month 1 | ~$19k |
| Engineer #2 (₹15L) | month 7 | ~$7k |
| Member Ops Lead (₹11L) | month 9 | ~$4k |
| Her salary (₹10L — modest but **real**: payroll, EPF, Form 16, ITR) | month 1 | ~$12k |
| Cloud, tooling, aggregator fees | ongoing | ~$16k |
| India compliance (statutory audit, GST, TDS, ROC) | ongoing | ~$3k |
| Delaware + MA entity, registered agent, US accounting | ongoing | ~$5k |
| Founders' agreement + IP assignment | Sept 2026 | ~$5k |
| India legal (DPDP, consents, contracts) | — | ~$4k |
| Content / GTM (her time; near-zero cash) | ongoing | ~$5k |
| **Year-one total** | | **~$99k** |

**Deliberate deferrals:** engineer #2 to month 7, member ops to month 9, and ⚠️ **US privacy + FDA counsel ($15–25k) into year two — but engaged BEFORE the first paying US member, not after.**

Her ₹10L is low on purpose. What matters for the petition is that the employment is **real and documented**, not large; the US salary *offered* in the L-1A carries more weight. *(Confirm with counsel — `01e §11` item 3.)*

Year-one revenue: product live ~month 5–7, India only. 60–100 members at ₹24,000 for a partial year ≈ **$14–21k**, gross profit ~$5–9k. **Net year-one burn ~$90–94k, leaving ~$56–60k.**

### ⚠️ The gate that decides everything

Year two needs: L-1A petition + business plan **$15–27.5k**, US privacy/FDA counsel **$15–25k**, EB-1C **$3.5k**, US Commercial Lead **$25–40k**, TP study **$2–4k** — **$61–100k against ~$58k remaining.**

> ⚠️ **So India + US revenue must cover the entire India payroll by month 15–18.** That payroll is **₹64L of staff plus her ₹10–15L ≈ ₹75–80L annualized** (`01e §2`). At the ~48–50% gross margin above, covering it needs roughly:
>
> | | Members | Revenue | Gross profit |
> |---|---|---|---|
> | India @ ₹24,000 | ~150 | ₹36L | ₹18L |
> | US @ $1,200 | ~125 | ~₹132L | ~₹66L |
> | **Total** | | **~₹1.68Cr** | **~₹84L** vs ~₹75–80L payroll |
>
> **~₹1.6–1.7Cr annualized by month 15–18. This is the single load-bearing assumption of both this file and `01e`** — not merely cash flow, but the thing that produces a filable org chart. Track it from month one, ahead of every other metric.
>
> ⚠️ **The 125 US members are the aggressive half.** The US launch only begins around month 10, so that is ~125 paying members inside 5–8 months, through community and referral channels only. If it looks unreachable by **gate G3 (30 Jun 2027)**, take the fork early rather than late.

If it slips, the fork is explicit: cut scope, add capital, or accept a **function-manager + reasonable-needs** petition (`01e §2`).

---

## §7 — Non-dilutive funding: worth real effort

Each of these does triple duty — cash, **independent government validation for the L-1A and EB-1C**, and record-building if she ever needs O-1A or EB-2 NIW (which `06-wife-career.md §9` found her weak on):

- **BIRAC BIG** (Biotechnology Ignition Grant) — non-dilutive, health-innovation focused; the calibration-engine thesis is a plausible fit.
- **Karnataka Elevate** — she will be Bengaluru-based, which is the qualifying condition.
- **DPIIT / Startup India recognition** — unlocks **§80-IAC** three-year profit exemption later, plus lighter compliance.

⚠️ **Apply, do not budget on it** — 6–12 months with milestone gates. *(Verify current ceilings and eligibility.)*

⚠️ **No equity round in year one.** Dilution complicates the FEMA position in `01e §1`, and a messy cap table weakens the story that she controls the company. Ownership is not legally required for L-1A, but simplicity is worth a great deal here.

---

## §8 — Team and the hiring plan

| Role | Location | When | Why |
|---|---|---|---|
| **CEO** (her) | Bengaluru, India-subsidiary payroll | Nov 2026 | `01e §2` — must **manage, not perform** |
| **CTO** (co-founder) | Massachusetts, Delaware payroll | Oct 2026 | Owns architecture and build. Gives the US entity real substance. |
| **Clinical Data Scientist** | Bengaluru | Nov 2026 | **Owns the calibration bands and drift models — this person is the IP** |
| Engineer #1 | Bengaluru | Nov 2026 | |
| Engineer #2 | Bengaluru | month 7 | |
| Member Ops Lead | Bengaluru | month 9 | ⚠️ JD **must state a degree requirement** (`01e §2`) |
| **Clinical advisor** — nephrologist or endocrinologist publishing on South Asian metabolic risk | any | Nov 2026 | Advisory equity or small retainer. Near-free, and materially strengthens grants, clinical credibility, and the petition. |
| Contract clinician panel | India + US | at launch | Per-review; US must be state-licensed |

⚠️ **Employees on payroll with EPF, not contractors.** USCIS discounts contractors heavily; the ~12% + 12% employer contribution is evidence spend.

⚠️ **Recruit before departure.** Post the roles in September 2026, interview by video, and have **signed offers for 2 November starts** so day one in Bengaluru is productive rather than recruiting. This is the difference between hitting and missing gate **G2** (`01e §7`) — the tightest gate in the plan.

---

## §9 — Distribution: the hardest problem, unsoftened

She has none. Consumer health CAC is brutal and the competition has hundred-million-dollar war chests.

⚠️ **For the $1,200 tier to work against $640 COGS, CAC must stay under roughly $150.** That number is unreachable through paid acquisition. It is reachable only through:

- **Community.** US alumni chapters (IIT/BITS/NIT networks are large, affluent and health-anxious), temples and cultural associations, South Asian employee resource groups at large US employers — ⚠️ **never through your access or Disney channels** (`01e §8`).
- **Content.** A rigorous, non-hypey newsletter on South Asian metabolic risk. Slowest channel, cheapest, compounds — and doubles as a personal record for a future O-1A or NIW.
- **Physician referral.** Indian-American PCPs and endocrinologists. High trust, low CAC, and the natural on-ramp to B2B.
- ❌ **Paid acquisition: avoid in year one.**

The co-founder's Massachusetts base is a genuine asset here — Boston has a large, affluent South Asian population and dense academic-medical networks.

⚠️ **Hard rule on pre-launch commitments:** collect **commitments and payment method on file, not charges**, until privacy and FDA counsel have scoped the product. The moment you charge for interpretation you are selling the thing that defines the regulatory line.

---

## §10 — The moat

❌ Not the integrations (commodity). ❌ Not the labs (commodity). ❌ Not the app.

✅ Three things compound, and none need capital:

1. A **longitudinal South-Asian biomarker dataset with matched wearable and dietary data** — genuinely rare.
2. **Calibrated reference bands and glycemic-response curves for Indian foods** — nobody has this at scale.
3. **The clinician network plus trust inside one specific community.**

---

## §11 — Phases

### Phase 0 — Pre-departure (6 Sept → ~10 Oct 2026) · scope: entity + banking + team offers

| Week | Do | Yields to |
|---|---|---|
| Sept 7 | Disney outside-activity clearance requested; **FEMA opinion commissioned**; startup lawyer engaged | — |
| Sept 14 | **Delaware C-corp formed**; **EIN** via co-founder as responsible party; **founders' + IP docs signed before any code**; Bengaluru roles posted | — |
| Sept 21 | **US business bank account** (co-founder in person, she a signatory); Stripe; MA foreign qualification; India candidate interviews by video | ⚠️ **Sept 23 `04c` rental gate** |
| Sept 28 – Oct 9 | **Signed offers for 2 Nov starts**; clinical advisor conversation | ⚠️ **Oct 7 `04c` flight-check** |

⚠️ **Explicit non-goals before the flight:** no code, no paying customers, no US privacy/FDA counsel, no India entity. All four are cheaper and easier from Bengaluru.

✅ **The co-founder relieves the EAD pressure.** A US-person co-founder can be the EIN responsible party and open the bank account as an officer, so her H-4 EAD expiry is no longer the binding constraint — she does not need to be a US-corp employee at all, since her qualifying year is India employment from November. Real relief in a badly overloaded month.

### Phase 1 — Nov 2026 → Oct 2027 (Year 1)

- **Nov 2026:** India Pvt Ltd incorporated as wholly-owned subsidiary (`01e §1`). She on payroll **day one** as Managing Director. Clinical Data Scientist + Engineer #1 start. **`01e §2` documentation regime begins.** First quarterly Delaware board minutes.
- **Dec 2026 – Feb 2027:** Calibration engine v1 from literature (MASALA, ICMR-INDIAB, KDIGO). Ingest via Vital, cloud-API devices only. Clinician console v1. **20–30 unpaid design partners** across both countries — also the seed dataset. *(Note: 1 Jan 2027 is when `04c`'s §871(d) withholding exposure starts.)*
- **Mar – Jun 2027:** Paid **India launch at ₹24,000/yr**. Engineer #2 at month 7. Target **60–100 paying India members**.
- **Jul – Oct 2027:** ⚠️ **US privacy + FDA counsel engaged — hard gate before the first paying US member.** **US launch at $1,200/yr** through community and referral channels. Delaware corp begins invoicing US members (~month 10). India scales toward 150–250. ⚠️ **30 Sept 2027 = `01d` EB-1A filing deadline** (trigger #2). **2 Nov 2027: her managerial year abroad completes.**

### Phase 2 — Nov 2027 → 2028

**31 Dec 2027 readiness deadline** (`01e §6`). **EB-1C filed as soon as eligible** for queue position. From Q1 2028 the L-1A is filable within 60 days — filed on trigger, held otherwise. ⚠️ Realistic US entry **late 2028, more likely Jan or Aug 2029** once the Mumbai interview queue is priced in.

### Phase 3 — Post-return

US-led growth; **B2B2C to US physician practices** and South-Asian-heavy employer populations — where software margins finally exist (§5).

---

## §12 — Kill criteria

Abandon or radically restructure if:

1. ⚠️ **Month 9 (Jul 2027):** organic/referral CAC above ~**$150** for the US tier. Spending more does not fix this.
2. ⚠️ **Month 12:** counsel concludes the product as designed is a **regulated device needing a 510(k)**. Redesign or stop.
3. ⚠️ **Month 15:** annualized revenue under **₹50L** with under **$40k** capital left. You cannot fund both payroll and the petition — **fund the petition.**
4. ⚠️ **Renewal intent under ~60%.** The entire thesis is quarterly trajectory, which lives or dies on renewal.
5. ⚠️ **Any asserted Disney IP claim** (`01e §8`).

> **Two framing points.** The business failing *later* does not invalidate a petition filed while it was genuinely operating. But the reverse matters more: ⚠️ **this must be a real company she would keep running regardless.** If it would be shut down the week after status was granted, that is a misrepresentation problem, not a business decision.

---

## §13 — Open items for licensed professionals

**US privacy / FDA / health-tech counsel** (engage by ~Jul 2027, before the first paying US member):
1. **FDA scoping opinion:** does the product as specified in §2–§3 stay within general wellness and outside the 2022 CDS guidance? Get it in writing.
2. **HIPAA business-associate analysis** once US clinician and lab contracts exist.
3. **FTC Health Breach Notification Rule** compliance review; confirm no ad-tech on authenticated surfaces.
4. **Washington My Health My Data Act** — separate consumer health data policy and consent flow.
5. **MA 201 CMR 17.00** Written Information Security Program.
6. Cross-border data-processing architecture (India staff, US consumer health data).

**Indian counsel:**
7. **DPDP Act 2023** consent notices, data-fiduciary obligations, breach process; current rule-notification status.
8. **Telemedicine Practice Guidelines 2020** compliance for Indian clinician review.
9. Lab-partner agreements; whether any activity touches the Clinical Establishments Act.

**India CA:** see `01e §11` items 6–10 (FEMA, resident director, FDI/FC-GPR, transfer pricing, DPIIT/§80-IAC).

**Immigration counsel:** see `01e §11` items 1–5.

---

## Cross-references

- `01e-wife-l1a-eb1c-track.md` — the immigration track this business carries. **Read §8 first.**
- `06-wife-career.md` — ⚠️ §6 hybrid income model **void** (she is not job-hunting); §§1–4 (edtech jobs, food-industry employment, baking) now **historical/deferred**; §9's independent-track conclusion **superseded**
- `05-parents-healthcare.md` — the founder story and the ₹2.3–4.7L/yr dialysis cost this product exists to prevent
- `04c-diy-rental-ops-ct.md` — the September gates this sprint yields to
- `08-TRACKER-JOURNAL.md` — G1–G5 and the September sprint tasks
