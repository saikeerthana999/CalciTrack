<p align="center">
  <img src="attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png" width="180" alt="CalciTrack Logo"/>
</p>

<h1 align="center">CalciTrack</h1>
<h3 align="center">Redefining Early Cardiovascular Risk Detection</h3>
<p align="center"><em>Doorstep Cardiac Screening &amp; Specialist Referral</em></p>
<p align="center">
  Invented by <strong>Sai Keerthana Cherukuri</strong> &nbsp;|&nbsp; MS4 Clinical Innovation Project
</p>

---

## My Philosophy: Detect Early. Stratify Precisely. Prevent Effectively.

> *"Cardiovascular disease does not begin with symptoms. It begins with risk."*

CalciTrack is built on a simple principle: risk must be **identified**, **measured**, and **acted upon** before it becomes disease.

| 🔍 Detect Early | 🎯 Stratify Precisely | 🛡️ Prevent Effectively |
|---|---|---|
| Identify subclinical risk using population-adjusted models and advanced biomarkers such as **Lp(a)** and **hs-CRP**. | Move beyond generalized scoring systems. Reclassify risk using **South Asian–specific thresholds** and individualized markers. | Translate risk into **clear clinical action**, enabling early intervention and reducing progression to acute events. |

---

## The Problem

South Asian populations experience premature heart disease **5–10 years earlier** than global averages. Because standard risk calculators (like Framingham or SCORE) were developed primarily on Western cohorts, they systematically **underestimate risk in South Asians**.

**CalciTrack applies the necessary "South Asian Lens" to identify risk before symptoms appear.**

---

## The Innovation

**CalciTrack** is a specialized clinical decision-support tool engineered to address the unique, often-hidden cardiovascular risk profiles within South Asian and Indian populations.

Invented by **Sai Keerthana Cherukuri**, a 4th-year medical student (MS4), this platform bridges the gap between high-complexity clinical data and community-level accessibility. By transitioning preventive care from stationary hospitals to the "doorstep" point-of-service, CalciTrack ensures that **geography is no longer a barrier to precision cardiology**.

---

## Core Capabilities

- **South Asian Adjusted Risk Engine:** Re-calibrates standard algorithms to account for the significantly higher baseline Coronary Artery Disease (CAD) risk in Asian Indian phenotypes.
- **Precision Marker Upgrades:** Implements automated reclassification logic using $Lp(a) > 50\ \text{mg/dL}$ and $hs\text{-}CRP \geq 2.0\ \text{mg/L}$ to identify "hidden" high-risk patients within the intermediate tier.
- **Female-Specific Enhancers:** Integrates critical non-traditional markers including Preeclampsia, Gestational Diabetes, Early Menopause, and PCOS history.
- **Field-Optimized Workflow:** Designed for the frontline with multi-language support (English, Hindi, Telugu, Tamil) and direct-to-specialist WhatsApp referral integration.
- **PDF Report Generation:** Downloadable clinical summary with patient risk profile, vascular age, and triage recommendation.

---

## Clinical Logic

### Base Risk Formula

```
Base Score = (Age × 0.15) + (SBP × 0.06)

Modifiers:
  + 2.0   Male sex
  + 2.0   South Asian / Indian ethnicity
  + 7.0   Current smoker / tobacco use
  + 8.0   Diabetes mellitus
  + 5.0   Each female-specific enhancer (preeclampsia, GDM, early menopause, PCOS)
  + 5.0   Each general enhancer (family CAD, CKD, Lp(a)↑, hs-CRP↑, metabolic syndrome)

Risk % = clamp( ((Total Score / 1.5) × 1.1), min=1.2, max=50.0 )
```

### Risk Stratification

| Risk % | Category | Clinical Action |
|---|---|---|
| < 5.0% | **LOW** | Life's Essential 8; re-evaluate in 3–5 years |
| 5.0–19.9% | **INTERMEDIATE** | CAC Scoring (Agatston) for reclassification |
| ≥ 19.9% | **HIGH** | High-intensity statin; specialist referral |
| INTERMEDIATE + Lp(a) >50 OR hs-CRP >2.0 | **HIGH (UPGRADED)** | Aggressive LDL-C lowering; stress testing |

### Precision Marker Upgrade Rule

If a patient scores **INTERMEDIATE** and has:
- **Lp(a) > 50 mg/dL** — genetically elevated, independently predictive (Wilson DP et al., J Clin Lipidol, 2022), OR
- **hs-CRP ≥ 2.0 mg/L** — chronic vascular inflammation (Ridker PM et al., CANTOS, NEJM 2017)

→ They are **automatically reclassified to HIGH (UPGRADED)** with aggressive treatment recommendation and critical flag on the clinical report.

### South Asian–Specific Thresholds

| Parameter | Standard | South Asian (CalciTrack) |
|---|---|---|
| BMI — Overweight | ≥ 25 | ≥ 23 |
| BMI — Obese | ≥ 30 | ≥ 25 |
| Waist (Men) | > 102 cm | > 90 cm (IDF 2006) |
| Waist (Women) | > 88 cm | > 80 cm (IDF 2006) |

---

## 6-Step Workflow

| Step | Tab | What It Does |
|---|---|---|
| 1 | **Screening** | Patient intake → risk score → visual gauge → triage → PDF report → WhatsApp referral |
| 2 | **What-If Analysis** | Current vs optimized vascular age + AHA Life's Essential 8 checklist |
| 3 | **Impact Simulator** | Set health goals, view projected risk reduction side-by-side |
| 4 | **Clinician Dashboard** | Session analytics, risk distribution charts, CSV export |
| 5 | **Education & Diet Guide** | Patient education cards + South Asian diet guide |
| 6 | **BMI Calculator** | South Asian BMI & waist circumference risk assessment |

---

## Features at a Glance

1. Multi-language UI (English, Hindi, Telugu, Tamil)
2. SVG visual risk gauge (speedometer style)
3. AHA Life's Essential 8 interactive checklist
4. South Asian diet guide with food swaps & Indian Heart Plate
5. Patient education cards (Lp(a), hs-CRP, Vascular Age, CAC, ASCVD)
6. Session analytics charts (risk tier, age group, gender)
7. CSV export for camp/clinic sessions
8. Automated follow-up scheduler based on risk tier
9. Evidence & guideline citations table (AHA/ACC, CSI, CANTOS)
10. BMI calculator with South Asian obesity thresholds

---

## Project Structure

```
CalciTrack/
├── app.py                  # Main Streamlit application (all 6 steps, ~900 lines)
├── translations.py         # Multi-language strings (English, Hindi, Telugu, Tamil)
├── .streamlit/
│   └── config.toml         # Server configuration (port 5000)
├── attached_assets/
│   └── *.png               # Logo and image assets
└── README.md               # This file
```

---

## Running the Application

```bash
streamlit run app.py --server.port 5000
```

---

## Evidence Base

| Guideline / Study | Relevance |
|---|---|
| AHA/ACC 2019 Primary Prevention Guidelines | Core ASCVD risk framework |
| CSI Consensus Statement 2020 | South Asian–specific CAD risk adjustments |
| Wilson DP et al., J Clin Lipidol 2022 | Lp(a) > 50 mg/dL as risk enhancer |
| Ridker PM et al., NEJM 2017 (CANTOS Trial) | hs-CRP ≥ 2.0 mg/L and statin benefit |
| IDF 2006 South Asian Waist Criteria | Waist circumference thresholds |
| WHO/AHA South Asian BMI Guidelines | Revised BMI obesity thresholds |

---

**Author:** Sai Keerthana Cherukuri
**Role:** MS4 Clinical Innovation Project
**Motto:** *Redefining Early Cardiovascular Risk Detection*
