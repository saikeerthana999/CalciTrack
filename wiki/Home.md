# Welcome to the CalciTrack Wiki

> **Redefining Early Cardiovascular Risk Detection**
> *Doorstep Cardiac Screening & Specialist Referral — Engineered for South Asian Populations*

**Invented by Sai Keerthana Cherukuri · MS4 Clinical Innovation Project**

---

## 📖 Wiki Navigation

| Page | Description |
|---|---|
| **[Home](Home)** | Project overview, philosophy, and quick start |
| **[Clinical Logic & Algorithm](Clinical-Logic)** | Full mathematical and clinical framework |
| **[Evidence Base](Evidence-Base)** | Guideline references and scientific citations |
| **[User Guide](User-Guide)** | Step-by-step guide for clinicians and health workers |
| **[South Asian Cardiovascular Risk](South-Asian-Risk)** | The epidemiological case for a tailored tool |

---

## What is CalciTrack?

CalciTrack is a **clinical decision-support application** for cardiovascular risk screening, triage, and specialist referral — designed specifically for South Asian and Indian populations.

It was built to solve a single, critical problem:

> Standard risk calculators — Framingham, SCORE, ACC/AHA Pooled Cohort — were developed on Western cohorts and **systematically underestimate** coronary artery disease risk in South Asians, who develop heart disease 5–10 years earlier than global averages.

CalciTrack applies a **South Asian–adjusted risk engine**, integrating:
- Population-specific ethnicity modifiers
- Precision biomarkers — Lp(a) and hs-CRP
- Female-specific cardiovascular risk enhancers
- South Asian BMI and waist circumference thresholds

---

## Core Philosophy

> *"Cardiovascular disease does not begin with symptoms. It begins with risk."*

CalciTrack is built on one principle: **risk must be identified, measured, and acted upon before it becomes disease.**

### 🔍 Detect Early
Identify subclinical cardiovascular risk using population-adjusted scoring models and advanced biomarkers — Lp(a) and hs-CRP — before the patient is symptomatic.

### 🎯 Stratify Precisely
Move beyond generalized scoring systems. Reclassify individual patients using South Asian–specific thresholds, precision biomarker upgrade logic, and individualized risk enhancers.

### 🛡️ Prevent Effectively
Translate risk scores into clear, actionable clinical decisions — enabling early statin initiation, specialist referral, and prevention of progression to acute cardiac events.

---

## Key Features

| # | Feature | Details |
|---|---|---|
| 1 | 🧮 South Asian Risk Engine | Re-calibrated algorithm with ethnicity modifier, SA-specific BMI/waist thresholds |
| 2 | 🔬 Precision Marker Upgrade | Lp(a) >50 and hs-CRP ≥2.0 trigger automatic INTERMEDIATE → HIGH reclassification |
| 3 | ♀️ Female-Specific Enhancers | Preeclampsia, GDM, PCOS, Early Menopause as quantified risk factors |
| 4 | 📊 Visual Risk Gauge | SVG speedometer — colour-coded real-time risk visualisation |
| 5 | 🌍 Multi-Language UI | English, Hindi, Telugu, Tamil — for community health workers |
| 6 | 📄 PDF Clinical Reports | Downloadable Heart Health Summary with vascular age and triage |
| 7 | 📲 WhatsApp Referral | Pre-filled specialist referral message from risk result |
| 8 | 📈 Clinician Dashboard | Session-level analytics, risk distribution charts, CSV export |
| 9 | ✅ Life's Essential 8 | AHA interactive health checklist with composite scoring |
| 10 | 🥗 South Asian Diet Guide | Culturally relevant food swaps and Indian Heart Plate model |

---

## Quick Start

```bash
git clone https://github.com/saikeerthana999/CalciTrack.git
cd CalciTrack
pip install streamlit pandas fpdf
streamlit run app.py --server.port 5000
```

---

## The 6-Step Workflow

| Step | Tab | Purpose |
|---|---|---|
| 1 | 🏥 Screening | Patient intake → Risk score → Visual gauge → PDF → WhatsApp referral |
| 2 | 🔮 What-If Analysis | Optimised vascular age comparison + Life's Essential 8 checklist |
| 3 | 🎯 Impact Simulator | Set health goals → See projected risk reduction side-by-side |
| 4 | 📊 Clinician Dashboard | Session analytics, risk distribution charts, CSV export |
| 5 | 📚 Education & Diet | Patient education cards + South Asian diet guide |
| 6 | 🧮 BMI Calculator | South Asian BMI thresholds + waist circumference risk assessment |

---

## South Asian Risk Context

| Parameter | Standard | South Asian (CalciTrack) | Reference |
|---|:---:|:---:|---|
| BMI Overweight | ≥ 25 kg/m² | ≥ 23 kg/m² | WHO Asia-Pacific |
| BMI Obese | ≥ 30 kg/m² | ≥ 25 kg/m² | WHO Asia-Pacific |
| Waist — Men | > 102 cm | > 90 cm | IDF 2006 |
| Waist — Women | > 88 cm | > 80 cm | IDF 2006 |
| Age of CAD onset | Standard avg | **5–10 years earlier** | CSI 2020 |

---

## Risk Stratification Summary

| 10-Year Risk | Category | Clinical Action | Follow-Up |
|---|:---:|---|:---:|
| < 5.0% | 🟢 **LOW** | Life's Essential 8 · Lifestyle counselling | 3–5 years |
| 5.0–19.9% | 🟠 **INTERMEDIATE** | CAC Scoring (Agatston) · Check Lp(a)/hs-CRP | 1 year |
| ≥ 19.9% | 🔴 **HIGH** | High-intensity statin · Specialist referral | 3–6 months |
| INTERMEDIATE + Lp(a)↑ or hs-CRP↑ | 🔴 **UPGRADED** | Aggressive LDL-C · Stress testing | Immediate |

---

## Citation

> Cherukuri, S.K. (2025). *CalciTrack: South Asian–Adjusted Cardiovascular Risk Detection Tool* [Software]. GitHub. https://github.com/saikeerthana999/CalciTrack

---

*Part of the CalciTrack Wiki · See navigation above for detailed clinical documentation*

---

<div align="center">

**CalciTrack** · *Redefining Early Cardiovascular Risk Detection*

Invented by **Sai Keerthana Cherukuri** · MS4 Clinical Innovation Project

*Detect Early · Stratify Precisely · Prevent Effectively*

</div>
