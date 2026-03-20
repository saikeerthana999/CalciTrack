<div align="center">

<img src="attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png" width="150" alt="CalciTrack Logo"/>

# CalciTrack
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

## 🎯 The Problem

> South Asian populations develop coronary artery disease **5–10 years earlier** than Western populations — yet every major risk calculator was built on Western cohorts.

The Framingham Risk Score, SCORE, and ACC/AHA Pooled Cohort Equations **systematically underestimate** cardiovascular risk in South Asians. The result: millions of preventable cardiac events.

**CalciTrack applies the South Asian Lens** — a population-adjusted clinical decision-support system that detects risk precisely, stratifies accurately, and enables early intervention.

---

## 💡 Philosophy

| 🔍 **Detect Early** | 🎯 **Stratify Precisely** | 🛡️ **Prevent Effectively** |
|:---:|:---:|:---:|
| Identify subclinical cardiovascular risk using population-adjusted scoring and advanced biomarkers — **Lp(a)** and **hs-CRP** | Move beyond generalized calculators. Reclassify risk using **South Asian–specific thresholds** and precision biomarker logic | Translate risk scores into **clear, actionable clinical decisions** — early statin initiation, referrals, and prevention strategies |

---

## 🏗️ System Architecture

```mermaid
graph TB
    A[👤 Patient Data Entry] --> B[⚙️ South Asian Risk Engine]
    B --> C{📊 10-Year Risk %}
    C --> D[🟢 LOW < 5%]
    C --> E[🟠 INTERMEDIATE 5–19.9%]
    C --> F[🔴 HIGH ≥ 19.9%]
    E --> G{🔬 Precision Markers}
    G --> |Lp a > 50 mg/dL OR hs-CRP ≥ 2.0| H[🔴 HIGH UPGRADED]
    G --> |Normal| I[🟠 Stay INTERMEDIATE]
    D --> J[📋 Lifestyle Counselling + 3–5yr Follow-up]
    I --> K[🏥 CAC Scoring + 1yr Follow-up]
    H --> L[💊 High-Intensity Statin + Specialist Referral]
    F --> L
    L --> M[📄 PDF Report + WhatsApp Referral]
    J --> M
    K --> M

    style A fill:#1e3a5f,color:#fff
    style B fill:#2d5a87,color:#fff
    style D fill:#166534,color:#fff
    style E fill:#92400e,color:#fff
    style F fill:#991b1b,color:#fff
    style H fill:#7f1d1d,color:#fff
    style I fill:#78350f,color:#fff
```

---

## 🧮 Clinical Algorithm

### Risk Scoring Formula

```mermaid
flowchart LR
    subgraph BASE["📐 Base Score"]
        A1["Age × 0.15"]
        A2["SBP × 0.06"]
        A1 --> A3["+"]
        A2 --> A3
    end

    subgraph DEMO["🧬 Demographics"]
        B1["+2.0 Male"]
        B2["+2.0 South Asian"]
        B3["+1.5 African"]
    end

    subgraph CLINICAL["⚕️ Clinical Factors"]
        C1["+8.0 Diabetes"]
        C2["+7.0 Smoker"]
        C3["+5.0 per Enhancer"]
    end

    subgraph FINAL["📊 Final Risk"]
        D1["Total Score"]
        D2["÷ 1.5 × 1.1"]
        D3["Clamp: 1.2% – 50%"]
        D1 --> D2 --> D3
    end

    BASE --> FINAL
    DEMO --> FINAL
    CLINICAL --> FINAL
```

### Risk Enhancers (+5.0 each)

| Category | Enhancers |
|---|---|
| ♀️ Female-Specific | Preeclampsia · Gestational Diabetes · Early Menopause · PCOS |
| 🧬 Genetic / Comorbid | Family CAD · CKD · Metabolic Syndrome |
| 🔬 Biomarker (Checkbox) | Elevated Lp(a) · Elevated hs-CRP |

---

## 🔬 Precision Marker Upgrade Logic

```mermaid
flowchart TD
    A([🩺 Patient Screened]) --> B{Risk Category?}

    B --> |"< 5%"| C([🟢 LOW\nLifestyle focus\nRe-evaluate: 3–5 years])
    B --> |"5–19.9%"| D{🔬 Check Precision Markers}
    B --> |"≥ 19.9%"| E([🔴 HIGH\nHigh-intensity statin\nSpecialist referral\nRe-evaluate: 3–6 months])

    D --> |"Lp(a) > 50 mg/dL\nOR hs-CRP ≥ 2.0 mg/L"| F([🔴 HIGH — UPGRADED ⚠️\nCRITICAL FLAG on report\nAggressive LDL-C lowering\nFunctional stress testing\nSpecialist referral])

    D --> |"Lp(a) ≤ 50 AND\nhs-CRP < 2.0"| G([🟠 INTERMEDIATE\nCAC Score Agatston\nModerate statin consideration\nRe-evaluate: 1 year])

    style C fill:#166534,color:#fff,stroke:#14532d
    style E fill:#991b1b,color:#fff,stroke:#7f1d1d
    style F fill:#7f1d1d,color:#fff,stroke:#450a0a
    style G fill:#92400e,color:#fff,stroke:#78350f
```

### Why These Two Markers?

| Marker | Threshold | Mechanism | Evidence |
|---|:---:|---|---|
| **Lp(a)** — Lipoprotein(a) | > 50 mg/dL | Genetically determined · Drives plaque + thrombosis · Not reduced by statins | Wilson DP et al., *J Clin Lipidol*, 2022 |
| **hs-CRP** — High-Sensitivity CRP | ≥ 2.0 mg/L | Chronic vascular inflammation · Predicts MI even in low-LDL patients | Ridker PM et al., *NEJM*, 2017 (CANTOS) |

---

## 🌏 The South Asian Lens

```mermaid
graph LR
    subgraph STANDARD["⚖️ Standard Calculators"]
        S1["BMI Obese ≥ 30 kg/m²"]
        S2["Waist Men > 102 cm"]
        S3["Waist Women > 88 cm"]
        S4["No ethnicity adjustment"]
        S5["No female enhancers"]
        S6["❌ Underestimates SA risk"]
    end

    subgraph CALCITRACK["🎯 CalciTrack — South Asian Lens"]
        C1["BMI Obese ≥ 25 kg/m² ✓"]
        C2["Waist Men > 90 cm ✓"]
        C3["Waist Women > 80 cm ✓"]
        C4["+2.0 South Asian modifier ✓"]
        C5["Preeclampsia / GDM / PCOS ✓"]
        C6["✅ Precision South Asian triage"]
    end

    STANDARD --> |"South Asian Lens Applied"| CALCITRACK

    style S6 fill:#991b1b,color:#fff
    style C6 fill:#166534,color:#fff
```

---

## 🗺️ 6-Step Clinical Workflow

```mermaid
graph LR
    S1["🏥 Step 1\nScreening\nRisk Score + Gauge\nPDF + WhatsApp"] -->
    S2["🔮 Step 2\nWhat-If Analysis\nVascular Age\nLife's Essential 8"] -->
    S3["🎯 Step 3\nImpact Simulator\nGoal-Setting\nRisk Reduction"] -->
    S4["📊 Step 4\nClinician Dashboard\nSession Analytics\nCSV Export"] -->
    S5["📚 Step 5\nEducation\nDiet Guide\nPatient Cards"] -->
    S6["🧮 Step 6\nBMI Calculator\nSouth Asian BMI\nWaist Risk"]

    style S1 fill:#1e3a5f,color:#fff
    style S2 fill:#2d5a87,color:#fff
    style S3 fill:#1e6b8a,color:#fff
    style S4 fill:#166534,color:#fff
    style S5 fill:#6b21a8,color:#fff
    style S6 fill:#92400e,color:#fff
```

---

## 💓 Vascular Age Calculation

```mermaid
flowchart LR
    A["🎂 Chronological Age"] --> B["Vascular Age = Age"]
    B --> C{"SBP > 120?"}
    C --> |Yes| D["+ SBP−120 × 0.1 years"]
    C --> |No| E["No change"]
    D --> F{"Current Smoker?"}
    E --> F
    F --> |Yes| G["+ 8 years"]
    F --> |No| H["No change"]
    G --> I{"Diabetes?"}
    H --> I
    I --> |Yes| J["+ 6 years"]
    I --> |No| K["= Final Vascular Age"]
    J --> K

    style K fill:#1e3a5f,color:#fff
```

**Example:** Age 45 · SBP 140 · Smoker · Diabetic
→ 45 + (140−120)×0.1 + 8 + 6 = **61 years biological vascular age**

---

## ✨ Core Features

| # | Feature | Description |
|---|---|---|
| 1 | 🌍 Multi-Language | Full UI in English, Hindi, Telugu, Tamil |
| 2 | 📊 Visual Risk Gauge | SVG speedometer — real-time color-coded risk |
| 3 | ✅ Life's Essential 8 | AHA interactive health checklist with scoring |
| 4 | 🥗 South Asian Diet Guide | Food swaps, Indian Heart Plate, spice guide |
| 5 | 🎓 Patient Education Cards | Lp(a), hs-CRP, Vascular Age, CAC, ASCVD explained simply |
| 6 | 📈 Session Analytics | Risk distribution, age group, gender breakdown charts |
| 7 | 📥 CSV Export | Download session screening data |
| 8 | 📅 Follow-Up Scheduler | Auto next-screening date by risk tier |
| 9 | 📖 Evidence Citations | AHA/ACC, CSI, CANTOS, IDF references table |
| 10 | ⚖️ SA BMI Calculator | South Asian thresholds + waist circumference risk |

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/saikeerthana999/CalciTrack.git
cd CalciTrack

# Install dependencies
pip install streamlit pandas fpdf

# Run the application
streamlit run app.py --server.port 5000
```

Open your browser at `http://localhost:5000`

---

## 📁 Project Structure

```
CalciTrack/
├── 📄 app.py                   # Main application — all 6 steps + methodology tab
├── 🌐 translations.py          # Multi-language strings (EN / HI / TE / TA)
├── 📖 README.md                # This file
├── 🤝 CONTRIBUTING.md          # Contributor guidelines
├── 📚 CITATION.cff             # Academic citation file (CFF format)
├── ⚖️  LICENSE                  # MIT License
├── 🚫 .gitignore               # Git ignore rules
├── 🔧 .streamlit/
│   └── config.toml             # Streamlit server configuration
└── 🖼️  attached_assets/
    └── *.png                   # Logo and image assets
```

---

## 📚 Evidence Base

| Reference | Year | Relevance in CalciTrack |
|---|:---:|---|
| AHA/ACC Primary Prevention Guidelines | 2019 | Core ASCVD framework · Statin initiation thresholds |
| CSI Consensus Statement — South Asian CVD | 2020 | South Asian CAD risk adjustment · +2.0 ethnicity modifier |
| Wilson DP et al., *J Clin Lipidol* | 2022 | Lp(a) >50 mg/dL as independent risk enhancer |
| Ridker PM et al., *NEJM* — CANTOS Trial | 2017 | hs-CRP ≥2.0 mg/L · Anti-inflammatory statin benefit |
| IDF Consensus Statement | 2006 | Waist circumference: Men >90cm · Women >80cm |
| WHO Asia-Pacific BMI Guidelines | 2004 | BMI obesity threshold ≥25 kg/m² for South Asians |

---

## 🔖 Citation

If you use CalciTrack in research, clinical presentations, or proceedings, please cite:

```bibtex
@software{calcitrack2025,
  author    = {Cherukuri, Sai Keerthana},
  title     = {CalciTrack: South Asian-Adjusted Cardiovascular Risk Detection},
  year      = {2025},
  url       = {https://github.com/saikeerthana999/CalciTrack},
  license   = {MIT}
}
```

> Cherukuri, S.K. (2025). *CalciTrack: South Asian–Adjusted Cardiovascular Risk Detection Tool* [Software]. https://github.com/saikeerthana999/CalciTrack

---

## 🤝 Contributing

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
