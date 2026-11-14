
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="LaneGuard AI",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 LaneGuard AI")
st.subheader("Supply Chain Shipment Risk Analytics Dashboard")
st.caption("Analyze shipment disruptions across transport, weather, products and geopolitical risk.")

uploaded_file = st.file_uploader("Upload your shipment CSV file", type=["csv"])

if uploaded_file is None:
    st.info("Please upload global_supply_chain_risk_2026.csv to view the dashboard.")
    st.stop()

df = pd.read_csv(uploaded_file)

# Standardize column names
df.columns = df.columns.str.strip()

required_columns = [
    "Shipment_ID", "Transport_Mode", "Product_Category",
    "Weather_Condition", "Geopolitical_Risk_Score",
    "Disruption_Occurred"
]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    st.error(f"Missing required columns: {', '.join(missing)}")
    st.stop()

# Prepare data
date_column = "Shipment_Date" if "Shipment_Date" in df.columns else "Date"

if date_column in df.columns:
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

df["Disruption_Occurred"] = pd.to_numeric(
    df["Disruption_Occurred"], errors="coerce"
)

df["Geopolitical_Risk_Score"] = pd.to_numeric(
    df["Geopolitical_Risk_Score"], errors="coerce"
)

df = df.dropna(subset=["Disruption_Occurred"])
df = df[df["Disruption_Occurred"].isin([0, 1])].copy()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

transport_options = sorted(df["Transport_Mode"].dropna().unique())
weather_options = sorted(df["Weather_Condition"].dropna().unique())

selected_transport = st.sidebar.multiselect(
    "Transport Mode",
    transport_options,
    default=transport_options
)

selected_weather = st.sidebar.multiselect(
    "Weather Condition",
    weather_options,
    default=weather_options
)

filtered = df[
    df["Transport_Mode"].isin(selected_transport)
    & df["Weather_Condition"].isin(selected_weather)
].copy()

if filtered.empty:
    st.warning("No shipments match the selected filters.")
    st.stop()

# KPI calculations
total_shipments = len(filtered)
disrupted_shipments = int(filtered["Disruption_Occurred"].sum())
disruption_rate = disrupted_shipments / total_shipments * 100

st.markdown("### 📊 Key Performance Indicators")

c1, c2, c3 = st.columns(3)
c1.metric("Total Shipments", f"{total_shipments:,}")
c2.metric("Disrupted Shipments", f"{disrupted_shipments:,}")
c3.metric("Disruption Rate", f"{disruption_rate:.2f}%")

st.divider()

# Transport risk
st.markdown("### 🚚 Disruption Rate by Transport Mode")

transport = (
    filtered.groupby("Transport_Mode")["Disruption_Occurred"]
    .mean().mul(100).reset_index(name="Disruption Rate (%)")
    .sort_values("Disruption Rate (%)", ascending=False)
)

fig_transport = px.bar(
    transport,
    x="Disruption Rate (%)",
    y="Transport_Mode",
    orientation="h",
    text_auto=".2f",
    title="Transport Mode Risk"
)
st.plotly_chart(fig_transport, use_container_width=True)

# Weather risk
st.markdown("### 🌦️ Disruption Rate by Weather Condition")

weather = (
    filtered.groupby("Weather_Condition")["Disruption_Occurred"]
    .mean().mul(100).reset_index(name="Disruption Rate (%)")
    .sort_values("Disruption Rate (%)", ascending=False)
)

fig_weather = px.bar(
    weather,
    x="Disruption Rate (%)",
    y="Weather_Condition",
    orientation="h",
    text_auto=".2f",
    title="Weather Condition Risk"
)
st.plotly_chart(fig_weather, use_container_width=True)

# Product risk
st.markdown("### 📦 Disruption Rate by Product Category")

product = (
    filtered.groupby("Product_Category")["Disruption_Occurred"]
    .mean().mul(100).reset_index(name="Disruption Rate (%)")
    .sort_values("Disruption Rate (%)", ascending=False)
)

fig_product = px.bar(
    product,
    x="Disruption Rate (%)",
    y="Product_Category",
    orientation="h",
    text_auto=".2f",
    title="Product Category Risk"
)
st.plotly_chart(fig_product, use_container_width=True)

# Geopolitical risk
st.markdown("### 🌍 Disruption Rate by Geopolitical Risk")

filtered["Risk Band"] = pd.cut(
    filtered["Geopolitical_Risk_Score"],
    bins=[-1, 3, 7, 10],
    labels=["Low (≤3)", "Medium (>3–7)", "High (>7)"]
)

risk = (
    filtered.groupby("Risk Band", observed=False)["Disruption_Occurred"]
    .mean().mul(100).reset_index(name="Disruption Rate (%)")
)

fig_risk = px.bar(
    risk,
    x="Disruption Rate (%)",
    y="Risk Band",
    orientation="h",
    text_auto=".2f",
    title="Geopolitical Risk Bands"
)
st.plotly_chart(fig_risk, use_container_width=True)

# Monthly trend
if date_column in filtered.columns:
    monthly_data = filtered.dropna(subset=[date_column]).copy()

    if not monthly_data.empty:
        monthly_data["Month"] = monthly_data[date_column].dt.to_period("M").astype(str)

        monthly = (
            monthly_data.groupby("Month")["Disruption_Occurred"]
            .mean().mul(100).reset_index(name="Disruption Rate (%)")
        )

        st.markdown("### 📈 Monthly Shipment Disruption Trend")

        fig_monthly = px.line(
            monthly,
            x="Month",
            y="Disruption Rate (%)",
            markers=True,
            title="Monthly Disruption Rate"
        )
        st.plotly_chart(fig_monthly, use_container_width=True)

# Data preview
with st.expander("View shipment data"):
    st.dataframe(filtered, use_container_width=True)

st.caption("LaneGuard AI | Supply Chain Risk Analytics Portfolio Project")
