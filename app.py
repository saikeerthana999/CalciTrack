import streamlit as st
import urllib.parse
import pandas as pd
import math
import io
from datetime import datetime, timedelta
from fpdf import FPDF
from translations import TRANSLATIONS

def safe_text(text):
    return text.encode('latin-1', 'replace').decode('latin-1')

def create_pdf_report(patient_name, examiner_name, exam_date, age, sex, risk, current_v_age, potential_v_age, status, note, motivation, rec):
    patient_name = safe_text(str(patient_name))
    examiner_name = safe_text(str(examiner_name))
    exam_date = safe_text(str(exam_date))
    status = safe_text(str(status))
    note = safe_text(str(note))
    motivation = safe_text(str(motivation))
    rec = safe_text(str(rec))
    sex = safe_text(str(sex))
    
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 18)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(200, 10, txt="CalciTrack: Advanced Vascular Report", ln=True, align='C')
    pdf.set_font("Arial", 'I', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 8, txt='Redefining Early Cardiovascular Risk Detection', ln=True, align='C')
    pdf.ln(5)
    
    pdf.set_font("Arial", '', 11)
    pdf.cell(200, 7, txt=f"Date of Examination: {exam_date}", ln=True)
    pdf.cell(200, 7, txt=f"Patient Name: {patient_name}", ln=True)
    pdf.cell(200, 7, txt=f"Patient Profile: {age} year old {sex}", ln=True)
    pdf.cell(200, 7, txt=f"Primary Motivation: {motivation}", ln=True)
    pdf.ln(5)
    
    pdf.set_fill_color(230, 230, 250)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(190, 10, txt="VASCULAR AGE ANALYSIS", ln=True, fill=True, align='C')
    
    pdf.set_font("Arial", '', 11)
    pdf.cell(95, 10, txt=f"Current Vascular Age: {current_v_age} years", border=1)
    pdf.cell(95, 10, txt=f"Target Vascular Age: {potential_v_age} years", border=1, ln=True)
    
    years_gained = max(0, current_v_age - potential_v_age)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(0, 128, 0)
    if years_gained > 0:
        pdf.cell(200, 15, txt=f"Potential Benefit: Gain back {years_gained} years of Heart Health!", ln=True, align='C')
    else:
        pdf.cell(200, 15, txt="Optimal: Your vascular health is at its best potential!", ln=True, align='C')
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"10-Year Cardiovascular Risk: {risk}%", ln=True)
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Precision Medicine Markers:", ln=True)
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 7, txt="This report integrates Lp(a) and hs-CRP inflammatory markers to provide a precision-based risk reclassification beyond standard age-based metrics.")
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Clinical Impression:", ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 7, txt=note)
    pdf.ln(3)
    
    pdf.set_fill_color(255, 255, 204)
    pdf.set_font("Arial", 'B', 13)
    pdf.cell(190, 10, txt=f"CLINICAL TRIAGE: {status}", ln=True, fill=True, align='C')
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 7, txt=f"Recommendation: {rec}")
    pdf.ln(5)
    
    pdf.set_font("Arial", '', 11)
    pdf.cell(200, 8, txt=f"Examined by: {examiner_name}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(200, 10, txt="Screen Early, Live Fully.", ln=True, align='C')
    
    return pdf.output(dest='S').encode('latin-1')

def render_gauge(risk_pct, size=250, zone_labels=None):
    if zone_labels is None:
        zone_labels = {"low": "LOW", "mid": "INTERMEDIATE", "high": "HIGH"}
    angle = min(risk_pct / 50.0 * 180, 180)
    if risk_pct < 5:
        color = "#4caf50"
        zone = zone_labels["low"]
    elif risk_pct < 20:
        color = "#ff9800"
        zone = zone_labels["mid"]
    else:
        color = "#f44336"
        zone = zone_labels["high"]
    
    needle_angle = 180 - angle
    needle_rad = math.radians(needle_angle)
    cx, cy = 125, 140
    needle_len = 80
    nx = cx + needle_len * math.cos(needle_rad)
    ny = cy - needle_len * math.sin(needle_rad)
    
    svg = f"""
    <svg width="{size}" height="{int(size*0.7)}" viewBox="0 0 250 175">
        <defs>
            <linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#4caf50"/>
                <stop offset="40%" style="stop-color:#ff9800"/>
                <stop offset="100%" style="stop-color:#f44336"/>
            </linearGradient>
        </defs>
        <path d="M 25 140 A 100 100 0 0 1 225 140" fill="none" stroke="#e0e0e0" stroke-width="20" stroke-linecap="round"/>
        <path d="M 25 140 A 100 100 0 0 1 225 140" fill="none" stroke="url(#gaugeGrad)" stroke-width="18" stroke-linecap="round"/>
        <line x1="{cx}" y1="{cy}" x2="{nx}" y2="{ny}" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="6" fill="{color}"/>
        <text x="{cx}" y="{cy + 25}" text-anchor="middle" font-size="22" font-weight="bold" fill="{color}">{risk_pct}%</text>
        <text x="{cx}" y="{cy + 42}" text-anchor="middle" font-size="12" fill="#666">{zone} RISK</text>
        <text x="25" y="160" font-size="9" fill="#999">0%</text>
        <text x="210" y="160" font-size="9" fill="#999">50%</text>
    </svg>
    """
    return svg

st.set_page_config(page_title="CalciTrack", page_icon="🧡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

if 'patient_log' not in st.session_state:
    st.session_state['patient_log'] = []
if 'current_result' not in st.session_state:
    st.session_state['current_result'] = None

def calculate_risk(age, sex, ethnicity, sbp, smoker, diabetes, gender_enhancers, general_enhancers):
    score = (age * 0.15) + (sbp * 0.06)
    if sex == "Male": score += 2.0
    if ethnicity == "South Asian / Indian": score += 2.0
    elif ethnicity == "African / African American": score += 1.5
    if smoker: score += 7.0
    if diabetes: score += 8.0
    
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

def get_followup_date(status):
    today = datetime.now()
    if "HIGH" in status:
        return (today + timedelta(days=120)).strftime("%B %d, %Y"), "3-6 months"
    elif status == "INTERMEDIATE":
        return (today + timedelta(days=365)).strftime("%B %d, %Y"), "1 year"
    else:
        return (today + timedelta(days=1095)).strftime("%B %d, %Y"), "3-5 years"

def get_bmi_category_sa(bmi):
    if bmi < 18.5:
        return "Underweight", "#2196f3"
    elif bmi < 23:
        return "Normal", "#4caf50"
    elif bmi < 25:
        return "Overweight (SA threshold)", "#ff9800"
    else:
        return "Obese (SA threshold)", "#f44336"

st.image("attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png", width=200)
st.markdown("""
    <div style="text-align: center; margin: 5px 0 15px 0;">
        <span style="font-size: 1.6em; font-weight: bold; font-style: italic; background: linear-gradient(90deg, #ff4b4b, #f5a623); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Redefining Early Cardiovascular Risk Detection</span>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 20px; border-radius: 12px; margin: 10px 0; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h2 style="color: #ffffff; margin: 0; font-size: 1.5em; font-weight: 600; letter-spacing: 0.5px;">Doorstep Cardiac Screening & Specialist Referral</h2>
        <p style="color: #f5a623; margin: 10px 0 0 0; font-size: 1.1em; font-weight: 500;">Invented by Sai Keerthana Cherukuri, 4th Year Medical Student</p>
        <p style="color: #a8d8f0; margin: 10px 0 0 0; font-size: 0.95em; font-style: italic; letter-spacing: 0.3px;">&#10077; My Philosophy: Detect Early. Stratify Precisely. Prevent Effectively. &#10078;</p>
    </div>
""", unsafe_allow_html=True)

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

with st.sidebar:
    lang = st.selectbox("🌐 Language", list(TRANSLATIONS.keys()))
    t = TRANSLATIONS[lang]
    
    st.header(f"🧪 {t['demo_mode']}")
    selected_demo = st.selectbox(t['select_demo'], list(demo_cases.keys()))
    demo_data = demo_cases[selected_demo]
    
    st.divider()
    
    st.header(f"❤️ {t['personal_profile']}")
    motivation = st.selectbox(t['motivation_label'], t['motivation_opts'])
    diet = st.radio(t['diet_label'], t['diet_opts'])
    sleep_apnea = st.checkbox(t['sleep_apnea'])
    
    st.markdown("---")
    st.subheader(f"🔄 {t['impact_sim']}")
    st.caption(t['impact_caption'])
    target_sbp = st.slider(t['goal_bp'], 110, 160, 120)
    quit_smoking_goal = st.checkbox(t['goal_nonsmoker'], value=True)
    manage_diabetes_goal = st.checkbox(t['goal_diabetes'], value=True)

with st.expander(f"📖 {t['how_to_use']}", expanded=False):
    st.markdown("""
### Welcome to CalciTrack!
CalciTrack is a mobile cardiac screening and triage tool designed for the South Asian/Indian population. Follow these simple steps to complete a full cardiovascular risk assessment.

---

### Step 1: Screening (Doorstep Triage)
1. **Select a Demo Patient** (optional) — Use the sidebar dropdown to auto-fill a sample profile.
2. **Fill in Patient Details** — Name, age, sex, ethnicity, systolic BP.
3. **Check Risk Enhancers** — Mark applicable conditions (pregnancy history for females, family CAD, CKD, etc.).
4. **Enter Precision Markers** (optional) — Lp(a) and hs-CRP values for precision grading.
5. **Click "Generate Result"** — View risk %, vascular age, clinical note, certificate, PDF & WhatsApp share.

### Step 2: What-If Analysis
- See **current vs. optimized vascular age** and how many years you could gain back.

### Step 3: Impact Simulator
- Set **sidebar health goals** (BP, smoking, diabetes) and see before/after risk comparison.

### Step 4: Clinician Dashboard
- Track all screened patients, view analytics charts, and export session data as CSV.

### Step 5: Education & Diet Guide
- Patient education cards explaining Lp(a), hs-CRP, vascular age, CAC scoring, and ASCVD.
- South Asian heart-healthy diet guide with smart food swaps and the Indian Heart Plate.

### Step 6: BMI Calculator
- South Asian-specific BMI thresholds (obesity at 23/25 vs. standard 25/30).
- Waist circumference risk assessment.

### Sidebar Quick Reference
| Section | What It Does |
|---|---|
| **Language** | Switch between English, Hindi, Telugu, Tamil |
| **Demo Mode** | Load a pre-built patient profile for testing |
| **Personal Profile** | Set motivation, diet, and sleep apnea flag |
| **Impact Simulator** | Set health goal sliders/checkboxes for Step 3 |

---

*Invented by Sai Keerthana Cherukuri, 4th Year Medical Student*
    """)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    f"🏥 {t['step1']}", f"🔮 {t['step2']}", f"🎯 {t['step3']}", 
    f"📊 {t['step4']}", f"📚 {t['step5']}", f"🧮 {t['step6']}"
])

with tab1:
    with st.container():
        col_a, col_b = st.columns([1, 2])
        
        with col_a:
            st.subheader(f"📋 {t['intake']}")
            patient_name = st.text_input(t['patient_name'], placeholder=t['patient_name'])
            examiner_name = st.text_input(t['examiner_name'], placeholder=t['examiner_name'])
            
            age = st.number_input(t['patient_age'], 18, 100, value=demo_data['age'] if demo_data else 45)
            sex = st.radio(t['bio_sex'], [t['male'], t['female']], index=0 if (not demo_data or demo_data['sex'] == "Male") else 1)
            sex_eng = "Male" if sex == t['male'] else "Female"
            ethnicity = st.selectbox(t['ethnicity'], ["South Asian / Indian", "Caucasian / White", "African / African American", "East Asian", "Hispanic / Latino", "Other"])
            sbp = st.slider(t['sbp_label'], 90, 200, value=demo_data['sbp'] if demo_data else 130)
            
            gender_enhancers = {}
            if sex_eng == "Female":
                st.info(t['pregnancy_history'])
                gender_enhancers['preeclampsia'] = st.checkbox(t['preeclampsia'], value=demo_data.get('pre_e', False) if demo_data else False)
                gender_enhancers['gdm'] = st.checkbox(t['gdm'], value=demo_data.get('gdm', False) if demo_data else False)
                gender_enhancers['early_menopause'] = st.checkbox(t['early_menopause'], value=demo_data.get('early_m', False) if demo_data else False)
                gender_enhancers['pcos'] = st.checkbox(t['pcos'], value=demo_data.get('pcos', False) if demo_data else False)

            st.write("---")
            st.write(f"**{t['risk_enhancers']}**")
            general_enhancers = {
                'premature_cad': st.checkbox(t['family_cad'], value=demo_data.get('f_hx', False) if demo_data else False),
                'ckd': st.checkbox(t['ckd'], value=demo_data.get('ckd', False) if demo_data else False),
                'lp_a': st.checkbox(t['elevated_lpa']),
                'hs_crp': st.checkbox(t['elevated_hscrp']),
                'metabolic_syndrome': st.checkbox(t['metabolic_syn'])
            }
            smoker = st.checkbox(t['tobacco'], value=demo_data.get('smoker', False) if demo_data else False)
            diabetes = st.checkbox(t['diabetes'], value=demo_data.get('diabetes', False) if demo_data else False)
            
            st.write("---")
            st.markdown(f"##### 🔬 {t['precision_markers']}")
            col_lpa, col_hscrp = st.columns(2)
            with col_lpa:
                lpa_value = st.number_input(t['lpa_input'], 0, 300, value=0, help="Genetic marker - values >50 may upgrade risk")
            with col_hscrp:
                hscrp_value = st.number_input(t['hscrp_input'], 0.0, 20.0, value=0.0, step=0.1, help="Inflammation marker - values >2.0 may upgrade risk")

            submit = st.button(t['generate'], use_container_width=True)

        with col_b:
            if submit:
                risk, color, status, rec = calculate_risk(age, sex_eng, ethnicity, sbp, smoker, diabetes, gender_enhancers, general_enhancers)
                v_age = age + (10 if risk > 7 else 0)
                
                upgraded = False
                if status == "INTERMEDIATE" and (lpa_value > 50 or hscrp_value > 2.0):
                    status = "HIGH (UPGRADED)"
                    color = "red"
                    rec = "High-intensity statin therapy and aggressive LDL-C lowering recommended. Direct referral for Specialist Consultation and possible Functional Stress Testing."
                    upgraded = True
                
                st.markdown(f"### {t['result']}: :{color}[{status} {t['risk_label']}]")
                
                gauge_svg = render_gauge(risk, zone_labels={"low": t['gauge_low'], "mid": t['gauge_mid'], "high": t['gauge_high']})
                st.markdown(f'<div style="text-align: center;">{gauge_svg}</div>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(t['ascvd_risk'], f"{risk}%")
                with col2:
                    st.metric(t['vascular_age'], f"{v_age} Yrs", delta=f"{v_age - age} yrs vs Bio")
                
                active_gender = [k.replace('_', ' ').title() for k, v in gender_enhancers.items() if v]
                active_general = [k.replace('_', ' ').title() for k, v in general_enhancers.items() if v]
                all_enhancers = active_gender + active_general
                exam_date = datetime.now().strftime("%B %d, %Y")
                
                display_patient_name = patient_name if patient_name else "Not provided"
                display_examiner_name = examiner_name if examiner_name else "Not provided"
                
                note = f"Patient: {display_patient_name} ({age}y {sex_eng}, {ethnicity}) - 10-Year Risk: {risk}%. Triage: {status} RISK."
                if all_enhancers:
                    note += f" Risk Enhancers: {', '.join(all_enhancers)}."
                if upgraded:
                    note += f" CRITICAL: Risk upgraded due to high Genetic/Inflammatory markers (Lp(a): {lpa_value} mg/dL, hs-CRP: {hscrp_value} mg/L)."
                
                st.subheader(f"📝 {t['clinical_impression']}")
                st.code(note, language=None)
                
                st.subheader(f"💊 {t['recommendation']}")
                st.info(rec)
                
                followup_date, followup_interval = get_followup_date(status)
                if "HIGH" in status:
                    followup_text = t['followup_high']
                elif status == "INTERMEDIATE":
                    followup_text = t['followup_intermediate']
                else:
                    followup_text = t['followup_low']
                
                st.markdown(f"""
                    <div style="background: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #1976d2; margin: 10px 0;">
                        <strong>📅 {t['followup_header']}:</strong> {followup_text}<br>
                        <strong>{t['next_screening']}:</strong> {followup_date}
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.subheader(f"📋 {t['guidelines_header']}")
                st.markdown("""
| Guideline | Reference | Key Point |
|---|---|---|
| **AHA/ACC 2019** | Arnett DK, et al. Circulation. 2019 | Pooled Cohort Equations for ASCVD risk; statin benefit groups |
| **CSI Consensus 2020** | Cardiological Society of India | South Asian-specific risk adjustment (+2.0 ethnicity factor) |
| **AHA Life's Essential 8** | Lloyd-Jones DM, et al. Circulation. 2022 | 8-metric framework for cardiovascular health optimization |
| **CAC Scoring (Agatston)** | Hecht HS, et al. JACC. 2017 | CAC >0 in intermediate risk favors statin initiation |
| **Lp(a) Consensus** | Wilson DP, et al. J Clin Lipidol. 2022 | Lp(a) >50 mg/dL = risk enhancer; consider for reclassification |
| **hs-CRP & Inflammation** | Ridker PM, et al. NEJM. 2017 | hs-CRP >=2.0 mg/L upgrades intermediate to high risk |
| **South Asian BMI Thresholds** | WHO Expert Consultation. Lancet. 2004 | Obesity at BMI >=23 (vs. >=25 for Western populations) |
| **Waist Circumference** | IDF Consensus 2006 | South Asian: Men >90cm, Women >80cm = central obesity |
                """)
                
                current_v_age = calculate_vascular_age(age, sex_eng, sbp, smoker, diabetes)
                potential_v_age = calculate_vascular_age(age, sex_eng, 120, False, False)
                
                st.session_state['current_result'] = {
                    'patient_name': display_patient_name,
                    'examiner_name': display_examiner_name,
                    'exam_date': exam_date,
                    'age': age,
                    'sex': sex_eng,
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
                    'hscrp_value': hscrp_value,
                    'followup_date': followup_date,
                    'followup_interval': followup_interval
                }
                
                st.success(f"✅ {t['result_success']}")
                
                st.write(f"### 🎯 {t['your_goal']} **{motivation}**")
                if sleep_apnea:
                    st.warning(f"⚠️ {t['sleep_warning']}")
                
                st.session_state['patient_log'].append({
                    "Date": exam_date,
                    "Patient": display_patient_name,
                    "Age": age, 
                    "Sex": sex_eng, 
                    "Risk %": risk, 
                    "Status": status,
                    "Examiner": display_examiner_name,
                    "Follow-Up": followup_date
                })
                
                wa_msg = urllib.parse.quote(f"*CalciTrack Referral*\n\n{note}")
                wa_url = f"https://wa.me/?text={wa_msg}"
                
                st.markdown(f"""
                    <a href="{wa_url}" target="_blank">
                        <button style="background-color:#25D366; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; font-weight:bold;">
                            📲 {t['share_whatsapp']}
                        </button>
                    </a>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                    <div style="border: 5px solid #ff4b4b; padding: 20px; border-radius: 10px; text-align: center; background-color: white; margin-top: 20px;">
                        <h2 style="color: #ff4b4b;">CalciTrack</h2>
                        <h4 style="font-style: italic;">Redefining Early Cardiovascular Risk Detection</h4>
                        <hr>
                        <h3>{heart_summary}</h3>
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
                """.format(v_age=v_age, status=status, note=note, exam_date=exam_date, patient_name=display_patient_name, examiner_name=display_examiner_name, rec=rec, heart_summary=t['heart_summary']), unsafe_allow_html=True)
                
                pdf_data = create_pdf_report(display_patient_name, display_examiner_name, exam_date, age, sex_eng, risk, current_v_age, potential_v_age, status, note, motivation, rec)
                st.download_button(
                    label=f"📄 {t['download_pdf']}",
                    data=pdf_data,
                    file_name=f"CalciTrack_{display_patient_name}_{exam_date}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

with tab2:
    st.header(f"🔮 {t['what_if_header']}")
    
    if st.session_state['current_result']:
        r = st.session_state['current_result']
        
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                <h2 style="color: white; margin: 0; text-align: center;">{t['what_if_question']}</h2>
                <p style="color: #e0e0e0; text-align: center; margin-top: 10px;">{t['what_if_desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        years_to_save = max(0, r['current_v_age'] - r['potential_v_age'])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
                <div style="background: #fff3e0; padding: 20px; border-radius: 10px; text-align: center; min-height: 150px;">
                    <h4 style="color: #e65100; margin: 0;">{label}</h4>
                    <h1 style="color: #e65100; margin: 10px 0; font-size: 3em;">{val}</h1>
                    <p style="color: #666;">{sub}</p>
                </div>
            """.format(label=t['current_state'], val=r['current_v_age'], sub=t['vascular_age_years']), unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div style="background: #e8f5e9; padding: 20px; border-radius: 10px; text-align: center; min-height: 150px;">
                    <h4 style="color: #2e7d32; margin: 0;">{label}</h4>
                    <h1 style="color: #2e7d32; margin: 10px 0; font-size: 3em;">{val}</h1>
                    <p style="color: #666;">{sub}</p>
                </div>
            """.format(label=t['optimized_state'], val=r['potential_v_age'], sub=t['target_vascular_age']), unsafe_allow_html=True)
        with col3:
            if years_to_save > 0:
                st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 20px; border-radius: 10px; text-align: center; min-height: 150px;">
                        <h4 style="color: white; margin: 0;">{t['your_potential']}</h4>
                        <h1 style="color: white; margin: 10px 0; font-size: 3em;">+{years_to_save}</h1>
                        <p style="color: #e0ffe0;">{t['years_gain']}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 20px; border-radius: 10px; text-align: center; min-height: 150px;">
                        <h4 style="color: white; margin: 0;">{t['optimal_status']}</h4>
                        <h1 style="color: white; margin: 10px 0; font-size: 2em;">{t['optimal_status']}</h1>
                        <p style="color: #e0ffe0;">{t['keep_up']}</p>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.subheader(f"💡 {t['essential8_header']}")
        st.caption(t['essential8_desc'])
        
        e8_items = [
            (t['e8_diet'], "🥗"), (t['e8_activity'], "🏃"), (t['e8_nicotine'], "🚭"), (t['e8_sleep'], "😴"),
            (t['e8_weight'], "⚖️"), (t['e8_cholesterol'], "🩸"), (t['e8_glucose'], "🍬"), (t['e8_bp'], "💓")
        ]
        
        e8_scores = []
        cols = st.columns(4)
        for i, (item, icon) in enumerate(e8_items):
            with cols[i % 4]:
                score = st.slider(f"{icon} {item}", 0, 100, 50, key=f"e8_{i}")
                e8_scores.append(score)
        
        avg_score = round(sum(e8_scores) / len(e8_scores))
        if avg_score >= 80:
            e8_color = "#4caf50"
            e8_label = t['e8_excellent']
        elif avg_score >= 60:
            e8_color = "#ff9800"
            e8_label = t['e8_moderate']
        else:
            e8_color = "#f44336"
            e8_label = t['e8_needs_improvement']
        
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, {e8_color}33, {e8_color}11); padding: 20px; border-radius: 12px; border-left: 6px solid {e8_color}; margin: 15px 0; text-align: center;">
                <h2 style="color: {e8_color}; margin: 0;">{t['e8_score']}: {avg_score}/100</h2>
                <p style="color: #666; font-size: 1.1em; margin-top: 5px;">{e8_label}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader(f"{t['how_optimize']}")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.info(f"🩺 **{t['target_bp_tip']}**")
        with col_b:
            st.info(f"🚭 **{t['quit_tobacco_tip']}**")
        with col_c:
            st.info(f"💊 **{t['manage_dm_tip']}**")
    else:
        st.warning(f"⚠️ {t['complete_step1']}")

with tab3:
    st.header(f"🎯 {t['impact_header']}")
    
    if st.session_state['current_result']:
        r = st.session_state['current_result']
        
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 25px; border-radius: 15px; margin-bottom: 20px;">
                <h2 style="color: white; margin: 0; text-align: center;">{t['set_goals']}</h2>
                <p style="color: #e0ffe0; text-align: center; margin-top: 10px;">{t['adjust_sidebar']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        target_smoker = not quit_smoking_goal
        target_diabetes = not manage_diabetes_goal if r['diabetes'] else False
        simulated_risk, _, simulated_status, simulated_rec = calculate_risk(
            r['age'], r['sex'], r['ethnicity'], target_sbp, 
            target_smoker, target_diabetes, r['gender_enhancers'], r['general_enhancers']
        )
        
        st.subheader(t['current_goals'])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(t['target_bp_label'], f"{target_sbp} mmHg", delta=f"{target_sbp - r['sbp']} {t['from_current']}")
        with col2:
            st.metric(t['smoking_goal'], t['nonsmoker'] if quit_smoking_goal else t['smoker'])
        with col3:
            st.metric(t['diabetes_goal'], t['controlled'] if manage_diabetes_goal else t['uncontrolled'])
        
        st.markdown("---")
        
        col_before, col_arrow, col_after = st.columns([2, 1, 2])
        with col_before:
            gauge_current = render_gauge(r['risk'], zone_labels={"low": t['gauge_low'], "mid": t['gauge_mid'], "high": t['gauge_high']})
            st.markdown(f"""
                <div style="background: #ffebee; padding: 20px; border-radius: 15px; text-align: center;">
                    <h3 style="color: #c62828; margin: 0;">{t['current_risk']}</h3>
                    {gauge_current}
                    <p style="color: #666;">{t['ten_year_cvd']}</p>
                </div>
            """, unsafe_allow_html=True)
        with col_arrow:
            st.markdown("""
                <div style="display: flex; align-items: center; justify-content: center; height: 250px;">
                    <h1 style="color: #4caf50; font-size: 4em;">→</h1>
                </div>
            """, unsafe_allow_html=True)
        with col_after:
            gauge_sim = render_gauge(simulated_risk, zone_labels={"low": t['gauge_low'], "mid": t['gauge_mid'], "high": t['gauge_high']})
            st.markdown(f"""
                <div style="background: #e8f5e9; padding: 20px; border-radius: 15px; text-align: center;">
                    <h3 style="color: #2e7d32; margin: 0;">{t['with_goals']}</h3>
                    {gauge_sim}
                    <p style="color: #666;">{t['projected_risk']}</p>
                </div>
            """, unsafe_allow_html=True)
        
        risk_reduction = round(r['risk'] - simulated_risk, 1)
        if risk_reduction > 0:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin-top: 20px; text-align: center;">
                    <h2 style="color: white; margin: 0;">🎉 {t['risk_reduce_msg']} {risk_reduction}%!</h2>
                    <p style="color: #e0e0e0; margin-top: 10px;">{t['significant_improvement']}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info(t['already_optimal'])
    else:
        st.warning(f"⚠️ {t['complete_step1']}")

with tab4:
    st.header(f"📈 {t['dashboard_header']}")
    
    if st.session_state['patient_log']:
        df = pd.DataFrame(st.session_state['patient_log'])
        st.dataframe(df, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(t['total_screened'], len(df))
        with col2:
            high_risk_count = len(df[df['Status'].str.contains('HIGH', na=False)])
            st.metric(t['high_risk_patients'], high_risk_count)
        with col3:
            intermediate_count = len(df[df['Status'] == 'INTERMEDIATE'])
            st.metric(t['intermediate_risk'], intermediate_count)
        
        st.markdown("---")
        
        chart_col1, chart_col2, chart_col3 = st.columns(3)
        
        with chart_col1:
            st.subheader(t['risk_distribution'])
            risk_counts = df['Status'].value_counts()
            st.bar_chart(risk_counts)
        
        with chart_col2:
            st.subheader(t['age_distribution'])
            age_bins = pd.cut(df['Age'], bins=[0, 30, 40, 50, 60, 100], labels=['<30', '30-40', '40-50', '50-60', '60+'])
            age_counts = age_bins.value_counts().sort_index()
            st.bar_chart(age_counts)
        
        with chart_col3:
            st.subheader(t['gender_breakdown'])
            gender_counts = df['Sex'].value_counts()
            st.bar_chart(gender_counts)
        
        st.markdown("---")
        
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"📥 {t['download_csv']}",
            data=csv_data,
            file_name=f"CalciTrack_Session_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        if st.button(t['clear_session']):
            st.session_state['patient_log'] = []
            st.rerun()
    else:
        st.write(t['no_patients'])

with tab5:
    st.header(f"📚 {t['education_header']}")
    
    edu_tab1, edu_tab2 = st.tabs([f"🎓 {t['edu_what_is']}", f"🥗 {t['diet_header']}"])
    
    with edu_tab1:
        edu_cards = [
            (t['edu_lpa_title'], t['edu_lpa'], "🧬", "#e3f2fd"),
            (t['edu_hscrp_title'], t['edu_hscrp'], "🔥", "#fce4ec"),
            (t['edu_vascular_title'], t['edu_vascular'], "🫀", "#f3e5f5"),
            (t['edu_cac_title'], t['edu_cac'], "🦴", "#e8f5e9"),
            (t['edu_ascvd_title'], t['edu_ascvd'], "📊", "#fff3e0"),
        ]
        
        for title, content, icon, bg_color in edu_cards:
            with st.expander(f"{icon} {title}", expanded=False):
                st.markdown(f"""
                    <div style="background: {bg_color}; padding: 20px; border-radius: 10px;">
                        <p style="font-size: 1.05em; line-height: 1.7; color: #333;">{content}</p>
                    </div>
                """, unsafe_allow_html=True)
    
    with edu_tab2:
        st.subheader(f"🔄 {t['diet_swap_title']}")
        swaps = [
            t['diet_swap_ghee'], t['diet_swap_salt'], t['diet_swap_rice'],
            t['diet_swap_maida'], t['diet_swap_sugar'], t['diet_swap_snack']
        ]
        for swap in swaps:
            parts = swap.split(" -> ")
            if len(parts) == 2:
                st.markdown(f"""
                    <div style="display: flex; align-items: center; padding: 10px; margin: 5px 0; background: #f5f5f5; border-radius: 8px;">
                        <span style="background: #ffcdd2; padding: 5px 12px; border-radius: 5px; font-weight: bold; color: #c62828;">❌ {parts[0]}</span>
                        <span style="margin: 0 15px; font-size: 1.3em;">→</span>
                        <span style="background: #c8e6c9; padding: 5px 12px; border-radius: 5px; font-weight: bold; color: #2e7d32;">✅ {parts[1]}</span>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.subheader(f"🥩 {t['diet_protein_title']}")
        st.success(t['diet_protein_veg'])
        st.info(t['diet_protein_nonveg'])
        
        st.markdown("---")
        
        st.subheader(f"🍽️ {t['diet_plate_title']}")
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e8f5e9, #c8e6c9); padding: 25px; border-radius: 15px; text-align: center; margin: 10px 0;">
                <h3 style="color: #2e7d32; margin: 0 0 10px 0;">🍽️ {t['diet_plate_title']}</h3>
                <p style="font-size: 1.1em; color: #333; line-height: 1.6;">{t['diet_plate']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.subheader(f"🌿 {t['diet_spice_title']}")
        st.markdown(f"""
            <div style="background: #fff8e1; padding: 20px; border-radius: 10px; border-left: 5px solid #f9a825;">
                <p style="font-size: 1.05em; line-height: 1.8; color: #333;">{t['diet_spices']}</p>
            </div>
        """, unsafe_allow_html=True)

with tab6:
    st.header(f"🧮 {t['bmi_header']}")
    
    bmi_col1, bmi_col2 = st.columns(2)
    
    with bmi_col1:
        weight = st.number_input(t['bmi_weight'], 20.0, 200.0, 70.0, step=0.5)
        height = st.number_input(t['bmi_height'], 100.0, 220.0, 165.0, step=0.5)
        waist = st.number_input(t['bmi_waist'], 50.0, 180.0, 80.0, step=0.5)
        bmi_sex = st.radio(t['bio_sex'], [t['male'], t['female']], key="bmi_sex")
        bmi_sex_eng = "Male" if bmi_sex == t['male'] else "Female"
        
        calc_bmi = st.button(t['bmi_calculate'], use_container_width=True)
    
    with bmi_col2:
        if calc_bmi:
            bmi = round(weight / ((height / 100) ** 2), 1)
            category, cat_color = get_bmi_category_sa(bmi)
            
            st.markdown(f"""
                <div style="background: {cat_color}22; padding: 30px; border-radius: 15px; text-align: center; border: 3px solid {cat_color};">
                    <h3 style="color: #333; margin: 0;">{t['bmi_result']}</h3>
                    <h1 style="color: {cat_color}; font-size: 4em; margin: 10px 0;">{bmi}</h1>
                    <p style="color: {cat_color}; font-size: 1.3em; font-weight: bold;">{category}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            st.subheader(f"📏 {t['bmi_sa_note']}")
            st.info(t['bmi_sa_explain'])
            
            st.markdown("""
| Category | Standard WHO | South Asian Threshold |
|---|---|---|
| Normal | < 25.0 | **< 23.0** |
| Overweight | 25.0 - 29.9 | **23.0 - 24.9** |
| Obese | >= 30.0 | **>= 25.0** |
            """)
            
            st.markdown("---")
            
            st.subheader(f"📐 {t['bmi_waist_risk']}")
            
            if bmi_sex_eng == "Male":
                waist_threshold = 90
                waist_msg = t['bmi_waist_male_high']
            else:
                waist_threshold = 80
                waist_msg = t['bmi_waist_female_high']
            
            if waist > waist_threshold:
                st.error(f"⚠️ {waist_msg} — {t['your_waist']}: **{waist} cm** ({t['waist_high_risk']})")
            else:
                st.success(f"✅ {t['waist_safe']} ({waist} cm)")
            
            st.markdown(f"""
| | Standard Threshold | South Asian Threshold |
|---|---|---|
| **{t['male']}** | > 102 cm | **> 90 cm** |
| **{t['female']}** | > 88 cm | **> 80 cm** |
            """)

st.write("---")
st.caption("Developed for Clinical Context. Algorithm adjusted for population-specific cardiovascular risk factors.")
