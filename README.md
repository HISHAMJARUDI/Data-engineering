# Data-engineering
Data engineering

# Global Patent Intelligence Data Pipeline

## 1. Project Overview

This project builds a simple data pipeline for global patent intelligence using real-world patent data from PatentsView.

The system collects patent data, cleans it using Python and pandas, stores the cleaned data in an SQLite database, analyzes the data using SQL queries, and generates reports in CSV, JSON, console output, and graph formats.

## 2. Project Pipeline

The pipeline follows this structure:

Data Source Files  
↓  
Python Script for Reading Data  
↓  
pandas for Data Cleaning  
↓  
SQLite Database Storage  
↓  
SQL Queries for Analysis  
↓  
CSV, JSON, Console, and Graph Reports  

## 3. Dataset Used

The project uses PatentsView granted patent data files, including:

- `g_patent.tsv`
- `g_patent_abstract.tsv`
- `g_inventor_disambiguated.tsv`
- `g_assignee_disambiguated.tsv`
- `g_location_disambiguated.tsv`

## 4. Tools and Technologies

- Python
- pandas
- SQLite
- SQL
- Matplotlib
- GitHub

## 5. Database Tables

The SQLite database contains the following tables:

### patents

Stores patent information.

Columns:

- patent_id
- title
- abstract
- filing_date
- year

### inventors

Stores inventor information.

Columns:

- inventor_id
- name
- country

### companies

Stores company or assignee information.

Columns:

- company_id
- name

### relationships

Connects patents, inventors, and companies.

Columns:

- patent_id
- inventor_id
- company_id

## 6. SQL Analysis Questions

The project answers the following questions:

1. Who are the top inventors by number of patents?
2. Which companies own the most patents?
3. Which countries produce the most patents?
4. How many patents are created each year?
5. How can patents, inventors, and companies be joined together?
6. How can a CTE query be used to simplify analysis?
7. How can inventors be ranked using SQL window functions?

## 7. Reports Generated

The project generates the following reports:

### CSV Reports

- `top_inventors.csv`
- `top_companies.csv`
- `top_countries.csv`
- `country_trends.csv`
- `yearly_patent_trends_full.csv`
- `inventor_ranking.csv`

### JSON Report

- `patent_report.json`

### Graph Reports

- `top_inventors.png`
- `top_companies.png`
- `top_countries.png`
- `yearly_patent_trends.png`

## 8. Main Findings

From the sample database of 50,000 patents:

- The top inventor was Kangguo Cheng with 56 patents.
- The top company was International Business Machines Corporation with 1,463 patents.
- The country with the most patents was the United States.
- Full yearly patent trend analysis covered 1976 to 2025.
- The highest patent year in the full trend analysis was 2019 with 392,618 patents.

## 9. How to Run the Project

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
