<div align="center">

<img src="attached_assets/logo_(3)_1774049373069.png" width="220" alt="CalciTrack Logo"/>

### Redefining Early Cardiovascular Risk Detection


*Doorstep Cardiac Screening & Specialist Referral — Engineered for South Asian Populations*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)]()
[![Languages](https://img.shields.io/badge/Languages-EN%20%7C%20HI%20%7C%20TE%20%7C%20TA-6366f1?style=flat-square)]()
[![Conference](https://img.shields.io/badge/Conference-Ready-f59e0b?style=flat-square)]()

<br/>

**Invented by [Sai Keerthana Cherukuri](https://github.com/saikeerthana999)**
MS4 Clinical Innovation Project

*"Cardiovascular disease does not begin with symptoms. It begins with risk."*

</div>

---

## The Problem

> South Asian populations develop coronary artery disease **5–10 years earlier** than Western populations — yet every major risk calculator was built on Western cohorts.

The Framingham Risk Score, SCORE, and ACC/AHA Pooled Cohort Equations **systematically underestimate** cardiovascular risk in South Asians. The result: millions of preventable cardiac events.

**CalciTrack applies the South Asian Lens** — a population-adjusted clinical decision-support system that detects risk precisely, stratifies accurately, and enables early intervention.

---

## Philosophy

| Detect Early | Stratify Precisely | Prevent Effectively |
|:---:|:---:|:---:|
| Identify subclinical cardiovascular risk using population-adjusted scoring and advanced biomarkers — **Lp(a)** and **hs-CRP** | Move beyond generalized calculators. Reclassify risk using **South Asian-specific thresholds** and precision biomarker logic | Translate risk scores into **clear, actionable clinical decisions** — early statin initiation, referrals, and prevention strategies |

---

## System Architecture

```mermaid
graph TB
    A[Patient Data Entry] --> B[South Asian Risk Engine]
    B --> C[10-Year Risk Percent]
    C --> D[LOW under 5 percent]
    C --> E[INTERMEDIATE 5 to 19.9 percent]
    C --> F[HIGH 19.9 percent or more]
    E --> G[Check Precision Markers]
    G -->|Lp-a above 50 OR hs-CRP above 2.0| H[HIGH UPGRADED]
    G -->|Normal values| I[Stay INTERMEDIATE]
    D --> J[Lifestyle Counselling and 3-5yr Follow-up]
    I --> K[CAC Scoring and 1yr Follow-up]
    H --> L[High-Intensity Statin and Specialist Referral]
    F --> L
    L --> M[PDF Report and WhatsApp Referral]
    J --> M
    K --> M
```

---

## Clinical Algorithm

### Risk Score Calculation

```mermaid
graph TD
    A[Start] --> B[Base Score = Age x 0.15 + SBP x 0.06]
    B --> C[Add Demographic Modifiers]
    C --> C1[Male sex plus 2.0]
    C --> C2[South Asian plus 2.0]
    C --> C3[African ethnicity plus 1.5]
    C1 --> D[Add Clinical Risk Factors]
    C2 --> D
    C3 --> D
    D --> D1[Diabetes plus 8.0]
    D --> D2[Smoker plus 7.0]
    D --> D3[Each Enhancer plus 5.0]
    D1 --> E[Total Score]
    D2 --> E
    D3 --> E
    E --> F[Risk Percent = Total divided by 1.5 multiplied by 1.1]
    F --> G[Clamp between 1.2 percent and 50 percent]
    G --> H[Final 10-Year Risk Percent]
```

### Risk Enhancers — +5.0 each

| Category | Enhancers |
|---|---|
| Female-Specific | Preeclampsia · Gestational Diabetes · Early Menopause · PCOS |
| Genetic / Comorbid | Family CAD · CKD · Metabolic Syndrome |
| Biomarker Checkbox | Elevated Lp(a) · Elevated hs-CRP |

---

## Precision Marker Upgrade — The Decision Tree

```mermaid
graph TD
    A[Patient Screened] --> B{Risk Category?}
    B -->|Less than 5 percent| C[LOW RISK\nLifestyle focus\nFollow-up 3-5 years]
    B -->|5 to 19.9 percent| D{Check Precision Markers}
    B -->|19.9 percent or more| E[HIGH RISK\nHigh-intensity statin\nSpecialist referral\nFollow-up 3-6 months]
    D -->|Lp-a above 50 mg-dL OR hs-CRP above 2.0 mg-L| F[HIGH UPGRADED\nCRITICAL FLAG on report\nAggressive LDL-C lowering\nFunctional stress testing\nSpecialist referral]
    D -->|Both values normal| G[INTERMEDIATE\nCAC Score recommended\nModerate statin consideration\nFollow-up 1 year]
```

### Why These Two Markers?

| Marker | Threshold | Mechanism | Evidence |
|---|:---:|---|---|
| **Lp(a)** Lipoprotein-a | > 50 mg/dL | Genetically determined · Drives plaque and thrombosis · Not reduced by statins | Wilson DP et al., *J Clin Lipidol*, 2022 |
| **hs-CRP** High-Sensitivity CRP | >= 2.0 mg/L | Chronic vascular inflammation · Predicts MI even in low-LDL patients | Ridker PM et al., *NEJM*, 2017 CANTOS |

---

## The South Asian Lens

```mermaid
graph LR
    subgraph Standard ["Standard Calculators"]
        S1[BMI Obese above 30]
        S2[Waist Men above 102 cm]
        S3[Waist Women above 88 cm]
        S4[No ethnicity adjustment]
        S5[No female enhancers]
    end

    subgraph CalciTrack ["CalciTrack South Asian Lens"]
        C1[BMI Obese above 25]
        C2[Waist Men above 90 cm]
        C3[Waist Women above 80 cm]
        C4[South Asian modifier plus 2.0]
        C5[Preeclampsia GDM PCOS Menopause]
    end

    Standard -->|South Asian Lens Applied| CalciTrack
```

---

## 6-Step Clinical Workflow

```mermaid
graph LR
    S1[Step 1\nScreening\nRisk Score\nPDF Report] -->
    S2[Step 2\nWhat-If Analysis\nVascular Age\nLife's Essential 8] -->
    S3[Step 3\nImpact Simulator\nGoal Setting\nRisk Reduction] -->
    S4[Step 4\nClinician Dashboard\nAnalytics\nCSV Export] -->
    S5[Step 5\nEducation\nDiet Guide\nPatient Cards] -->
    S6[Step 6\nBMI Calculator\nSouth Asian BMI\nWaist Risk]
```

---

## Vascular Age Calculation

```mermaid
graph LR
    A[Chronological Age] --> B[Start with Age]
    B --> C{SBP above 120?}
    C -->|Yes| D[Add SBP minus 120 times 0.1 years]
    C -->|No| E[No change]
    D --> F{Current Smoker?}
    E --> F
    F -->|Yes| G[Add 8 years]
    F -->|No| H[No change]
    G --> I{Diabetes?}
    H --> I
    I -->|Yes| J[Add 6 years]
    I -->|No| K[Final Vascular Age]
    J --> K
```

**Example:** Age 45 · SBP 140 · Smoker · Diabetic
→ 45 + (140−120)×0.1 + 8 + 6 = **61 years biological vascular age**

---

## Core Features

| # | Feature | Description |
|---|---|---|
| 1 | Multi-Language | Full UI in English, Hindi, Telugu, Tamil |
| 2 | Visual Risk Gauge | SVG speedometer — real-time colour-coded risk |
| 3 | Life's Essential 8 | AHA interactive health checklist with scoring |
| 4 | South Asian Diet Guide | Food swaps, Indian Heart Plate, spice guide |
| 5 | Patient Education Cards | Lp(a), hs-CRP, Vascular Age, CAC, ASCVD explained simply |
| 6 | Session Analytics | Risk distribution, age group, gender breakdown charts |
| 7 | CSV Export | Download session screening data |
| 8 | Follow-Up Scheduler | Auto next-screening date by risk tier |
| 9 | Evidence Citations | AHA/ACC, CSI, CANTOS, IDF references table |
| 10 | SA BMI Calculator | South Asian thresholds and waist circumference risk |

---

## Quick Start

```bash
git clone https://github.com/saikeerthana999/CalciTrack.git
cd CalciTrack
pip install streamlit pandas fpdf
streamlit run app.py --server.port 5000
```

---

## Project Structure

```
CalciTrack/
├── app.py                   # Main application — all 6 steps + methodology tab
├── translations.py          # Multi-language strings (EN / HI / TE / TA)
├── README.md                # This file
├── CONTRIBUTING.md          # Contributor guidelines
├── CITATION.cff             # Academic citation file
├── LICENSE                  # MIT License
├── .gitignore               # Git ignore rules
├── .streamlit/
│   └── config.toml          # Streamlit server configuration
└── attached_assets/
    └── *.png                # Logo and image assets
```

---

## Evidence Base

| Reference | Year | Relevance in CalciTrack |
|---|:---:|---|
| AHA/ACC Primary Prevention Guidelines | 2019 | Core ASCVD framework · Statin initiation thresholds |
| CSI Consensus Statement — South Asian CVD | 2020 | South Asian CAD risk adjustment · Ethnicity modifier |
| Wilson DP et al., *J Clin Lipidol* | 2022 | Lp(a) >50 mg/dL as independent risk enhancer |
| Ridker PM et al., *NEJM* — CANTOS Trial | 2017 | hs-CRP >=2.0 mg/L · Anti-inflammatory statin benefit |
| IDF Consensus Statement | 2006 | Waist circumference: Men >90cm · Women >80cm |
| WHO Asia-Pacific BMI Guidelines | 2004 | BMI obesity threshold >=25 for South Asians |

---

## Citation

```bibtex
@software{calcitrack2025,
  author    = {Cherukuri, Sai Keerthana},
  title     = {CalciTrack: South Asian-Adjusted Cardiovascular Risk Detection},
  year      = {2025},
  url       = {https://github.com/saikeerthana999/CalciTrack},
  license   = {MIT}
}
```

---

## Contributing

Contributions from clinicians, researchers, and developers are welcome.
Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

<div align="center">

---

### CalciTrack

*Redefining Early Cardiovascular Risk Detection*

**Invented by Sai Keerthana Cherukuri · MS4 Clinical Innovation Project**

[![GitHub](https://img.shields.io/badge/GitHub-saikeerthana999-181717?style=flat-square&logo=github)](https://github.com/saikeerthana999)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

*Detect Early · Stratify Precisely · Prevent Effectively*

---

</div>
