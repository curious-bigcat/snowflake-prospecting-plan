# Snowflake Prospecting Plan

A [Cortex Code](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code) skill that acts as a deep research specialist supporting Snowflake AI & Data Cloud account teams in account planning and strategic prospecting.

Given a target account, the skill conducts comprehensive web research across 8 dimensions and generates a use-case driven prospecting plan with prioritized Snowflake opportunities — exported as a branded PDF report.

## What It Does

1. **Account Intake** — Collects company name, industry, geography, and relationship status
2. **Financial & Business Research** — Revenue, growth, segments, strategic investments
3. **Stakeholder & Org Mapping** — Executive sponsors, technical decision makers, influencers
4. **Digital, Data & AI Maturity** — Scores maturity across 4 dimensions with evidence
5. **Technology & Competitive Landscape** — Current tech stack, vendor relationships, competitors
6. **Risks, Initiatives & Market Signals** — External signals, challenges, strategic priorities
7. **Snowflake Positioning & Report** — Maps findings to Snowflake use cases, generates 12-section report
8. **PDF Export** — Produces a professionally styled PDF using Snowflake Inc's brand theme

## Output

A 12-section prospecting plan covering:

- Executive summary with top opportunities
- Stakeholder map with decision-maker profiles
- Financial and business context
- Digital, data & AI maturity scoring
- Technology and vendor landscape
- Competitive positioning analysis
- Risk and gap identification with Snowflake mitigations
- Strategic initiative alignment
- Prioritized Snowflake use-case opportunities (High/Medium/Low)
- Recommended engagement strategy and next steps

Exported as a Snowflake-branded PDF with cover page, styled tables, priority badges, and page numbering.

## Skill Structure

```
.cortex/skills/snowflake-prospecting-plan/
├── SKILL.md                              # Main skill definition (8-phase workflow)
├── pyproject.toml                        # Python dependencies (weasyprint, jinja2, markdown)
├── references/
│   ├── report_template.md                # 12-section report structure + PDF export instructions
│   ├── research_framework.md             # Web search templates + maturity scoring framework
│   └── snowflake_positioning.md          # Capability mapping + competitive positioning tables
├── scripts/
│   └── generate_pdf.py                   # JSON -> HTML -> PDF via WeasyPrint + Jinja2
└── templates/
    └── report.html                       # Snowflake-branded HTML/CSS template
```

## How to Use

### 1. Install the Skill

Clone this repo into your project's `.cortex/skills/` directory:

```bash
# From your project root
git clone https://github.com/curious-bigcat/snowflake-prospecting-plan.git \
  .cortex/skills/snowflake-prospecting-plan
```

Or copy the `.cortex/skills/snowflake-prospecting-plan/` folder into your own project.

For global installation (available across all projects):

```bash
git clone https://github.com/curious-bigcat/snowflake-prospecting-plan.git \
  ~/.snowflake/cortex/skills/snowflake-prospecting-plan
```

### 2. Invoke the Skill

Open [Cortex Code](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code) and use any of these prompts:

```
Create a prospecting plan for Acme Corp
```
```
Account analysis for Netflix
```
```
Snowflake positioning for Walmart
```
```
Strategic prospecting for Deutsche Bank
```

### 3. Provide Account Details

The skill will ask for:

| Field | Required | Example |
|-------|----------|---------|
| Company name | Yes | "Acme Corp" |
| Industry | Optional | "Retail", "Financial Services" |
| Geography | Optional | "US - San Francisco" |
| Known contacts | Optional | "Jane Doe - CTO" |
| Snowflake relationship | Optional | "New prospect" / "Existing customer" |
| Focus areas | Optional | "AI/ML adoption", "Data governance" |

### 4. Research Phase (Automatic)

After you confirm, the skill automatically runs web research across 8 dimensions:

1. Financial & business profile
2. Stakeholder & org mapping
3. Digital, data & AI maturity assessment
4. Technology stack discovery
5. Competitive landscape analysis
6. Market signals & external intelligence
7. Risk & challenge identification
8. Strategic initiative mapping

Each phase uses targeted web searches and compiles findings internally.

### 5. Review the Report

The skill presents a 12-section text report. You can then:

- **Export as PDF** — Generates a Snowflake-branded PDF in your working directory
- **Deep-dive** into any section for more detail
- **Refine** the use-case prioritization
- **Save** as markdown
- **Generate** a call prep brief for a specific stakeholder

### 6. PDF Export

When you choose PDF export, the skill:

1. Assembles all research data into structured JSON
2. Renders it through a Snowflake-branded HTML template
3. Converts to PDF via WeasyPrint

The output file is saved as `{company}_prospecting_plan.pdf` in your working directory.

> **Note:** PDF generation requires Python 3.11+ and installs dependencies automatically via `uv run`.

## PDF Brand Theme

The PDF output uses Snowflake Inc's official brand colors:

| Color | Hex | Usage |
|-------|-----|-------|
| Snowflake Blue | `#29B5E8` | Accents, list markers, highlights |
| Dark Blue | `#11567F` | Section headers, table headers |
| Navy | `#0D2B45` | Cover page background, score cards |
| Light Blue | `#E8F4FD` | Alternating table rows, callouts |
| Accent | `#00A1D9` | Links, interactive elements |

## Requirements

- [Cortex Code](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code) with `web_search` and `web_fetch` access
- Python 3.11+ (for PDF generation via `uv run`)
- Optional: Active Snowflake connection for existing customer account assessment
