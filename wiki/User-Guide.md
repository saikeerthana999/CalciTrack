# User Guide — Step-by-Step Clinical Walkthrough

> **For Clinicians, Community Health Workers, and Medical Students**

---

## Who Is This Tool For?

CalciTrack is designed for:
- **Primary care physicians** conducting preventive cardiology consultations
- **Community health workers** running mobile screening camps
- **Medical students and residents** learning cardiovascular risk assessment
- **Cardiologists** triaging patients for advanced workup

---

## Before You Begin

**What you need for a full screening:**
- Patient's age and biological sex
- Systolic blood pressure (mmHg)
- Smoking / tobacco status
- Diabetes status
- Family history of premature CAD (optional)
- Lp(a) and hs-CRP lab values (optional but recommended)

**Minimum required:** Age, sex, SBP — everything else adds precision.

---

## Step 1 — Screening

This is the core screening interface.

### How to use:
1. Select a **language** from the sidebar (English, Hindi, Telugu, Tamil)
2. Enter the **patient name** and basic demographics
3. Select **biological sex**
4. Enter **systolic blood pressure**
5. Check all applicable **risk factors** (smoking, diabetes, family history)
6. Check all applicable **risk enhancers** (preeclampsia, GDM, PCOS, etc.)
7. Enter **Lp(a) value** (mg/dL) if available — leave at 0 if not
8. Enter **hs-CRP value** (mg/L) if available — leave at 0 if not
9. Click **"Calculate Risk"**

### What you get:
- **10-year cardiovascular risk %**
- **Visual risk gauge** — colour-coded speedometer
- **Risk tier** — LOW / INTERMEDIATE / HIGH / HIGH (UPGRADED)
- **Clinical impression** — narrative triage recommendation
- **Vascular Age**
- **Follow-up scheduling** — next recommended screening date
- **Heart Health Summary Certificate** — printable PDF
- **WhatsApp Referral** — pre-filled specialist referral message

### Understanding the Upgrade:
If Lp(a) >50 or hs-CRP ≥2.0 AND the patient is INTERMEDIATE — the result will show **HIGH (UPGRADED)** with a critical flag. This requires immediate clinical action.

---

## Step 2 — What-If Analysis

Shows the patient what their risk profile *could* look like with lifestyle optimisation.

### How to use:
1. View the side-by-side comparison:
   - **Current Vascular Age** vs **Optimised Vascular Age**
2. Use the **Life's Essential 8 checklist** — 8 sliders for:
   - Diet, Physical Activity, Nicotine, Sleep, Weight, Cholesterol, Blood Glucose, Blood Pressure
3. Each slider generates a 0–100 composite health score
4. Read the lifestyle optimisation tips at the bottom

### Clinical use:
Use this during the consultation to show the patient the concrete impact of lifestyle changes — e.g., "If you quit smoking and control your BP, your vascular age would be 8 years younger."

---

## Step 3 — Impact Simulator

Allows you to set specific, achievable goals and simulate their effect.

### How to use:
1. Use the **sidebar controls** to set goals:
   - Target systolic BP
   - Quit smoking (yes/no)
   - Manage diabetes (yes/no)
2. The screen shows:
   - **Current risk gauge** (left)
   - **Projected risk gauge** after achieving goals (right)
   - **Risk reduction %**

### Clinical use:
Excellent for motivational interviewing — showing a patient visually how much their risk drops with specific, achievable interventions.

---

## Step 4 — Clinician Dashboard

Designed for **camp-style multi-patient screenings**.

### Features:
- **Session patient table** — all patients screened in this session
- **Summary metrics** — total screened, high-risk count, average risk %
- **Bar charts:**
  - Risk tier distribution (LOW / INTERMEDIATE / HIGH)
  - Age group breakdown
  - Gender breakdown
- **CSV Export** — download all session data for records or referral

### Clinical use:
Run a community cardiac camp, screen 20–30 patients, and at the end export the full session data with risk profiles for follow-up and referral coordination.

---

## Step 5 — Education & Diet Guide

**Patient-facing** educational content.

### Patient Education Cards (expandable):
- **What is Lp(a)?** — Plain language explanation
- **What is hs-CRP?** — Inflammation and heart risk
- **What is Vascular Age?** — Why your heart may be older than you
- **What is a CAC Score?** — Coronary Artery Calcium scoring explained
- **What is ASCVD Risk?** — 10-year risk explained simply

### South Asian Diet Guide:
- **Smart food swaps** — Ghee → Olive oil, White rice → Millets, etc.
- **Heart-protective protein sources**
- **The Indian Heart Plate** — proportion model
- **Heart-protective spices** — Turmeric, Ginger, Garlic, Fenugreek

---

## Step 6 — BMI Calculator

Uses **South Asian–specific thresholds**.

### How to use:
1. Enter weight (kg), height (cm), waist circumference (cm), sex
2. Click **Calculate BMI**
3. View:
   - BMI value with South Asian category
   - Waist circumference risk assessment (Men >90cm / Women >80cm)
   - Comparison table: Standard vs South Asian thresholds

---

## Step 7 — Methodology (📐)

A **clinical and conference reference tab** containing:
- The full mathematical formula with visual breakdown
- Risk stratification pyramid
- Lp(a)/hs-CRP decision tree
- South Asian lens comparison
- Vascular age walkthrough
- 6-step workflow pipeline
- Evidence base table

Use this tab when **presenting to doctors, researchers, or conference panels** — it provides a complete, visual walkthrough of the clinical logic.

---

## Demo Mode

CalciTrack includes **18 pre-built clinical demo cases** for training and presentations:

| # | Case | Key Feature |
|---|---|---|
| 1 | Young Male Smoker | Elevated risk from smoking modifier |
| 2 | Female Post-Preeclampsia | Female enhancer pathway |
| 3 | Young Genetic Risk | Family history + South Asian modifier |
| 4 | High Risk Elderly (CKD) | CKD enhancer + age |
| 5 | Metabolic Trio | Smoker + Diabetes combination |
| 6 | Low Risk Young Female | PCOS only — near-baseline |
| 7 | Early Menopause | Female-specific menopause enhancer |
| ... | + 11 more | Various clinical presentations |

Select a demo case from the sidebar to auto-populate the form.

---

*Part of the CalciTrack Wiki · [← Back to Home](Home)*

---

<div align="center">

**CalciTrack** · *Redefining Early Cardiovascular Risk Detection*

Invented by **Sai Keerthana Cherukuri** · MS4 Clinical Innovation Project

*Detect Early · Stratify Precisely · Prevent Effectively*

</div>
