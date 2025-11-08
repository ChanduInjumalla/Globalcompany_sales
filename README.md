🌍 GLOBAL SALES PERFORMANCE — End-to-End Data Pipeline
🔥 Raw CSV ➜ Python ETL ➜ SQLite DW ➜ SQL KPIs ➜ BI (Excel + Power BI)
🎯 Objective

Quantify global commercial performance and expose where value concentration actually lives — region, item type, channel & time.

This is not a toy dashboard.
This is a mini data engineering + analytics product.

🧱 Architecture
Layer	Tech	Purpose
Ingestion	pandas	Load + normalize raw CSV
Storage	SQLite	Analytical storage w/ single fact table
Logic	SQL	Business metrics, aggregations, segmentation
Consumption	Power BI + Excel	KPI surfacing, visual decision layer
✅ Delivered KPIs (SQL)
KPI	Why it matters
Top 5 Regions by Total Revenue	Where our money actually comes from
Top 3 Item Types by Total Profit	Category profitability & pricing signal
Quarterly Avg Revenue YoY	Seasonality + revenue cyclicality

all SQL lives in query.sql — pure reproducible logic

🧪 Pipeline Flow
project1-dataset.csv
        │
        ▼
main.py  --> cleans, type derives, builds sales_data.db
        ▼
query.sql --> computes revenue/profit/quarter behaviour
        ▼
export.py --> ships final dataset back to CSV for BI
        ▼
Power BI --> business layer + storytelling

📊 BI Outcome

Power BI dashboard includes:

KPI card block (Total Revenue / Profit / Margin %)

Geo bubble Map: Profit by Country

Monthly Revenue Trend (2010–2017)

Online vs Offline order mix

PBIX file included in repo.

🧠 Core Skills Flexed

schema rationalization

date casting & type enforcement

quarter bucketing logic using STRFTIME()

dimensional slicing

BI friendly export design

🗃 Repository Contents
File	Purpose
main.py	ETL + DB load
export.py	DB ➜ CSV export
query.sql	KPI computations
project1-dataset.csv	raw source
sales_data.db	analytical DB
sales_export.csv	cleaned output for BI