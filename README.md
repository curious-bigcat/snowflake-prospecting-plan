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

## Usage

Invoke the skill in Cortex Code with any of these triggers:

- "Create a prospecting plan for [Company]"
- "Account analysis for [Company]"
- "Snowflake positioning for [Company]"
- "Strategic prospecting for [Company]"

The skill will guide you through the research phases interactively, then generate the full report and offer PDF export.

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
