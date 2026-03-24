---
name: snowflake-prospecting-plan
description: "Create a Snowflake AI & Data Cloud use-case driven prospecting plan for a customer account. Acts as a deep research specialist supporting account teams in account planning and strategic prospecting. Conducts comprehensive analysis covering: key stakeholders, financial overview, digital/data/AI maturity, technology landscape, market intelligence, competitive landscape, risks/challenges, and strategic initiatives. Maps all findings to Snowflake positioning opportunities. Use when: account planning, prospecting plan, customer research, account strategy, strategic prospecting, account analysis, customer intelligence, prospect research, account review. Triggers: prospecting plan, account plan, customer research, account strategy, account analysis, customer intelligence, strategic prospecting, prospect research, account review, use case prospecting, snowflake positioning."
---

# Snowflake Use-Case Driven Prospecting Plan

Act as a deep research specialist supporting Snowflake AI & Data Cloud account teams in account planning and strategic prospecting. For any given account, conduct a comprehensive and structured analysis, then map findings to Snowflake use-case opportunities.

## Prerequisites

- Internet access for web research (`web_search`, `web_fetch`)
- Optional: Active Snowflake connection if the prospect already has an account (enables internal account assessment via the `snowflake-account-assessment` skill)

## Setup

1. **Load** `references/research_framework.md` for web search templates and research methodology
2. **Load** `references/snowflake_positioning.md` for Snowflake capability-to-use-case mapping
3. **Load** `references/report_template.md` for final output structure

---

## Workflow

```
Phase 1: Account Intake
  ↓
Phase 2: Financial & Business Research
  ↓
Phase 3: Stakeholder & Org Mapping
  ↓
Phase 4: Digital, Data & AI Maturity
  ↓
Phase 5: Technology & Competitive Landscape
  ↓
Phase 6: Risks, Initiatives & Market Signals
  ↓
Phase 7: Snowflake Positioning & Report
  ↓
Phase 8: PDF Export (Snowflake Brand Theme)
```

---

### Phase 1: Account Intake & Setup

**Goal:** Gather target account details and establish research scope.

**Actions:**

1. **Ask** user for account details:
   ```
   To create a prospecting plan, I need:
   1. Company name (required)
   2. Industry / vertical (if known)
   3. Geography / HQ location (if known)
   4. Known contacts or stakeholders (if any)
   5. Any existing Snowflake relationship? (new prospect / existing customer / expansion)
   6. Specific focus areas or priorities for the account team?
   ```

2. **If existing Snowflake customer:** Note that internal account data can supplement web research. Suggest running `snowflake-account-assessment` skill separately for internal platform analysis.

3. **Confirm** research scope with user:
   ```
   Account Research Plan
   =====================
   Company:     [name]
   Industry:    [detected or provided]
   Geography:   [detected or provided]
   Relationship: [new / existing / expansion]
   Focus:       [any specific areas]

   I will now research this account across 8 dimensions:
   1. Key Stakeholders & Decision Makers
   2. Financial & Business Overview
   3. Digital, Data & AI Maturity
   4. Technology & Platform Landscape
   5. External Signals & Market Intelligence
   6. Competitive Landscape
   7. Key Issues, Risks & Challenges
   8. Strategic Initiatives & Priorities

   Proceed with research?
   ```

**STOP**: Wait for user confirmation before proceeding.

---

### Phase 2: Financial & Business Research

**Goal:** Build a financial and business profile of the target account.

**Actions:**

1. **Execute** web searches using templates from `references/research_framework.md`:
   - `web_search("{company} annual report revenue earnings {current_year}")`
   - `web_search("{company} business segments revenue breakdown")`
   - `web_search("{company} investor presentation strategic priorities {current_year}")`
   - `web_search("{company} recent news acquisitions partnerships {current_year}")`

2. **If public company:** Fetch recent earnings/10-K data:
   - `web_search("{company} 10-K SEC filing {current_year}")`
   - `web_search("{company} earnings call transcript latest quarter")`

3. **If private company:** Look for funding rounds, estimated revenue, growth signals:
   - `web_search("{company} funding valuation revenue estimate")`
   - `web_search("{company} Crunchbase PitchBook")`

4. **Compile:**
   - Revenue, growth trends, profitability
   - Key business segments and revenue drivers
   - Recent strategic investments and priorities
   - Notable partnerships, acquisitions, divestitures

**Output:** Financial & Business Profile (internal — feeds into Phase 7 report)

---

### Phase 3: Stakeholder & Org Mapping

**Goal:** Identify executive sponsors, influencers, and technical decision-makers relevant to data, AI, and cloud strategy.

**Actions:**

1. **Execute** stakeholder searches:
   - `web_search("{company} Chief Data Officer VP Data Analytics")`
   - `web_search("{company} CTO CIO Chief Technology Officer")`
   - `web_search("{company} VP Engineering Head of Data Platform")`
   - `web_search("{company} Chief AI Officer VP Machine Learning")`
   - `web_search("{company} Chief Digital Officer VP Digital Transformation")`

2. **Search** for public presence and influence signals:
   - `web_search("{stakeholder_name} {company} conference presentation data")`
   - `web_search("{stakeholder_name} {company} LinkedIn published articles")`

3. **Search** job postings for org structure signals:
   - `web_search("{company} hiring data engineer data scientist cloud architect site:linkedin.com OR site:greenhouse.io OR site:lever.co")`

4. **Map** stakeholders into categories:
   - **Executive Sponsors** (C-level: CDO, CTO, CIO, CDAO)
   - **Technical Decision Makers** (VP/Director: Data Platform, Engineering, Cloud)
   - **Influencers** (Sr. Managers, Architects, Principal Engineers)
   - **Budget Holders** (CFO, VP Finance — if data/AI spend relevant)

5. **Note** for each stakeholder:
   - Title and role
   - Alignment to data/AI/cloud strategy
   - Public visibility (speaker, author, active on social)
   - Potential Snowflake champion signals

**Output:** Stakeholder Map (internal — feeds into Phase 7 report)

---

### Phase 4: Digital, Data & AI Maturity Assessment

**Goal:** Assess the organization's maturity across digital transformation, data platform, and AI/ML adoption.

**Actions:**

1. **Research** published tech/engineering content:
   - `web_search("{company} engineering blog data platform architecture")`
   - `web_search("{company} tech stack data infrastructure")`
   - `web_search("{company} data governance data mesh data lakehouse")`

2. **Research** AI/ML adoption:
   - `web_search("{company} artificial intelligence machine learning use cases")`
   - `web_search("{company} AI strategy GenAI generative AI {current_year}")`
   - `web_search("{company} data science team ML platform")`

3. **Analyze** job postings for maturity signals:
   - `web_search("{company} jobs data engineer Snowflake Databricks BigQuery")`
   - `web_search("{company} jobs machine learning MLOps AI engineer")`

4. **Score** maturity using framework from `references/research_framework.md`:
   - **Digital Transformation**: Early / Progressing / Advanced / Leader
   - **Data Platform Maturity**: Siloed / Consolidating / Unified / Self-Service
   - **AI/ML Adoption**: Experimental / Departmental / Scaled / AI-First
   - **Data Governance**: Ad-hoc / Emerging / Established / Automated

5. **Document** evidence for each rating.

**Output:** Maturity Assessment (internal — feeds into Phase 7 report)

---

### Phase 5: Technology & Competitive Landscape

**Goal:** Map current technology vendors/platforms and competitive dynamics.

**Actions:**

1. **Research** technology stack:
   - `web_search("{company} cloud provider AWS Azure GCP")`
   - `web_search("{company} data warehouse Snowflake Databricks Redshift BigQuery Synapse")`
   - `web_search("{company} analytics BI Tableau Power BI Looker Sigma")`
   - `web_search("{company} ETL data integration Informatica dbt Fivetran Matillion")`
   - `web_search("{company} AI platform SageMaker Vertex Bedrock Dataiku")`

2. **Check** technology review sites:
   - `web_search("site:stackshare.io {company}")`
   - `web_search("site:builtwith.com {company}")`

3. **Research** competitive landscape:
   - `web_search("{company} competitors market position {industry}")`
   - `web_search("{company} vs {competitor} market share")`
   - `web_search("{industry} market leaders competitive analysis {current_year}")`

4. **Map** technology landscape:
   - **Cloud Providers**: Which hyperscalers, multi-cloud vs single
   - **Data Platform**: Current warehouse/lakehouse/lake
   - **Analytics & BI**: Visualization and reporting tools
   - **Data Integration**: ETL/ELT, CDC, streaming tools
   - **AI/ML Platform**: Training, serving, MLOps tooling
   - **Key Vendor Partnerships**: Published partnerships, ISV relationships

5. **Identify** Snowflake positioning opportunities:
   - Where Snowflake can replace or complement existing tools
   - Cross-reference with `references/snowflake_positioning.md`
   - Net-new opportunities (capabilities not currently addressed)

6. **Compile** competitive landscape:
   - Primary competitors and their data/AI strategies
   - Competitive pressures driving technology investment
   - Differentiation strategies

**Output:** Technology Map & Competitive Analysis (internal — feeds into Phase 7 report)

---

### Phase 6: Risks, Initiatives & Market Signals

**Goal:** Capture external signals, identify risks, and map strategic initiatives.

**Actions:**

1. **Research** external signals:
   - `web_search("{company} {industry} analyst report Gartner Forrester IDC {current_year}")`
   - `web_search("{company} news announcement {current_year}")`
   - `web_search("{industry} trends digital transformation {current_year}")`
   - `web_search("{industry} regulations compliance data privacy {current_year}")`

2. **Identify** key issues and risks:
   - Operational challenges (from earnings calls, press)
   - Technology risks (legacy systems, tech debt, vendor lock-in)
   - Market challenges (competition, disruption, regulatory)
   - Data/AI gaps (governance, security, scalability)

3. **Map** strategic initiatives:
   - Published transformation programs
   - AI/data-driven initiatives with stated business outcomes
   - Digital modernization efforts
   - Sustainability / ESG data initiatives

4. **For each risk/gap**, note how Snowflake can help mitigate.

**Output:** Risks, Signals & Initiatives Analysis (internal — feeds into Phase 7 report)

---

### Phase 7: Snowflake Positioning & Report Generation

**Goal:** Synthesize all research into a comprehensive prospecting plan with Snowflake use-case recommendations.

**Actions:**

1. **Load** `references/snowflake_positioning.md` for capability mapping

2. **Cross-reference** all findings to identify top Snowflake opportunities:
   - Match each risk/gap/initiative to specific Snowflake capabilities
   - Score each opportunity: **High / Medium / Low** priority based on:
     - Business impact (revenue, cost, risk, compliance)
     - Data readiness (does the company likely have the data?)
     - Competitive displacement potential (replaces competitor or fills gap)
     - Stakeholder alignment (is there a champion for this?)

3. **Generate** the full report using `references/report_template.md` structure:

   ```
   ═══════════════════════════════════════════════════════════
     SNOWFLAKE USE-CASE DRIVEN PROSPECTING PLAN
   ═══════════════════════════════════════════════════════════

   1. EXECUTIVE SUMMARY
   2. KEY STAKEHOLDERS & DECISION MAKERS
   3. FINANCIAL & BUSINESS OVERVIEW
   4. DIGITAL, DATA & AI MATURITY
   5. TECHNOLOGY & PLATFORM LANDSCAPE
   6. EXTERNAL SIGNALS & MARKET INTELLIGENCE
   7. COMPETITIVE LANDSCAPE
   8. KEY ISSUES, RISKS & CHALLENGES
   9. STRATEGIC INITIATIVES & PRIORITIES
   10. SNOWFLAKE USE-CASE OPPORTUNITIES (Prioritized)
   11. RECOMMENDED ENGAGEMENT STRATEGY
   12. NEXT STEPS & CALL TO ACTION
   ```

4. **Present** the full report to user.

5. **After the report**, offer next steps:
   ```
   Would you like me to:
   1. Export this report as a branded PDF? (Snowflake theme)
   2. Deep-dive into any specific section?
   3. Refine the Snowflake use-case prioritization?
   4. Save this plan to a markdown file?
   5. Run an internal Snowflake account assessment (if existing customer)?
   6. Generate a call prep brief for a specific stakeholder?
   ```

**STOP**: Present report and wait for user direction.

---

### Phase 8: PDF Export (Snowflake Brand Theme)

**Goal:** Generate a professionally styled PDF report using Snowflake Inc's brand colors and design system.

**Trigger:** User requests PDF export (option 1 from Phase 7, or at any time after report is generated).

**Actions:**

1. **Build** a JSON data file containing all report data collected during Phases 2-7. The JSON must match the template variables defined in `templates/report.html`. Structure:

   ```json
   {
     "company_name": "...",
     "report_date": "YYYY-MM-DD",
     "prepared_for": "...",
     "industry": "...",
     "geography": "...",
     "relationship": "New Prospect | Existing Customer | Expansion",
     "executive_summary": {
       "revenue": "...",
       "employees": "...",
       "key_finding": "...",
       "top_opportunities": [{"name": "...", "priority": "HIGH|MEDIUM|LOW"}],
       "maturity": {"Digital Transformation": "...", "Data Platform": "...", "AI/ML": "...", "Governance": "..."}
     },
     "stakeholder_groups": {"Executive Sponsors": [{"name":"...","title":"...","alignment":"...","notes":"..."}]},
     "org_insights": ["..."],
     "financials": {"revenue":"...","growth":"...","profitability":"...","segments":"...","highlights":["..."],"investments":["..."]},
     "maturity_scores": [{"dimension":"...","level":"...","evidence":"..."}],
     "maturity_findings": ["..."],
     "maturity_gaps": ["..."],
     "tech_landscape": [{"category":"...","current":"...","opportunity":"..."}],
     "vendor_relationships": ["..."],
     "announcements": ["..."],
     "analyst_coverage": ["..."],
     "industry_trends": ["..."],
     "partnerships": ["..."],
     "competitors": [{"name":"...","positioning":"...","maturity":"...","threat":"HIGH|MEDIUM|LOW"}],
     "competitive_pressures": ["..."],
     "differentiation": ["..."],
     "risks": [{"issue":"...","category":"...","mitigation":"..."}],
     "initiatives": [{"initiative":"...","status":"...","outcome":"...","alignment":"..."}],
     "opportunities": [{"use_case":"...","priority":"HIGH|MEDIUM|LOW","capabilities":"...","impact":"...","readiness":"...","score":"..."}],
     "engagement": {
       "entry_point": "...",
       "lead_use_case": "...",
       "poc": "...",
       "key_messages": ["..."],
       "objections": [{"objection":"...","response":"..."}]
     },
     "next_steps": ["..."],
     "sources": ["..."]
   }
   ```

2. **Save** the JSON data to a temporary file:
   ```bash
   # Save to working directory
   cat > {company_slug}_report_data.json << 'EOF'
   { ... assembled JSON ... }
   EOF
   ```

3. **Generate** the PDF using the bundled script:
   ```bash
   uv run --project .cortex/skills/snowflake-prospecting-plan \
     python .cortex/skills/snowflake-prospecting-plan/scripts/generate_pdf.py \
     --data {company_slug}_report_data.json \
     --output {company_slug}_prospecting_plan.pdf
   ```

4. **Confirm** output to user:
   ```
   PDF report generated successfully:
     → {company_slug}_prospecting_plan.pdf

   The report includes:
   - Snowflake-branded cover page
   - Table of contents
   - All 12 sections with branded styling
   - Page numbers and confidential footer
   ```

5. **Clean up** the temporary JSON file:
   ```bash
   rm {company_slug}_report_data.json
   ```

**Design:** The PDF uses Snowflake Inc's official brand theme:
- **Primary Blue** (#29B5E8) — accents, list markers, highlights
- **Dark Blue** (#11567F) — section headers, table headers, strong text
- **Navy** (#0D2B45) — cover page background, score cards
- **Light Blue** (#E8F4FD) — alternating table rows, callout backgrounds
- **Accent** (#00A1D9) — links, interactive elements
- Priority badges: HIGH (red), MEDIUM (orange), LOW (green)

---

## Stopping Points

- **Phase 1**: After account intake — confirm details before research
- **Phase 7**: After report generation — present for review and offer PDF export

**Resume rule:** Upon user approval, proceed with their chosen next action. Do NOT re-ask questions already answered.

## Error Handling

**If company cannot be found via web search:**
- Ask user for the company website URL
- Try `web_fetch` on the company site directly
- If still insufficient, ask user to provide known context manually

**If company is very private (no public data):**
- Note data gaps explicitly in the report
- Focus on industry-level analysis and inference
- Mark affected sections as "Limited Data — Requires Direct Discovery"

**If industry is unclear:**
- Present top 2-3 likely industries based on web results
- Ask user to confirm before proceeding

## Output

A comprehensive Snowflake use-case driven prospecting plan containing:
- Executive summary with key findings
- Stakeholder map with decision-maker profiles
- Financial and business context
- Digital, data & AI maturity scoring
- Technology and vendor landscape map
- Competitive positioning analysis
- Risk and gap identification with Snowflake mitigations
- Strategic initiative alignment
- Prioritized Snowflake use-case opportunities (High/Medium/Low)
- Recommended engagement strategy and next steps
- **PDF export** with Snowflake Inc branded theme (cover page, styled tables, page numbers)
