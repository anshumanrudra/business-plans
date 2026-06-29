#!/usr/bin/env python3
"""
Compile comprehensive India relocation plan from workflow research findings.
"""
import json
import sys
from pathlib import Path
from datetime import datetime

def load_research_findings(json_file):
    """Load research findings from JSON file."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def extract_findings_by_label(results):
    """Extract and organize findings by research area."""
    organized = {
        'immigration': [],
        'education': [],
        'employment': [],
        'city_comparison': [],
        'financial': [],
        'eb1a': [],
        'logistics': []
    }

    for result in results:
        if 'result' in result and 'findings' in result['result']:
            findings = result['result']['findings']

            # Categorize based on finding content
            for finding in findings:
                category = finding.get('category', '').lower()

                if any(kw in category for kw in ['h1b', 'visa', 'oci', 'immigration', 'tax']):
                    organized['immigration'].append(finding)
                elif any(kw in category for kw in ['school', 'education', 'curriculum', 'cbse', 'icse']):
                    organized['education'].append(finding)
                elif any(kw in category for kw in ['job', 'employment', 'work', 'mba', 'cook', 'baker']):
                    organized['employment'].append(finding)
                elif any(kw in category for kw in ['bengaluru', 'kolkata', 'healthcare', 'dialysis', 'city', 'cost of living']):
                    organized['city_comparison'].append(finding)
                elif any(kw in category for kw in ['house', 'mortgage', 'rent', 'financial', '401k', 'banking', 'savings']):
                    organized['financial'].append(finding)
                elif any(kw in category for kw in ['eb1a', 'green card', 'publication', 'patent', 'award']):
                    organized['eb1a'].append(finding)
                elif any(kw in category for kw in ['moving', 'shipping', 'logistics', 'flight', 'storage', 'customs']):
                    organized['logistics'].append(finding)

    return organized

def generate_executive_summary(findings_org):
    """Generate executive summary."""
    summary = f"""# INDIA RELOCATION PLAN - EXECUTIVE SUMMARY
Generated: {datetime.now().strftime('%B %d, %Y')}

## RECOMMENDATION: BENGALURU (Primary Choice)

### Rationale:
1. **Father's Medical Care**: Your 76-year-old father requires dialysis 3x/week at Narayana Health, Bommasandra, Bengaluru. Proximity is critical for quality of life and emergency response.
2. **Family Support**: Your sibling lives in Choodasandra, Bengaluru - provides immediate support network.
3. **Better Education**: Bengaluru has more international schools with IB/American curriculum (essential for smooth US transition).
4. **Employment**: Superior job market for your wife - more schools, corporate jobs, and food business opportunities.
5. **Infrastructure**: Better internet, power reliability crucial for potential remote US work and EB1A activities.

### Key Trade-offs:
- **Cost**: Bengaluru is 30% more expensive than Kolkata (₹60K-80K vs ₹40K-60K rent)
- **Distance from Parents' House**: ~1800 km from Bankinagar, WB vs ~150 km if in Kolkata
- **Air Quality**: Bengaluru has better air quality than Kolkata
- **Verdict**: Father's immediate health needs and kids' education outweigh cost savings

## CRITICAL TIMELINE: 12 Weeks to Departure

**Target Departure**: Late August / Early September 2026
**Current Date**: June 29, 2026
**Time Remaining**: ~8-10 weeks

### Must-Complete by Departure:
- [ ] School admissions secured (Weeks 1-3)
- [ ] Disney employment status resolved (Week 1)
- [ ] Immigration consultation completed (Week 1-2)
- [ ] House rented to tenants (Weeks 2-6)
- [ ] Tesla loan paid off + storage booked (Weeks 3-4)
- [ ] Flights booked (Week 3)
- [ ] International movers booked (Week 5)
- [ ] Temporary housing in Bengaluru booked (Week 4)

## TOTAL COST ESTIMATE

### One-Time Relocation Costs:
| Item | Cost (USD) |
|------|------------|
| Tesla loan payoff | $25,000 |
| India security deposit (₹7 lakhs) | $8,400 |
| Flights (family of 4, one-way premium economy) | $6,000-8,000 |
| International shipping (20 boxes, sea freight) | $2,000-4,000 |
| Moving/packing | $1,000-2,000 |
| Furniture/appliances in India | $2,400-3,600 |
| First month temp housing | $600-950 |
| Miscellaneous (documents, medical, etc.) | $2,000-3,000 |
| **TOTAL ONE-TIME** | **$47,400-56,950** |

### Ongoing Monthly Costs (India):
| Item | Cost (USD/month) |
|------|------------------|
| Rent (3BHK Bengaluru) | $720-960 |
| Utilities + Maintenance | $120-180 |
| Groceries/Food | $350-450 |
| Schools (2 kids) | $400-800 |
| Transportation | $100-150 |
| Health insurance | $80-120 |
| Miscellaneous | $150-200 |
| **TOTAL MONTHLY INDIA** | **$1,920-2,860** |

### Ongoing Monthly Costs (US Obligations):
| Item | Cost (USD/month) |
|------|------------------|
| Mortgage payment | $1,800 |
| Less: Rental income | -($2,500-3,000) |
| **Net housing** | **-($700-1,200)** (surplus) |
| Tesla storage | $150-250 |
| Tesla insurance (comprehensive only) | $50-80 |
| US property insurance/maintenance | $200-300 |
| **TOTAL US OBLIGATIONS** | **$400-630** |
| Less rental surplus | -($700-1,200) |
| **NET US CASH FLOW** | **+$100-800/month** (positive) |

### Total Monthly Costs: $1,920-2,860 (India) + $0-630 (net US) = $1,920-3,490/month

### 3-Year Total Cost:
- Year 1: $47,400 (one-time) + $28,000 (monthly avg) = **$75,400**
- Year 2: $28,000
- Year 3: $28,000
- **TOTAL 3-YEAR COST: $131,400**

### Savings Potential:
**If staying in US (CT):**
- Housing: $2,500/month (mortgage + property tax + insurance)
- Utilities: $300/month
- Food: $1,200/month
- Schools: $0 (public school)
- Transportation: $500/month (2 cars)
- Health insurance: $800/month (family)
- **Total US monthly: $5,300/month = $63,600/year**

**India monthly: $2,200/month average = $26,400/year**
**Annual savings in India: $37,200/year**
**3-year savings: $111,600**

**NET RESULT: Relocation approximately cost-neutral after accounting for savings vs US living costs and rental income surplus.**

## TOP 10 RISKS & MITIGATION

1. **H1B Status Loss**
   - **Risk**: Extended absence abandons H1B status; cannot return on same visa
   - **Mitigation**: Accept status loss; rely on approved I-140 and plan EB1A path; consult immigration attorney (WeGreened)

2. **School Admission Timing**
   - **Risk**: Academic year starts July-August; may miss enrollment window
   - **Mitigation**: START TODAY - call schools immediately; offer to pay premium for mid-year admission if needed

3. **House Rental Delays**
   - **Risk**: Cannot find tenant; forced to carry mortgage without offset
   - **Mitigation**: Hire property manager NOW; price competitively; offer partially furnished; 2-month buffer in budget

4. **Tesla Battery Degradation**
   - **Risk**: $10K-15K battery replacement if not maintained during 3-year storage
   - **Mitigation**: Pay friend/family $50/month for quarterly check + charge; set Tesla app alerts

5. **Father's Health Deterioration**
   - **Risk**: CKD progression or dialysis complications
   - **Mitigation**: Live in Bengaluru near Narayana Health; build relationship with nephrologist; have emergency funds

6. **Kids' Education Gaps**
   - **Risk**: Curriculum mismatch causes grade-level loss when returning to US
   - **Mitigation**: Choose IB or American curriculum school; supplement with Khan Academy; keep standardized test readiness

7. **Wife Employment Delays**
   - **Risk**: Takes 6+ months to secure job; income gap
   - **Mitigation**: Start job search remotely before arrival; consider starting small baking business immediately for cash flow

8. **US-Born Son Visa Issues**
   - **Risk**: OCI application delays prevent travel/residency in India
   - **Mitigation**: Apply for OCI immediately (4-6 week processing); have birth certificate, passport, photos ready; can enter on US passport initially

9. **Exchange Rate Volatility**
   - **Risk**: INR strengthens against USD; living costs increase 10-15%
   - **Mitigation**: Lock in exchange rates for 6-month blocks via Wise; maintain 3-month buffer in INR

10. **EB1A Case Insufficient**
    - **Risk**: 3 years not enough to build strong EB1A evidence; stuck in EB2 backlog
    - **Mitigation**: Start EB1A activities immediately (publications, open source, speaking); get quarterly immigration attorney reviews; fallback: NIW or EB2 wait

## SUCCESS CRITERIA

### Week 4 Milestones (August 1, 2026):
- ✅ School admission confirmations received
- ✅ Disney employment resolution documented
- ✅ Immigration strategy confirmed with attorney
- ✅ Tenant selected and lease signed
- ✅ Flights booked

### Pre-Departure Milestones (Late August 2026):
- ✅ Tesla in storage with maintenance plan
- ✅ International shipment dispatched
- ✅ House handed to property manager
- ✅ Temporary housing in Bengaluru confirmed

### Month 1 in India Milestones (September 2026):
- ✅ Kids started school
- ✅ Long-term apartment secured
- ✅ Wife job search active or business started
- ✅ Bank accounts and local setup complete

### Year 1 Milestones (September 2027):
- ✅ Kids thriving in school - no education gaps
- ✅ Wife employed or business generating ₹40K+/month
- ✅ EB1A activities: 2+ publications, 1 conference talk, active open source
- ✅ Father's health stable with dialysis routine
- ✅ US rental income consistent

### Year 3 Milestones (2029):
- ✅ EB1A petition filed or ready to file
- ✅ Kids ready for US high school transition
- ✅ Financial position stronger than pre-relocation
- ✅ US house maintained and appreciated in value

---
**NEXT ACTIONS: See detailed action plan sections below.**
"""
    return summary

def generate_immigration_plan(findings):
    """Generate immigration action plan."""
    content = """
# IMMIGRATION & VISA ACTION PLAN

## OVERVIEW
Your relocation involves complex immigration considerations across three different immigration statuses:
1. **You**: H1B holder (losing status), I-140 approved EB2, building EB1A case
2. **Wife**: H4 EAD holder (status dependent on your H1B)
3. **US-born son**: US citizen needing OCI for India stay
4. **India-born son**: Indian citizen, no issues

## KEY FINDINGS SUMMARY

"""

    for finding in findings:
        content += f"### {finding['category']}\n\n"
        content += "**Key Points:**\n"
        for point in finding['key_points']:
            content += f"- {point}\n"
        content += "\n**Action Items:**\n"
        for action in finding['action_items']:
            content += f"- [ ] {action}\n"
        if 'timeline' in finding:
            content += f"\n**Timeline:** {finding['timeline']}\n"
        if 'estimated_cost' in finding:
            content += f"**Estimated Cost:** {finding['estimated_cost']}\n"
        if 'risks' in finding:
            content += "\n**Risks:**\n"
            for risk in finding['risks']:
                content += f"- ⚠️ {risk}\n"
        content += "\n---\n\n"

    content += """
## IMMIGRATION TIMELINE & CHECKLIST

### WEEK 1 (July 1-7, 2026)
- [ ] Schedule consultation with WeGreened or Murthy Law Firm (immigration attorneys specializing in EB1A)
- [ ] Notify Disney Streaming HR about relocation plans - discuss:
  - [ ] Leave of absence possibility (unlikely to be approved for 1-3 years)
  - [ ] Remote work from India possibility (likely not H1B compliant)
  - [ ] Resignation with good standing for future rehire
- [ ] Gather documents for OCI application (US-born son):
  - [ ] Birth certificate with apostille
  - [ ] US passport copy
  - [ ] Your Indian passport copy
  - [ ] Wife's Indian passport copy
  - [ ] Photos (35mm x 35mm, specific requirements)
  - [ ] Proof of address
- [ ] Understand I-140 portability: Confirm your approved I-140 is portable (can use priority date with future employer)

### WEEK 2 (July 8-14, 2026)
- [ ] Submit OCI application for US-born son at BLS International or VFS Global (4-6 week processing)
- [ ] Complete immigration attorney consultation - get written strategy for:
  - [ ] H1B abandonment implications
  - [ ] Maintaining EB2 priority date (May 2021)
  - [ ] EB1A petition timeline and requirements
  - [ ] Re-entry to US strategies (new H1B, L1, or wait for green card)
- [ ] File FBAR (Foreign Bank Account Report) if you have >$10K in foreign accounts - ongoing requirement
- [ ] Set up annual tax filing plan with CPA experienced in expat taxation:
  - [ ] Foreign Earned Income Exclusion (FEIE) if working for Indian employer
  - [ ] Foreign Tax Credit for taxes paid in India
  - [ ] Continued US tax filing requirement as US tax resident

### WEEK 3-4 (July 15-28, 2026)
- [ ] Receive OCI card for US-born son (or prepare to travel on US passport with visa if delayed)
- [ ] Finalize employment separation with Disney - ensure:
  - [ ] I-140 approval notice in your records
  - [ ] Employment verification letter for future use
  - [ ] 401K rollover plan (can keep in US account)
  - [ ] Final paycheck and benefits termination

### WEEK 5-8 (August 2026)
- [ ] Apply for PAN card (Permanent Account Number) in India - required for banking, taxes
  - Online application at incometaxindiaefiling.gov.in
  - Processing: 15-20 days
  - Required for: Opening bank accounts, filing taxes, financial transactions
- [ ] Register for Aadhaar card (takes 90 days after arrival) - required for:
  - School admissions
  - Bank accounts (temporarily PAN + passport accepted)
  - Government services
  - SIM cards

### BEFORE DEPARTURE (Late August 2026)
- [ ] Confirm with immigration attorney: No outstanding US immigration obligations
- [ ] Carry physical documents:
  - [ ] Passports (all family members)
  - [ ] OCI card (US-born son)
  - [ ] I-140 approval notice (keep original + 3 copies)
  - [ ] H1B approval notices (historical record)
  - [ ] Birth certificates (kids)
  - [ ] Marriage certificate
  - [ ] Educational certificates (degrees, transcripts)
  - [ ] Employment letters
  - [ ] Vaccination records
- [ ] Understand: You are abandoning H1B status; will need new work authorization to return to US employment

## POST-ARRIVAL INDIA (Month 1-3)

### Month 1
- [ ] Apply for Aadhaar cards (all Indian citizens in family) at enrollment center
  - Biometric data collection
  - Takes 90 days to receive card
  - Temporary enrollment number usable immediately
- [ ] Open NRO (Non-Resident Ordinary) bank account:
  - For receiving funds from US
  - For local expenses
  - Options: HDFC, ICICI, Axis (good NRI services)
- [ ] Register with FRRO (Foreigners Regional Registration Office) if required:
  - US-born son on long-term stay (>180 days) may need registration
  - Check latest rules - OCI holders usually exempt
- [ ] Set up international money transfer:
  - Wise (formerly TransferWise) - lowest fees (~0.5-1%)
  - XE Money Transfer
  - Bank wire as fallback (3-5% fees)

### Month 3
- [ ] Receive Aadhaar cards
- [ ] Link Aadhaar with PAN (required for tax filing)
- [ ] Register for Indian health insurance (family floater plan):
  - Options: HDFC Ergo, ICICI Lombard, Star Health
  - ₹25,000-40,000/year for family of 4
  - Covers hospitalization, pre-existing after waiting period

## TAX PLANNING

### US Tax Obligations (Ongoing)
You remain US tax residents and must file US tax returns annually:
- **Form 1040**: Annual income tax return
- **FBAR (FinCEN Form 114)**: If >$10K in foreign accounts at any time
- **FATCA (Form 8938)**: Report foreign financial assets >$200K ($400K married)
- **Foreign Earned Income Exclusion**: Up to $120,000 per person excluded if working for Indian employer
- **Foreign Tax Credit**: Offset US taxes with taxes paid to India
- **Deadline**: April 15 (automatic 2-month extension for expats to June 15)

### India Tax Obligations
- **Residential Status**: You'll become India tax residents after 182 days in financial year
- **Tax on Global Income**: India taxes global income for residents
- **PAN Card**: Required for filing taxes
- **ITR Filing**: Annual by July 31
- **Double Taxation Treaty**: US-India treaty prevents double taxation (claim foreign tax credit in US)

### Action Items:
- [ ] Hire CPA with expat experience (US side): $500-1,000/year
- [ ] Hire Chartered Accountant (India side): ₹15,000-30,000/year
- [ ] Set up estimated tax payments if needed (if wife has Indian income)
- [ ] Keep meticulous records of:
  - [ ] Foreign income (from US sources)
  - [ ] Indian income (if any)
  - [ ] Foreign bank accounts
  - [ ] Days in US vs India (for residency determination)

## RE-ENTRY TO US STRATEGY

### Scenario 1: EB1A Approved (Best Case)
- **Timeline**: File EB1A in Year 2-3, approval in 6-12 months
- **Re-entry**: Immigrant visa → Green card → Return to US in any job
- **Priority Date**: Can use May 2021 date from EB2 I-140 if EB1A denied

### Scenario 2: EB1A Pending or Denied
- **Option A**: New H1B petition from new US employer (subject to cap lottery, unless cap-exempt employer)
- **Option B**: L1 visa if working for multinational with India office
- **Option C**: O1 visa (extraordinary ability) using same evidence as EB1A
- **Option D**: Wait for EB2 priority date to become current (India EB2 heavily backlogged - could be 5-10+ years)

### Scenario 3: Kids' Education Timeline Forces Return
- **If EB1A not approved**: You may need to return on new H1B or other visa
- **Consider**: Having wife and kids return first (they can re-enter as you sort out visa)
- **Risk Mitigation**: Start EB1A activities immediately to maximize chances

## MAINTAINING TIES TO US

While in India, maintain ties for smoother eventual return:
- [ ] Keep US bank accounts active (minimum balances, monthly transactions)
- [ ] Maintain US credit cards (use monthly and pay off to keep credit score)
- [ ] Keep US driver's license valid (renew online if CT allows)
- [ ] File US taxes on time every year
- [ ] Keep US phone number (Google Voice free or T-Mobile international plan)
- [ ] Maintain professional network (LinkedIn, conferences, publications)
- [ ] Keep US address as "permanent address" (parents/sibling)

## GOTCHAS & WARNINGS

⚠️ **DO NOT** misrepresent your location to US employer - H1B fraud is serious
⚠️ **DO NOT** attempt to maintain H1B while working remotely from India long-term - violates LCA
⚠️ **DO** keep I-140 approval notice safe - critical for priority date portability
⚠️ **DO** maintain continuous tax filing - gaps can complicate future immigration
⚠️ **DO** keep detailed records of EB1A-building activities (publications, talks, code, recognition)
⚠️ **DO** understand your "priority date" concept - it's your place in green card line, survives I-140 cancellation if approved for 180+ days (yours was approved with PD May 2021, so you're safe)

---
**CONSULT QUALIFIED IMMIGRATION ATTORNEY - This is general guidance, not legal advice.**
"""
    return content

def generate_education_plan(findings):
    """Generate education action plan."""
    content = """
# EDUCATION PLAN

## CURRICULUM CHOICE RECOMMENDATION: IB (International Baccalaureate) or American Curriculum

### Rationale:
1. **Smooth US Re-entry**: IB and American curricula are globally recognized and align with US Common Core standards
2. **Credit Transfer**: US schools readily accept IB/American curriculum transcripts
3. **College Preparation**: IB Diploma Programme (grades 11-12) is highly valued by US colleges
4. **English Language**: IB/American schools teach in English, maintain language proficiency
5. **Extracurriculars**: IB schools emphasize well-rounded education (sports, arts, community service)

### Why NOT CBSE/ICSE:
- **Curriculum Gap**: CBSE/ICSE curricula differ significantly from US Common Core (especially math sequence)
- **Grade-Level Risk**: Transitioning back may require repeating a grade or summer catch-up courses
- **Language**: More local language exposure (Hindi/Kannada), less English emphasis
- **College Prep**: US SAT/ACT prep not integrated; would need separate tutoring

## TOP SCHOOL RECOMMENDATIONS - BENGALURU

"""

    for finding in findings:
        content += f"### {finding['category']}\n\n"
        content += "**Key Points:**\n"
        for point in finding['key_points']:
            content += f"- {point}\n"
        content += "\n**Action Items:**\n"
        for action in finding['action_items']:
            content += f"- [ ] {action}\n"
        if 'timeline' in finding:
            content += f"\n**Timeline:** {finding['timeline']}\n"
        if 'estimated_cost' in finding:
            content += f"**Estimated Cost:** {finding['estimated_cost']}\n"
        content += "\n---\n\n"

    content += """
## SCHOOL ADMISSION ACTION PLAN

### IMMEDIATE (Week 1 - July 1-7, 2026)
- [ ] **CALL SCHOOLS TODAY** - Academic year 2026-27 has likely started (July/August start)
- [ ] Priority targets for 13-year-old (Grade 8) and 7-year-old (Grade 2):
  1. **Oakridge International School** - Sarjapur Road
     - Phone: +91-80-2783-5825
     - Email: admissions@oakridge.in
     - Request: Mid-year admission possibility, waitlist status
  2. **The International School Bangalore (TISB)** - Nagarabhavi
     - Phone: +91-80-2843-5773
     - Email: admissions@tisb.org
     - Request: Admission for both grades, transfer credit policy
  3. **Greenwood High International School** - Sarjapur Road
     - Phone: +91-80-6737-2400
     - Email: info@greenwoodhigh.edu.in
     - Request: Immediate admission, IB/IGCSE program details
  4. **Inventure Academy** - Whitefield
     - Phone: +91-80-6843-7777
     - Email: admissions@inventureacademy.com
  5. **Indus International School** - Sarjapur Road
     - Phone: +91-80-4967-0700
     - Email: admissions@indusschool.com

### Week 1 Tasks:
- [ ] Prepare admission documents (get these ready BEFORE calling):
  - [ ] US school transcripts (request official transcripts from current CT school)
  - [ ] Birth certificates
  - [ ] Passport copies
  - [ ] Immunization records
  - [ ] Recent photos
  - [ ] Previous report cards (2-3 years)
  - [ ] Recommendation letters from current teachers (request ASAP)
- [ ] Explain situation to schools:
  - Family relocating from US for 2-3 years
  - Kids in Connecticut public schools (strong academic standing)
  - Need curriculum aligned with eventual US return (IB/American)
  - Willing to pay admission fees immediately to secure spots
- [ ] Ask schools:
  - [ ] Availability for Grade 2 and Grade 8
  - [ ] Mid-year admission policy (if academic year has started)
  - [ ] Total fees (tuition + admission + deposits + transportation + extras)
  - [ ] Curriculum offered (IB PYP/MYP/DP, IGCSE, American)
  - [ ] Extracurriculars: Taekwondo, swimming availability
  - [ ] Admission test/interview requirements
  - [ ] Timeline for decision

### Week 2 (July 8-14, 2026):
- [ ] Request official transcripts from current school in CT:
  - Irving A. Robbins Middle School (if 13-year-old) or
  - West District Elementary School (if younger)
  - Allow 5-7 days for processing
- [ ] Get teacher recommendation letters
- [ ] Complete online applications for top 3 schools
- [ ] Schedule admission tests/interviews (may be online/Zoom initially)
- [ ] Prepare kids for admission assessments:
  - [ ] English: Reading comprehension, writing sample
  - [ ] Math: Grade-appropriate problem-solving
  - [ ] General reasoning/aptitude

### Week 3 (July 15-21, 2026):
- [ ] Complete admission tests/interviews
- [ ] Receive admission offers (ideally)
- [ ] Compare offers:
  - [ ] Total cost
  - [ ] Curriculum fit
  - [ ] School location vs housing search area
  - [ ] Extracurricular programs
  - [ ] Parent reviews/reputation
- [ ] Accept offer and pay admission fees immediately

### Week 4-5 (July 22 - August 4, 2026):
- [ ] Complete enrollment paperwork
- [ ] Pay term fees
- [ ] Order uniforms and supplies
- [ ] Arrange school transportation (if needed)
- [ ] Attend parent orientation (may be virtual initially)

### Post-Arrival (September 2026):
- [ ] First day of school (or continuation if mid-year admitted)
- [ ] Meet teachers and administrators
- [ ] Set up parent-teacher communication
- [ ] Enroll kids in Taekwondo and swimming programs:
  - [ ] Schools often have after-school clubs
  - [ ] External: Taekwondo academies (many in Bangalore), swimming pools at apartment complexes or private clubs

## SCHOOL COST BREAKDOWN (Annual per Child)

### Tuition Range - IB/International Schools:
| School Tier | Annual Tuition | Admission Fee | Deposit | Total Year 1 |
|-------------|----------------|---------------|---------|--------------|
| Premium (Oakridge, TISB) | ₹5-8 lakhs | ₹3-5 lakhs | ₹1-2 lakhs | ₹9-15 lakhs |
| Mid-tier (Greenwood, Inventure) | ₹3-5 lakhs | ₹2-3 lakhs | ₹50K-1 lakh | ₹5.5-9 lakhs |
| Budget International | ₹2-3 lakhs | ₹1-1.5 lakhs | ₹25-50K | ₹3.25-5 lakhs |

**For two kids (one in Grade 8, one in Grade 2):**
- **Year 1**: ₹10-20 lakhs ($12,000-24,000) including admission fees
- **Year 2-3**: ₹6-12 lakhs/year ($7,200-14,400) tuition only

### Additional Costs (Annual):
- **Transportation**: ₹60,000-120,000 ($720-1,440) per child if using school bus
- **Uniforms**: ₹10,000-20,000 ($120-240) per child
- **Books & Supplies**: ₹15,000-25,000 ($180-300) per child
- **Extracurriculars** (Taekwondo, Swimming): ₹40,000-80,000 ($480-960) per child
- **Field Trips/Events**: ₹10,000-20,000 ($120-240) per child

**Total Annual Education Cost (Both Kids): ₹8-15 lakhs ($9,600-18,000) after Year 1**

## TAEKWONDO & SWIMMING

### Taekwondo Academies (Bengaluru):
1. **Korea Taekwondo Academy** - HSR Layout
   - Phone: +91-99001-73535
   - Cost: ₹4,000-5,000/month per child
2. **Team Karnataka Taekwondo** - Multiple locations
3. **Black Belt Taekwondo Academy** - Sarjapur Road
4. **Many schools have in-house Taekwondo clubs** - inquire during admission

### Swimming:
1. **School pools** - Many international schools have swimming pools (TISB, Oakridge)
2. **Apartment complex pools** - Target apartments with pools for practice
3. **Private coaching**:
   - Residential complexes often have coaching programs
   - Cost: ₹2,000-4,000/month per child
4. **Swimming clubs**:
   - Basavanagudi Aquatic Centre
   - Vijayanagar Aquatic Centre
   - Cost: ₹3,000-5,000/month + membership

## AVOIDING EDUCATION GAPS

### Strategies:
1. **Choose IB/American curriculum** - minimizes gap
2. **Supplement with online learning**:
   - [ ] **Khan Academy** (free) - Math, Science, aligned with US Common Core
   - [ ] **IXL** ($20/month) - Practice problems for all subjects
   - [ ] **Time4Learning** ($25-30/month) - Full US curriculum online
3. **Maintain grade-level reading**:
   - [ ] Subscribe to Epic Books (digital library)
   - [ ] Monthly book shipments from Amazon India
   - [ ] Encourage 30+ minutes daily reading
4. **Standardized test prep** (if returning before high school):
   - [ ] Year before return: Practice PSAT/SAT if 13-year-old entering high school
5. **Summer bridge programs** (if needed):
   - Upon return to US, enroll in summer programs to ensure grade-level readiness

### Monitoring Progress:
- [ ] Quarterly parent-teacher meetings
- [ ] Request detailed report cards showing grade-level competency
- [ ] Compare curriculum coverage vs US Common Core standards
- [ ] Address gaps immediately with tutoring (tutors widely available in India, ₹500-1,000/hour)

## SCHOOLING IN KOLKATA (If you choose Kolkata instead)

### Top International Schools:
1. **Calcutta International School** - IB curriculum, ₹4-6 lakhs/year
2. **Mahadevi Birla World Academy** - IB, ₹3-5 lakhs/year
3. **Lakshmipat Singhania Academy** - ICSE/ISC, ₹1.5-2.5 lakhs/year

**Cost**: 20-30% lower than Bengaluru
**Concern**: Fewer international schools, less expat community, Bengali language dominance

---
**START SCHOOL APPLICATIONS IMMEDIATELY - This is the most time-sensitive action item.**
"""
    return content

def main():
    """Main compilation function."""
    print("Loading research findings...")
    results = load_research_findings('research_findings_raw.json')

    print(f"Found {len(results)} research results")

    print("Organizing findings...")
    organized = extract_findings_by_label(results)

    print("Generating documents...")

    # Generate Executive Summary
    exec_summary = generate_executive_summary(organized)
    with open('01_executive_summary.md', 'w') as f:
        f.write(exec_summary)
    print("✅ Generated: 01_executive_summary.md")

    # Generate Immigration Plan
    immigration_plan = generate_immigration_plan(organized['immigration'])
    with open('02_immigration_visa_plan.md', 'w') as f:
        f.write(immigration_plan)
    print("✅ Generated: 02_immigration_visa_plan.md")

    # Generate Education Plan
    education_plan = generate_education_plan(organized['education'])
    with open('03_education_plan.md', 'w') as f:
        f.write(education_plan)
    print("✅ Generated: 03_education_plan.md")

    print("\n✅ Compilation complete! Check the output files.")

if __name__ == "__main__":
    main()
