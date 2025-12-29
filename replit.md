# CalciTrack India - Mobile Cardiac Triage System

## Overview
CalciTrack India is a mobile point-of-service cardiac screening application built with Streamlit, specifically adapted for the South Asian/Indian population. It calculates 10-year cardiovascular disease risk using an algorithm adjusted for South Asian premature CAD risk factors.

## Features
- Patient intake form with India-specific clinical data
- Risk calculation adjusted for South Asian population (higher baseline risk)
- India-specific risk enhancers (tobacco/bidi use, premature CAD family history, metabolic syndrome)
- Color-coded triage status (Green/Yellow/Red)
- Vascular age calculation (typically higher gap for South Asians)
- Clinical guidance recommendations for Indian context

## Project Structure
- `app.py` - Main Streamlit application
- `.streamlit/config.toml` - Streamlit server configuration

## Running the Application
The app runs via Streamlit on port 5000:
```
streamlit run app.py --server.port 5000
```

## Risk Categories (Adjusted for Indian Population)
- **LOW RISK (Green)**: < 5.0% - Heart-healthy diet, follow-up in 1-2 years
- **INTERMEDIATE (Yellow)**: 5.0% - 10.0% - Recommend CAC or CT Coronary Angio
- **HIGH RISK (Red)**: > 10.0% - Urgent cardiology referral for premature CAD

## India-Specific Risk Factors
- Smoker / Tobacco / Bidi User
- Diabetes (HbA1c > 6.5)
- Family History of Early Heart Attack (Premature CAD)
- Central Obesity / High Waist-to-Hip Ratio (Metabolic Syndrome)

## Dependencies
- streamlit
- pandas
- folium
- streamlit-folium

## Technical Notes
- Uses st.session_state to persist calculation results across Streamlit reruns
- Default age set to 40 (vs 50 in Western models) due to earlier CAD onset in South Asians
- South Asian Multiplier applied to risk calculations
- Disclaimer: Educational/prototype tool, not for clinical use
