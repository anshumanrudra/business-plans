#!/usr/bin/env python3
"""
Generate remaining relocation plan documents.
"""
import json

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

            for finding in findings:
                category = finding.get('category', '').lower()

                if any(kw in category for kw in ['h1b', 'visa', 'oci', 'immigration', 'tax']):
                    organized['immigration'].append(finding)
                elif any(kw in category for kw in ['school', 'education', 'curriculum', 'cbse', 'icse']):
                    organized['education'].append(finding)
                elif any(kw in category for kw in ['job', 'employment', 'work', 'mba', 'cook', 'baker', 'food business', 'baking', 'catering']):
                    organized['employment'].append(finding)
                elif any(kw in category for kw in ['bengaluru', 'kolkata', 'healthcare', 'dialysis', 'city', 'cost of living', 'air quality', 'infrastructure']):
                    organized['city_comparison'].append(finding)
                elif any(kw in category for kw in ['house', 'mortgage', 'rent', 'financial', '401k', 'banking', 'savings', 'property management']):
                    organized['financial'].append(finding)
                elif any(kw in category for kw in ['eb1a', 'green card', 'publication', 'patent', 'award', 'open source', 'conference']):
                    organized['eb1a'].append(finding)
                elif any(kw in category for kw in ['moving', 'shipping', 'logistics', 'flight', 'storage', 'customs']):
                    organized['logistics'].append(finding)

    return organized

def generate_employment_plan(findings):
    """Generate wife employment plan."""
    content = """
# WIFE EMPLOYMENT PLAN

## OVERVIEW
Your wife (40 years old) currently works in an elementary school in Connecticut on H4 EAD. She has:
- MBA from Sikkim Manipal University (distance learning)
- Excellent cooking & baking skills
- Experience in elementary school environment
- Duration in India: 2-3 years (should influence job vs business decision)

## KEY CONSIDERATIONS
- **H4 EAD becomes invalid** when your H1B status ends (upon relocation)
- **Can work freely in India** as Indian citizen - no work authorization needed
- **Short timeframe** (2-3 years) may affect employer willingness to hire vs starting own business

## JOB OPTIONS ANALYSIS

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
## RECOMMENDED STRATEGY: HYBRID APPROACH

Given the 2-3 year timeframe and uncertain duration, I recommend a **hybrid approach**:

### Phase 1 (Months 1-3): Start Home Baking Business
**Why:**
- Immediate income without job search delays
- Flexible schedule during family settling-in period
- Low startup capital (₹50,000-100,000)
- Can operate from home while kids adjust to school
- Bangalore has thriving demand for quality baked goods

**Action Plan:**
1. **Week 1-2 (Arrival)**: Market research
   - [ ] Join Bangalore food/baking groups on Facebook, WhatsApp
   - [ ] Research competitors: Existing home bakers, Cake shops, cafes
   - [ ] Identify niche: American-style baking (brownies, cookies, cupcakes), custom cakes, health-focused options
2. **Week 3-4**: Setup
   - [ ] Source baking equipment (oven, mixer, pans) - ₹30,000-50,000
   - [ ] Register business (optional for small-scale): Udyam registration (free, MSME benefits)
   - [ ] Get FSSAI license (Food Safety) - Basic license for home-based: ₹100, processing 7-30 days
   - [ ] Set up social media: Instagram, Facebook pages
   - [ ] Design simple menu and pricing
3. **Month 2**: Soft Launch
   - [ ] Offer samples to neighbors, school parents, sibling's colleagues
   - [ ] Price competitively: Cookies ₹200-300/dozen, Cakes ₹800-2,000, Custom cakes ₹1,500-5,000
   - [ ] Take orders via WhatsApp/Instagram DM
   - [ ] Deliver locally or offer pickup
4. **Month 3**: Scale
   - [ ] Get customer feedback and refine menu
   - [ ] Expand marketing: School parent groups, apartment complexes, corporate gifting
   - [ ] Target: ₹30,000-50,000/month revenue in Month 3

**Expected Income: ₹20,000-50,000/month** (part-time, home-based)

### Phase 2 (Months 4-12): Explore School Jobs While Continuing Business

Once settled and business is running, explore school job opportunities:

**Target Roles:**
- Teaching Assistant / Teacher's Aide at international schools
- Primary school teacher (if she has teaching certification)
- School administrator / office coordinator
- After-school program coordinator

**Advantages of Waiting 3-6 Months:**
- Family settled, less chaos
- Proof of India-based address and stability
- Networking through kids' school (parents, teachers)
- Aadhaar card obtained (often required for formal employment)

**Job Search Strategy:**
1. **Network through kids' school**:
   - [ ] Attend parent-teacher meetings, volunteer for school events
   - [ ] Express interest to school admin about job opportunities
   - [ ] Many schools prefer hiring parents (already invested in school community)
2. **Apply directly to schools**:
   - [ ] Oakridge, TISB, Greenwood, Inventure (where kids study)
   - [ ] Other international schools: Canadian International, Sishu Griha, Stonehill
3. **Job portals**:
   - [ ] Naukri.com, LinkedIn, Indeed India
   - [ ] Search: "Primary teacher Bangalore", "School administrator Bangalore"
4. **Teaching certification** (if needed):
   - [ ] Consider online TEFL/TESOL certification (6-12 weeks, $200-400)
   - [ ] Boosts employability at international schools

**Expected Salary: ₹30,000-60,000/month** (teaching assistant to teacher level)

### Phase 3 (Year 2-3): Scale Food Business OR Commit to School Job

**Option A: Scale Baking Business**
If home baking is successful and enjoyable:
- [ ] Hire part-time help (₹10,000-15,000/month)
- [ ] Expand to corporate catering (office birthday cakes, event catering)
- [ ] Partner with cafes/restaurants to supply baked goods
- [ ] Potential income: ₹60,000-100,000/month with scaling

**Option B: Full-Time School Job**
If school environment is preferred:
- [ ] Move to full-time teaching role (₹40,000-80,000/month)
- [ ] Stop or minimize baking business (perhaps weekends only for regulars)

## FOOD BUSINESS MODELS (Detailed)

### 1. Home-Based Baking (Recommended for Start)
**Investment**: ₹50,000-100,000
**Items**:
- Oven (OTG or convection): ₹15,000-25,000
- Stand mixer: ₹10,000-15,000
- Baking pans, tools: ₹5,000-10,000
- Initial ingredients: ₹10,000
- Packaging: ₹5,000
- Marketing/website: ₹5,000
**Pros**: Low overhead, flexible hours, work from home
**Cons**: Limited capacity, regulatory restrictions on home-based food business (but widely practiced)

### 2. Cloud Kitchen / Commercial Kitchen Rental
**Investment**: ₹200,000-500,000
**Monthly Costs**: Kitchen rental ₹15,000-30,000 + ingredients + labor
**When**: If home-based scales beyond capacity (20+ orders/week)
**Pros**: Can scale significantly, professional setup, no regulatory issues
**Cons**: Higher fixed costs, longer commute, need more capital

### 3. Catering Service
**Investment**: ₹100,000-200,000
**Focus**: Corporate events, birthday parties, weddings
**Requirements**: Food safety certification, catering license, transport
**Expected Income**: ₹50,000-150,000/month depending on events booked
**Pros**: High-margin events, can charge premium
**Cons**: Irregular income (event-based), requires team for large events

### 4. Cooking Classes
**Investment**: ₹20,000-50,000 (marketing + demo supplies)
**Format**: American baking classes for Indian home bakers, Online or in-person
**Price**: ₹1,500-3,000 per person per session
**Target**: 2-3 classes/month with 5-10 students = ₹15,000-90,000/month
**Pros**: High margin, scalable online, builds brand
**Cons**: Requires marketing, curriculum development

## INCOME PROJECTIONS & COMPARISON

| Option | Month 1-3 | Month 4-12 | Year 2-3 | Setup Cost | Effort |
|--------|-----------|------------|----------|------------|--------|
| **Home Baking** | ₹10-30K | ₹30-50K | ₹50-100K | ₹50-100K | Medium |
| **School Job (PT)** | ₹0 | ₹20-40K | ₹30-50K | ₹0 | Medium |
| **School Job (FT)** | ₹0 | ₹30-60K | ₹50-80K | ₹0 | High |
| **Cloud Kitchen** | N/A | ₹40-80K | ₹80-150K | ₹200-500K | High |
| **Catering** | ₹5-20K | ₹30-80K | ₹50-150K | ₹100-200K | High (Variable) |
| **Cooking Classes** | ₹0-10K | ₹15-40K | ₹30-90K | ₹20-50K | Medium |

**Recommendation**: Start with **Home Baking** (immediate income, low risk) + Pursue **School Job** after 3-6 months (stable income, structured hours)

Combined income potential Year 1: ₹40,000-70,000/month
Combined income potential Year 2-3: ₹60,000-100,000/month

## REGULATORY REQUIREMENTS - FOOD BUSINESS

### FSSAI License (Food Safety and Standards Authority of India)
**Required for**: Any food business in India
**Types**:
1. **Basic Registration**: For businesses with turnover < ₹12 lakhs/year
   - Cost: ₹100
   - Valid: 1-5 years
   - Process: Online application at fssai.gov.in, 7-30 days
   - Required for: Home-based baking
2. **State License**: For turnover ₹12 lakhs - ₹20 crores/year
   - Cost: ₹2,000-5,000
   - Required for: Cloud kitchen, catering
3. **Documents needed**:
   - [ ] PAN card
   - [ ] Aadhaar card
   - [ ] Proof of address
   - [ ] Photo

**Action**: Apply for Basic Registration in Month 1 (₹100, 30-day process)

### Udyam Registration (MSME)
**Optional but recommended**
- Benefits: Loans, government schemes, credibility
- Cost: Free
- Process: Online at udyamregistration.gov.in
- Requirements: Aadhaar, PAN

### GST Registration
**Required if**: Turnover > ₹40 lakhs/year (unlikely in first 2 years)
**If below threshold**: No GST registration needed
**Action**: Monitor revenue; register if approaching ₹40 lakhs annually

### Trade License (Municipal Corporation)
**Required for**: Commercial food establishments (shops, restaurants)
**NOT required for**: Home-based food businesses in most cases
**Action**: Skip unless scaling to commercial kitchen

## NETWORKING & MARKETING

### Online Presence:
- [ ] Instagram business account: Post photos, reels of baked goods, behind-the-scenes
- [ ] Facebook page: Join local buy/sell groups, food groups
- [ ] WhatsApp Business: Professional catalog, automated responses
- [ ] Google My Business: For local discovery (free)
- [ ] Website (optional): Using free platforms like Wix, WordPress.com (₹0-5,000/year)

### Offline Marketing:
- [ ] Distribute flyers in apartment complexes (with permission)
- [ ] Samples at school events, sibling's workplace
- [ ] Word of mouth: Ask satisfied customers to refer
- [ ] Partner with local stores/cafes to display business cards

### Customer Acquisition:
- [ ] Month 1: Friends, family, neighbors (trust-based)
- [ ] Month 2-3: Apartment communities, school parents
- [ ] Month 4+: Online orders, repeat customers, corporate gifting

## JOB SEARCH RESOURCES

### Job Portals:
1. **Naukri.com** - India's largest job portal
2. **LinkedIn** - Professional networking + job search
3. **Indeed India** - Aggregates jobs from multiple sources
4. **TimesJobs.com** - Specializes in education sector
5. **Schools' Direct Websites** - Careers section

### Search Keywords:
- "Primary school teacher Bangalore"
- "Teaching assistant Bangalore"
- "Montessori teacher Bangalore"
- "International school jobs Bangalore"
- "School administrator Bangalore"
- "Early childhood educator Bangalore"

### Networking:
- [ ] Join "Bangalore Expat Teachers" groups on Facebook
- [ ] Connect with teachers at kids' school
- [ ] Attend education job fairs (check in Bangalore events)
- [ ] LinkedIn: Connect with school principals, HR managers

## TIMELINE & ACTION PLAN

### Pre-Departure (July-August 2026):
- [ ] Research Bangalore food business landscape (online)
- [ ] Join Bangalore food/baking groups on Facebook
- [ ] Update resume and LinkedIn for school job search
- [ ] Research international schools in target residential areas

### Month 1 (September 2026) - Settle & Setup:
- [ ] Focus on family settlement
- [ ] Market research: Visit local bakeries, cafes, talk to home bakers
- [ ] Apply for PAN and Aadhaar
- [ ] Order baking equipment online (Amazon India, Flipkart)
- [ ] Set up Instagram/Facebook pages for baking business
- [ ] Bake samples for neighbors and sibling's family/friends

### Month 2 (October 2026) - Soft Launch:
- [ ] Apply for FSSAI basic registration (₹100)
- [ ] Complete Udyam registration (free, MSME benefits)
- [ ] Soft launch baking business: Take 5-10 orders
- [ ] Get feedback and refine offerings
- [ ] Update resume for school jobs (with India address now available)
- [ ] Start networking at kids' school events

### Month 3-4 (November-December 2026) - Ramp Up:
- [ ] Scale baking: Target 15-20 orders/month
- [ ] Expand marketing to school parents, apartment groups
- [ ] Apply to 10-15 school jobs on Naukri, LinkedIn
- [ ] Attend school job interviews
- [ ] Target income: ₹30,000-50,000 from baking + potential job offer

### Month 5-6 (January-February 2027) - Stabilize:
- [ ] Baking business running: ₹40,000-60,000/month OR
- [ ] School job secured: ₹30,000-60,000/month OR
- [ ] Both: Part-time baking + Part-time school role
- [ ] Evaluate: Which path is more fulfilling and financially rewarding?

### Year 2-3 (2027-2029) - Optimize:
- [ ] If baking: Scale to ₹60,000-100,000/month (hire help, expand services)
- [ ] If school: Advance to senior teacher or coordinator role (₹50,000-80,000)
- [ ] If both: Balance based on preference and financial needs

## COST-BENEFIT ANALYSIS

### Option 1: Home Baking Business
**Pros**:
- ✅ Immediate income (Month 1-2)
- ✅ Flexible schedule (work around kids' needs)
- ✅ Low startup cost (₹50K-100K)
- ✅ Scalable (can grow to ₹100K+/month)
- ✅ Builds entrepreneurship skills
- ✅ American-style baking is underserved niche in Bangalore

**Cons**:
- ❌ Irregular income initially
- ❌ Requires self-marketing and customer acquisition
- ❌ Home-based may have space/hygiene challenges
- ❌ No employment benefits (PF, insurance, leave)

**Best for**: If she enjoys independent work, has entrepreneurial drive, wants flexible hours

### Option 2: School Job
**Pros**:
- ✅ Stable monthly income
- ✅ Structured hours (school schedule)
- ✅ Benefits: PF (Provident Fund), health insurance, paid leave
- ✅ Professional environment
- ✅ Networking in education sector
- ✅ Kids' school may offer employee discounts

**Cons**:
- ❌ Takes 3-6 months to secure job
- ❌ Fixed hours (less flexibility)
- ❌ Income ceiling (₹50K-80K likely max for 2-3 year stint)
- ❌ May require additional certification (TEFL/TESOL)

**Best for**: If she prefers structure, stable income, professional environment, doesn't want business risk

### Option 3: Hybrid (Recommended)
**Pros**:
- ✅ Immediate income from baking while job searching
- ✅ Diversified income (not dependent on single source)
- ✅ Can scale baking or pivot to full-time job based on preference
- ✅ Balances flexibility and stability

**Cons**:
- ❌ Requires juggling both in early months
- ❌ May be exhausting initially

**Best for**: Maximizing income and optionality in short 2-3 year timeframe

## FINANCIAL PROJECTIONS

### Scenario 1: Home Baking Only
- **Year 1**: ₹20K (M1-3) → ₹40K (M4-12) = ₹4.2 lakhs income
- **Year 2**: ₹50K/month = ₹6 lakhs
- **Year 3**: ₹60K/month = ₹7.2 lakhs
- **3-Year Total**: ₹17.4 lakhs ($20,880)
- **Costs**: ₹1 lakh setup + ₹10K/month ingredients/marketing = ₹4.6 lakhs
- **Net Income**: ₹12.8 lakhs ($15,360) over 3 years

### Scenario 2: School Job Only
- **Year 1**: ₹0 (M1-4) + ₹40K (M5-12) = ₹3.2 lakhs
- **Year 2**: ₹50K/month = ₹6 lakhs
- **Year 3**: ₹60K/month = ₹7.2 lakhs
- **3-Year Total**: ₹16.4 lakhs ($19,680)
- **Costs**: ₹0 setup
- **Net Income**: ₹16.4 lakhs ($19,680) over 3 years

### Scenario 3: Hybrid (Baking + School Part-Time)
- **Year 1**: ₹30K/month = ₹3.6 lakhs
- **Year 2**: ₹60K/month = ₹7.2 lakhs
- **Year 3**: ₹70K/month = ₹8.4 lakhs
- **3-Year Total**: ₹19.2 lakhs ($23,040)
- **Costs**: ₹1 lakh setup + ₹5K/month = ₹2.8 lakhs
- **Net Income**: ₹16.4 lakhs ($19,680) over 3 years

**Verdict**: Hybrid approach yields highest total income (₹19.2 lakhs) with manageable costs.

---
**NEXT STEP: Start baking research and Instagram setup even BEFORE departure to hit ground running.**
"""
    return content

def generate_city_comparison(findings):
    """Generate city comparison document."""
    content = """
# BENGALURU VS KOLKATA - COMPREHENSIVE COMPARISON

## EXECUTIVE RECOMMENDATION: **BENGALURU**

**Score**: Bengaluru 8/10, Kolkata 6/10

### Quick Verdict:
**Choose Bengaluru** because:
1. ✅ Father's dialysis location (Narayana Health, Bommasandra)
2. ✅ Sibling's support network (Choodasandra)
3. ✅ Better international schools (IB/American curriculum)
4. ✅ Superior job market for wife
5. ✅ Better infrastructure (internet, power)

**Kolkata advantages**:
1. ✅ 30% lower cost of living
2. ✅ Proximity to parents' house (Bankinagar, ~150 km vs ~1800 km)
3. ✅ Simpler, slower-paced lifestyle

**Bengaluru disadvantages outweigh Kolkata advantages because**:
- Father's immediate health needs (dialysis 3x/week) require proximity - cannot be in Kolkata
- If father is in Bengaluru for dialysis, your primary care goal is met there
- Kids' education quality and US-transition readiness more important than cost savings for 2-3 year period

## DETAILED COMPARISON

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
## SIDE-BY-SIDE COMPARISON TABLE

| Factor | Bengaluru | Kolkata | Winner |
|--------|-----------|---------|--------|
| **Healthcare** | Narayana Health (dialysis 3x/wk), top hospitals | Good hospitals but father not based here | BLR ✅ |
| **Family Proximity** | Sibling in Choodasandra | Parents' house 150 km away | Split |
| **Rent (3BHK)** | ₹60-80K/month | ₹40-60K/month | KOL ✅ |
| **Schools (Intl)** | 10+ IB/American schools | 3-5 international schools | BLR ✅ |
| **Wife Job Market** | Excellent (tech hub, many schools) | Moderate | BLR ✅ |
| **Air Quality** | Moderate (better than Delhi/Kolkata) | Poor (industrial pollution) | BLR ✅ |
| **Infrastructure** | Excellent internet, reliable power | Frequent power cuts, slower internet | BLR ✅ |
| **Traffic** | Heavy (plan 1.5-2hr commutes) | Heavy (but smaller city, 1hr commutes) | KOL ✅ |
| **Climate** | Pleasant year-round (15-30°C) | Humid summers (35-40°C), mild winters | BLR ✅ |
| **Expat Community** | Large (tech professionals) | Small | BLR ✅ |
| **Cultural Activities** | Abundant (concerts, theater, tech events) | Moderate (Tagore culture, literature) | BLR ✅ |
| **Cost of Living** | High (metro) | 30% lower | KOL ✅ |
| **Language** | Kannada + English widely spoken | Bengali dominant, less English | BLR ✅ |
| **Total Score** | **10 wins** | **3 wins** | **BLR** |

## DETAILED FACTOR ANALYSIS

### 1. Healthcare & Father's Dialysis

**Bengaluru**:
- ✅ Father already receiving dialysis at Narayana Health, Bommasandra
- ✅ Established relationship with nephrologist
- ✅ Dialysis routine stable (3x/week)
- ✅ Your presence nearby for emergencies, appointments
- ✅ Other top hospitals: Apollo, Fortis, Manipal
- ✅ Medical infrastructure world-class

**Kolkata**:
- ❌ Father would need to be in Bengaluru anyway for dialysis
- ⚠️ If father moves to Kolkata with you: Disrupts established care, high risk
- ✅ Good hospitals (AMRI, Apollo Gleneagles, Ruby Hospital)
- ⚠️ Mother managing father's dialysis commute from Bankinagar to Kolkata (150 km) is impractical

**Verdict**: **Bengaluru wins decisively**. Father's medical needs anchor the decision.

### 2. Family Support & Proximity

**Bengaluru**:
- ✅ Sibling in Choodasandra (10-15 km from likely your housing area)
- ✅ Immediate help with settling in, babysitting, local advice
- ✅ Sibling's kids (12, 10 years) close in age to your kids - built-in cousins' bonding
- ✅ Father & mother in Bengaluru for dialysis (can visit daily/weekly)

**Kolkata**:
- ✅ Parents' own house in Bankinagar, Nadia (150 km from Kolkata)
- ⚠️ But father needs dialysis in Bengaluru (not feasible to be in Kolkata)
- ❌ No immediate family in Kolkata if you're based there
- ⚠️ You'd be visiting Bengaluru regularly anyway (for father) - defeats purpose of being in Kolkata

**Verdict**: **Bengaluru wins**. Sibling's support + father's medical needs outweigh parents' house location.

### 3. Cost of Living

**Bengaluru**:
- Rent: ₹60-80K/month (3BHK, Sarjapur/HSR Layout)
- Food: ₹15-20K/month (groceries)
- Transportation: ₹8-12K/month (Uber/Ola, no car)
- Utilities: ₹5-8K/month
- **Total**: ₹88-120K/month (₹10.5-14.4 lakhs/year)

**Kolkata**:
- Rent: ₹40-60K/month (3BHK, Salt Lake/New Town)
- Food: ₹12-15K/month
- Transportation: ₹5-8K/month
- Utilities: ₹4-6K/month
- **Total**: ₹61-89K/month (₹7.3-10.7 lakhs/year)

**Annual Savings in Kolkata**: ₹3.2-3.7 lakhs ($3,840-4,440)
**3-Year Savings**: ₹9.6-11.1 lakhs ($11,520-13,320)

**Verdict**: **Kolkata wins on cost**, but savings of ~$12K over 3 years is not enough to outweigh:
- Father's health risks from moving dialysis care
- Kids' education quality difference
- Wife's income potential difference (she could earn ₹20-30K more/month in BLR = ₹7.2-10.8 lakhs over 3 years, offsetting cost difference)

### 4. Education (International Schools)

**Bengaluru**:
- **10+ IB/American curriculum schools**:
  1. Oakridge International (IB PYP, MYP, DP)
  2. The International School Bangalore - TISB (IB)
  3. Inventure Academy (IB)
  4. Greenwood High (IB, IGCSE)
  5. Indus International (IB, IGCSE)
  6. Canadian International School (IB)
  7. Stonehill International (IB)
  8. Gear Innovative International School (IB)
  9. Neev Academy (IB PYP)
  10. Sishu Griha Montessori (American Montessori)
- **Tuition**: ₹3-8 lakhs/year per child
- **Curriculum alignment**: Excellent for US return
- **Extracurriculars**: Taekwondo, swimming widely available

**Kolkata**:
- **3-5 international schools**:
  1. Calcutta International School (IB)
  2. Mahadevi Birla World Academy (IB)
  3. Singapore International School
  4. La Martiniere (prestigious but ICSE, not international)
  5. Lakshmipat Singhania Academy (ICSE/ISC)
- **Tuition**: ₹2-6 lakhs/year (20% cheaper)
- **Concern**: Fewer IB schools, less expat community, Bengali language dominance

**Verdict**: **Bengaluru wins clearly**. Quality and choice of US-aligned curriculum far superior.

### 5. Wife Employment Opportunities

**Bengaluru**:
- **School jobs**: 50+ international schools hiring teachers/admin
- **Corporate jobs**: Abundant (MNCs, tech companies) for MBA roles
- **Food business**: Large expat community, high demand for American/Western-style baking
- **Catering**: Corporate culture = high demand for event catering
- **Salary**: ₹40-80K/month (school teacher/admin)
- **Entrepreneurship**: Strong ecosystem, many home-based businesses

**Kolkata**:
- **School jobs**: 10-15 international schools (fewer options)
- **Corporate jobs**: Moderate (fewer MNCs, traditional business culture)
- **Food business**: Demand present but less expat community, more traditional tastes
- **Salary**: ₹30-60K/month (20-25% lower)

**Income difference**: ₹10-20K/month (₹3.6-7.2 lakhs over 3 years)

**Verdict**: **Bengaluru wins**. Higher income potential offsets higher cost of living.

### 6. Infrastructure & Connectivity

**Bengaluru**:
- ✅ Internet: 100+ Mbps fiber broadband (ACT, Airtel, Hathway) - ₹1,000-2,000/month
- ✅ Power: Reliable (occasional outages but backup generators common)
- ✅ Water: Cauvery water supply + borewell backup
- ✅ Airport: Kempegowda International (45 km, well-connected)
- ✅ Tech hub: Strong infrastructure for remote work, video calls

**Kolkata**:
- ⚠️ Internet: 50-100 Mbps available but less reliable
- ❌ Power: Frequent power cuts (common in summer)
- ⚠️ Water: Municipal supply + backup, but quality issues
- ✅ Airport: Netaji Subhash Chandra Bose International (well-connected)
- ⚠️ Infrastructure: Aging, slower upgrades

**Verdict**: **Bengaluru wins**. Critical for potential remote US work and EB1A activities (publications, video presentations).

### 7. Air Quality & Climate

**Bengaluru**:
- **AQI**: 50-150 (moderate, better than Delhi/Mumbai/Kolkata)
- **Climate**: Pleasant year-round (15-30°C), called "Garden City"
- **Monsoon**: June-September (manageable rain)
- **Pollution**: Traffic-related, but not industrial

**Kolkata**:
- **AQI**: 100-250 (poor to very poor, especially winter)
- **Climate**: Humid summers (35-40°C, oppressive), mild winters
- **Monsoon**: Heavy rainfall (July-September)
- **Pollution**: Industrial + vehicular

**Verdict**: **Bengaluru wins**. Better for kids' health and outdoor activities.

### 8. Expat & NRI Community

**Bengaluru**:
- ✅ Large NRI community (tech returnees)
- ✅ Expat groups: Facebook, Meetup, InterNations
- ✅ American/Western culture represented (restaurants, stores)
- ✅ Easy to find like-minded families at international schools

**Kolkata**:
- ⚠️ Small expat community (mostly British Council, consulate staff)
- ⚠️ Traditional Bengali culture dominant
- ⚠️ Less Western amenities

**Verdict**: **Bengaluru wins**. Easier social integration for family returning from US.

### 9. Activities & Lifestyle

**Bengaluru**:
- ✅ Taekwondo: 10+ academies
- ✅ Swimming: Apartment pools, clubs, public pools
- ✅ Concerts, theater, tech meetups
- ✅ Outdoor: Nandi Hills, Cubbon Park, weekend getaways (Coorg, Ooty)
- ✅ Restaurants: Global cuisines widely available

**Kolkata**:
- ✅ Cultural: Tagore legacy, literature, art (if interested)
- ⚠️ Fewer Western-style activities
- ⚠️ Taekwondo/martial arts less common
- ✅ Swimming: Available but fewer options
- ✅ Restaurants: Excellent Bengali cuisine, moderate global options

**Verdict**: **Bengaluru wins** for kids' activities and family lifestyle aligned with US upbringing.

### 10. EB1A Building Opportunities

**Bengaluru**:
- ✅ Tech hub: Abundant conferences, meetups, speaking opportunities
- ✅ Networking: Access to US tech companies' India offices (potential remote work)
- ✅ Coworking spaces: Good environment for open source contributions
- ✅ Publication opportunities: Tech blogs, IEEE chapters active
- ✅ Mentoring: Many tech bootcamps, universities for guest lectures

**Kolkata**:
- ⚠️ Smaller tech ecosystem
- ⚠️ Fewer conferences and speaking opportunities
- ⚠️ Less aligned with Silicon Valley culture

**Verdict**: **Bengaluru wins**. Critical for EB1A evidence building (publications, speaking, recognition).

## HYBRID SCENARIO: CAN YOU SPLIT TIME?

**Option**: Live in Bengaluru (primary) + Visit Kolkata/Bankinagar (secondary)

**Feasibility**:
- ✅ Bengaluru → Kolkata: 1,800 km, 2-hour flight (₹3,000-6,000/person one-way)
- ✅ Visit parents in Bankinagar every 2-3 months (3-4 day trips)
- ✅ School holidays: Spend extended time in Kolkata (summer/winter breaks)
- ✅ Total trips/year: 4-6 visits (cost: ₹1-1.5 lakhs/year for family of 4)

**Verdict**: **Best of both worlds**. Live in Bengaluru (father's care, kids' school, wife's job), visit Kolkata regularly (parents, nostalgia, cultural roots).

## FINAL DECISION MATRIX

| Factor | Weight | BLR Score | KOL Score | BLR Weighted | KOL Weighted |
|--------|--------|-----------|-----------|--------------|--------------|
| Father's health | 30% | 10 | 2 | 3.0 | 0.6 |
| Kids' education | 25% | 9 | 6 | 2.25 | 1.5 |
| Wife employment | 15% | 8 | 6 | 1.2 | 0.9 |
| Cost of living | 10% | 5 | 9 | 0.5 | 0.9 |
| Infrastructure | 10% | 9 | 6 | 0.9 | 0.6 |
| Quality of life | 10% | 8 | 6 | 0.8 | 0.6 |
| **TOTAL** | **100%** | - | - | **8.65/10** | **5.1/10** |

**Final Verdict: BENGALURU wins decisively (8.65 vs 5.1)**

## ACTION PLAN

### Decision Confirmed: BENGALURU

**Next Steps**:
1. **School applications**: Focus on Bengaluru schools only (Oakridge, TISB, Greenwood, Inventure)
2. **Housing search**: Sarjapur Road, HSR Layout, Bellandur (near schools and sibling)
3. **Wife job search**: Target Bengaluru schools, food business research
4. **Temporary housing booking**: Serviced apartment in Sarjapur area
5. **Kolkata visits**: Plan 4-6 trips/year to visit parents (budget ₹1-1.5 lakhs/year)

---
**BENGALURU IS THE CLEAR CHOICE - Proceed with confidence.**
"""
    return content

def main():
    """Main function to generate remaining documents."""
    print("Loading research findings...")
    results = load_research_findings('research_findings_raw.json')
    print(f"Found {len(results)} research results")

    print("Organizing findings...")
    organized = extract_findings_by_label(results)

    print("Generating remaining documents...")

    # Generate Employment Plan
    employment_plan = generate_employment_plan(organized['employment'])
    with open('04_wife_employment_plan.md', 'w') as f:
        f.write(employment_plan)
    print("✅ Generated: 04_wife_employment_plan.md")

    # Generate City Comparison
    city_comparison = generate_city_comparison(organized['city_comparison'])
    with open('05_city_comparison_bengaluru_vs_kolkata.md', 'w') as f:
        f.write(city_comparison)
    print("✅ Generated: 05_city_comparison_bengaluru_vs_kolkata.md")

    print("\n✅ Additional documents generated successfully!")

if __name__ == "__main__":
    main()
