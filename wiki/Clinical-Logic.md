# Clinical Logic & Algorithm

> **CalciTrack — Technical Reference for Clinicians and Evaluators**

---

## 📐 The Risk Scoring Formula

CalciTrack computes a **10-year cardiovascular risk percentage** using a weighted additive model adjusted for South Asian population characteristics.

### Step 1: Base Score

```
Base Score = (Age × 0.15) + (Systolic Blood Pressure × 0.06)
```

| Variable | Coefficient | Rationale |
|---|:---:|---|
| Age | × 0.15 | Linear age-risk relationship per decade |
| Systolic BP | × 0.06 | Each 10 mmHg elevation increases risk ~6% |

### Step 2: Demographic Modifiers

| Modifier | Value | Reference |
|---|:---:|---|
| Male sex | +2.0 | Higher baseline ASCVD risk in males |
| South Asian / Indian ethnicity | +2.0 | CSI Consensus 2020 — premature CAD adjustment |
| African / African American | +1.5 | AHA/ACC 2019 — elevated baseline risk |

### Step 3: Clinical Risk Factors

| Risk Factor | Value | Rationale |
|---|:---:|---|
| Current smoker / tobacco | +7.0 | ~2x relative risk increase |
| Diabetes mellitus | +8.0 | Equivalent to prior MI in risk magnitude |
| Each risk enhancer (see below) | +5.0 | Per AHA/ACC 2019 risk-enhancing criteria |

### Step 4: Risk Enhancers (+5.0 each)

**Female-Specific Enhancers:**
- Preeclampsia history
- Gestational Diabetes (GDM)
- Early Menopause (< 40 years)
- Polycystic Ovary Syndrome (PCOS)

**General Enhancers:**
- Family history of premature CAD (first-degree relative, male <55 / female <65)
- Chronic Kidney Disease (CKD)
- Metabolic Syndrome
- Elevated Lp(a) (checkbox — qualitative entry)
- Elevated hs-CRP (checkbox — qualitative entry)

### Step 5: Final Risk Calculation

```
Total Score   =   Base Score + All Modifiers + All Enhancers

Risk %        =   clamp( (Total Score ÷ 1.5) × 1.1,  min = 1.2%,  max = 50.0% )
```

The `clamp` function ensures the result is never below 1.2% (minimum biological risk) or above 50.0% (clinical ceiling for 10-year ASCVD risk reporting).

---

## 📊 Risk Stratification

| 10-Year Risk % | Category | Colour | Clinical Decision |
|---|:---:|:---:|---|
| < 5.0% | **LOW** | 🟢 Green | Lifestyle counselling · Life's Essential 8 |
| 5.0 – 19.9% | **INTERMEDIATE** | 🟠 Orange | CAC Scoring (Agatston) for reclassification |
| ≥ 19.9% | **HIGH** | 🔴 Red | High-intensity statin · Specialist referral |
| INTERMEDIATE + Lp(a)↑ or hs-CRP↑ | **HIGH (UPGRADED)** | 🔴 Red | Aggressive treatment · CRITICAL flag |

---

## 🔬 Precision Marker Reclassification

### The Upgrade Rule

This is the central clinical innovation in CalciTrack's triage logic.

```
IF   patient_risk_tier == INTERMEDIATE
AND  (lpa_value > 50 mg/dL  OR  hscrp_value >= 2.0 mg/L)
THEN reclassify → HIGH (UPGRADED)
     flag       → "CRITICAL: Risk upgraded due to genetic/inflammatory markers"
     recommend  → High-intensity statin + Specialist Referral + Stress Testing
```

### Two-Level Biomarker Approach

**Level 1 — Qualitative (Checkboxes)**
Clinicians who know a patient has elevated markers but lack exact values can check the qualitative boxes. Each adds +5.0 to the base score.

**Level 2 — Quantitative (Numeric Lab Values)**
When actual lab values are entered, the precision upgrade rule fires independently — even if the checkboxes are not selected. This triggers reclassification from INTERMEDIATE to HIGH (UPGRADED).

### Why Lp(a)?

- **Genetically determined** — cannot be reduced by diet or conventional statins
- Levels >50 mg/dL independently predict atherosclerotic events and thrombosis
- Particularly elevated in South Asian populations — and frequently undiagnosed
- Drives oxidised phospholipid–mediated plaque progression
- **Reference:** Wilson DP et al., *J Clin Lipidol*, 2022

### Why hs-CRP?

- Reflects chronic, low-grade vascular inflammation
- Levels ≥2.0 mg/L predict first myocardial infarction even in patients with normal LDL-C
- The CANTOS trial (Ridker et al., NEJM 2017) demonstrated that reducing inflammation with canakinumab reduced cardiovascular events — validating hs-CRP as a causal, not merely associative, marker
- **Reference:** Ridker PM et al., *New England Journal of Medicine*, 2017

---

## 💓 Vascular Age Calculation

Vascular Age represents the **biological age of the cardiovascular system** — often significantly higher than chronological age in high-risk patients.

```
Vascular Age = Chronological Age
             + (SBP − 120) × 0.1     [if SBP > 120 mmHg]
             + 8 years                [if current smoker]
             + 6 years                [if diabetes mellitus]
```

### Clinical Example

| Parameter | Value |
|---|---|
| Chronological Age | 45 years |
| Systolic BP | 140 mmHg |
| Smoker | Yes |
| Diabetes | Yes |
| **Vascular Age** | **45 + (140−120)×0.1 + 8 + 6 = 61 years** |

This 16-year discrepancy between chronological and vascular age is a powerful communication tool for patient engagement.

---

## ⚖️ South Asian–Specific Thresholds

### BMI Classification

| BMI Range | Standard | South Asian (CalciTrack) |
|---|:---:|:---:|
| Underweight | < 18.5 | < 18.5 |
| Normal | 18.5 – 24.9 | 18.5 – 22.9 |
| Overweight | 25.0 – 29.9 | 23.0 – 24.9 |
| Obese | ≥ 30.0 | **≥ 25.0** |

*Reference: WHO Expert Consultation, Lancet 2004; WHO Asia-Pacific Guidelines*

### Waist Circumference Risk Thresholds

| Sex | Standard (IDF) | South Asian (CalciTrack) |
|---|:---:|:---:|
| Male | > 102 cm | **> 90 cm** |
| Female | > 88 cm | **> 80 cm** |

*Reference: IDF Consensus Statement on Metabolic Syndrome, 2006*

---

## 📅 Follow-Up Scheduling

CalciTrack auto-generates the recommended next screening date based on the risk tier at the time of assessment:

| Risk Tier | Follow-Up Interval | Rationale |
|---|:---:|---|
| LOW | 3–5 years | Stable low-risk · Lifestyle focus |
| INTERMEDIATE | 1 year | Annual reassessment · Await CAC result |
| HIGH | 3–6 months | Active management · Treatment response monitoring |
| HIGH (UPGRADED) | Immediate + 3 months | Critical markers · Urgent referral |

---

## 🔁 Life's Essential 8 — AHA Health Checklist

CalciTrack integrates the AHA Life's Essential 8 framework with 8 interactive sliders, each scored 0–100:

| Metric | Poor (0–49) | Intermediate (50–74) | Optimal (75–100) |
|---|---|---|---|
| Diet | Poor dietary choices | Some healthy choices | Mediterranean/DASH adherence |
| Physical Activity | < 150 min/week | 150 min/week | > 150 min vigorous/week |
| Nicotine | Current smoker | Former smoker | Never / >5yr cessation |
| Sleep | < 6 hrs or > 9 hrs | 6–7 hrs or 9 hrs | 7–9 hours |
| Weight (BMI) | Obese | Overweight | Normal range |
| Cholesterol | High LDL untreated | Borderline | Optimal with/without treatment |
| Blood Glucose | Diabetic | Prediabetic | Normal |
| Blood Pressure | ≥ 140/90 | 120–139/80–89 | < 120/80 |

*Reference: Lloyd-Jones DM et al., Circulation, 2022*

---

*Part of the CalciTrack Wiki · [← Back to Home](Home)*

---

<div align="center">

**CalciTrack** · *Redefining Early Cardiovascular Risk Detection*

Invented by **Sai Keerthana Cherukuri** · MS4 Clinical Innovation Project

*Detect Early · Stratify Precisely · Prevent Effectively*

</div>
