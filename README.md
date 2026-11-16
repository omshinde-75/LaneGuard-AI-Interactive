# 🚢 LaneGuard AI – Supply Chain Shipment Risk Analytics

<p align="center">
  <b>An Interactive Data Analytics Project for Understanding and Analyzing Supply Chain Shipment Disruptions</b>
</p>

<p align="center">
  <a href="https://laneguard-ai-interactive-smrqkq4hk33qjl9r67ads4.streamlit.app/">🚀 Live Dashboard</a> |
  <a href="https://github.com/omshinde-75/LaneGuard-AI-Interactive">💻 GitHub Repository</a> |
  <a href="https://www.kaggle.com/datasets/nudratabbas/global-supply-chain-risk-and-logistics-2024-2026">📊 Dataset Source</a>
</p>

---

## 📌 Project Overview

LaneGuard AI is an interactive supply chain risk analytics dashboard designed to analyze shipment disruptions and identify patterns across transportation modes, weather conditions, product categories, and geopolitical risk levels.

The project transforms raw shipment data into meaningful business insights using Python, SQL, Excel, Power BI, and interactive data visualizations.

The dashboard allows users to explore shipment performance through dynamic filters, KPI metrics, and interactive charts.

**The main objective is to understand shipment disruption patterns and help identify potential supply chain risk factors through data analysis.**

## 🎯 Project Objectives

- Analyze shipment disruption patterns.
- Calculate total and disrupted shipments.
- Compare disruption rates across transportation modes.
- Understand the relationship between weather conditions and disruptions.
- Analyze disruption rates across product categories.
- Explore geopolitical risk levels and shipment disruptions.
- Visualize monthly shipment disruption trends.
- Build an interactive dashboard for business insights.

## 📊 Key Performance Indicators

The original dataset contains 5,000 shipment records.

| KPI | Result |
|---|---:|
| Total Shipments | 5,000 |
| Disrupted Shipments | 3,063 |
| Non-Disrupted Shipments | 1,937 |
| Overall Disruption Rate | 61.26% |
| Non-Disruption Rate | 38.74% |

## 🖥️ Live Interactive Dashboard

Explore the deployed dashboard:

**[🚀 Open LaneGuard AI Live Dashboard](https://laneguard-ai-interactive-smrqkq4hk33qjl9r67ads4.streamlit.app/)**

### Dashboard Features

- Automatic dataset loading.
- Interactive transport mode filters.
- Weather condition filters.
- Product category filters.
- Dynamic KPI cards.
- Transport mode disruption analysis.
- Weather-based disruption analysis.
- Product category risk analysis.
- Geopolitical risk analysis.
- Monthly shipment disruption trends.
- Shipment data preview.
- Download filtered shipment data as CSV.

## 📸 Dashboard Screenshots

Screenshots of the project dashboard will be added here.

Once screenshots are uploaded into the `screenshots/` folder, use:

```markdown
![LaneGuard AI Dashboard](screenshots/dashboard-overview.png)
```

Additional screenshots can include:

- KPI overview
- Transport mode analysis
- Weather condition analysis
- Product category analysis
- Geopolitical risk analysis
- Interactive filters

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and dashboard development |
| Pandas | Data cleaning and manipulation |
| Plotly | Interactive charts and visualizations |
| Streamlit | Interactive web dashboard |
| SQL / MySQL | Data storage and analytical queries |
| Microsoft Excel | Data quality checks and validation |
| Power BI | Business intelligence dashboard |
| GitHub | Version control and project documentation |
| Kaggle | Dataset source |

## 📂 Dataset Information

**Dataset:** Global Supply Chain Risk & Logistics 2024–2026

**Source:** Kaggle

[Download Dataset](https://www.kaggle.com/datasets/nudratabbas/global-supply-chain-risk-and-logistics-2024-2026)

The dataset contains 5,000 shipment records and 14 columns.

### Dataset Columns

1. Shipment_ID
2. Date
3. Origin_Port
4. Destination_Port
5. Transport_Mode
6. Product_Category
7. Distance_km
8. Weight_MT
9. Fuel_Price_Index
10. Geopolitical_Risk_Score
11. Weather_Condition
12. Carrier_Reliability_Score
13. Lead_Time_Days
14. Disruption_Occurred

## 🔍 Data Analysis Performed

### 1. Data Cleaning and Validation

- Checked missing values.
- Checked duplicate shipment IDs.
- Validated shipment records.
- Checked numerical columns and disruption labels.
- Prepared data for analysis.

### 2. SQL Analysis

SQL was used to explore shipment disruption patterns.

Key analytical areas:

- Total shipment counts.
- Disrupted versus non-disrupted shipments.
- Disruption rates by transport mode.
- Disruption rates by weather condition.
- Monthly disruption trends.
- Geopolitical risk analysis.
- Product category comparisons.

### 3. Power BI Dashboard

Created a business intelligence dashboard containing:

- KPI cards.
- Monthly shipment disruption trend.
- Transport mode risk comparison.
- Weather condition analysis.
- Product category disruption analysis.
- Geopolitical risk analysis.
- Interactive slicers.

### 4. Python Interactive Dashboard

Developed a Streamlit web application with:

- Automatic CSV loading.
- Interactive filters.
- Dynamic KPI calculations.
- Plotly visualizations.
- Shipment data preview.
- Filtered CSV export.

## 📈 Key Insights

Based on the overall dataset analysis:

- Out of 5,000 shipments, 3,063 experienced disruptions.
- The overall shipment disruption rate is 61.26%.
- The dataset contains 1,937 non-disrupted shipments.
- Transportation mode, weather, product category, and geopolitical risk provide different dimensions for analyzing shipment disruptions.
- Interactive filtering makes it possible to investigate specific shipment groups.

## ⚙️ Project Structure

```text
LaneGuard-AI-Interactive/
│
├── app.py
│
├── global_supply_chain_risk_2026.csv
│
├── requirements.txt
│
├── README.md
│
└── screenshots/
    ├── dashboard-overview.png
    ├── transport-analysis.png
    ├── weather-analysis.png
    ├── product-analysis.png
    └── geopolitical-risk.png
```

The screenshots folder is a planned addition; create it and upload your screenshots when available.

## 🚀 Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/omshinde-75/LaneGuard-AI-Interactive.git
```

### Step 2: Open the project directory

```bash
cd LaneGuard-AI-Interactive
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```bash
streamlit run app.py
```

### Step 5: Open the local dashboard

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

## 📦 Requirements

The project uses the following Python libraries:

- Streamlit
- Pandas
- Plotly

Install them using:

```bash
pip install streamlit pandas plotly
```

## 💡 Future Improvements

- Add machine learning models for shipment disruption prediction.
- Develop shipment risk scoring.
- Add shipment delay prediction.
- Integrate real-time weather information.
- Add automated risk alerts.
- Connect the dashboard to a live database.
- Improve geographical shipment risk visualization.

*These are planned improvements, not currently implemented features.*

## ⚠️ Project Notes

- This project is an analytics and visualization application, not a production shipment prediction system.
- The current dashboard analyzes the provided dataset.
- The dataset is sourced from Kaggle.
- The project does not currently use a trained machine learning model.
- The Power BI dashboard and Streamlit dashboard are separate deliverables.

## 👨‍💻 Author

**Om Shinde**

BE Computer Engineering Student  
Aspiring Data Analyst | Data Science Enthusiast

- GitHub: [@omshinde-75](https://github.com/omshinde-75)
- LinkedIn: [Om Shinde](https://www.linkedin.com/in/om-rajendra-shinde/)

---

<p align="center">
  <b>Built with Python, SQL, Power BI, Excel and Streamlit.</b>
</p>

<p align="center">
  🚢 Turning shipment data into meaningful supply chain insights.
</p>
