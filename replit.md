# CalciTrack - Mobile Cardiac Triage System

## Overview
CalciTrack is a mobile point-of-service cardiac screening application built with Streamlit. It calculates 10-year cardiovascular disease risk using a simplified MESA/ASCVD-based algorithm and provides triage recommendations.

## Features
- Patient intake form with demographic and clinical data
- Risk calculation based on age, sex, ethnicity, blood pressure, and risk enhancers
- Color-coded triage status (Green/Yellow/Red)
- Vascular age calculation
- Interactive map showing nearby cardiology partners for referrals
- Clinical guidance recommendations

## Project Structure
- `app.py` - Main Streamlit application
- `.streamlit/config.toml` - Streamlit server configuration

## Running the Application
The app runs via Streamlit on port 5000:
```
streamlit run app.py --server.port 5000
```

## Risk Categories
- **LOW RISK (Green)**: < 5.0% - Routine follow-up
- **INTERMEDIATE (Yellow)**: 5.0% - 7.5% - Recommend CAC Scan
- **HIGH RISK (Red)**: > 7.5% - Urgent cardiology referral

## Dependencies
- streamlit
- pandas
- folium
- streamlit-folium

## Technical Notes
- Uses st.session_state to persist calculation results across Streamlit reruns
- Map centered on NYC coordinates (40.7128, -74.0060) by default
- Disclaimer: Educational/prototype tool, not for clinical use
