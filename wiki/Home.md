![CalciTrack Logo](https://raw.githubusercontent.com/saikeerthana999/CalciTrack/main/attached_assets/logo_(3)_1774049373069.png)

# CalciTrack — Wiki Home

**Redefining Early Cardiovascular Risk Detection**

*Doorstep Cardiac Screening & Specialist Referral — Engineered for South Asian Populations*

Invented by **Sai Keerthana Cherukuri** · MS4 Clinical Innovation Project

*"Cardiovascular disease does not begin with symptoms. It begins with risk."*

---

## Wiki Navigation

| Page | What You Will Find |
|---|---|
| **[Home](Home)** | Project overview, philosophy, features, and quick start |
| **[Clinical Logic & Algorithm](Clinical-Logic)** | Full mathematical model, risk formula, biomarker rules, vascular age |
| **[Evidence Base](Evidence-Base)** | Peer-reviewed citations and guideline mapping |
| **[User Guide](User-Guide)** | Step-by-step walkthrough for clinicians and health workers |

---

## What Is CalciTrack?

CalciTrack is a **clinical decision-support application** for cardiovascular risk screening, triage, and specialist referral — designed specifically for South Asian and Indian populations.

It was built to solve one critical problem:

> Standard risk calculators — Framingham, SCORE, ACC/AHA Pooled Cohort — were developed on Western cohorts and **systematically underestimate** coronary artery disease risk in South Asians, who develop heart disease **5–10 years earlier** than global averages.

CalciTrack corrects this by applying a **South Asian–adjusted risk engine** that integrates:

- Population-specific ethnicity modifiers
- Precision biomarkers — Lp(a) and hs-CRP — for hidden risk detection
- Female-specific cardiovascular risk enhancers (preeclampsia, GDM, PCOS, early menopause)
- South Asian BMI and waist circumference thresholds

---

## Philosophy

CalciTrack is built on one principle: risk must be identified, measured, and acted upon **before it becomes disease**.

**Detect Early** — Identify subclinical cardiovascular risk using population-adjusted scoring and advanced biomarkers before the patient is symptomatic.

**Stratify Precisely** — Move beyond generalized scoring. Reclassify individual patients using South Asian–specific thresholds and precision biomarker upgrade logic.

**Prevent Effectively** — Translate risk scores into clear, actionable clinical decisions — early statin initiation, specialist referral, and prevention of acute cardiac events.

---

## Key Features

| Feature | Description |
|---|---|
| South Asian Risk Engine | Re-calibrated algorithm with ethnicity modifier and SA-specific BMI and waist thresholds |
| Precision Marker Upgrade | Lp(a) >50 and hs-CRP ≥2.0 trigger automatic INTERMEDIATE → HIGH reclassification |
| Female-Specific Enhancers | Preeclampsia, GDM, PCOS, and Early Menopause as quantified risk factors |
| Visual Risk Gauge | SVG speedometer — colour-coded real-time risk visualisation |
| Multi-Language UI | English, Hindi, Telugu, Tamil — for community health workers |
| PDF Clinical Reports | Downloadable Heart Health Summary with vascular age and triage recommendation |
| WhatsApp Referral | Pre-filled specialist referral message generated from the risk result |
| Clinician Dashboard | Session-level analytics, risk distribution charts, and CSV export |
| Life's Essential 8 | AHA interactive health checklist with composite scoring |
| South Asian Diet Guide | Culturally relevant food swaps and the Indian Heart Plate model |

---

## The 6-Step Workflow

**Step 1 — Screening**
Patient data entry, 10-year risk calculation, visual risk gauge, clinical impression, vascular age, PDF report, and WhatsApp referral.

**Step 2 — What-If Analysis**
Side-by-side comparison of current vascular age vs optimised vascular age. Includes the Life's Essential 8 interactive checklist.

**Step 3 — Impact Simulator**
Set specific goals (target BP, smoking cessation, diabetes management) and see the projected risk reduction in real time with before/after gauges.

**Step 4 — Clinician Dashboard**
Session-level analytics for multi-patient camp settings. Risk distribution charts, age and gender breakdown, and CSV export.

**Step 5 — Education & Diet Guide**
Patient education cards for Lp(a), hs-CRP, vascular age, CAC scoring, and ASCVD risk. South Asian diet guide with food swaps, the Indian Heart Plate, and heart-protective spices.

**Step 6 — BMI Calculator**
South Asian–specific BMI classification and waist circumference risk assessment with threshold comparison table.

---

## Risk Stratification at a Glance

| 10-Year Risk | Category | Clinical Action | Follow-Up |
|---|:---:|---|:---:|
| Below 5.0% | LOW | Lifestyle counselling · Life's Essential 8 | 3–5 years |
| 5.0 – 19.9% | INTERMEDIATE | CAC Scoring · Check Lp(a) and hs-CRP | 1 year |
| 19.9% or above | HIGH | High-intensity statin · Specialist referral | 3–6 months |
| INTERMEDIATE + elevated Lp(a) or hs-CRP | HIGH (UPGRADED) | Aggressive LDL-C · Stress testing · Urgent referral | Immediate |

---

## South Asian Thresholds vs Standard

| Parameter | Standard Calculators | CalciTrack | Reference |
|---|:---:|:---:|---|
| BMI Overweight | 25 kg/m² or above | 23 kg/m² or above | WHO Asia-Pacific 2004 |
| BMI Obese | 30 kg/m² or above | 25 kg/m² or above | WHO Asia-Pacific 2004 |
| Waist — Men | above 102 cm | above 90 cm | IDF 2006 |
| Waist — Women | above 88 cm | above 80 cm | IDF 2006 |
| Age of CAD onset | Standard average | 5–10 years earlier | CSI 2020 |

---

## Quick Start

```bash
git clone https://github.com/saikeerthana999/CalciTrack.git
cd CalciTrack
pip install streamlit pandas fpdf
streamlit run app.py --server.port 5000
```

---

## Citation

Cherukuri, S.K. (2025). *CalciTrack: South Asian–Adjusted Cardiovascular Risk Detection Tool* [Software]. GitHub. https://github.com/saikeerthana999/CalciTrack

---

*CalciTrack · Detect Early · Stratify Precisely · Prevent Effectively*
