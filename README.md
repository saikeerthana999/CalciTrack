<p align="center">
  <img src="attached_assets/Gemini_Generated_Image_fa87vfa87vfa87vf_1767032834009.png" width="160" alt="CalciTrack Logo"/>
</p>

<h1 align="center">CalciTrack</h1>
<h3 align="center">Redefining Early Cardiovascular Risk Detection</h3>
<p align="center"><em>Doorstep Cardiac Screening &amp; Specialist Referral for South Asian Populations</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Languages-EN%20%7C%20HI%20%7C%20TE%20%7C%20TA-blue?style=for-the-badge"/>
</p>

<p align="center">
  Invented by <strong>Sai Keerthana Cherukuri</strong> &nbsp;|&nbsp; MS4 Clinical Innovation Project
</p>

---

## The Problem

> South Asian populations experience premature heart disease **5–10 years earlier** than global averages.

Standard risk calculators — Framingham, SCORE, ASCVD Pooled Cohort — were developed primarily on Western cohorts. They **systematically underestimate risk** in South Asians, leaving a clinically significant gap in early detection.

**CalciTrack applies the "South Asian Lens" to identify cardiovascular risk before symptoms appear.**

---

## My Philosophy

> *"Cardiovascular disease does not begin with symptoms. It begins with risk."*

CalciTrack is built on one principle: risk must be **identified**, **measured**, and **acted upon** before it becomes disease.

| 🔍 Detect Early | 🎯 Stratify Precisely | 🛡️ Prevent Effectively |
|:---:|:---:|:---:|
| Identify subclinical risk using population-adjusted models and advanced biomarkers — **Lp(a)** and **hs-CRP** | Move beyond generalized scoring. Reclassify risk using **South Asian–specific thresholds** and individualized precision markers | Translate risk into **clear clinical action**, enabling early intervention before progression to acute events |

---

## The Innovation

**CalciTrack** is a specialized clinical decision-support application that bridges high-complexity cardiology data with community-level accessibility.

By transitioning preventive care from stationary hospitals to the **"doorstep" point of service**, CalciTrack ensures that geography, language, and access are no longer barriers to precision cardiology.

---

## Core Capabilities

| Feature | Description |
|---|---|
| 🧮 **South Asian Risk Engine** | Re-calibrates standard algorithms for the higher baseline CAD risk in Asian Indian phenotypes |
| 🔬 **Precision Marker Upgrade** | Auto-reclassifies INTERMEDIATE → HIGH using Lp(a) >50 mg/dL or hs-CRP ≥2.0 mg/L |
| ♀️ **Female-Specific Enhancers** | Integrates Preeclampsia, GDM, Early Menopause, and PCOS as quantified risk factors |
| 🌍 **Multi-Language UI** | Full interface in English, Hindi, Telugu, and Tamil |
| 📊 **Visual Risk Gauge** | SVG speedometer gauge with real-time risk color coding |
| 📋 **PDF Clinical Reports** | Downloadable Heart Health Summary with vascular age and triage recommendations |
| 📲 **WhatsApp Referral** | Direct specialist referral message pre-filled from the risk result |
| 🏥 **Clinician Dashboard** | Session-level analytics, risk distribution charts, and CSV export |

---

## Clinical Logic

### Risk Scoring Formula

```
Base Score  =  (Age × 0.15) + (Systolic BP × 0.06)

Modifiers:
  + 2.0   Male sex
  + 2.0   South Asian / Indian ethnicity
  + 1.5   African / African American ethnicity
  + 7.0   Current smoker / tobacco use
  + 8.0   Diabetes mellitus
  + 5.0   Per female-specific enhancer (Preeclampsia, GDM, Early Menopause, PCOS)
  + 5.0   Per general enhancer (Family CAD, CKD, Lp(a)↑, hs-CRP↑, Metabolic Syndrome)

Final Risk %  =  clamp( (Total Score ÷ 1.5) × 1.1,  min = 1.2%,  max = 50.0% )
```

### Risk Stratification

| 10-Year Risk | Category | Recommended Action |
|:---:|:---:|---|
| < 5.0% | 🟢 **LOW** | Life's Essential 8; re-evaluate in 3–5 years |
| 5.0 – 19.9% | 🟠 **INTERMEDIATE** | CAC Scoring (Agatston) for reclassification |
| ≥ 19.9% | 🔴 **HIGH** | High-intensity statin; specialist referral |
| INTERMEDIATE + Lp(a)↑ or hs-CRP↑ | 🔴 **HIGH (UPGRADED)** | Aggressive LDL-C lowering; stress testing |

### Precision Marker Reclassification

The key clinical innovation — applied to INTERMEDIATE-risk patients only:

```
IF  Patient is INTERMEDIATE  AND  (Lp(a) > 50 mg/dL  OR  hs-CRP ≥ 2.0 mg/L)
THEN  Reclassify → HIGH (UPGRADED)
      Flag → "CRITICAL: Risk upgraded due to genetic/inflammatory markers"
      Recommend → High-intensity statin + Specialist referral
```

> Based on: Wilson DP et al. (J Clin Lipidol, 2022) for Lp(a); Ridker PM et al. (CANTOS, NEJM 2017) for hs-CRP.

### South Asian–Specific Thresholds

| Parameter | Standard Threshold | South Asian (CalciTrack) | Reference |
|---|:---:|:---:|---|
| BMI Overweight | ≥ 25 kg/m² | ≥ 23 kg/m² | WHO Asia-Pacific |
| BMI Obese | ≥ 30 kg/m² | ≥ 25 kg/m² | WHO Asia-Pacific |
| Waist — Men | > 102 cm | > 90 cm | IDF 2006 |
| Waist — Women | > 88 cm | > 80 cm | IDF 2006 |

---

## 6-Step Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│  Step 1: Screening        Patient intake → Risk score → Triage      │
│  Step 2: What-If          Vascular age + Life's Essential 8         │
│  Step 3: Impact Simulator Set goals → Projected risk reduction      │
│  Step 4: Clinician Dashboard Session analytics + CSV export         │
│  Step 5: Education & Diet South Asian diet guide + Education cards  │
│  Step 6: BMI Calculator   South Asian BMI + Waist risk assessment   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/saikeerthana999/CalciTrack.git
cd CalciTrack

# Install dependencies
pip install streamlit pandas fpdf

# Run the application
streamlit run app.py --server.port 5000
```

---

## Project Structure

```
CalciTrack/
├── app.py                    # Main application — all 6 steps (~900 lines)
├── translations.py           # Multi-language strings (EN / HI / TE / TA)
├── README.md                 # Project documentation
├── CONTRIBUTING.md           # Contributor guidelines
├── CITATION.cff              # Academic citation file
├── LICENSE                   # MIT License
├── .gitignore                # Git ignore rules
├── .streamlit/
│   └── config.toml           # Streamlit server configuration
└── attached_assets/
    └── *.png                 # Logo and image assets
```

---

## Evidence Base

| Reference | Relevance to CalciTrack |
|---|---|
| AHA/ACC 2019 Primary Prevention Guidelines | Core ASCVD risk framework and statin thresholds |
| CSI Consensus Statement 2020 | South Asian–specific CAD risk adjustment |
| Wilson DP et al., J Clin Lipidol 2022 | Lp(a) >50 mg/dL as independent risk enhancer |
| Ridker PM et al., NEJM 2017 (CANTOS) | hs-CRP ≥2.0 mg/L and anti-inflammatory statin benefit |
| IDF Consensus 2006 | South Asian waist circumference cut-offs |
| WHO Asia-Pacific Guidelines | Revised BMI obesity thresholds for Asian populations |

---

## Vascular Age Formula

```
Vascular Age  =  Chronological Age
              +  (SBP − 120) × 0.1    [if SBP > 120]
              +  8 years               [if current smoker]
              +  6 years               [if diabetes]
```

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Citation

If you use CalciTrack in research, clinical presentations, or conference proceedings, please cite using the [CITATION.cff](CITATION.cff) file or:

> Cherukuri, S.K. (2025). *CalciTrack: South Asian–Adjusted Cardiovascular Risk Detection Tool* [Software]. GitHub. https://github.com/saikeerthana999/CalciTrack

---

## Contributing

We welcome contributions from clinicians, data scientists, and developers. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

<p align="center">
  <strong>Author:</strong> Sai Keerthana Cherukuri &nbsp;|&nbsp; MS4 Clinical Innovation Project<br/>
  <em>Redefining Early Cardiovascular Risk Detection</em>
</p>
