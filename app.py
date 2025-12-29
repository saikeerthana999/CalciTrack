import streamlit as st
import urllib.parse
import pandas as pd
from datetime import datetime
from fpdf import FPDF

def create_pdf_report(patient_name, examiner_name, exam_date, age, sex, risk, v_age, status, note, motivation, rec):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(255, 75, 75)
    pdf.cell(200, 10, txt="CalciTrack", ln=True, align='C')
    
    pdf.set_font("Arial", 'I', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt='"Care Ever, Neglect Never"', ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Heart Health Summary", ln=True, align='C')
    pdf.ln(5)
    
    pdf.set_font("Arial", '', 11)
    pdf.cell(200, 8, txt=f"Date of Examination: {exam_date}", ln=True)
    pdf.cell(200, 8, txt=f"Patient Name: {patient_name}", ln=True)
    pdf.cell(200, 8, txt=f"Patient Profile: {age} year old {sex}", ln=True)
    pdf.cell(200, 8, txt=f"Primary Motivation: {motivation}", ln=True)
    pdf.ln(5)
    
    pdf.set_fill_color(240, 240, 240)
    pdf.rect(10, pdf.get_y(), 190, 30, 'F')
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"10-Year Cardiovascular Risk: {risk}%", ln=True)
    pdf.cell(200, 10, txt=f"Estimated Vascular Age: {v_age} Years", ln=True)
    pdf.cell(200, 10, txt=f"Triage Status: {status}", ln=True)
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Clinical Impression:", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 8, txt=note)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Recommendation:", ln=True)
    pdf.set_font("Arial", 'I', 11)
    pdf.multi_cell(0, 8, txt=rec)
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 11)
    pdf.cell(200, 8, txt=f"Examined by: {examiner_name}", ln=True)
    
    pdf.ln(15)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(255, 75, 75)
    pdf.cell(200, 10, txt="Screen Early, Live Fully.", ln=True, align='C')
    
    return pdf.output(dest='S').encode('latin-1')

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
    
    premature_cad = general_enhancers.get('premature_cad', False)
    
    if risk_pct < 5.0 and not premature_cad:
        status = "LOW"
        color = "green"
        rec = "Encourage 'Life's Essential 8' (Healthy diet, Activity, No Tobacco). Re-evaluate in 3-5 years."
    elif 5.0 <= risk_pct < 19.9:
        status = "INTERMEDIATE"
        color = "orange"
        rec = "CSI/AHA Guidelines recommend CAC Scoring (Agatston Method) for RISK RECLASSIFICATION. A score >0 favors initiation of statin therapy."
    else:
        status = "HIGH"
        color = "red"
        rec = "High-intensity statin therapy and aggressive LDL-C lowering recommended. Direct referral for Specialist Consultation and possible Functional Stress Testing."
    
    return risk_pct, color, status, rec

# --- UI LAYOUT ---
st.image("attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png", width=200)
st.markdown("""
    <div style="text-align: center; margin: 5px 0 15px 0;">
        <span style="font-size: 1.8em; font-weight: bold; font-style: italic; background: linear-gradient(90deg, #ff4b4b, #f5a623); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">"Care Ever, Neglect Never"</span>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 20px; border-radius: 12px; margin: 10px 0; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="color: #ffffff; margin: 0; font-size: 1.5em; font-weight: 600; letter-spacing: 0.5px;">Doorstep Cardiac Screening & Specialist Referral</h2>
        <p style="color: #f5a623; margin: 10px 0 0 0; font-size: 1.1em; font-weight: 500;">Invented by Sai Keerthana Cherukuri, 4th Year Medical Student</p>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR: Personal Profile ---
with st.sidebar:
    st.header("❤️ Personal Profile")
    motivation = st.selectbox("I want to stay healthy for...", ["My Family", "My Children's Future", "My Work", "Religious Pilgrimage"])
    diet = st.radio("Dietary Habit", ["Pure Veg", "Non-Veg", "Eggetarian"])
    sleep_apnea = st.checkbox("Heavy Snoring / Daytime Sleepiness")

tab1, tab2 = st.tabs(["🏥 Step 1: Doorstep Triage", "📊 Step 2: Clinician's Dashboard"])

with tab1:
    with st.container():
        col_a, col_b = st.columns([1, 2])
        
        with col_a:
            st.subheader("📋 Intake")
            patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
            examiner_name = st.text_input("Examiner / Doctor Name", placeholder="Enter examiner name")
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
                risk, color, status, rec = calculate_risk(age, sex, ethnicity, sbp, smoker, diabetes, gender_enhancers, general_enhancers)
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
                exam_date = datetime.now().strftime("%B %d, %Y")
                
                display_patient_name = patient_name if patient_name else "Not provided"
                display_examiner_name = examiner_name if examiner_name else "Not provided"
                
                note = f"Patient: {display_patient_name} ({age}y {sex}, {ethnicity}) - 10-Year Risk: {risk}%. Triage: {status} RISK."
                if all_enhancers:
                    note += f" Risk Enhancers: {', '.join(all_enhancers)}."
                
                st.subheader("📝 Clinical Impression")
                st.code(note, language=None)
                
                # Recommendation
                st.subheader("💊 Recommendation")
                st.info(rec)
                
                # Personal Goal Display
                st.write(f"### 🎯 Your Goal: To stay healthy for **{motivation}**")
                if sleep_apnea:
                    st.warning("⚠️ Note: Your snoring may be linked to heart strain. Discuss 'Sleep Apnea' with your doctor.")
                
                # Save to Dashboard
                st.session_state['patient_log'].append({
                    "Date": exam_date,
                    "Patient": display_patient_name,
                    "Age": age, 
                    "Sex": sex, 
                    "Risk %": risk, 
                    "Status": status,
                    "Examiner": display_examiner_name
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
                        <p><strong>Date of Examination:</strong> {exam_date}</p>
                        <p><strong>Patient Name:</strong> {patient_name}</p>
                        <p>This is to certify that a cardiac risk screening was performed.</p>
                        <div style="display: flex; justify-content: space-around; margin: 15px 0;">
                            <div><strong>Vascular Age:</strong> {v_age} Years</div>
                            <div><strong>Triage Status:</strong> {status}</div>
                        </div>
                        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0; text-align: left;">
                            <strong>Clinical Impression:</strong><br>
                            <span style="font-size: 0.95em;">{note}</span>
                        </div>
                        <div style="background-color: #e8f4f8; padding: 15px; border-radius: 8px; margin: 15px 0; text-align: left;">
                            <strong>Recommendation:</strong><br>
                            <span style="font-size: 0.95em; font-style: italic;">{rec}</span>
                        </div>
                        <hr>
                        <p><strong>Examined by:</strong> {examiner_name}</p>
                        <p style="font-weight: bold; color: #ff4b4b;">Screen Early, Live Fully.</p>
                    </div>
                """.format(v_age=v_age, status=status, note=note, exam_date=exam_date, patient_name=display_patient_name, examiner_name=display_examiner_name, rec=rec), unsafe_allow_html=True)
                
                # PDF Download Button
                pdf_data = create_pdf_report(display_patient_name, display_examiner_name, exam_date, age, sex, risk, v_age, status, note, motivation, rec)
                st.download_button(
                    label="📄 Download Patient Summary PDF",
                    data=pdf_data,
                    file_name=f"CalciTrack_{display_patient_name}_{exam_date}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

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
