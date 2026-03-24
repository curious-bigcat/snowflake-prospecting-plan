#!/usr/bin/env python3
"""
Generate a Snowflake-branded PDF prospecting report from JSON data.

Usage:
    uv run --project <skill_dir> python <skill_dir>/scripts/generate_pdf.py \
        --data report_data.json \
        --output report.pdf

The JSON file must contain the report data dictionary matching the
Jinja2 template variables defined in templates/report.html.
"""

import argparse
import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def load_data(data_path: str) -> dict:
    """Load and validate report data from JSON file."""
    path = Path(data_path)
    if not path.exists():
        print(f"Error: Data file not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ensure required top-level keys have defaults
    defaults = {
        "company_name": "Unknown Company",
        "report_date": "—",
        "prepared_for": "—",
        "industry": "—",
        "geography": "—",
        "relationship": "New Prospect",
        "executive_summary": {},
        "stakeholder_groups": {},
        "org_insights": [],
        "financials": {},
        "maturity_scores": [],
        "maturity_findings": [],
        "maturity_gaps": [],
        "tech_landscape": [],
        "vendor_relationships": [],
        "announcements": [],
        "analyst_coverage": [],
        "industry_trends": [],
        "partnerships": [],
        "competitors": [],
        "competitive_pressures": [],
        "differentiation": [],
        "risks": [],
        "initiatives": [],
        "opportunities": [],
        "engagement": {},
        "next_steps": [],
        "sources": [],
    }

    for key, default in defaults.items():
        data.setdefault(key, default)

    return data


def render_pdf(data: dict, output_path: str) -> str:
    """Render HTML template with data and convert to PDF."""
    # Resolve template directory relative to this script
    skill_dir = Path(__file__).resolve().parent.parent
    template_dir = skill_dir / "templates"

    if not (template_dir / "report.html").exists():
        print(f"Error: Template not found at {template_dir}/report.html", file=sys.stderr)
        sys.exit(1)

    # Load and render Jinja2 template
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=False,
    )
    template = env.get_template("report.html")
    html_content = template.render(**data)

    # Convert HTML to PDF
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    HTML(
        string=html_content,
        base_url=str(template_dir),
    ).write_pdf(str(output))

    return str(output.resolve())


def main():
    parser = argparse.ArgumentParser(
        description="Generate Snowflake-branded PDF prospecting report"
    )
    parser.add_argument(
        "--data",
        required=True,
        help="Path to JSON file containing report data",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output PDF file path",
    )

    args = parser.parse_args()

    print(f"Loading report data from: {args.data}")
    data = load_data(args.data)

    print(f"Generating PDF for: {data['company_name']}")
    result_path = render_pdf(data, args.output)

    print(f"PDF generated successfully: {result_path}")


if __name__ == "__main__":
    main()
