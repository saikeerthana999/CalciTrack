import streamlit as st
import urllib.parse
import pandas as pd

# --- APP CONFIG ---
st.set_page_config(page_title="CalciTrack", page_icon="🧡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state to store "Clinician's Dashboard" data
if 'patient_log' not in st.session_state:
    st.session_state['patient_log'] = []

# --- RISK ENGINE ---
def calculate_risk(age, sex, ethnicity, sbp, smoker, diabetes, gender_enhancers, general_enhancers):
    # Base logic adjusted for population-specific CAD risk
    score = (age * 0.15) + (sbp * 0.06)
    if sex == "Male": score += 2.0
    if ethnicity == "South Asian / Indian": score += 2.0
    elif ethnicity == "African / African American": score += 1.5
    if smoker: score += 7.0
    if diabetes: score += 8.0
    
    # Weight Gender-Specific Enhancers
    gender_pts = sum([5.0 for v in gender_enhancers.values() if v])
    general_pts = sum([5.0 for v in general_enhancers.values() if v])
    
    risk_pct = round(min(max(((score + gender_pts + general_pts) / 1.5) * 1.1, 1.2), 50.0), 1)
    
    if risk_pct < 5.0: return risk_pct, "green", "LOW"
    elif 5.0 <= risk_pct < 10.0: return risk_pct, "orange", "INTERMEDIATE"
    else: return risk_pct, "red", "HIGH"

# --- UI LAYOUT ---
st.image("attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png", width=200)
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 20px; border-radius: 12px; margin: 10px 0; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="color: #ffffff; margin: 0; font-size: 1.5em; font-weight: 600; letter-spacing: 0.5px;">Doorstep Cardiac Screening & Specialist Referral</h2>
        <p style="color: #f5a623; margin: 10px 0 0 0; font-size: 1.1em; font-weight: 500;">Invented by Sai Keerthana Cherukuri, 4th Year Medical Student</p>
    </div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🏥 Step 1: Doorstep Triage", "📊 Step 2: Clinician's Dashboard"])

with tab1:
    with st.container():
        col_a, col_b = st.columns([1, 2])
        
        with col_a:
            st.subheader("📋 Intake")
            age = st.number_input("Patient Age", 18, 100, 45)
            sex = st.radio("Biological Sex", ["Male", "Female"])
            ethnicity = st.selectbox("Ethnicity", ["South Asian / Indian", "Caucasian / White", "African / African American", "East Asian", "Hispanic / Latino", "Other"])
            sbp = st.slider("Systolic BP (mmHg)", 90, 200, 130)
            
            # --- CONDITIONAL LOGIC BASED ON GENDER ---
            gender_enhancers = {}
            if sex == "Female":
                st.info("Pregnancy & Hormonal History")
                gender_enhancers['preeclampsia'] = st.checkbox("History of Preeclampsia")
                gender_enhancers['gdm'] = st.checkbox("Gestational Diabetes")
                gender_enhancers['early_menopause'] = st.checkbox("Menopause < 40 yrs")
                gender_enhancers['pcos'] = st.checkbox("PCOS Diagnosis")

            st.write("---")
            st.write("**High-Yield Risk Enhancers**")
            general_enhancers = {
                'premature_cad': st.checkbox("Family History of Early Coronary Artery Disease"),
                'ckd': st.checkbox("Chronic Kidney Disease"),
                'lp_a': st.checkbox("Elevated Lp(a) (>50 mg/dL)"),
                'hs_crp': st.checkbox("hs-CRP ≥ 2.0 mg/L"),
                'metabolic_syndrome': st.checkbox("Central Obesity / Metabolic Syndrome")
            }
            smoker = st.checkbox("Tobacco / Smoker")
            diabetes = st.checkbox("Diabetes")

            submit = st.button("Generate Result", use_container_width=True)

        with col_b:
            if submit:
                risk, color, status = calculate_risk(age, sex, ethnicity, sbp, smoker, diabetes, gender_enhancers, general_enhancers)
                v_age = age + (10 if risk > 7 else 0)
                
                # Visuals
                st.markdown(f"### Result: :{color}[{status} RISK]")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("10-Year ASCVD Risk", f"{risk}%")
                with col2:
                    st.metric("Estimated Vascular Age", f"{v_age} Yrs", delta=f"{v_age - age} yrs vs Bio")
                
                # Clinical Note
                active_gender = [k.replace('_', ' ').title() for k, v in gender_enhancers.items() if v]
                active_general = [k.replace('_', ' ').title() for k, v in general_enhancers.items() if v]
                all_enhancers = active_gender + active_general
                
                note = f"Patient ({age}y {sex}, {ethnicity}) - 10-Year Risk: {risk}%. Triage: {status} RISK."
                if all_enhancers:
                    note += f" Risk Enhancers: {', '.join(all_enhancers)}."
                
                st.subheader("📝 Clinical Impression")
                st.code(note, language=None)
                
                # Save to Dashboard
                st.session_state['patient_log'].append({
                    "Age": age, 
                    "Sex": sex, 
                    "Ethnicity": ethnicity,
                    "Risk %": risk, 
                    "Status": status,
                    "Enhancers": len(all_enhancers)
                })
                
                # WhatsApp Share
                wa_msg = urllib.parse.quote(f"*CalciTrack Referral*\n\n{note}")
                wa_url = f"https://wa.me/?text={wa_msg}"
                
                st.markdown(f"""
                    <a href="{wa_url}" target="_blank">
                        <button style="background-color:#25D366; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; font-weight:bold;">
                            📲 Share Referral via WhatsApp
                        </button>
                    </a>
                """, unsafe_allow_html=True)
                
                # Heart Health Summary Certificate
                st.markdown("""
                    <div style="border: 5px solid #ff4b4b; padding: 20px; border-radius: 10px; text-align: center; background-color: white; margin-top: 20px;">
                        <h2 style="color: #ff4b4b;">CalciTrack</h2>
                        <h4 style="font-style: italic;">"Care Ever, Neglect Never"</h4>
                        <hr>
                        <h3>Heart Health Summary</h3>
                        <p>This is to certify that a cardiac risk screening was performed today.</p>
                        <div style="display: flex; justify-content: space-around;">
                            <div><strong>Vascular Age:</strong> {v_age} Years</div>
                            <div><strong>Triage Status:</strong> {status}</div>
                        </div>
                        <hr>
                        <p style="font-weight: bold; color: #ff4b4b;">Screen Early, Live Fully.</p>
                    </div>
                """.format(v_age=v_age, status=status), unsafe_allow_html=True)

with tab2:
    st.header("📈 Mobile Clinic Session Summary")
    
    if st.session_state['patient_log']:
        df = pd.DataFrame(st.session_state['patient_log'])
        st.dataframe(df, use_container_width=True)
        
        # Summary Analytics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Screened", len(df))
        with col2:
            high_risk_count = len(df[df['Status'] == 'HIGH'])
            st.metric("High Risk Patients", high_risk_count)
        with col3:
            intermediate_count = len(df[df['Status'] == 'INTERMEDIATE'])
            st.metric("Intermediate Risk", intermediate_count)
        
        # Button to Clear
        if st.button("Clear Session Data"):
            st.session_state['patient_log'] = []
            st.rerun()
    else:
        st.write("No patients screened in this session yet.")

st.write("---")
st.caption("Developed for Clinical Context. Algorithm adjusted for population-specific cardiovascular risk factors.")
