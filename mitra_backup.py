import streamlit as st
import random
from datetime import datetime

st.set_page_config
# --- MOBILE FIX - ADDED ---
st.markdown("""
<style>
.block-container {padding: 0.8rem !important; max-width: 100% !important;}
h1 {font-size: 24px !important;}
[data-testid="stMetric"] {background: #F8F9FA; padding: 10px; border-radius: 12px;}
iframe {width: 100% !important;}
@media (max-width: 600px) {
  h1 {font-size: 20px !important;}
  [data-testid="stMetricValue"] {font-size: 20px !important;}
}
</style>
""", unsafe_allow_html=True)

# --- MOBILE FRIENDLY CSS ---
st.markdown("""
<style>
    .block-container {padding-top: 1rem; padding-bottom: 1rem; padding-left: 1rem; padding-right: 1rem; max-width: 100% !important;}
    .stButton>button {width: 100%; border-radius: 12px; height: 48px; background: #0E7C5B; color: white; font-weight: bold; font-size: 16px;}
    .stTextInput>div>div>input, .stSelectbox>div>div {border-radius: 12px; font-size: 16px;}
    h1 {font-size: 28px !important; text-align: center;}
    h3 {font-size: 18px !important;}
    .metric-card {background: #F0F7F4; padding: 15px; border-radius: 15px; text-align: center; border: 1px solid #D6E8E0;}
}
</style>
""", unsafe_allow_html=True)
st.title("🏙️ Amaravati Mitra")
# --- HEADER ---
st.title("🌆 Amaravati Mitra")
st.markdown("<p style='text-align:center; color:gray;'>AI Citizen Assistant | Amaravati Smart City Digital Twin</p>", unsafe_allow_html=True)
st.markdown("**Amaravati Mitra** helps citizens report civic issues in Telugu / English and get instant Department, Phone, Solution Days & Complaint ID. Built for Amaravati Capital Region - Seed Access Road, Thullur, Mangalagiri, Vaddeswaram & more.", unsafe_allow_html=True)

# --- TOP METRICS - GRIEVANCE DASHBOARD ---
st.subheader("📊 Live Grievance Metrics - Today")
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Total Complaints", "1,248", "+42 today")
with c2: st.metric("Resolved", "987", "79%")
with c3: st.metric("In Progress", "211", "17%")
with c4: st.metric("Avg. Response", "2.4 Days", "-0.5 Days")

# --- AQI + WEATHER ROW ---
st.subheader("🌤️ Amaravati Live Environment")
aq1, aq2, aq3 = st.columns(3)
with aq1:
    st.markdown("<div class='aqi-good'>AQI: 68 - Good 😊<br>PM2.5: 18 | PM10: 42</div>", unsafe_allow_html=True)
with aq2:
    st.markdown("<div class='metric-card'>🌡️ Temperature<br><b>32°C - Sunny</b><br>Humidity: 62%</div>", unsafe_allow_html=True)
with aq3:
    st.markdown("<div class='metric-card'>🚦 Traffic - Seed Access Rd<br><b>Moderate</b><br>Peak: 9 AM - 11 AM</div>", unsafe_allow_html=True)

st.divider()

# --- MAIN - 2 COLUMNS FOR MOBILE ---
left, right = st.columns([1, 1])

with left:
    st.subheader("📝 Report Issue")
    zone = st.selectbox("Select Your Zone", ["Seed Access Road", "Thullur", "Mangalagiri", "Vaddeswaram", "Undavalli", "Penamaka", "Velagapudi", "Mandadam"])
    issue = st.text_input("Type your problem (Telugu / English)", placeholder="Ex: Vaddeswaram lo road lo pothole undi / water leakage")
    ask = st.button("Ask Mitra 🚀")

with right:
    st.subheader("💬 Mitra Reply")
    if ask and issue:
        issue_low = issue.lower()
        if "road" in issue_low or "pothole" in issue_low:
            dept, phone, days = "Roads & Buildings Dept", "0863-2340101", "3-5 Days"
        elif "water" in issue_low or "leakage" in issue_low:
            dept, phone, days = "Water Supply Dept", "0863-2340102", "1-2 Days"
        elif "light" in issue_low or "street" in issue_low:
            dept, phone, days = "Electrical Dept", "0863-2340103", "1-2 Days"
        elif "garbage" in issue_low or "chetta" in issue_low:
            dept, phone, days = "Sanitation Dept", "0863-2340104", "1 Day"
        elif "drainage" in issue_low:
            dept, phone, days = "Drainage Dept", "0863-2340105", "2-3 Days"
        else:
            dept, phone, days = "Municipal Corporation", "0863-2340100", "3-5 Days"

        cid = f"AMR{random.randint(1000,9999)}"
        st.success(f"Namaste! Mee complaint **{zone}** lo ardham ayyindi.")
        st.markdown(f"""
        **Zone:** {zone}  
        **Department:** {dept}  
        **Phone:** {phone}  
        **Expected Solution:** {days}  
        **Complaint ID:** {cid}  
        **Status:** In Progress  
        **Reported At:** {datetime.now().strftime('%d %b %Y, %I:%M %p')}
        """)
        wa_text = f"Amaravati Mitra Complaint {cid} - {zone} - {dept} - {phone}"
        st.link_button("📲 Share on WhatsApp", f"https://wa.me/?text={wa_text}")
    elif ask:
        st.warning("Please type your problem first.")
    else:
        st.info("👆 Select Zone, type problem & click Ask Mitra. Example: 'water leakage'")

st.divider()
st.markdown("### 📈 Grievance by Category")
g1, g2, g3, g4, g5 = st.columns(5)
with g1: st.markdown("<div class='metric-card'>🛣️ Road<br><b>342</b></div>", unsafe_allow_html=True)
with g2: st.markdown("<div class='metric-card'>💧 Water<br><b>298</b></div>", unsafe_allow_html=True)
with g3: st.markdown("<div class='metric-card'>💡 Light<br><b>187</b></div>", unsafe_allow_html=True)
with g4: st.markdown("<div class='metric-card'>🗑️ Garbage<br><b>256</b></div>", unsafe_allow_html=True)
with g5: st.markdown("<div class='metric-card'>🚰 Drainage<br><b>165</b></div>", unsafe_allow_html=True)

st.caption("Demo Data | Amaravati Mitra - Built with Python + Streamlit | For Citizen Awareness | AQI data is sample for demo, connect OpenWeather / CPCB API for live data")