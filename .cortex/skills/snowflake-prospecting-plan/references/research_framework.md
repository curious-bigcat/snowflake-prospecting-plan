# Research Framework — Web Search Templates & Methodology

Structured research templates for each phase of the prospecting plan. Use these query patterns as starting points — adapt based on company name, industry, and geography.

---

## Search Query Templates by Phase

### Phase 2: Financial & Business

**Public Companies:**
```
"{company}" annual revenue earnings {year}
"{company}" 10-K annual report SEC filing
"{company}" earnings call transcript Q{quarter} {year}
"{company}" business segments revenue breakdown
"{company}" investor presentation strategic priorities
"{company}" acquisitions partnerships {year}
"{company}" market cap growth trajectory
```

**Private Companies:**
```
"{company}" funding round Series valuation
"{company}" Crunchbase revenue estimate
"{company}" PitchBook company profile
"{company}" growth headcount employees
"{company}" customer base market position
```

### Phase 3: Stakeholders

```
"{company}" Chief Data Officer CDO
"{company}" CTO "Chief Technology Officer"
"{company}" CIO "Chief Information Officer"
"{company}" "VP Data" OR "VP Analytics" OR "VP Engineering"
"{company}" "Chief AI Officer" OR "VP Machine Learning" OR "Head of AI"
"{company}" "Chief Digital Officer" OR "VP Digital Transformation"
"{company}" "Head of Data Platform" OR "Director Data Engineering"
"{stakeholder_name}" "{company}" conference keynote presentation
"{stakeholder_name}" "{company}" published article data AI
site:linkedin.com "{company}" "data" OR "analytics" OR "AI" director VP
```

### Phase 4: Digital & AI Maturity

```
"{company}" engineering blog data platform
"{company}" tech stack technology infrastructure
"{company}" data warehouse cloud migration
"{company}" data governance data catalog
"{company}" data mesh data fabric architecture
"{company}" machine learning AI use cases production
"{company}" generative AI GenAI strategy {year}
"{company}" MLOps ML platform deployment
"{company}" hiring data engineer Snowflake Databricks BigQuery
"{company}" hiring "machine learning engineer" OR "AI engineer" OR "data scientist"
```

### Phase 5: Technology Landscape

```
"{company}" cloud provider AWS Azure GCP multi-cloud
"{company}" Snowflake OR Databricks OR Redshift OR BigQuery
"{company}" Tableau OR "Power BI" OR Looker OR Sigma OR Qlik
"{company}" dbt OR Fivetran OR Matillion OR Informatica OR Talend
"{company}" SageMaker OR "Vertex AI" OR Bedrock OR Dataiku OR H2O
site:stackshare.io "{company}"
site:builtwith.com "{company}"
"{company}" technology partner ecosystem vendor
```

### Phase 5b: Competitive Landscape

```
"{company}" competitors market share {industry}
"{company}" vs {competitor_1} vs {competitor_2}
{industry} market leaders competitive landscape {year}
"{company}" competitive advantage differentiation strategy
{industry} Gartner Magic Quadrant OR Forrester Wave {year}
```

### Phase 6: Risks, Signals & Initiatives

```
"{company}" challenges risks {year}
"{company}" digital transformation initiative program
"{company}" AI strategy data strategy announcement
"{company}" regulatory compliance {industry_regulation}
"{company}" cybersecurity data breach privacy
"{company}" ESG sustainability data reporting
{industry} trends disruption {year}
{industry} regulations data privacy compliance {year}
"{company}" analyst report Gartner Forrester IDC
```

---

## Digital & AI Maturity Scoring Framework

### Digital Transformation Maturity

| Level | Signals |
|-------|---------|
| **Early** | No public tech blog; legacy-heavy job postings; no cloud mentions; waterfall references |
| **Progressing** | Cloud migration underway; some SaaS adoption; hybrid architecture; hiring for cloud roles |
| **Advanced** | Cloud-native or cloud-first strategy; API-driven; DevOps/CI-CD mature; microservices |
| **Leader** | Published innovation stories; open-source contributions; engineering brand; tech conference speakers |

### Data Platform Maturity

| Level | Signals |
|-------|---------|
| **Siloed** | Multiple disconnected databases; no central warehouse; department-level tools only |
| **Consolidating** | Migrating to central platform; data warehouse project underway; hiring data engineers |
| **Unified** | Central data platform in production; governance emerging; self-service BI growing |
| **Self-Service** | Governed data mesh/marketplace; data products; advanced lineage; broad analyst access |

### AI/ML Adoption

| Level | Signals |
|-------|---------|
| **Experimental** | No public AI mentions; no ML job postings; maybe pilot discussions |
| **Departmental** | AI in 1-2 departments; published PoC or pilot; hiring first data scientists |
| **Scaled** | ML in production across multiple use cases; MLOps tooling; dedicated AI team |
| **AI-First** | AI embedded in core products/services; published AI research; AI leadership team |

### Data Governance

| Level | Signals |
|-------|---------|
| **Ad-hoc** | No governance mentions; no CDO; compliance-driven only |
| **Emerging** | CDO appointed; governance program announced; catalog project underway |
| **Established** | Published governance framework; classification in place; access controls mature |
| **Automated** | Policy-as-code; automated classification; real-time quality monitoring; lineage tracking |

---

## Job Posting Analysis Guide

Job postings reveal technology stack and maturity. Look for:

**Technology signals:**
- Explicit tool mentions (Snowflake, Databricks, Redshift, etc.)
- Cloud certifications required (AWS, Azure, GCP)
- Programming languages (Python, Scala, Java, SQL, dbt)
- Framework mentions (Spark, Kafka, Airflow, Terraform)

**Maturity signals:**
- "Build from scratch" → Early stage
- "Scale existing platform" → Growing/Established
- "Optimize and govern" → Mature
- Number of data/AI roles open → Investment level
- Seniority of roles → Team maturity (hiring ICs vs. leaders)

**Organizational signals:**
- Reporting structure (CDO reports to CEO vs CIO)
- Team size mentions
- Cross-functional vs centralized data team
