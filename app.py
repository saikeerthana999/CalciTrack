import streamlit as st
import folium
from streamlit_folium import st_folium

# --- PAGE CONFIG & STYLING ---
st.set_page_config(page_title="CalciTrack | Mobile Cardiac Triage", page_icon="❤️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'risk_data' not in st.session_state:
    st.session_state.risk_data = None

# --- CLINICAL ENGINE (Based on MESA/ASCVD Variables) ---
def calculate_calcitrack_risk(age, sex, ethnicity, sbp, smoker, diabetes, ckd):
    # Simplified clinical coefficients for prototyping
    base_risk = (age * 0.12) + (sbp * 0.04)
    if sex == "Male": base_risk += 2.0
    if ethnicity == "African American": base_risk += 1.5
    if smoker: base_risk += 5.0
    if diabetes: base_risk += 6.5
    if ckd: base_risk += 4.0
    
    # Normalize to 10-year percentage
    risk_pct = round(min(max(base_risk / 1.8, 1.2), 45.0), 1)
    
    # Determine Triage Category
    if risk_pct < 5.0:
        return risk_pct, "green", "LOW RISK", "Routine follow-up. Maintain heart-healthy lifestyle."
    elif 5.0 <= risk_pct < 7.5:
        return risk_pct, "orange", "INTERMEDIATE (Yellow)", "Action: Recommend Coronary Artery Calcium (CAC) Scan to clarify risk."
    else:
        return risk_pct, "red", "HIGH RISK (Red)", "Urgent: Referral to Cardiologist for clinical evaluation and statin therapy discussion."

# --- APP UI ---
st.title("🛡️ CalciTrack")
st.caption("Mobile Point-of-Service Cardiac Screening | v1.0 MVP")

# Sidebar for Intake
with st.sidebar:
    st.header("📋 Patient Intake")
    age = st.number_input("Age", 18, 100, 50)
    sex = st.radio("Biological Sex", ["Male", "Female"])
    ethnicity = st.selectbox("Ethnicity", ["White", "African American", "Hispanic", "Chinese"])
    sbp = st.slider("Systolic BP (mmHg)", 90, 200, 130)
    st.write("---")
    st.write("**Risk Enhancers**")
    smoker = st.checkbox("Current Smoker")
    diabetes = st.checkbox("Diabetes")
    ckd = st.checkbox("Chronic Kidney Disease")
    
    if st.button("Generate Triage Result", use_container_width=True):
        risk, color, status, rec = calculate_calcitrack_risk(age, sex, ethnicity, sbp, smoker, diabetes, ckd)
        v_age = age + (7 if risk > 5 else 0) + (10 if risk > 15 else 0)
        st.session_state.show_results = True
        st.session_state.risk_data = {
            'risk': risk,
            'color': color,
            'status': status,
            'rec': rec,
            'v_age': v_age,
            'age': age
        }

# Main Dashboard Logic
if st.session_state.show_results and st.session_state.risk_data:
    data = st.session_state.risk_data
    risk = data['risk']
    color = data['color']
    status = data['status']
    rec = data['rec']
    v_age = data['v_age']
    patient_age = data['age']

    # 1. Triage Header
    st.markdown(f"### Triage Status: :{color}[{status}]")
    
    # 2. Visual Empathy Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("10-Year CHD Risk", f"{risk}%")
    with col2:
        st.metric("Vascular Age", f"{v_age} Yrs", delta=f"{v_age - patient_age} yrs vs Bio")
    with col3:
        st.metric("Target SBP", "<120 mmHg")

    st.info(f"**Clinical Guidance:** {rec}")

    # 3. Point of Service Map
    if risk >= 5.0:
        st.write("---")
        st.subheader("📍 Doorstep Referral: Nearest Cardiology Partners")
        
        # Center of Map (Mocked for Demo - use Replit Secrets for real GPS)
        lat, lon = 40.7128, -74.0060 
        
        m = folium.Map(location=[lat, lon], zoom_start=13, control_scale=True)
        
        # Add Mobile Clinic (Blue)
        folium.Marker([lat, lon], tooltip="Mobile Clinic Location", icon=folium.Icon(color='blue', icon='truck', prefix='fa')).add_to(m)
        
        # Add Partner Clinics (Red)
        partners = [
            {"name": "Heart & Vascular Institute", "coords": [lat+0.01, lon+0.02]},
            {"name": "Advanced Imaging (CAC Scans)", "coords": [lat-0.015, lon-0.01]}
        ]
        for p in partners:
            folium.Marker(p["coords"], popup=p["name"], icon=folium.Icon(color='red', icon='heart', prefix='fa')).add_to(m)
            
        st_folium(m, width=1000, height=400)
        
        # 4. Digital Packet Export
        st.button("📧 Send Digital Referral Packet to Specialist")

else:
    st.write("👈 Fill out the patient intake form on the left to begin triage.")

# Footer Disclaimer
st.write("---")
st.caption("**Disclaimer:** This tool is for medical student project purposes and uses a simplified MESA-based algorithm. It is not a substitute for professional clinical judgment.")
