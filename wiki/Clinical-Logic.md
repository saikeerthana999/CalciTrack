# Clinical Logic & Algorithm

**CalciTrack — Technical Reference for Clinicians and Evaluators**

[← Back to Home](Home)

---

## The Risk Scoring Formula

CalciTrack computes a **10-year cardiovascular risk percentage** using a weighted additive model adjusted for South Asian population characteristics. The formula builds in five layers — each adding precision.

---

### Layer 1 — Base Score

```
Base Score = (Age × 0.15) + (Systolic Blood Pressure × 0.06)
```

| Variable | Coefficient | Clinical Rationale |
|---|:---:|---|
| Age | × 0.15 | Each year of life accumulates vascular wear — linear age-risk relationship across adult decades |
| Systolic BP | × 0.06 | Each 10 mmHg above optimal increases arterial wall stress and plaque progression risk |

The base score alone accounts for the two most consistent, time-dependent predictors of cardiovascular events.

---

### Layer 2 — Demographic Modifiers

| Modifier | Points Added | Clinical Rationale |
|---|:---:|---|
| Male sex | +2.0 | Men develop CAD approximately 7–10 years earlier than women. Oestrogen provides partial cardioprotection in premenopausal women. |
| South Asian / Indian ethnicity | +2.0 | CSI Consensus 2020 — South Asians develop premature CAD 5–10 years earlier and have higher rates of insulin resistance and dyslipidaemia at equivalent BMI. |
| African / African American | +1.5 | Higher rates of hypertension-related cardiac disease and baseline cardiovascular risk at equivalent BP levels. |

---

### Layer 3 — Major Clinical Risk Factors

| Risk Factor | Points Added | Clinical Rationale |
|---|:---:|---|
| Current smoker or tobacco | +7.0 | Smoking directly injures vascular endothelium, accelerates atherosclerosis, promotes thrombosis, and lowers HDL. Approximately 2–4x relative risk increase. |
| Diabetes mellitus | +8.0 | Treated as a CAD-risk equivalent in international guidelines — a diabetic patient without prior heart disease carries the same event risk as someone who has already had a myocardial infarction. |

---

### Layer 4 — Risk Enhancers (+5.0 each)

Each of the following adds 5.0 points to the total score.

**Female-Specific Enhancers**

| Enhancer | Why It Matters |
|---|---|
| Preeclampsia | Reflects underlying vascular vulnerability — 2x long-term stroke risk, 4x hypertension risk |
| Gestational Diabetes (GDM) | Marker of insulin resistance that often persists post-pregnancy — 7x risk of developing Type 2 diabetes |
| Early Menopause (before age 40) | Premature loss of oestrogen's cardioprotective effect — accelerated cardiovascular ageing |
| PCOS | Associated with insulin resistance, central obesity, dyslipidaemia, and chronic low-grade inflammation |

**General Enhancers**

| Enhancer | Why It Matters |
|---|---|
| Family history of premature CAD | First-degree relative with CAD before age 55 (male) or 65 (female) — suggests shared genetic vulnerability |
| Chronic Kidney Disease (CKD) | Accelerates vascular calcification, promotes anaemia and renin-angiotensin activation — a heart-kidney cycle |
| Metabolic Syndrome | Three or more of: central obesity, high triglycerides, low HDL, elevated BP, elevated glucose — doubles event risk |
| Elevated Lp(a) (qualitative checkbox) | Genetic cholesterol driver that statins cannot reduce — adds score when exact value is unavailable |
| Elevated hs-CRP (qualitative checkbox) | Marker of vascular inflammation — adds score when lab value is not available |

---

### Layer 5 — Final Risk Calculation

```
Total Score = Base Score + Demographic Modifiers + Clinical Factors + Enhancers

Risk %      = clamp( (Total Score ÷ 1.5) × 1.1,  minimum 1.2%,  maximum 50.0% )
```

**Why divide by 1.5?**
Converts the raw weighted score into a percentage range that aligns with published 10-year ASCVD data from the ACC/AHA Pooled Cohort Equations.

**Why multiply by 1.1?**
A 10% upward correction accounts for the documented systematic underestimation of risk in South Asian populations when standard Western calculators are applied.

**Why clamp at 1.2% and 50%?**
No living adult has zero cardiovascular risk — 1.2% represents the biological floor. Above 50%, the clinical action is identical regardless of the precise number, so reporting beyond this ceiling adds no clinical utility.

---

### Worked Example

**Patient:** 52-year-old South Asian woman · SBP 142 · Smoker · PCOS · No diabetes

| Component | Calculation | Score |
|---|---|:---:|
| Age | 52 × 0.15 | 7.8 |
| SBP | 142 × 0.06 | 8.52 |
| South Asian | Fixed modifier | +2.0 |
| Smoker | Fixed modifier | +7.0 |
| PCOS | Enhancer | +5.0 |
| **Total** | | **30.32** |
| **Risk %** | (30.32 ÷ 1.5) × 1.1 | **~22.2%** |
| **Category** | 19.9% or above | **HIGH RISK** |

---

## Risk Stratification

| 10-Year Risk % | Category | Clinical Decision | Follow-Up |
|---|:---:|---|:---:|
| Below 5.0% | LOW | Lifestyle counselling · Life's Essential 8 · Dietary guidance | 3–5 years |
| 5.0 – 19.9% | INTERMEDIATE | CAC Scoring (Agatston) · Check Lp(a) and hs-CRP quantitatively | 1 year |
| 19.9% or above | HIGH | High-intensity statin · Specialist referral · Possible stress testing | 3–6 months |
| INTERMEDIATE + Lp(a) above 50 or hs-CRP above 2.0 | HIGH (UPGRADED) | Aggressive LDL-C lowering · Stress testing · CRITICAL flag on report | Immediate |

---

## Precision Marker Reclassification — The Upgrade Rule

This is the central clinical innovation in CalciTrack's triage logic.

```
IF   patient_risk_tier == INTERMEDIATE
AND  ( Lp(a) > 50 mg/dL  OR  hs-CRP >= 2.0 mg/L )
THEN reclassify  →  HIGH (UPGRADED)
     flag        →  "CRITICAL: Risk upgraded due to genetic or inflammatory markers"
     recommend   →  High-intensity statin + Specialist Referral + Stress Testing
```

**Why Lp(a) matters:**
Lp(a) is genetically determined — it cannot be reduced by diet or conventional statins. Levels above 50 mg/dL independently predict atherosclerotic events and thrombosis. It is particularly elevated in South Asian populations and frequently undiagnosed because standard risk tools do not include it.

*Reference: Wilson DP et al., Journal of Clinical Lipidology, 2022*

**Why hs-CRP matters:**
hs-CRP reflects chronic, low-grade vascular inflammation — the kind that smoulders silently inside artery walls. Levels at or above 2.0 mg/L predict first myocardial infarction even in patients with normal LDL-C. The CANTOS trial established vascular inflammation as a causal — not merely associative — pathway to cardiac events.

*Reference: Ridker PM et al., New England Journal of Medicine, 2017*

**Two-level biomarker approach:**

- **Qualitative (checkboxes):** Clinicians who know a patient has elevated markers but lack exact values can check the qualitative boxes. Each adds +5.0 to the base score.
- **Quantitative (numeric values):** When actual lab values are entered, the upgrade rule fires independently — even if the checkboxes are not selected. This triggers reclassification from INTERMEDIATE to HIGH (UPGRADED).

---

## Vascular Age Calculation

Vascular Age represents the **biological age of the cardiovascular system** — often significantly higher than chronological age in patients with uncontrolled risk factors.

```
Vascular Age = Chronological Age
             + (SBP − 120) × 0.1     [only if SBP > 120 mmHg]
             + 8 years                [if current smoker]
             + 6 years                [if diabetes mellitus]
```

| Modifier | Points | Rationale |
|---|:---:|---|
| Blood pressure above 120 | (SBP − 120) × 0.1 | Each 10 mmHg above optimal = approximately 1 year of added vascular ageing |
| Current smoker | +8 years | Tobacco accelerates every dimension of vascular disease — endothelial injury, plaque formation, thrombosis |
| Diabetes mellitus | +6 years | Glycation, oxidative stress, and inflammation accelerate arterial stiffening by approximately 6 years |

**Example:** Age 45 · SBP 140 · Smoker · Diabetic
→ 45 + (140 − 120) × 0.1 + 8 + 6 = **61 years biological vascular age**

This 16-year gap between chronological and vascular age is one of the most powerful patient communication tools in preventive medicine.

---

## South Asian–Specific Thresholds

### BMI Classification

| BMI Range | Standard | South Asian (CalciTrack) |
|---|:---:|:---:|
| Underweight | Below 18.5 | Below 18.5 |
| Normal | 18.5 – 24.9 | 18.5 – 22.9 |
| Overweight | 25.0 – 29.9 | 23.0 – 24.9 |
| Obese | 30.0 or above | **25.0 or above** |

*Reference: WHO Expert Consultation, Lancet 2004*

### Waist Circumference Thresholds

| Sex | Standard (IDF) | South Asian (CalciTrack) |
|---|:---:|:---:|
| Male | above 102 cm | **above 90 cm** |
| Female | above 88 cm | **above 80 cm** |

*Reference: IDF Consensus Statement on Metabolic Syndrome, 2006*

South Asians accumulate dangerous visceral fat (fat around internal organs) at smaller waist sizes than Europeans. This visceral fat is metabolically active — it drives insulin resistance and inflammation far more aggressively than subcutaneous fat.

---

## Follow-Up Scheduling

CalciTrack auto-generates the recommended next screening date based on the risk tier at the time of assessment.

| Risk Tier | Follow-Up Interval | Rationale |
|---|:---:|---|
| LOW | 3–5 years | Stable low-risk · Lifestyle focus |
| INTERMEDIATE | 1 year | Annual reassessment · Await CAC result |
| HIGH | 3–6 months | Active management · Treatment response monitoring |
| HIGH (UPGRADED) | Immediate + 3 months | Critical markers · Urgent referral |

---

## Life's Essential 8 — AHA Health Checklist

CalciTrack integrates the AHA Life's Essential 8 framework with 8 interactive sliders, each scored 0–100.

| Metric | Poor (0–49) | Intermediate (50–74) | Optimal (75–100) |
|---|---|---|---|
| Diet | Poor choices | Some healthy choices | Mediterranean or DASH adherence |
| Physical Activity | Below 150 min per week | 150 min per week | Above 150 min vigorous per week |
| Nicotine | Current smoker | Former smoker | Never or above 5 years cessation |
| Sleep | Below 6 hrs or above 9 hrs | 6–7 hrs | 7–9 hours |
| Weight (BMI) | Obese | Overweight | Normal range |
| Cholesterol | High LDL untreated | Borderline | Optimal with or without treatment |
| Blood Glucose | Diabetic | Prediabetic | Normal |
| Blood Pressure | 140/90 or above | 120–139 / 80–89 | Below 120/80 |

*Reference: Lloyd-Jones DM et al., Circulation, 2022*

---

[← Back to Home](Home) | [Evidence Base →](Evidence-Base)

---

*CalciTrack · Detect Early · Stratify Precisely · Prevent Effectively*
*Invented by Sai Keerthana Cherukuri · MS4 Clinical Innovation Project*
