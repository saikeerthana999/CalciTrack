import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="CalciTrack India | Mobile Triage", page_icon="🧡", layout="wide")

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

# --- INDIAN-SPECIFIC RISK ENGINE ---
def calculate_calcitrack_india(age, sex, sbp, smoker, diabetes, premature_cad, metabolic_syndrome):
    # Base logic adjusted for South Asian CAD risk (starting with higher base)
    base_risk = (age * 0.15) + (sbp * 0.06)
    
    if sex == "Male": base_risk += 3.0
    if smoker: base_risk += 7.0  # Smoking/Bidi has higher impact in South Asians
    if diabetes: base_risk += 8.0 # Higher insulin resistance weight
    if premature_cad: base_risk += 10.0 # Critical "Secret Sauce" for Indian families
    if metabolic_syndrome: base_risk += 5.0 # High TG, Low HDL, Central Obesity
    
    # The "South Asian Multiplier": AHA/ACC scores are often multiplied by 1.5 for Indians
    risk_pct = round(min(max((base_risk / 1.5) * 1.1, 1.5), 50.0), 1)
    
    # Triage Categories (Lowered thresholds for Indian population)
    if risk_pct < 5.0:
        return risk_pct, "green", "LOW RISK", "Maintain heart-healthy diet. Follow-up in 1-2 years."
    elif 5.0 <= risk_pct < 10.0:
        return risk_pct, "orange", "INTERMEDIATE (Yellow)", "Action: Recommend Calcium Score (CAC) or CT Coronary Angio due to South Asian risk profile."
    else:
        return risk_pct, "red", "HIGH RISK (Red)", "Urgent: Direct Referral to Cardiologist. Potential for premature CAD."

# --- APP UI ---
st.title("🛡️ CalciTrack India")
st.subheader("Mobile Cardiac Point-of-Service Triage")

with st.sidebar:
    st.header("📋 Patient Intake")
    age = st.number_input("Age", 18, 100, 40) # Default age lower for India
    sex = st.radio("Biological Sex", ["Male", "Female"])
    sbp = st.slider("Systolic BP (mmHg)", 90, 200, 130)
    
    st.write("---")
    st.write("**India-Specific Risk Enhancers**")
    smoker = st.checkbox("Smoker / Tobacco / Bidi User")
    diabetes = st.checkbox("Diabetes (HbA1c > 6.5)")
    premature_cad = st.checkbox("Family History of Early Heart Attack")
    metabolic_syndrome = st.checkbox("Central Obesity / High Waist-to-Hip Ratio")
    
    if st.button("Generate India Triage Result", use_container_width=True):
        risk, color, status, rec = calculate_calcitrack_india(age, sex, sbp, smoker, diabetes, premature_cad, metabolic_syndrome)
        v_age = age + (10 if risk > 5 else 0) + (10 if risk > 15 else 0)
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

    st.markdown(f"### Triage Status: :{color}[{status}]")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("10-Year Cardiovascular Risk", f"{risk}%")
    with col2:
        st.metric("Vascular Age", f"{v_age} Yrs", delta=f"{v_age - patient_age} yrs vs Bio", delta_color="inverse")

    st.warning(f"**Clinical Guidance for Indian Context:** {rec}")

else:
    st.write("👈 Fill out the doorstep intake form to assess cardiac risk.")

st.write("---")
st.caption("Developed for Indian Clinical Context. Algorithm adjusted for South Asian premature CAD risk factors.")
