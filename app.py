
import streamlit as st
import pandas as pd
import json
from pathlib import Path

# PAGE CONFIG

st.set_page_config(
    page_title="Global Patent Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# PATHS

REPORTS_DIR = Path("reports")

# LOAD DATA

@st.cache_data
def load_csv(file_name):
    path = REPORTS_DIR / file_name
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()

@st.cache_data
def load_json(file_name):
    path = REPORTS_DIR / file_name
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

top_inventors = load_csv("top_inventors.csv")
top_companies = load_csv("top_companies.csv")
top_countries = load_csv("top_countries.csv")
country_trends = load_csv("country_trends.csv")
yearly_trends = load_csv("yearly_patent_trends_full.csv")
ranking = load_csv("inventor_ranking.csv")
report_json = load_json("patent_report.json")

# TITLE

st.title("Global Patent Intelligence Dashboard")
st.write(
    "This dashboard presents analysis from the Global Patent Intelligence Data Pipeline by Hisham Jarudi Luzige. "
      "It shows top inventors, leading companies, top patent-producing countries, and yearly patent trends."
)

# METRICS

st.subheader(" Project Summary")

total_patents = report_json.get("total_patents_in_main_database", "N/A")
trend_summary = report_json.get("yearly_trends_summary", {})

col1, col2, col3, col4 = st.columns(4)

col1.metric("Main Database Patents", total_patents)
col2.metric("First Trend Year", trend_summary.get("first_year", "N/A"))
col3.metric("Last Trend Year", trend_summary.get("last_year", "N/A"))
col4.metric(
    "Highest Patent Year",
    f"{trend_summary.get('highest_year', 'N/A')} "
    f"({trend_summary.get('highest_year_patents', 'N/A')})"
)

# TOP COUNTRIES

st.subheader("Top Patent-Producing Countries")

if not top_countries.empty:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.dataframe(top_countries, use_container_width=True)

    with col2:
        chart_data = top_countries.set_index("country")["total_patents"]
        st.bar_chart(chart_data)
else:
    st.warning("top_countries.csv not found.")

# TOP COMPANIES

st.subheader(" Top Companies by Patent Ownership")

if not top_companies.empty:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.dataframe(top_companies, use_container_width=True)

    with col2:
        chart_data = top_companies.set_index("name")["total_patents"]
        st.bar_chart(chart_data)
else:
    st.warning("top_companies.csv not found.")

# TOP INVENTORS

st.subheader("Top Inventors")

if not top_inventors.empty:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.dataframe(top_inventors, use_container_width=True)

    with col2:
        chart_data = top_inventors.set_index("name")["total_patents"]
        st.bar_chart(chart_data)
else:
    st.warning("top_inventors.csv not found.")

# YEARLY TRENDS

st.subheader(" Patent Trends Over Time")

if not yearly_trends.empty:
    yearly_trends["year"] = yearly_trends["year"].astype(int)
    yearly_trends = yearly_trends.sort_values("year")

    selected_years = st.slider(
        "Select year range",
        int(yearly_trends["year"].min()),
        int(yearly_trends["year"].max()),
        (int(yearly_trends["year"].min()), int(yearly_trends["year"].max()))
    )

    filtered_years = yearly_trends[
        (yearly_trends["year"] >= selected_years[0]) &
        (yearly_trends["year"] <= selected_years[1])
    ]

    st.line_chart(
        filtered_years.set_index("year")["total_patents"]
    )

    st.dataframe(filtered_years, use_container_width=True)
else:
    st.warning("yearly_patent_trends_full.csv not found.")

# INVENTOR RANKING

st.subheader("Inventor Ranking Using SQL Window Function")

if not ranking.empty:
    st.dataframe(ranking, use_container_width=True)
else:
    st.warning("inventor_ranking.csv not found.")

# COUNTRY TRENDS

st.subheader(" Country Trends from Main Sample")

if not country_trends.empty:
    countries = sorted(country_trends["country"].dropna().unique())

    selected_country = st.selectbox(
        "Select a country",
        countries
    )

    selected_country_data = country_trends[
        country_trends["country"] == selected_country
    ]

    st.dataframe(selected_country_data, use_container_width=True)

    if "year" in selected_country_data.columns:
        st.line_chart(
            selected_country_data.set_index("year")["total_patents"]
        )
else:
    st.warning("country_trends.csv not found.")

# PROJECT EXPLANATION

st.subheader("Summary of the Project")

st.write("""
This dashboard is the final reporting layer of the data pipeline.

The project follows this flow:

**Raw patent files → Python/pandas cleaning → SQLite database → SQL queries → CSV/JSON/visual reports → Streamlit dashboard**

It demonstrates Big Data concepts such as volume, variety, data cleaning, structured storage, analytical SQL, and visual reporting.
""")

st.success("Dashboard loaded successfully ")
