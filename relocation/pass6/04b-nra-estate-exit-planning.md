# NRA Estate Tax, Exit Timing & Account Migration

*pass6 addendum, 2026-08-17. Companion to `04-financial-tax.md` (which covers residency, DTAA, FTC, the house, 401k contributions, and NRE/NRO banking). This file fills the gaps `04` did not cover at all: **US estate tax exposure as a non-resident alien, the departure-year 183-day capital-gains trap, the exact tax-free sale window, cost-basis reset, brokerage migration, and the US-citizen child's lifelong US tax obligations.***

*Triggered by a widely-shared r/returnToIndia financial write-up (June 2025). That post is a good checklist but **several of its claims are stale or wrong for your facts** — §9 below lists the corrections so you don't act on them.*

> **⚠️ NOT tax or legal advice.** Everything here needs sign-off from a **cross-border CPA**, a **US estate attorney**, and an **India CA**. Where I could not verify a claim against a primary source, it is marked **[VERIFY]**. Figures are 2026 rules; INR/USD ~₹86.

---

## 0. The Five Things That Matter Most

| # | Gap | Why it's urgent |
|---|---|---|
| 1 | **US estate tax: your exemption collapses from ~$15M to $60,000** once you're non-US-domiciled. On a ~$365k US-situs estate that's **~$97k of tax**. Nowhere in pass6. | Do estate planning **before** you leave |
| 2 | **Your wife gets NO marital deduction** — she's an Indian citizen (§2056(d)). Assets to her are taxed, unless a **QDOT**. | Changes your will/trust structure |
| 3 | **Do NOT sell US stock Oct–Dec 2026.** You'll have 273+ US days in 2026, so §871(a)(2) hits NRA capital gains at a flat **30%**. | The tax-free window is **2027–2028**, not Dec 2026 |
| 4 | **Your EB-1A filing contradicts a "closer connection to India" tax claim** — and an approved I-140 bars the Form 8840 exception outright. `01d` builds a US-ties folder that is adverse evidence for `04`'s tax position. | Cross-document conflict; resolve by **not** claiming early residency termination |
| 5 | **Your 7-year-old is a US citizen → lifelong US tax + FBAR/8938 filer.** Any Indian account, PPF, or mutual fund in his name creates PFIC/reporting problems. | Do not open Indian investment accounts in his name |

---

## 1. US Estate Tax — The Biggest Uncovered Risk

### A. The exemption cliff

As a US resident/domiciliary your estate exemption is ~$15M (2026). As a **non-US-domiciled non-citizen**, the unified credit drops to **$13,000 (IRC §2102(b)(1))** — which is exactly the tax on **$60,000** of taxable estate. Above that, graduated rates rise to **40%**.

⚠️ **There is no US-India estate tax treaty.** *(Verified against the IRS estate & gift tax treaty list — 15 countries: Australia, Austria, Canada, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, Netherlands, South Africa, Switzerland, UK. India is absent.)* So no treaty relief, no prorated larger exemption. The $60k is what you get.

### B. What is US-situs (in your estate) vs not

| Asset | US-situs? | Your exposure |
|---|---|---|
| **US house** | ✅ **YES** — US real property | Largest item |
| **401(k) / Roth 401(k) / IRA** | ✅ **YES** | ~$45k + 2026 contributions |
| **Stock of US corporations** (Robinhood, Schwab — incl. US-listed ETFs) | ✅ **YES** — regardless of where held or which broker | Variable |
| **HSA** | ✅ **YES** | Small |
| **529 plan** | ⚠️ **[VERIFY]** — treatment is unsettled | Small |
| **Tangible property in US** (the Tesla, furniture) | ✅ **YES** | ~$30k Tesla |
| **Cash in US bank accounts** | ❌ **NO** — excluded by **§2105(b)** | Safe |
| **Life insurance on your life** | ❌ **NO** — excluded by **§2105(a)** | Safe — and this is the funding tool (§3) |
| **Indian assets** (2 Bengaluru properties, NRE/NRO, EPF) | ❌ **NO** | Outside US estate |

### C. Your rough number

Illustrative — plug in real values with your CPA. Using the §2001(c) rate schedule less the $13,000 credit:

| US-situs gross estate | Estate tax owed |
|---|---|
| $60,000 | $0 |
| $150,000 | ~$25,800 |
| $250,000 | ~$57,800 |
| **$365,000** *(house ~$300k + 401k ~$65k)* | **~$96,900** |
| $500,000 | ~$142,800 |

**A ~$365k US-situs estate generates ~$97k of US estate tax — payable before your family sees the money.** Add brokerage balances and the Tesla and it climbs.

### D. ⚠️ Your wife does NOT get the unlimited marital deduction

This is the point almost every returning-NRI write-up misses, and it applies squarely to you: **IRC §2056(d) denies the marital deduction for property passing to a non-US-citizen spouse.** Your wife is an Indian citizen/OCI.

Normally "everything to spouse" defers all estate tax. For you it does **not** — assets passing to her are taxed above the $60k.

**The fix:** a **Qualified Domestic Trust (QDOT)** under §2056A, which restores the marital deduction if the trust meets strict rules (US trustee, distribution/withholding conditions). This must be **drafted into your will/trust before death** — it cannot be improvised afterward (a limited post-mortem reformation exists but is not something to rely on).

**Action:** when you execute the cross-border wills (`04 §8.C`), explicitly ask the estate attorney about **QDOT provisions** given a non-citizen spouse. This is a specific instruction — most template wills won't include it.

### E. Domicile ≠ income-tax residency — and the answer is genuinely uncertain for you

The Reddit post treats "NRA for income tax" and "non-domiciled for estate tax" as the same thing. **They are not.** Estate tax turns on **domicile** — physical presence plus *intent to remain indefinitely* — a subjective, facts-and-circumstances test. Income tax turns on day-counting.

Your facts point **both ways**, which is the uncomfortable part:

- **Toward continued US domicile** (→ full ~$15M exemption, but **worldwide** assets in the US estate base, including the Bengaluru properties): retained US house, US accounts, US-citizen child, a **pending EB-1A specifically asserting intent to return and work in the US**, a "time-boxed assignment" framing, stored Tesla.
- **Toward India domicile** (→ $60k exemption, US-situs only): family relocated, kids in Indian school, parents in your household, Indian employer, H-1B surrendered, long-term lease.

**Plan for the bad case.** You cannot control which way the IRS would characterize it, and the downside is asymmetric — so structure as if the **$60k exemption applies**, while keeping the domicile record clean. Note the perverse feature: the EB-1A evidence that helps immigration also argues for continued US domicile, which *raises* the exemption but *pulls your Indian real estate into the US estate*. Have the estate attorney and immigration counsel look at this together — do not let them work in isolation.

### F. Mechanics your executor will face

- **Form 706-NA** is the NRA estate return; filing is required once US-situs gross estate exceeds **$60,000** (due 9 months from death, extendable).
- **IRS transfer certificate:** Fidelity/Schwab/your 401k custodian **will not release assets to a foreign beneficiary** until the executor produces one, proving the estate tax was satisfied. This routinely takes **many months to over a year** and is the single biggest practical pain point.
- **Consequence:** your family in India could be locked out of the 401k and brokerage for a year or more, at exactly the moment they need liquidity.
- **Mitigation:** hold enough **India-side liquidity** (RFC/FCNR/NRE) plus **Indian life insurance** that nobody is waiting on a US transfer certificate to pay rent or school fees.

**Actions (§1):**
1. Ask the estate attorney about **QDOT provisions** for a non-citizen spouse.
2. Get a written **US-situs asset schedule** with values; recompute the exposure.
3. Have estate counsel + immigration counsel reconcile the **domicile vs EB-1A** tension.
4. Keep **12+ months of family living costs India-side** so no one depends on a transfer certificate.

---

## 2. Reducing US-Situs Exposure — Options and Honest Verdicts

| Option | Verdict for you |
|---|---|
| **Hold cash in US banks instead of US stocks** | ✅ **Works** — bank deposits are excluded (§2105(b)). Simple, real, no downside beyond FX/return drag. |
| **US term life insurance to fund the tax** | ✅ **Best single move** — proceeds are non-US-situs (§2105(a)) and liquid immediately. See §3. |
| **Gift US stocks to family as an NRA** | ✅ **Works for intangibles** — an NRA can gift **unlimited US stock with zero US gift tax** (intangibles are outside US gift tax for NRAs). ⚠️ **Does NOT work for the house** — US real estate gifts by an NRA **are** subject to US gift tax. ⚠️ Gifting also means giving up the asset irrevocably. |
| **Irish-domiciled ETFs via IBKR** | ⚠️ **Not yet, and not while you're a US person** — see §4. Correct in principle, badly timed in the Reddit post. |
| **UGMA/UTMA custodial account for the 7-yo** | ⚠️ **Narrow use only.** Removes assets from your estate, but: irrevocable, he controls it at majority, you may **not** use it for parental support (food/housing), hurts future US financial aid, and it makes him a US-taxpayer owner of the assets. Fine for an earmarked college pot; wrong for money you intend to live on. |
| **Foreign corporation / trust to hold the 401k** | ❌ **Impossible.** A 401k/IRA is legally tied to you individually. You cannot move it out of your estate. Plan for the tax; don't chase avoidance. |
| **Put the life policy in a US trust** | ❌ **Counterproductive** — can convert non-US-situs proceeds into a US-situs asset. **Own the policy directly.** |
| **Sell the US house before leaving** | ❌ Contradicts the retained-house strategy in `04a` and the EB-1A US-ties record. But note it *is* the only way to remove the largest US-situs item — revisit only if the rental thesis collapses. |

---

## 3. Life Insurance — Buy/Confirm BEFORE You Leave

Life insurance is the cleanest answer to the estate-tax problem: **proceeds on the life of an NRA are not US-situs (§2105(a))**, they bypass probate when a beneficiary is named, and they arrive fast — no transfer certificate.

**Time-critical:** US insurers largely **will not underwrite a new policy for someone already living abroad**, and non-citizen underwriting is restrictive even in the US. If you want US-dollar coverage, it must be **in force before departure**.

⚠️ **Check the residency/expatriation clause on any existing US policy.** Many US term policies are priced for a US resident and contain foreign-residence or extended-travel provisions. "Covered while traveling to India" is **not** the same as "covered after permanently relocating to India." **Get written confirmation from the carrier that coverage continues after permanent relocation** — this is a five-minute email that protects a seven-figure payout.

**Recommended structure (a 50/50 split, matching the practical consensus):**
- **US policy in USD** — sized to cover the estimated estate tax (~$100-150k) plus a buffer; pays in dollars, funds the US liability directly.
- **Indian term policy in INR** — larger face value, cheap, and a **far easier claim process for your wife from India**. This is the one the family will actually rely on day to day.

**Also:**
- Name **primary and contingent beneficiaries directly on the policy** — a will does not override a beneficiary designation.
- **Do not name a minor directly.** Insurers can't pay a large sum to a minor; it forces court involvement. Name a trust, or a custodian/guardian structure, and confirm it works cross-border.
- Write a **Letter of Instruction** (policy numbers, carrier contacts, claim steps, document locations) and leave copies both countries.
- Own the US policy **directly, not in a US trust** (§2 above).

**Actions (§3):** get written carrier confirmation on foreign residency; buy/top up US term **before departure**; buy the Indian term policy; fix primary + contingent beneficiaries; write the Letter of Instruction.

---

## 4. Departure-Year Timing — The 183-Day Trap and Your Real Tax-Free Window

### A. The trap that voids the "sell in December" plan

**IRC §871(a)(2):** a nonresident alien present in the US **183 days or more during the taxable year** pays a flat **30%** on US-source capital gains. *(Verified against the statute.)*

You plan to depart **~1st week Oct 2026**, so you'll have **~273+ US days in calendar 2026.** Therefore:

> ⚠️ **Selling appreciated US stock in Oct–Dec 2026 — even after you're an NRA — triggers a flat 30% US tax on the gains.** The "move in August, sell in December, pay nothing" strategy circulating on Reddit **does not work in your departure year.** (The original author corrected this in the comments; the post body still misleads.)

The stated reason for the December rush — beating a January remittance tax — is also moot (§9.1).

### B. Your actual residency map

| Period | US status | India status | Foreign gains taxed? |
|---|---|---|---|
| Jan–Sep 2026 | Resident | Non-Resident | US: yes |
| **Oct–Dec 2026** | NRA but **273+ US days** | Non-Resident | ⚠️ **US: 30% flat** — do not sell |
| **Calendar 2027** | **NRA** (auto — see C) | NR (FY26-27) → **RNOR** (FY27-28) | ✅ **Neither** |
| **Calendar 2028** | **NRA** | **RNOR** (FY27-28, FY28-29) | ✅ **Neither** |
| Jan–Mar 2029 | NRA | **RNOR** (FY28-29 ends 31 Mar 2029) | ✅ Neither |
| **FY2029-30 onward** | NRA | ⚠️ **ROR** — worldwide income taxable | ❌ Taxed in India |

> ### 🎯 **The golden window is 1 Jan 2027 → 31 Mar 2029.** Not December 2026.

⚠️ **Correction to `04 §1`:** it says RNOR runs "~2-3 years" without pinning the end. Mapped against an Oct 2026 arrival, **ROR begins FY2029-30** (by then you fail both the 9-of-10-years test and the 729-day test). Since you plan to return to the US around Year 2.5-3 (~early-to-mid 2029), **you may exit before ROR ever bites** — but confirm the day counts annually, because RNOR is **re-tested every single FY** (it is not an automatic 2-3 year grant).

### C. ✅ Your 2027 NRA status is automatic — but keep US visits under 31 days

Substantial Presence Test for 2027 = days(2027) + ⅓(273 in 2026) + ⅙(365 in 2025) = days(2027) + 91 + 61 = days(2027) + 152.

- The SPT also requires **31+ days in the current year**. So **if you spend fewer than 31 days in the US in 2027, you are automatically a nonresident** — no closer-connection argument, no Form 8840, no election needed.
- Even above 31 days you'd need days(2027) < 31 to stay under 183 — so **31 days is the operative ceiling either way.**

> **Rule: keep total US presence under 31 days in calendar 2027 (and watch 2028).** This single constraint secures your NRA status cleanly. Fortunately EB-1A consular processing happens **in India** (Mumbai/Delhi), so it shouldn't force US trips — verify against `01d`.

### D. The cost-basis reset — a real tactic pass6 doesn't mention

Inside the golden window, gains are untaxed in **both** countries. So you can **sell appreciated US positions and immediately rebuy them**, resetting your cost basis to current market at **zero tax cost**.

- Your basis becomes today's price, so gains that accrue *before* the window are permanently wiped from the future taxable base.
- Later sales — after you're ROR in India, or a US resident again — are computed from the **higher** basis.
- **No US wash-sale problem:** §1091 disallows wash-sale *losses* only. It does not affect gain recognition, so a same-day repurchase is fine when you're harvesting **gains**. *(Confirm with the CPA if you also intend to harvest losses.)*
- You do **not** have to repatriate the money — this is purely a basis exercise. Keep the proceeds in the US brokerage.

### E. ⚠️ Do not remit foreign income to India in the year you earn it

RNOR shields foreign-source income **provided it is not received in India** in that year. So:
- **Realize gains into your US brokerage/bank account**, not into an Indian account.
- Remit later — after the RNOR year closes — as **accumulated capital**, not current-year income. Transfers of past savings aren't income.
- Keep clean records tying each remittance to a prior-year realization. This paper trail is the whole defense.

### F. Departure-year US filing: **recommend full-year resident for 2026, not dual-status**

The Reddit post pushes a dual-status return. For you, that's probably the wrong call:

- **Dual-status costs you real money:** no standard deduction, and **no married-filing-jointly**.
- ⚠️ **The closer-connection exception is barred for you.** IRS guidance is explicit that anyone who "personally applied, or took other steps" toward LPR status — and it **names Form I-140 and I-485** — is **ineligible**. You have an approved I-140 (2021 PD) and are filing EB-1A. *(Verified on the IRS closer-connection page.)* Whether that statutory bar also reaches the §7701(b)(2)(B) residency-*termination*-date test is a **[VERIFY]** question for your CPA — but either way, your EB-1A filing is **adverse evidence** on any closer-connection showing.
- ⚠️ **Cross-document conflict:** `01d §0` deliberately builds a US-ties folder (retained house, US-citizen son, US accounts, stored Tesla, "coming to the US to continue work" statement under 8 CFR 204.5(h)(5)). Every one of those facts argues you have a **closer connection to the US**, not India. Do not let your CPA file an aggressive early-termination position that your immigration file directly contradicts — a conflicting record is worse than either position alone.

**Resolution — and it's clean:** you don't *need* early residency termination, because §4.A already tells you not to realize gains in 2026. So:

> **File 2026 as a full-year US resident (MFJ + standard deduction), realize gains in 2027–2028 instead.** You get the better filing status, you avoid the 30% §871(a)(2) hit, you keep your EB-1A narrative consistent, and you lose nothing — because the tax-free window was never in 2026.

Your Oct–Dec 2026 Disney India salary becomes US-reportable under this approach, but it's one quarter of an Indian salary and the **Foreign Tax Credit (Form 1116)** should absorb it. From 2027 you file **1040-NR** only for US-source income (the rental).

**Actions (§4):** confirm the full-year-resident-2026 recommendation with the CPA in writing; **no US stock sales Oct–Dec 2026**; calendar the 2027–2028 sale/basis-reset window; cap 2027 US presence under 31 days; keep the day-count log from day one.

---

## 5. Brokerage & Retirement Account Migration — Do It Before You Fly

Most of this must happen **while you are still a US resident**. Doing it from India is harder or impossible.

### A. Robinhood — resolve this before departure (sharpens the open item in `08`)
**Robinhood does not support non-US-resident account holders.** Expect restriction or forced closure once you change your address, and it will not do a 401k→IRA rollover for a non-resident. Options:
1. **ACATS transfer in-kind to a NRA-friendly broker while still a US resident** — preferred; preserves positions and basis, no taxable event.
2. Liquidate before departure — but that realizes gains in **2026 at resident rates**, wasting the 2027 window.
3. Do nothing — worst case; risks a forced liquidation at a time you don't choose.

> **Recommendation: transfer in-kind to Schwab International or IBKR before departure, then realize gains in 2027.** This captures both benefits.

### B. Which custodians work for an NRA
- **Interactive Brokers (IBKR)** — best NRA support; also the route to non-US ETFs. **Open while still in the US** (onboarding is far easier as a US resident).
- **Charles Schwab** (incl. Schwab International) — generally workable; already your planned US hub.
- **Fidelity** — generally maintains existing accounts with a foreign address; new accounts harder.
- ⚠️ **Confirm in writing, from the custodian's international desk — not a retail branch.** Branch staff are unreliable on non-resident policy (a recurring theme in the Reddit thread: branch said "no foreign address," the international desk said yes).

### C. File Form W-8BEN with every institution
On becoming an NRA, file **W-8BEN** with each bank, broker, and the 401k custodian. It certifies foreign status, prevents incorrect backup withholding, and **claims the US-India treaty rate on dividends instead of the 30% statutory rate** *(exact treaty rate for portfolio dividends — **[VERIFY]** with the CPA against Article 10)*. Without a valid W-8BEN you default to 30% and may face account restrictions. **Re-file every 3 years** — they expire.

⚠️ Note the asymmetry: **W-8BEN stops withholding on capital gains but not on dividends.** Dividends are always taxed at the treaty/statutory rate for an NRA — the gains exemption doesn't extend to them. Factor that into whether you hold dividend-heavy US funds.

### D. Any 401k → IRA rollover: do it BEFORE you leave
Some custodians won't process a rollover for a non-resident. If a rollover or Roth conversion is part of the plan, **execute it while still a US resident** — or at minimum confirm in writing that your custodian will do it for an NRA.

⚠️ **But note the tension with `04 §5.J`,** which says to do conversions *inside* the RNOR window. Both can't always be true. Resolve as: **administratively, roll over before departure; tax-wise, time any taxable conversion into the RNOR window.** A Roth conversion is a *US-taxable* event in the conversion year regardless of India — so the "do it in RNOR" logic protects you from *India* tax, not US tax. Get the CPA to model this explicitly; `04 §5` currently glosses over it.

### E. If you ever take a 401k distribution as an NRA
`04 §5.I` correctly says don't. If it happens anyway:
- **Mandatory withholding** (commonly a flat 30%) at source — a prepayment, not the final tax.
- **NRAs cannot claim the standard deduction** on Form 1040-NR — so taxable income is higher than a resident's on the same withdrawal.
- The treaty may reduce the rate on the earnings portion **[VERIFY]**; reconcile on the 1040-NR.
- The 10% early-withdrawal penalty still applies under 59½.

**Actions (§5):** open IBKR **now**, while in the US; ACATS Robinhood → Schwab/IBKR before departure; get written NRA policy from each custodian's **international desk**; file W-8BEN everywhere on status change and calendar the 3-year renewal; decide the rollover question before flying.

---

## 6. India-Side Gaps

### A. RFC account — more useful than `04 §8.B` suggests
`04` mentions RFC only as a redesignation destination when RNOR ends. It's more than that:
- An **RFC (Resident Foreign Currency)** account lets a returning NRI **hold savings in USD inside India** — not just new earnings, but transferred existing savings.
- **Interest is tax-free in India during RNOR** (taxable once ROR).
- ⚠️ **Limitation:** RFC is a deposit/FD product. You **cannot** invest in equities from it without converting to INR. It's an FX-risk hedge and a liquidity pool, not an investment account.
- ⚠️ To fund it you must remit **in USD**. Most transfer services (including Wise) convert to INR on the way. Your bank can send USD as USD for a flat fee (~$45). **Use a bank wire, not Wise, when the destination is RFC** — this contradicts the blanket "use Wise" guidance in `04 §6`, which is right for INR but wrong for RFC.

### B. ⚠️ Section 89A / Rule 21AAA / Form 10EE — 401k timing-mismatch relief
**Entirely missing from pass6, and directly relevant to your 401k.**

The problem: India may tax retirement-account **growth on an accrual basis** while the US taxes only on **withdrawal** — a timing mismatch that can create Indian tax on gains you haven't received, with no matching foreign tax credit.

**Section 89A** (with **Rule 21AAA**, elected on **Form 10EE**) lets a resident defer Indian taxation on income from a retirement account in a **notified country** until the year of withdrawal, aligning the two systems.

**[VERIFY] with your India CA — I could not retrieve primary text (Indian government sites blocked automated access):**
1. Is the **US a notified country** for §89A? (Commonly reported as US/UK/Canada — confirm.)
2. **Form 10EE deadline** — believed due **on or before the ITR due date for the first relevant year**, and the election is understood to be **irrevocable**. Missing the deadline may forfeit the relief permanently.
3. Does it cover **Roth** accounts, or only pre-tax 401k/IRA? (This matters a lot to you — see `04 §5.E` on India not recognizing Roth status.)
4. Does the election interact with RNOR (which already shields foreign income), i.e. is it only needed from the year you become **ROR**?

> **Why this is urgent despite the ROR date being ~FY2029-30:** if the election must be made in the *first* year the income arises and is irrevocable, a wait-and-see approach can silently forfeit it. **Put this on the CA's list at the first India return, not later.** PwC's India summary notes that relief rules for overseas retirement withdrawal timing mismatches remain partly unprescribed — so expect ambiguity and document your position.

### C. ⚠️ Schedule FA + Black Money Act — severe penalties
Once you are **Resident and Ordinarily Resident**, you must disclose **all foreign assets** in **Schedule FA** of the Indian return — US house, 401k, brokerage, bank accounts, insurance.
- Non-disclosure exposes you to the **Black Money (Undisclosed Foreign Income and Assets) Act**, with a penalty commonly cited at **₹10 lakh per year** plus prosecution risk. This is not a filing nicety.
- **RNOR is generally exempt** from Schedule FA — which is exactly why the **ROR transition (FY2029-30)** is a hard compliance trigger, not just a tax-rate change.
- If you leave before ROR, this may never apply — but if the return slips, it does. **Add it to the RNOR-end calendar trigger in `04 §8.B`.**

### D. Indian capital gains — `04` has no foreign-asset gains rules
For gains realized **after** RNOR ends (or on Indian assets), the post-23-July-2024 regime applies *(verified via PwC India)*:
- **Indexation was largely removed.** LTCG on unlisted/foreign assets is now **12.5% without indexation**. The old "20% with indexation" is gone for these. Immovable property acquired before 23 July 2024 keeps a 12.5%-no-indexation vs 20%-with-indexation choice.
- **Holding period:** >24 months = long-term for foreign/unlisted shares and ETFs (12 months applies to Indian-listed securities and equity MFs).
- Listed Indian equity: **STCG 20%**, **LTCG 12.5%** with ₹1.25L exempt.
- LTCG surcharge is capped at 15%; capital losses carry forward 8 years.

### E. PFIC — the constraint the Reddit post ignores
`04 §8.D` correctly flags Indian mutual funds as **PFICs**. Extend the same logic:
- **Irish-domiciled ETFs are also PFICs for US persons.** The Reddit post recommends them without mentioning this. They only make sense **after** you are cleanly out of US-person status — and given your EB-1A plans to make you a US person again, the window in which they're advantageous may be short and the compliance drag long. **Don't buy them on the strength of that post.** Model it with the CPA against your actual GC timeline.
- ⚠️ **Never buy Indian mutual funds, ULIPs, or PPF in the US-citizen 7-year-old's name** — see §7.
- Some Indian AMCs refuse US-person NRI money outright (FATCA burden). Check before assuming SIPs can continue.

---

## 7. ⚠️ Your US-Citizen 7-Year-Old Has Lifelong US Tax Obligations

**Completely absent from pass6, and a genuine trap** — this is the single easiest way for this move to create a durable problem.

Your younger son is a **US citizen**, so he is a **US person for tax purposes for life**, regardless of where he lives:
- **He must file US tax returns on worldwide income** once he has income above the filing thresholds.
- **FBAR (FinCEN 114)** applies to *his* foreign accounts if the aggregate exceeds **$10,000** — including accounts a parent opens for him. A minor is required to file; the parent signs.
- **Form 8938 (FATCA)** may also apply.
- ⚠️ **Any Indian mutual fund, ULIP, or similar in his name is a PFIC** — punitive US tax and a **Form 8621 per fund, per year**, potentially for decades.
- ⚠️ **PPF / Sukanya Samriddhi / minor-account gift schemes** are exactly what Indian relatives suggest for a child, and they are **US-tax-toxic** for him.
- **Form 3520:** if he receives gifts from you (as NRAs) totaling **over $100,000** in a year, **he** must file Form 3520. The gift isn't taxable income to him — but the reporting is mandatory and penalties are steep. This directly constrains the §2-gifting strategy: gift to him and you trigger his 3520.
- His US citizenship is also what makes the estate-tax picture asymmetric across your two children — worth raising with the estate attorney.

> **Rules to adopt now:**
> 1. **Do not open Indian mutual fund, PPF, ULIP, or insurance-investment accounts in the 7-year-old's name.** Cash savings accounts only, kept small.
> 2. **Tell your parents and sibling** — well-meaning relatives open these for grandchildren. Say no in advance.
> 3. **Track any gifts to him** against the $100k/yr Form 3520 threshold.
> 4. Add "**7-yo's US tax/FBAR position**" to the cross-border CPA's scope explicitly. He is a separate client matter, not a footnote on your return.

*(By contrast, your 13-year-old is an Indian citizen on H-4 — no US tax obligations once he's no longer a US resident. The asymmetry between the two children is real and needs separate handling in both the wills and the tax plan.)*

---

## 8. Keeping US Financial Infrastructure Alive

Partly covered in `03`; the finance-specific pieces belong here.

### A. Credit cards — downgrade, don't cancel
- **Keep 1-2 cards**: your **oldest** account (protects credit-history length) and at least one with **no foreign transaction fee** (~3% otherwise).
- **Downgrade rather than cancel** high-annual-fee cards — a "product change" to a no-fee card in the same family keeps the credit line and account age, protecting your score. Cancelling shortens history and cuts total credit.
- **Set autopay for the full statement balance** from a funded US account. A missed payment from 8,000 miles and 10.5 time zones away is an avoidable, disproportionate hit.
- Keep US mailing address current on every retained card.
- ⚠️ **Card renewal:** expiring cards need a deliverable US address. Confirm the issuer will mail to your forwarding address, or plan to have a trusted relative forward it.
- **Why it matters for you specifically:** you intend to **return to the US in 2.5-3 years** and will need mortgage/auto/rental credit immediately. A preserved score is worth real money — this is not housekeeping.

### B. Mail forwarding — not currently in the plan
Set up a **virtual mailbox / mail-forwarding service** (e.g. Traveling Mailbox, Earth Class Mail) or use a trusted relative's address. You need a reliable US address for cards, tax notices, insurance, brokerage statements, and IRS correspondence. ⚠️ Note this is **already partly planned in `01d §0`** for the EB-1A address of record — **use the same address** so the immigration and financial records are consistent.

### C. US phone number for 2FA — the item that breaks everything else
Losing your US number silently locks you out of bank and brokerage 2FA. Practical experience from the thread:
- **Cheapest reliable approach:** keep a **T-Mobile (or any T-Mobile-network) prepaid line** (~$10-15/mo) on **Wi-Fi calling**, with the phone in airplane mode + Wi-Fi. Works for calls and OTPs from India.
- **Google Voice is unreliable for OTPs** — many institutions block VoIP numbers, and the VoIP database updates over time, so a number that works today can stop working later. **Do not make it your only 2FA path.**
- ⚠️ **Porting your real number to a VoIP provider can immediately break bank OTPs.** Reported first-hand: porting from AT&T triggered instant OTP failure at both BofA and Chase.
- **Recommendation: keep the physical US SIM on a cheap prepaid plan.** Treat it as critical infrastructure, not a $15 nuisance.

### D. Bank foreign-address policy — go to the international desk
Retail branches routinely say "we can't add a foreign address"; international/premium customer service often can. **Get it in writing from the right desk.** Also:
- Do **small periodic transactions** so accounts don't go dormant (dormancy triggers freezes and, eventually, escheatment).
- ⚠️ **The real risk is an account freeze you can't resolve from India.** Mitigate with a **US financial power of attorney** for a trusted person, plus your **RLT co-trustee** (`04a §4`) who can already act on the house.

### E. Segregating consulting income — probably unnecessary (see §9.3)
If you or your wife do US consulting from India, you'll file **W-8BEN** with clients and report on **Form 1040-NR**. You do **not** need a US work visa — the work is performed outside the US — and your SSN suffices for their reporting. **Registering as an Indian sole proprietor is simpler** than a US LLC (no US state/federal entity filings). But see §9.3: the elaborate two-bank-account scheme the Reddit post recommends rests on a repealed rule.

---

## 9. ⚠️ Corrections — Do Not Act On These Reddit Claims

The source post is from **June 2025** and several claims are stale or wrong. Each correction below is verified against a primary source.

**1. "A 3.5% remittance tax hits transfers to India — sell before January."** ❌ **Wrong, and it drove a harmful conclusion.**
The enacted law (**IRC §4475**, OBBBA §70604, Pub. L. 119-21) imposes **1%**, not 3.5%, and it applies **only** where "the sender provides cash, a money order, a cashier's check, or any other similar physical instrument." **Bank and brokerage transfers — including Wise ACH — are exempt.** Applies to transfers after 31 Dec 2025. *(Verified: IRS Notice 2025-55.)*
→ **Consequence: the entire "sell in December 2026 to beat the January tax" rationale is void** — and following it would have walked you into the 30% §871(a)(2) trap in §4.A. **Wire normally; ignore the remittance tax.**

**2. "Irish ETF gains get 20% with indexation in India."** ❌ **Outdated.** Indexation was **removed** for these assets from 23 July 2024. Foreign ETFs held >24 months are now **12.5% without indexation**. The post's worked ₹714 example is obsolete. *(Verified: PwC India.)*

**3. "Keep two US bank accounts so consulting deposits don't make your personal account US-situs."** ❌ **Based on a rule repealed in 1966.** The **pre-1966** version of §2105 turned on whether the decedent "was not engaged in business in the United States." Current **§2105(b)** instead uses the §871(i)/§871(h) interest-exemption tests, and **attaches no trade-or-business condition to bank deposits.** *(Verified against the statute and its amendment notes.)* → **Skip the elaborate two-account scheme.** Separate accounts are fine for bookkeeping; they're not buying you estate-tax protection.

**4. "You must be physically in the US to apply for Social Security."** ❌ **Overstated.** You can file through the **Federal Benefits Unit** at the US Embassy/Consulate in India. No US trip required.
✅ **But the real issue the post misses — the Alien Nonpayment Provision (§202(t)):** as a **non-citizen** outside the US for **6 consecutive calendar months**, benefits are **suspended** unless an exception applies. **Good news for you:** SSA's country chart lists **India as "Yes"** for the **40-quarters-of-coverage** and **10-years-US-residence** exceptions (AEC 3/4) — so with 40 QCs (~10 years of US work) or 10 years' US residence, you can be paid while living in India. India has **no** totalization or treaty-based exception, so those two routes are the only ones. *(Verified: SSA POMS RS 02610.010 / RS 02610.015.)*
→ **Action: pull your SSA earnings statement now and count your quarters of coverage.** If you're near but under 40 QCs, that's a concrete reason to value remaining US-payroll quarters — and it's a fact you can only act on before leaving.

**5. "NRA capital gains are tax-free — sell any time after you become an NRA."** ❌ **Not in your departure year** — §871(a)(2)'s 183-day rule. The author corrected this in the comments; the post body still misleads. See §4.A.

**6. "There's a guaranteed 2-3 year RNOR window."** ❌ **RNOR is re-tested every FY.** It is not a fixed grant. Confirm status annually (`04 §1` gets this right; the post doesn't).

**7. "Use a will."** ⚠️ **Incomplete** — a US will forces probate. `04a §4` already recommends a **revocable living trust** for the house, which is correct. Add the **QDOT** point from §1.D, which neither the post nor pass6 covers.

**8. "$190,000 non-citizen-spouse gift limit."** ⚠️ **Applies to tangible/real property only.** For an NRA gifting **intangibles** (US stock), there's no US gift tax at all — so the annual exclusion is beside the point. But note the corollary the post buries: **US real estate gifted by an NRA IS subject to US gift tax** — so your house cannot be gifted away cheaply.

---

## 10. Consolidated Action List

### Before departure (~Oct 2026) — most of this cannot be done from India
1. **Get written carrier confirmation** that existing US term life stays in force after **permanent** relocation. *(5-minute email, protects a 7-figure payout.)*
2. **Buy/top up US term life** sized to the estimated estate tax (~$100-150k + buffer); own it **directly, not in a trust**; set primary + contingent beneficiaries; **never name a minor directly**.
3. **Buy Indian term life** (the policy your wife will realistically claim on).
4. **Estate attorney: QDOT provisions** for a non-citizen spouse — add to the cross-border wills workstream in `04 §8.C`.
5. **Reconcile domicile vs EB-1A** — estate counsel + immigration counsel in the same conversation.
6. **Open IBKR now** (easier as a US resident).
7. **ACATS Robinhood → Schwab International or IBKR in-kind** — resolves the open item in `08`; do **not** liquidate in 2026.
8. **Written NRA policy from each custodian's international desk** (not a branch): Schwab, Fidelity, 401k custodian, banks.
9. **Any 401k→IRA rollover: do it now**, while still a US resident.
10. **Pull your SSA earnings statement**; count quarters of coverage toward 40.
11. **Set up mail forwarding** — same address as the `01d §0` EB-1A address of record.
12. **Keep a T-Mobile-network prepaid US line** with Wi-Fi calling for 2FA. Do **not** rely on Google Voice; do **not** port your real number to VoIP.
13. **Downgrade** (don't cancel) high-fee cards; keep the oldest + a no-FX-fee card; autopay full balance.
14. **Execute a US financial power of attorney** for a trusted person (account-freeze insurance).
15. **US-situs asset schedule with values** → recompute the estate-tax exposure.
16. **Apostille** the marriage certificate and the 7-yo's birth certificate *(already in `00`/`02` — confirm done)*.

### Departure year (Oct–Dec 2026)
17. ⚠️ **Do NOT sell appreciated US stock.** 30% flat under §871(a)(2).
18. **File W-8BEN** with every bank, broker, and the 401k custodian on status change; calendar the 3-year renewal.
19. **Confirm with the CPA in writing: file 2026 as a full-year US resident** (MFJ + standard deduction), not dual-status — and confirm this is consistent with the EB-1A record.
20. **Start the day-count log** for both countries from day one.

### The golden window (Jan 2027 → Mar 2029)
21. **Realize US capital gains here** — untaxed in both countries.
22. **Run the cost-basis reset** (sell + immediately rebuy) on long-held appreciated positions.
23. ⚠️ **Keep proceeds in US accounts in the year realized** — do not remit to India that year. Remit later as accumulated capital; document the trail.
24. ⚠️ **Keep US presence under 31 days in calendar 2027**; watch 2028.
25. **India CA: Form 10EE / §89A** at the **first** India return — confirm US-notified status, deadline, irrevocability, and Roth coverage before the chance is lost.
26. **Fund RFC via a USD bank wire, not Wise** (Wise converts to INR).
27. **Confirm RNOR status every FY** — it is re-tested annually.

### Ongoing / triggers
28. **RNOR-end trigger (FY2029-30)** → redesignate NRE/NRO → resident/RFC (`04 §8.B`) **and** add the **Schedule FA / Black Money Act** disclosure obligation to that same trigger.
29. **Never open Indian MF/PPF/ULIP accounts in the 7-yo's name**; brief parents and sibling; add his US tax/FBAR position to the CPA's scope.
30. **Maintain 12+ months of family living costs India-side** so nobody waits on an IRS transfer certificate.
31. **Small periodic transactions** on US accounts to prevent dormancy.

---

## 11. Questions for Your Professionals

**Cross-border CPA:**
1. Full-year resident vs dual-status for 2026 — and does our EB-1A filing create a conflict with any closer-connection position? *(§4.F)*
2. Does the §7701(b)(3)(C) green-card bar reach the residency-**termination**-date test, given our approved I-140? *(§4.F, [VERIFY])*
3. Confirm the 2027–2028 window is tax-free in the US for capital gains; confirm the under-31-days-in-2027 analysis. *(§4.C)*
4. Cost-basis reset: any wash-sale or step-transaction concern when harvesting **gains**? *(§4.D)*
5. Exact US-India treaty rate on portfolio dividends, and does W-8BEN secure it? *(§5.C)*
6. Roth conversion — US-taxable in the conversion year regardless of RNOR? Model pre-departure vs in-window. *(§5.D — `04 §5` glosses over this)*
7. Our 7-year-old US citizen: filing obligations, FBAR, PFIC exposure, Form 3520 thresholds. *(§7)*
8. 529 and HSA treatment once we're NRAs and India-resident. *(§1.B, §6)*
9. FIRPTA: if we ever sell the US house as foreign persons — 15% withholding on gross, Form 8288-B to reduce, and does the §121 exclusion survive a 2-3 year rental absence? *(not covered in `04a`)*

**US estate attorney:**
10. **QDOT** provisions for a non-citizen spouse — draft them in. *(§1.D)*
11. Are we US-domiciled or India-domiciled for estate tax, given a pending EB-1A asserting intent to return? Which way should we plan? *(§1.E)*
12. Life insurance ownership structure — confirm direct ownership keeps proceeds non-US-situs. *(§3)*
13. Different treatment needed for the US-citizen child vs the Indian-citizen child in the wills. *(§7)*

**India CA:**
14. **§89A / Rule 21AAA / Form 10EE:** is the US notified? Deadline? Irrevocable? Does it cover Roth? *(§6.B — the highest-value unanswered question)*
15. Confirm the FY-by-FY residency map and the exact ROR start date. *(§4.B)*
16. Schedule FA obligations and the Black Money Act trigger point. *(§6.C)*
17. RFC funding mechanics and USD-in/USD-held confirmation. *(§6.A)*
18. Documentation standard for proving a remittance is prior-year capital, not current-year income. *(§4.E)*

---

**Bottom line:** pass6's finance chapter was built around **income** tax and missed **estate** tax entirely — a ~$97k exposure on a ~$365k US-situs estate, made worse because your Indian-citizen wife gets **no marital deduction** without a QDOT. The fix is cheap and mostly pre-departure: **term life in force before you fly, QDOT language in the wills, and India-side liquidity** so no one waits on an IRS transfer certificate. Second, the tax-free selling window is **Jan 2027 → Mar 2029, not Dec 2026** — selling in your departure year triggers a flat **30%** under §871(a)(2), and the remittance-tax rationale for rushing was never real (1%, cash only, bank transfers exempt). Third, **file 2026 as a full-year US resident** — it's better filing status *and* it keeps your tax record consistent with the EB-1A story `01d` is deliberately building. Fourth, **migrate the brokerage before you leave** — Robinhood won't carry a non-resident and in-kind transfer beats liquidating. Fifth, **your 7-year-old is a lifelong US taxpayer**: no Indian mutual funds, PPF, or ULIPs in his name, ever, and tell the relatives before someone helpfully opens one.
