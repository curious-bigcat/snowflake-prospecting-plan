# Snowflake Positioning — Capability-to-Use-Case Mapping

Map prospect findings to specific Snowflake AI & Data Cloud capabilities. Use during Phase 7 to identify and prioritize Snowflake opportunities.

---

## Core Platform Capabilities

### Data Warehousing & Analytics
| Capability | Use When You Find | Business Pitch |
|---|---|---|
| Elastic Compute (Warehouses) | Legacy on-prem DW; performance complaints; scaling issues | Instant scale, no tuning, pay-per-second |
| Multi-Cluster Warehouses | Concurrency issues; BI query queues; user complaints | Automatic scaling for any number of concurrent users |
| Zero-Copy Cloning | Long dev/test cycles; production data access delays | Instant dev/test environments at zero storage cost |
| Time Travel | Data recovery needs; audit requirements; compliance | Point-in-time recovery, regulatory compliance |
| Search Optimization | LIKE/substring queries on large tables; text search needs | Sub-second search on billions of rows |
| Query Acceleration | Unpredictable ad-hoc query workloads; outlier queries | Offload compute-intensive portions automatically |
| Materialized Views | Repetitive aggregation queries; dashboard performance | Pre-computed results, auto-maintained |

### Data Engineering & Pipelines
| Capability | Use When You Find | Business Pitch |
|---|---|---|
| Dynamic Tables | Complex ETL orchestration; Airflow/dbt heavy; data freshness SLAs | Declarative pipelines, auto-refresh, no orchestration code |
| Streams + Tasks | CDC requirements; event-driven processing; real-time needs | Native change tracking without Kafka/Debezium |
| Snowpipe / Snowpipe Streaming | High-volume continuous ingestion; Kafka-based loading | Sub-second ingestion, auto-scaling, serverless |
| External Stages (S3/ADLS/GCS) | Data lake patterns; Parquet/ORC/Avro files | Query data in place, no copy needed |
| Iceberg Tables | Multi-engine requirements; open format mandate; lakehouse strategy | Full Iceberg support with Snowflake performance |
| Stored Procedures (Python/Java) | Complex transformations; Spark workloads; custom UDFs | Run Python/Java natively in Snowflake, no separate cluster |

### AI, ML & Advanced Analytics
| Capability | Use When You Find | Business Pitch |
|---|---|---|
| Cortex AI Functions | Text analytics needs; sentiment, classification, extraction | Built-in AI — no ML expertise needed, SQL-callable |
| Cortex AI Complete (LLM) | GenAI interest; chatbot needs; content generation | Enterprise-grade LLMs on your data, no data leaves Snowflake |
| Cortex Search | RAG/knowledge base needs; document search; Q&A over docs | Managed vector search + LLM retrieval in one service |
| Cortex Analyst | Business user self-service; natural language BI; semantic layer | Ask questions in English, get SQL answers from governed data |
| Cortex Agents | Multi-step AI workflows; AI assistants; tool-using agents | Orchestrated AI agents with access to your data tools |
| ML Model Registry | MLOps needs; model versioning; model serving | Managed model lifecycle from training to serving |
| Snowpark ML | Custom ML training; feature engineering; Python ML pipelines | Train models at warehouse scale, no external infrastructure |
| Notebooks | Exploration/experimentation; data science collaboration | Git-integrated notebooks running on Snowflake compute |

### Data Governance & Security
| Capability | Use When You Find | Business Pitch |
|---|---|---|
| Dynamic Data Masking | PII/PHI exposure; compliance mandates; role-based access | Column-level masking without changing queries or apps |
| Row Access Policies | Multi-tenant data; regional access; department segmentation | Row-level security, declarative, centralized |
| Object Tagging & Classification | No data catalog; unknown sensitive data; compliance gaps | Auto-classify PII/PHI, tag-based policy enforcement |
| Data Metric Functions (DMFs) | Data quality issues; trust deficit; no monitoring | Automated quality checks, anomaly detection, SLA tracking |
| Lineage & Access History | No impact analysis; change risk; audit requirements | End-to-end lineage, column-level, automatic |
| Network Policies | Security requirements; IP restrictions; zero-trust | Network-level access control, PrivateLink support |

### Data Sharing & Collaboration
| Capability | Use When You Find | Business Pitch |
|---|---|---|
| Secure Data Sharing | B2B data exchange; partner data needs; subsidiary data | Live data sharing, no ETL, no copies, governed |
| Data Clean Rooms | Privacy-safe analytics; advertising measurement; cross-org | Collaborate on data without exposing raw records |
| Snowflake Marketplace | Third-party data needs; enrichment; market data | 2000+ live data sets, instant access, no integration |
| Data Listings (Publishing) | Data monetization opportunity; partner ecosystem | Publish data products to partners or Marketplace |

### Data Applications
| Capability | Use When You Find | Business Pitch |
|---|---|---|
| Streamlit in Snowflake | Internal tool needs; data app requests; dashboard gaps | Build Python apps on Snowflake data, governed, deployed instantly |
| Snowpark Container Services | Custom app hosting; Docker workloads; GPU needs | Run any container on Snowflake compute, full isolation |
| Native Apps Framework | ISV distribution; packaged analytics; partner solutions | Distribute apps through Marketplace with provider logic |

---

## Competitive Positioning

### vs. Databricks
| Scenario | Snowflake Advantage |
|---|---|
| Data warehouse-first workloads | Superior warehouse performance, simpler operations, no cluster management |
| Data sharing / collaboration | Native cross-account sharing (Databricks requires Delta Sharing setup) |
| Governance & security | Built-in masking, row access, classification (Databricks requires Unity Catalog add-on) |
| Business user self-service | Cortex Analyst, Streamlit in Snowflake, Marketplace |
| Mixed SQL + Python workloads | Snowpark + SQL in one platform vs. separate Spark clusters |

### vs. Google BigQuery
| Scenario | Snowflake Advantage |
|---|---|
| Multi-cloud requirement | Runs on AWS, Azure, GCP (BigQuery is GCP-only) |
| Workload isolation | Separate warehouses per team/workload (BigQuery shares slots) |
| Data sharing across clouds | Cross-cloud data sharing (BigQuery limited to GCP) |
| Governance maturity | Dynamic masking, row access, tags (BigQuery more limited) |

### vs. Amazon Redshift
| Scenario | Snowflake Advantage |
|---|---|
| Elasticity / scaling | Instant scale up/down, multi-cluster (Redshift requires resize/RA3 planning) |
| Zero management | No vacuuming, no sort keys, no distribution keys |
| Semi-structured data | Native VARIANT type, auto-schema detection (Redshift SUPER type more limited) |
| AI/ML built-in | Cortex AI functions, ML model registry (Redshift requires SageMaker integration) |

### vs. Azure Synapse
| Scenario | Snowflake Advantage |
|---|---|
| Simplicity | Single, consistent SQL engine (Synapse has dedicated/serverless/Spark pools) |
| Cross-cloud | Not locked to Azure (Synapse is Azure-only) |
| Data sharing | Native sharing without Azure-specific setup |
| AI integration | Cortex AI functions built-in (Synapse requires Azure ML/OpenAI integration) |

---

## Opportunity Scoring Rubric

Score each identified opportunity on 4 dimensions (1-5 each):

| Dimension | 1 (Low) | 3 (Medium) | 5 (High) |
|---|---|---|---|
| **Business Impact** | Nice-to-have; marginal improvement | Meaningful efficiency or insight gain | Revenue, compliance, or risk-critical |
| **Data Readiness** | Data doesn't exist yet | Some data available, gaps to fill | Data already collected and accessible |
| **Competitive Displacement** | No incumbent to displace | Incumbent exists but has weaknesses | Clear displacement path with advantages |
| **Stakeholder Alignment** | No known champion | Relevant team exists, no contact yet | Identified champion or executive sponsor |

**Priority Classification:**
- **High** (16-20 total): Lead with this in initial conversations
- **Medium** (10-15 total): Include in broader platform pitch
- **Low** (4-9 total): Park for future expansion conversations
