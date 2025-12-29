import streamlit as st
import urllib.parse
import pandas as pd
from datetime import datetime
from fpdf import FPDF

def create_pdf_report(patient_name, examiner_name, exam_date, age, sex, risk, current_v_age, potential_v_age, status, note, motivation, rec):
    pdf = FPDF()
    pdf.add_page()
    
    # Professional Header
    pdf.set_font("Arial", 'B', 18)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(200, 10, txt="CalciTrack: Advanced Vascular Report", ln=True, align='C')
    pdf.set_font("Arial", 'I', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 8, txt='"Care Ever, Neglect Never"', ln=True, align='C')
    pdf.ln(5)
    
    # Patient Info
    pdf.set_font("Arial", '', 11)
    pdf.cell(200, 7, txt=f"Date of Examination: {exam_date}", ln=True)
    pdf.cell(200, 7, txt=f"Patient Name: {patient_name}", ln=True)
    pdf.cell(200, 7, txt=f"Patient Profile: {age} year old {sex}", ln=True)
    pdf.cell(200, 7, txt=f"Primary Motivation: {motivation}", ln=True)
    pdf.ln(5)
    
    # The "What-If" Comparative Table
    pdf.set_fill_color(230, 230, 250)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(190, 10, txt="VASCULAR AGE ANALYSIS", ln=True, fill=True, align='C')
    
    pdf.set_font("Arial", '', 11)
    pdf.cell(95, 10, txt=f"Current Vascular Age: {current_v_age} years", border=1)
    pdf.cell(95, 10, txt=f"Target Vascular Age: {potential_v_age} years", border=1, ln=True)
    
    # High-Impact Highlight
    years_gained = max(0, current_v_age - potential_v_age)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(0, 128, 0)
    if years_gained > 0:
        pdf.cell(200, 15, txt=f"Potential Benefit: Gain back {years_gained} years of Heart Health!", ln=True, align='C')
    else:
        pdf.cell(200, 15, txt="Optimal: Your vascular health is at its best potential!", ln=True, align='C')
    
    # Risk Summary
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"10-Year Cardiovascular Risk: {risk}%", ln=True)
    pdf.ln(3)
    
    # Advanced Biomarkers Section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Precision Medicine Markers:", ln=True)
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 7, txt="This report integrates Lp(a) and hs-CRP inflammatory markers to provide a precision-based risk reclassification beyond standard age-based metrics.")
    pdf.ln(3)
    
    # Clinical Impression
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Clinical Impression:", ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 7, txt=note)
    pdf.ln(3)
    
    # Actionable Triage Box
    pdf.set_fill_color(255, 255, 204)
    pdf.set_font("Arial", 'B', 13)
    pdf.cell(190, 10, txt=f"CLINICAL TRIAGE: {status}", ln=True, fill=True, align='C')
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 7, txt=f"Recommendation: {rec}")
    pdf.ln(5)
    
    # Footer
    pdf.set_font("Arial", '', 11)
    pdf.cell(200, 8, txt=f"Examined by: {examiner_name}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(200, 0, 0)
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
if 'current_result' not in st.session_state:
    st.session_state['current_result'] = None

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

# --- VASCULAR AGE ENGINE ---
def calculate_vascular_age(age, sex, sbp, smoker, diabetes):
    v_age = age
    if sbp > 120:
        v_age += (sbp - 120) * 0.1
    if smoker:
        v_age += 8
    if diabetes:
        v_age += 6
    if sex == "Male":
        v_age += 2
    return round(v_age)

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

# --- MOCK DATASET ENGINE ---
demo_cases = {
    "None (Manual Entry)": None,
    "1. Young Male Smoker (ED)": {"age": 42, "sex": "Male", "sbp": 135, "smoker": True, "diabetes": False, "ed": True, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "2. Female Post-Preeclampsia (GDM)": {"age": 48, "sex": "Female", "sbp": 128, "smoker": False, "diabetes": True, "pre_e": True, "gdm": True, "pcos": False, "early_m": False, "ckd": False},
    "3. Young Genetic Risk (South Asian)": {"age": 35, "sex": "Male", "sbp": 145, "smoker": False, "diabetes": False, "ed": False, "f_hx": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "4. High Risk Elderly (CKD)": {"age": 62, "sex": "Female", "sbp": 155, "smoker": False, "diabetes": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": True},
    "5. The Metabolic Trio (Smoker/DM)": {"age": 50, "sex": "Male", "sbp": 130, "smoker": True, "diabetes": True, "ed": False, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "6. Low Risk Young Female": {"age": 38, "sex": "Female", "sbp": 115, "smoker": False, "diabetes": False, "pre_e": False, "gdm": False, "pcos": True, "early_m": False, "ckd": False},
    "7. Early Menopause Risk": {"age": 52, "sex": "Female", "sbp": 140, "smoker": False, "diabetes": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": True, "ckd": False},
    "8. Middle-Aged HTN (Male)": {"age": 45, "sex": "Male", "sbp": 160, "smoker": False, "diabetes": False, "ed": False, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "9. Female Smoker (Borderline)": {"age": 44, "sex": "Female", "sbp": 120, "smoker": True, "diabetes": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "10. Premature Family History (Male)": {"age": 29, "sex": "Male", "sbp": 125, "smoker": False, "diabetes": False, "ed": False, "f_hx": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "11. Diabetic Male (ED Link)": {"age": 55, "sex": "Male", "sbp": 138, "smoker": False, "diabetes": True, "ed": True, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "12. Geriatric High Risk": {"age": 68, "sex": "Female", "sbp": 145, "smoker": False, "diabetes": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": True},
    "13. Baseline Healthy Male": {"age": 33, "sex": "Male", "sbp": 118, "smoker": False, "diabetes": False, "ed": False, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "14. Silent Obstetric Risk": {"age": 41, "sex": "Female", "sbp": 132, "smoker": False, "diabetes": False, "pre_e": True, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "15. Strong Genetic Load (HTN/DM)": {"age": 47, "sex": "Male", "sbp": 150, "smoker": False, "diabetes": True, "ed": False, "f_hx": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "16. Post-PCOS Metabolic Shift": {"age": 58, "sex": "Female", "sbp": 135, "smoker": False, "diabetes": False, "pre_e": False, "gdm": False, "pcos": True, "early_m": False, "ckd": False},
    "17. Asymptomatic Male Smoker": {"age": 52, "sex": "Male", "sbp": 125, "smoker": True, "diabetes": False, "ed": False, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "18. Young DM (Maternal Hx)": {"age": 34, "sex": "Female", "sbp": 110, "smoker": False, "diabetes": True, "pre_e": False, "gdm": True, "pcos": False, "early_m": False, "ckd": False},
    "19. Age-Borderline (Candidate for CAC)": {"age": 60, "sex": "Male", "sbp": 142, "smoker": False, "diabetes": False, "ed": False, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "20. Subtle Vascular Warning (ED)": {"age": 43, "sex": "Male", "sbp": 128, "smoker": False, "diabetes": False, "ed": True, "f_hx": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "21. Critical Poly-Risk": {"age": 65, "sex": "Female", "sbp": 165, "smoker": True, "diabetes": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": True},
    "22. Early HTN Management": {"age": 38, "sex": "Male", "sbp": 148, "smoker": False, "diabetes": False, "ed": False, "f_hx": False, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "23. Accelerated Female Aging": {"age": 46, "sex": "Female", "sbp": 124, "smoker": False, "diabetes": False, "pre_e": True, "gdm": False, "pcos": False, "early_m": True, "ckd": False},
    "24. High-Load Genetic Triage": {"age": 54, "sex": "Male", "sbp": 136, "smoker": False, "diabetes": True, "ed": False, "f_hx": True, "pre_e": False, "gdm": False, "pcos": False, "early_m": False, "ckd": False},
    "25. PCOS Monitoring Case": {"age": 31, "sex": "Female", "sbp": 115, "smoker": False, "diabetes": False, "pre_e": False, "gdm": False, "pcos": True, "early_m": False, "ckd": False}
}

# --- SIDEBAR ---
with st.sidebar:
    st.header("🧪 Demo Mode")
    selected_demo = st.selectbox("Select a Mock Patient Profile", list(demo_cases.keys()))
    demo_data = demo_cases[selected_demo]
    
    st.divider()
    
    st.header("❤️ Personal Profile")
    motivation = st.selectbox("I want to stay healthy for...", ["My Family", "My Children's Future", "My Work", "Religious Pilgrimage"])
    diet = st.radio("Dietary Habit", ["Pure Veg", "Non-Veg", "Eggetarian"])
    sleep_apnea = st.checkbox("Heavy Snoring / Daytime Sleepiness")
    
    st.markdown("---")
    st.subheader("🔄 Impact Simulator")
    st.caption("Set your health goals to see potential risk reduction")
    target_sbp = st.slider("Goal Systolic BP", 110, 160, 120)
    quit_smoking_goal = st.checkbox("Goal: Non-Smoker", value=True)
    manage_diabetes_goal = st.checkbox("Goal: Diabetes Controlled", value=True)

tab1, tab2, tab3, tab4 = st.tabs(["🏥 Step 1: Screening", "🔮 Step 2: What-If Analysis", "🎯 Step 3: Impact Simulator", "📊 Step 4: Clinician Dashboard"])

with tab1:
    with st.container():
        col_a, col_b = st.columns([1, 2])
        
        with col_a:
            st.subheader("📋 Intake")
            patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
            examiner_name = st.text_input("Examiner / Doctor Name", placeholder="Enter examiner name")
            
            # Use demo data if selected
            age = st.number_input("Patient Age", 18, 100, value=demo_data['age'] if demo_data else 45)
            sex = st.radio("Biological Sex", ["Male", "Female"], index=0 if (not demo_data or demo_data['sex'] == "Male") else 1)
            ethnicity = st.selectbox("Ethnicity", ["South Asian / Indian", "Caucasian / White", "African / African American", "East Asian", "Hispanic / Latino", "Other"])
            sbp = st.slider("Systolic BP (mmHg)", 90, 200, value=demo_data['sbp'] if demo_data else 130)
            
            # --- CONDITIONAL LOGIC BASED ON GENDER ---
            gender_enhancers = {}
            if sex == "Female":
                st.info("Pregnancy & Hormonal History")
                gender_enhancers['preeclampsia'] = st.checkbox("History of Preeclampsia", value=demo_data.get('pre_e', False) if demo_data else False)
                gender_enhancers['gdm'] = st.checkbox("Gestational Diabetes", value=demo_data.get('gdm', False) if demo_data else False)
                gender_enhancers['early_menopause'] = st.checkbox("Menopause < 40 yrs", value=demo_data.get('early_m', False) if demo_data else False)
                gender_enhancers['pcos'] = st.checkbox("PCOS Diagnosis", value=demo_data.get('pcos', False) if demo_data else False)

            st.write("---")
            st.write("**High-Yield Risk Enhancers**")
            general_enhancers = {
                'premature_cad': st.checkbox("Family History of Early Coronary Artery Disease", value=demo_data.get('f_hx', False) if demo_data else False),
                'ckd': st.checkbox("Chronic Kidney Disease", value=demo_data.get('ckd', False) if demo_data else False),
                'lp_a': st.checkbox("Elevated Lp(a) (>50 mg/dL)"),
                'hs_crp': st.checkbox("hs-CRP ≥ 2.0 mg/L"),
                'metabolic_syndrome': st.checkbox("Central Obesity / Metabolic Syndrome")
            }
            smoker = st.checkbox("Tobacco / Smoker", value=demo_data.get('smoker', False) if demo_data else False)
            diabetes = st.checkbox("Diabetes", value=demo_data.get('diabetes', False) if demo_data else False)
            
            # --- ADVANCED CLINICAL MODULE ---
            st.write("---")
            st.markdown("##### 🔬 Advanced Precision Markers")
            col_lpa, col_hscrp = st.columns(2)
            with col_lpa:
                lpa_value = st.number_input("Lp(a) (mg/dL)", 0, 300, value=0, help="Genetic marker - values >50 may upgrade risk")
            with col_hscrp:
                hscrp_value = st.number_input("hs-CRP (mg/L)", 0.0, 20.0, value=0.0, step=0.1, help="Inflammation marker - values >2.0 may upgrade risk")

            submit = st.button("Generate Result", use_container_width=True)

        with col_b:
            if submit:
                risk, color, status, rec = calculate_risk(age, sex, ethnicity, sbp, smoker, diabetes, gender_enhancers, general_enhancers)
                v_age = age + (10 if risk > 7 else 0)
                
                # Risk Upgrade based on Precision Markers
                upgraded = False
                if status == "INTERMEDIATE" and (lpa_value > 50 or hscrp_value > 2.0):
                    status = "HIGH (UPGRADED)"
                    color = "red"
                    rec = "High-intensity statin therapy and aggressive LDL-C lowering recommended. Direct referral for Specialist Consultation and possible Functional Stress Testing."
                    upgraded = True
                
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
                if upgraded:
                    note += f" CRITICAL: Risk upgraded due to high Genetic/Inflammatory markers (Lp(a): {lpa_value} mg/dL, hs-CRP: {hscrp_value} mg/L)."
                
                st.subheader("📝 Clinical Impression")
                st.code(note, language=None)
                
                # Recommendation
                st.subheader("💊 Recommendation")
                st.info(rec)
                
                # Store results for other tabs
                current_v_age = calculate_vascular_age(age, sex, sbp, smoker, diabetes)
                potential_v_age = calculate_vascular_age(age, sex, 120, False, False)
                
                st.session_state['current_result'] = {
                    'patient_name': display_patient_name,
                    'examiner_name': display_examiner_name,
                    'exam_date': exam_date,
                    'age': age,
                    'sex': sex,
                    'ethnicity': ethnicity,
                    'sbp': sbp,
                    'smoker': smoker,
                    'diabetes': diabetes,
                    'risk': risk,
                    'status': status,
                    'color': color,
                    'rec': rec,
                    'note': note,
                    'v_age': v_age,
                    'current_v_age': current_v_age,
                    'potential_v_age': potential_v_age,
                    'gender_enhancers': gender_enhancers,
                    'general_enhancers': general_enhancers,
                    'motivation': motivation,
                    'upgraded': upgraded,
                    'lpa_value': lpa_value,
                    'hscrp_value': hscrp_value
                }
                
                st.success("✅ Result generated! Navigate to **Step 2** for What-If Analysis and **Step 3** for Impact Simulator.")
                
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
                pdf_data = create_pdf_report(display_patient_name, display_examiner_name, exam_date, age, sex, risk, current_v_age, potential_v_age, status, note, motivation, rec)
                st.download_button(
                    label="📄 Download Patient Summary PDF",
                    data=pdf_data,
                    file_name=f"CalciTrack_{display_patient_name}_{exam_date}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

with tab2:
    st.header("🔮 What-If Analysis: Your Heart's Potential")
    
    if st.session_state['current_result']:
        r = st.session_state['current_result']
        
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                <h2 style="color: white; margin: 0; text-align: center;">What if you optimized your lifestyle?</h2>
                <p style="color: #e0e0e0; text-align: center; margin-top: 10px;">See how lifestyle changes could transform your vascular health</p>
            </div>
        """, unsafe_allow_html=True)
        
        years_to_save = max(0, r['current_v_age'] - r['potential_v_age'])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
                <div style="background: #fff3e0; padding: 20px; border-radius: 10px; text-align: center; height: 150px;">
                    <h4 style="color: #e65100; margin: 0;">Current State</h4>
                    <h1 style="color: #e65100; margin: 10px 0; font-size: 3em;">{}</h1>
                    <p style="color: #666;">Vascular Age (Years)</p>
                </div>
            """.format(r['current_v_age']), unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div style="background: #e8f5e9; padding: 20px; border-radius: 10px; text-align: center; height: 150px;">
                    <h4 style="color: #2e7d32; margin: 0;">Optimized State</h4>
                    <h1 style="color: #2e7d32; margin: 10px 0; font-size: 3em;">{}</h1>
                    <p style="color: #666;">Target Vascular Age</p>
                </div>
            """.format(r['potential_v_age']), unsafe_allow_html=True)
        with col3:
            if years_to_save > 0:
                st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 20px; border-radius: 10px; text-align: center; height: 150px;">
                        <h4 style="color: white; margin: 0;">Your Potential</h4>
                        <h1 style="color: white; margin: 10px 0; font-size: 3em;">+{years_to_save}</h1>
                        <p style="color: #e0ffe0;">Years to Gain Back!</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 20px; border-radius: 10px; text-align: center; height: 150px;">
                        <h4 style="color: white; margin: 0;">Your Status</h4>
                        <h1 style="color: white; margin: 10px 0; font-size: 2em;">Optimal!</h1>
                        <p style="color: #e0ffe0;">Keep it up!</p>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("How to Optimize:")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.info("🩺 **Target BP: 120 mmHg**\nMeditation, low sodium, medication")
        with col_b:
            st.info("🚭 **Quit Tobacco**\nNicotine patches, counseling")
        with col_c:
            st.info("💊 **Manage Diabetes**\nDiet, exercise, medication adherence")
    else:
        st.warning("⚠️ Please complete **Step 1: Screening** first to see your What-If Analysis.")

with tab3:
    st.header("🎯 Impact Simulator: Your Goal Tracker")
    
    if st.session_state['current_result']:
        r = st.session_state['current_result']
        
        st.markdown("""
            <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                <h2 style="color: white; margin: 0; text-align: center;">Set Your Health Goals</h2>
                <p style="color: #e0ffe0; text-align: center; margin-top: 10px;">Adjust the sidebar sliders to see how achievable targets reduce your risk</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Calculate simulated risk based on sidebar goals
        target_smoker = not quit_smoking_goal
        target_diabetes = not manage_diabetes_goal if r['diabetes'] else False
        simulated_risk, _, simulated_status, simulated_rec = calculate_risk(
            r['age'], r['sex'], r['ethnicity'], target_sbp, 
            target_smoker, target_diabetes, r['gender_enhancers'], r['general_enhancers']
        )
        
        st.subheader("Your Current Goals (from sidebar):")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Target BP", f"{target_sbp} mmHg", delta=f"{target_sbp - r['sbp']} from current")
        with col2:
            st.metric("Smoking Goal", "Non-Smoker" if quit_smoking_goal else "Smoker")
        with col3:
            st.metric("Diabetes Goal", "Controlled" if manage_diabetes_goal else "Uncontrolled")
        
        st.markdown("---")
        
        col_before, col_arrow, col_after = st.columns([2, 1, 2])
        with col_before:
            st.markdown(f"""
                <div style="background: #ffebee; padding: 30px; border-radius: 15px; text-align: center;">
                    <h3 style="color: #c62828; margin: 0;">Current Risk</h3>
                    <h1 style="color: #c62828; font-size: 4em; margin: 10px 0;">{r['risk']}%</h1>
                    <p style="color: #666;">10-Year CVD Risk</p>
                </div>
            """, unsafe_allow_html=True)
        with col_arrow:
            st.markdown("""
                <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
                    <h1 style="color: #4caf50; font-size: 4em;">→</h1>
                </div>
            """, unsafe_allow_html=True)
        with col_after:
            st.markdown(f"""
                <div style="background: #e8f5e9; padding: 30px; border-radius: 15px; text-align: center;">
                    <h3 style="color: #2e7d32; margin: 0;">With Your Goals</h3>
                    <h1 style="color: #2e7d32; font-size: 4em; margin: 10px 0;">{simulated_risk}%</h1>
                    <p style="color: #666;">Projected Risk</p>
                </div>
            """, unsafe_allow_html=True)
        
        risk_reduction = round(r['risk'] - simulated_risk, 1)
        if risk_reduction > 0:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin-top: 20px; text-align: center;">
                    <h2 style="color: white; margin: 0;">🎉 You could reduce your risk by {risk_reduction}%!</h2>
                    <p style="color: #e0e0e0; margin-top: 10px;">That's a significant improvement in your heart health outlook.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Your current health metrics are already optimized based on these goals!")
    else:
        st.warning("⚠️ Please complete **Step 1: Screening** first to use the Impact Simulator.")

with tab4:
    st.header("📈 Mobile Clinic Session Summary")
    
    if st.session_state['patient_log']:
        df = pd.DataFrame(st.session_state['patient_log'])
        st.dataframe(df, use_container_width=True)
        
        # Summary Analytics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Screened", len(df))
        with col2:
            high_risk_count = len(df[df['Status'].str.contains('HIGH', na=False)])
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
