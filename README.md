🚚 LaneGuard AI – Supply Chain Risk Analytics

**An interactive data analytics project for identifying, analyzing, and understanding supply chain shipment disruptions.**

LaneGuard AI transforms shipment data into meaningful business insights using SQL, Python, Power BI, and interactive visualizations. The project explores how transport modes, weather conditions, product categories, and geopolitical risks relate to shipment disruptions.

---

## 📌 Project Overview

Supply chains face several risks, including adverse weather, transportation challenges, fuel price changes, and geopolitical uncertainty.

LaneGuard AI analyzes shipment records to identify disruption patterns and help understand the factors associated with shipment delays and disruptions.

The project includes data quality checks, SQL-based analysis, an interactive Power BI dashboard, and a Python-based Streamlit application.

## 🎯 Project Objectives

- Analyze shipment disruption patterns.
- Identify disruption rates across different transport modes.
- Understand the impact of weather conditions on shipments.
- Compare disruption rates across product categories.
- Analyze geopolitical risk levels and shipment disruptions.
- Track monthly shipment disruption trends.
- Present business insights through interactive dashboards.

## 📊 Dataset Information

**Dataset:** Global Supply Chain Risk & Logistics 2024–2026  
**Source:** Kaggle  
**Total Records:** 5,000 shipments  
**Data Format:** CSV

Dataset source:

[Global Supply Chain Risk & Logistics 2024–2026 – Kaggle](https://www.kaggle.com/datasets/nudratabbas/global-supply-chain-risk-and-logistics-2024-2026)

### Important Dataset Columns

| Column | Description |
|---|---|
| Shipment_ID | Unique shipment identifier |
| Date | Shipment date |
| Origin_Port | Shipment origin |
| Destination_Port | Shipment destination |
| Transport_Mode | Transportation method |
| Product_Category | Product classification |
| Distance_km | Shipment distance |
| Weight_MT | Shipment weight |
| Fuel_Price_Index | Fuel price indicator |
| Geopolitical_Risk_Score | Geopolitical risk score |
| Weather_Condition | Weather during shipment |
| Carrier_Reliability_Score | Carrier reliability |
| Lead_Time_Days | Shipment lead time |
| Disruption_Occurred | Shipment disruption indicator |

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Microsoft Excel | Data inspection and quality validation |
| MySQL 8.0 | Data storage and management |
| SQL | Data analysis and analytical views |
| Power BI | Interactive business intelligence dashboard |
| Python | Application development |
| Pandas | Data processing |
| Streamlit | Interactive web application |
| Plotly | Data visualization |

## 📈 Key Performance Indicators

The project dataset contains 5,000 shipment records.

| KPI | Result |
|---|---:|
| Total Shipments | 5,000 |
| Disrupted Shipments | 3,063 |
| Non-Disrupted Shipments | 1,937 |
| Disruption Rate | 61.26% |
| Non-Disruption Rate | 38.74% |

**Key observation:** 61.26% of the recorded shipments were marked as disrupted in the analyzed dataset.

## 📊 Power BI Dashboard Features

The Power BI dashboard provides an interactive view of shipment disruption patterns.

### Dashboard Analysis

1. **Monthly Shipment Disruption Trend** – Tracks shipment disruption rates over time.
2. **Disruption Rate by Transport Mode** – Compares disruption rates across Air, Rail, Sea, and Road.
3. **Disruption Rate by Weather Condition** – Analyzes disruption patterns across different weather conditions.
4. **Disruption Rate by Product Category** – Compares disruption rates across product categories.
5. **Disruption Rate by Geopolitical Risk** – Examines disruption rates across geopolitical risk bands.

### Interactive Filters

- Transport Mode
- Weather Condition

The dashboard updates its visuals and KPI values according to the selected filters.

## 🗄️ SQL Analysis

MySQL was used to store the shipment dataset and perform analytical queries.

The SQL analysis included:

- Total shipment count.
- Disrupted and non-disrupted shipment counts.
- Overall disruption rate.
- Disruption rate by transport mode.
- Disruption rate by weather condition.
- Monthly disruption analysis.
- Product category risk analysis.
- Geopolitical risk analysis.

Analytical SQL views were also created to organize the results for dashboard reporting.

## 🐍 Python Application

A Streamlit application is included in this repository.

The application uses Python, Pandas, and Plotly for interactive shipment data analysis and visualization.

**Main application file:** `app.py`

## 📁 Repository Structure

```text
LaneGuard-AI-Interactive/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/omshinde-75/LaneGuard-AI-Interactive.git
```

### 2. Open the project folder

```bash
cd LaneGuard-AI-Interactive
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.

## 💡 Business Value

LaneGuard AI demonstrates how data analytics can support supply chain risk analysis by:

- Highlighting shipment disruption patterns.
- Comparing risk across transportation methods.
- Identifying weather-related disruption patterns.
- Understanding geopolitical risk categories.
- Supporting data-driven operational decisions.

## 🔮 Future Improvements

- Develop machine learning models to predict shipment disruption risk.
- Add shipment-level risk scoring.
- Introduce advanced filtering and drill-down analysis.
- Add real-time shipment monitoring.
- Improve the dashboard with additional business KPIs.
- Deploy the application publicly.

## 👨‍💻 Author

**Om Shinde**

Computer Engineering Student | Aspiring Data Analyst

GitHub: [omshinde-75](https://github.com/omshinde-75)

LinkedIn: [Om Shinde](https://www.linkedin.com/in/om-rajendra-shinde)

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.

**LaneGuard AI – Turning Supply Chain Data into Actionable Insights.**
:::
