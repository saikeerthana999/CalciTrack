import streamlit as st
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(page_title="CalciTrack | Clinical Triage", page_icon="🧡", layout="wide")

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

# --- RISK ENGINE WITH ENHANCERS ---
def calculate_calcitrack_risk(age, sex, ethnicity, sbp, smoker, diabetes, enhancers):
    # Base logic adjusted for South Asian CAD risk
    base_risk = (age * 0.15) + (sbp * 0.06)
    
    if sex == "Male": base_risk += 3.0
    if ethnicity == "South Asian / Indian": base_risk += 2.0
    elif ethnicity == "African / African American": base_risk += 1.5
    if smoker: base_risk += 7.0 
    if diabetes: base_risk += 8.0 
    
    # Weighting for Risk Enhancers
    enhancer_points = 0
    if enhancers['premature_cad']: enhancer_points += 10.0
    if enhancers['lp_a']: enhancer_points += 7.0
    if enhancers['hs_crp']: enhancer_points += 4.0
    if enhancers['ckd']: enhancer_points += 5.0
    if enhancers['metabolic_syndrome']: enhancer_points += 5.0
    
    risk_pct = round(min(max(((base_risk + enhancer_points) / 1.5) * 1.1, 1.5), 50.0), 1)
    
    # Triage Categories
    if risk_pct < 5.0 and not enhancers['premature_cad']:
        return risk_pct, "green", "LOW RISK", "Routine follow-up."
    elif 5.0 <= risk_pct < 10.0 or enhancers['premature_cad']:
        return risk_pct, "orange", "INTERMEDIATE (Yellow)", "Action: Recommend Calcium Score (CAC) to clarify risk."
    else:
        return risk_pct, "red", "HIGH RISK (Red)", "Urgent: Direct Cardiology Referral required."

# --- APP UI ---
st.image("attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png", width=200)
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 20px; border-radius: 12px; margin: 10px 0; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="color: #ffffff; margin: 0; font-size: 1.5em; font-weight: 600; letter-spacing: 0.5px;">Doorstep Cardiac Screening & Specialist Referral</h2>
        <p style="color: #f5a623; margin: 10px 0 0 0; font-size: 1.1em; font-weight: 500;">Invented by Sai Keerthana Cherukuri, 4th Year Medical Student</p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("📋 Patient Intake")
    age = st.number_input("Age", 18, 100, 45)
    sex = st.radio("Biological Sex", ["Male", "Female"])
    ethnicity = st.selectbox("Ethnicity", ["South Asian / Indian", "Caucasian / White", "African / African American", "East Asian", "Hispanic / Latino", "Other"])
    sbp = st.slider("Systolic BP (mmHg)", 90, 200, 130)
    
    st.write("---")
    st.write("**High-Yield Risk Enhancers**")
    smoker = st.checkbox("Smoker / Tobacco User")
    diabetes = st.checkbox("Diabetes")
    premature_cad = st.checkbox("Family History of Premature CAD")
    lp_a = st.checkbox("Elevated Lp(a) (>50 mg/dL)")
    hs_crp = st.checkbox("hs-CRP ≥ 2.0 mg/L")
    ckd = st.checkbox("Chronic Kidney Disease (CKD)")
    metabolic_syndrome = st.checkbox("Central Obesity / Metabolic Syndrome")
    
    enhancers = {
        "premature_cad": premature_cad, "lp_a": lp_a, 
        "hs_crp": hs_crp, "ckd": ckd, "metabolic_syndrome": metabolic_syndrome
    }
    
    if st.button("Generate Triage Result", use_container_width=True):
        risk, color, status, rec = calculate_calcitrack_risk(age, sex, ethnicity, sbp, smoker, diabetes, enhancers)
        v_age = age + (12 if risk > 7 else 0)
        
        active_enhancers = [k.replace('_', ' ').title() for k, v in enhancers.items() if v]
        note = f"Patient is a {age}yo {sex} ({ethnicity}) with a calculated 10-year risk of {risk}%. "
        if active_enhancers:
            note += f"Risk is significantly amplified by: {', '.join(active_enhancers)}. "
        note += f"Recommended Action: {rec}"
        
        st.session_state.show_results = True
        st.session_state.risk_data = {
            'risk': risk,
            'color': color,
            'status': status,
            'rec': rec,
            'v_age': v_age,
            'age': age,
            'note': note
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
    note = data['note']

    # 1. Triage Results
    st.markdown(f"### Triage Result: :{color}[{status}]")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("10-Year ASCVD Risk", f"{risk}%")
    with col2:
        st.metric("Vascular Age", f"{v_age} Yrs", delta=f"{v_age - patient_age} yrs vs Bio")

    st.warning(f"**Clinical Guidance:** {rec}")

    # 2. THE CLINICAL NOTE (Automated)
    st.subheader("📝 Clinical Impression")
    st.code(note, language=None)

    # 3. WHATSAPP REFERRAL
    whatsapp_msg = urllib.parse.quote(f"*CalciTrack Referral*\n\n{note}")
    wa_url = f"https://wa.me/?text={whatsapp_msg}"
    
    st.markdown(f"""
        <a href="{wa_url}" target="_blank">
            <button style="background-color:#25D366; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; font-weight:bold;">
                📲 Share Referral via WhatsApp
            </button>
        </a>
    """, unsafe_allow_html=True)

else:
    st.write("👈 Fill out the doorstep intake form to assess cardiac risk.")

st.write("---")
st.caption("Developed for Clinical Context. Algorithm adjusted for population-specific cardiovascular risk factors.")
