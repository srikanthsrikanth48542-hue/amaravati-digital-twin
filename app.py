# app.py - Amaravati Digital Twin Dashboard
import streamlit as st
import pandas as pd
import random
import folium
from streamlit_folium import st_folium

# Import our data from data.py
from data import zones_df, construction_df, land_total, land_returned, grievance_total, grievance_solved, grievance_pending

st.set_page_config(page_title="Amaravati Digital Twin", layout="wide")

st.title("🏛️ Amaravati Digital Twin Dashboard")
if st.button("▶️ Simulate Next Day"):
    st.success("1 Day Passed: Construction increased by 2% | New sensor data generated! Refresh page to see changes.")
    st.balloons()
st.markdown("**AICCC Mini Prototype | Inspired by APCRDA** | Live Status of Amaravati Capital City")

# --- TOP 4 CARDS ---
col1, col2, col3, col4 = st.columns(4)
avg_progress = int(construction_df["Progress %"].mean())

with col1:
    st.metric("Avg Construction Progress", f"{avg_progress}%")
with col2:
    delayed = len(construction_df[construction_df["Status"] == "Delayed"])
    st.metric("Delayed Projects", f"{delayed}")
with col3:
    # Fake live sensor
    air_quality = random.randint(80, 180)
    st.metric("Air Quality (AQI)", air_quality)
with col4:
    st.metric("Grievances Pending", grievance_pending)

st.divider()

# --- LEFT: MAP, RIGHT: CONSTRUCTION CHART ---
left, right = st.columns([2, 1])

with left:
    st.subheader("🗺️ Amaravati City Map - Live Zones")
    # Create map centered on Amaravati
    m = folium.Map(location=[16.52, 80.51], zoom_start=13)
    for index, row in zones_df.iterrows():
        color = "green" if row["Status"] == "On Track" else "red"
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Zone']} - {row['Progress']}% - {row['Status']}",
            tooltip=row["Zone"],
            icon=folium.Icon(color=color)
        ).add_to(m)
    st_folium(m, width=700, height=400)

with right:
    st.subheader("🏗️ Construction Progress")
    st.dataframe(construction_df, use_container_width=True)
    st.bar_chart(construction_df.set_index("Project")["Progress %"])

st.divider()

# --- LIVE SENSORS + ALERTS ---
st.subheader("📡 Live IoT Sensors (Simulated)")

c1, c2, c3, c4 = st.columns(4)
temp = random.randint(28, 38)
traffic = random.randint(40, 98)
humidity = random.randint(45, 75)
water = random.randint(60, 95)

c1.metric("Temperature", f"{temp}°C")
c2.metric("Traffic", f"{traffic}%")
c3.metric("Humidity", f"{humidity}%")
c4.metric("Water Level", f"{water}%")

# Alerts - This is the Twin Brain
if air_quality > 150:
    st.error("🚨 ALERT: High Pollution in Secretariat Zone! AQI is " + str(air_quality))
if traffic > 90:
    st.error("🚨 ALERT: Traffic Jam on Seed Capital Road! Traffic is " + str(traffic) + "%")
if temp > 35:
    st.warning("⚠️ ALERT: High Temperature in Amaravati - " + str(temp) + "°C")
else:
    st.success("✅ All Zones Normal - No Major Alerts")

st.divider()

# --- LAND + GRIEVANCE ---
st.subheader("🌾 Land Pooling & Citizen Grievance")
lc1, lc2 = st.columns(2)
with lc1:
    st.write(f"Total Land Pooled: **{land_total} Acres**")
    st.progress(land_returned / land_total)
    st.write(f"Returned as Developed Plots: **{land_returned} Acres**")
with lc2:
    st.write(f"Total Grievances: **{grievance_total}**")
    st.write(f"Solved: **{grievance_solved}** | Pending: **{grievance_pending}**")
    st.progress(grievance_solved / grievance_total)

st.divider()

# --- GRIEVANCE FORM ---
st.subheader("📝 Raise New Grievance")
name = st.text_input("Your Name")
zone = st.selectbox("Select Zone", zones_df["Zone"].tolist())
issue = st.text_area("Your Issue")
if st.button("Submit Grievance"):
    if name and issue:
        st.success(f"Thank you {name}! Your grievance for {zone} has been recorded.")
    else:
        st.warning("Please fill Name and Issue")

st.markdown("---")
st.caption("Prototype inspired by APCRDA AICCC | Built with Python + Streamlit | Data is simulated for demo")