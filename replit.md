# CalciTrack - Mobile Cardiac Screening & Triage System

## Overview
CalciTrack is a mobile point-of-service cardiac screening application built with Streamlit, specifically adapted for the South Asian/Indian population. It calculates 10-year cardiovascular disease risk using an algorithm adjusted for South Asian premature CAD risk factors. Invented by Sai Keerthana Cherukuri, 4th Year Medical Student.

## Features
1. **Step 1: Screening** — Patient intake, risk calculation, visual risk gauge, clinical impression, triage recommendation, follow-up scheduler, evidence citations, Heart Health Summary certificate, PDF export, WhatsApp referral sharing
2. **Step 2: What-If Analysis** — Vascular age comparison (current vs optimized), Life's Essential 8 interactive checklist with scoring, lifestyle optimization tips
3. **Step 3: Impact Simulator** — Sidebar goal-setting (BP, smoking, diabetes), before/after risk comparison with visual gauges
4. **Step 4: Clinician Dashboard** — Session patient table, summary metrics, bar charts (risk distribution, age groups, gender breakdown), CSV export
5. **Step 5: Education & Diet Guide** — Patient education cards (Lp(a), hs-CRP, vascular age, CAC, ASCVD), South Asian diet guide with food swaps, Indian Heart Plate, heart-protective spices
6. **Step 6: BMI Calculator** — South Asian-specific BMI thresholds (obesity at 23/25), waist circumference risk assessment

## Multi-Language Support
- English, Hindi, Telugu, Tamil
- Language selector in sidebar
- All UI labels translated via translations.py

## Project Structure
- `app.py` — Main Streamlit application (all 6 steps)
- `translations.py` — Multi-language translation dictionary (English, Hindi, Telugu, Tamil)
- `.streamlit/config.toml` — Streamlit server configuration
- `attached_assets/` — Logo and demo case data

## Running the Application
```
streamlit run app.py --server.port 5000
```

## Risk Categories
- **LOW RISK (Green)**: < 5.0% without premature CAD — Re-evaluate in 3-5 years
- **INTERMEDIATE (Orange)**: 5.0% - 19.9% — CAC Scoring recommended
- **HIGH RISK (Red)**: >= 19.9% — Statin therapy, specialist referral
- **HIGH (UPGRADED)**: Intermediate upgraded by Lp(a) >50 or hs-CRP >2.0

## Risk Enhancers
- Female-specific: Preeclampsia, GDM, Early Menopause, PCOS
- General: Family CAD, CKD, Elevated Lp(a), hs-CRP, Metabolic Syndrome, Smoking, Diabetes

## Dependencies
- streamlit
- pandas
- fpdf
