# User Guide — Step-by-Step Clinical Walkthrough

**For Clinicians, Community Health Workers, and Medical Students**

[← Back to Home](Home)

---

## Who Is This Tool For?

CalciTrack is designed for use by:

- **Primary care physicians** conducting preventive cardiology consultations
- **Community health workers** running mobile cardiac screening camps
- **Medical students and residents** learning cardiovascular risk assessment
- **Cardiologists** triaging patients for advanced workup or specialist referral

---

## What You Need Before Starting

**Minimum required to run a screening:**
Age · Biological sex · Systolic blood pressure

**Additional inputs that add precision:**
Smoking status · Diabetes status · Family history of premature CAD · Risk enhancers (preeclampsia, GDM, PCOS, etc.) · Lp(a) lab value (mg/dL) · hs-CRP lab value (mg/L)

The more inputs provided, the more accurate and clinically meaningful the result. The tool is designed to be useful even with just the minimum — but lab values unlock the precision marker upgrade pathway.

---

## Step 1 — Screening

This is the core of CalciTrack. It takes patient data and produces a full triage assessment.

**How to use:**
1. Select a **language** from the sidebar — English, Hindi, Telugu, or Tamil
2. Enter the **patient name** and basic demographics
3. Select **biological sex**
4. Enter **systolic blood pressure** in mmHg
5. Check all applicable **risk factors** — smoking, diabetes, family history
6. Check all applicable **risk enhancers** — preeclampsia, GDM, PCOS, early menopause, CKD, metabolic syndrome
7. Enter **Lp(a) value** in mg/dL if available — leave at 0 if not
8. Enter **hs-CRP value** in mg/L if available — leave at 0 if not
9. Click **Calculate Risk**

**What the result gives you:**
- 10-year cardiovascular risk percentage
- Visual risk gauge — colour-coded speedometer
- Risk tier: LOW / INTERMEDIATE / HIGH / HIGH (UPGRADED)
- Clinical impression — a plain-language triage recommendation
- Vascular age — how old the patient's cardiovascular system is biologically
- Follow-up scheduling — the recommended next screening date
- Heart Health Summary Certificate — a downloadable PDF
- WhatsApp Referral — a pre-filled specialist referral message ready to send in one tap

**Understanding the precision upgrade:**
If Lp(a) is above 50 mg/dL or hs-CRP is at or above 2.0 mg/L, and the patient scores in the INTERMEDIATE tier, CalciTrack will automatically reclassify them as HIGH (UPGRADED) with a CRITICAL flag. This requires immediate clinical action — do not treat this result as intermediate.

---

## Step 2 — What-If Analysis

This step shows the patient what their risk profile could look like with lifestyle optimisation — turning a risk number into a conversation about change.

**How to use:**
1. View the side-by-side comparison of current vascular age vs optimised vascular age
2. Work through the **Life's Essential 8 checklist** — 8 sliders covering diet, physical activity, nicotine use, sleep, weight, cholesterol, blood glucose, and blood pressure
3. Each slider generates a 0–100 score; the composite shows the patient's overall cardiovascular health standing
4. Read the personalised lifestyle optimisation tips at the bottom

**How to use this clinically:**
Show the patient both vascular age figures during the consultation. The gap between them — measured in biological years — is the clearest way to communicate the impact of change. For example: "If you quit smoking and bring your blood pressure under 120, your vascular age would be 9 years younger than it is today."

---

## Step 3 — Impact Simulator

This step sets specific, measurable goals and simulates their effect on the patient's 10-year risk — in real time.

**How to use:**
1. Use the **sidebar controls** to set goals:
   - Target systolic blood pressure
   - Smoking cessation (toggle)
   - Diabetes management (toggle)
2. The screen displays two risk gauges side by side — current risk on the left, projected risk after achieving goals on the right
3. The risk reduction percentage is shown between the two gauges

**How to use this clinically:**
This is an ideal motivational interviewing tool. Rather than telling a patient to be healthier, you can show them: "Here is exactly how much your 10-year risk drops if you reach this blood pressure target." Concrete, visual, and personalised.

---

## Step 4 — Clinician Dashboard

Designed for **camp-style multi-patient screening environments** where many patients are assessed in a single session.

**What it shows:**
- Session patient table — every patient screened in this session with their name, age, sex, risk percentage, and tier
- Summary metrics — total screened, number in each risk tier, average risk percentage
- Bar charts — risk tier distribution, age group breakdown, gender breakdown
- CSV Export — download the complete session dataset for referral tracking and medical records

**How to use this clinically:**
At the end of a community cardiac camp, use this dashboard to identify how many patients require urgent referral, understand the risk profile of the community screened, and export a clean data file for follow-up coordination. The risk distribution chart gives you an at-a-glance summary of the camp's clinical yield.

---

## Step 5 — Education & Diet Guide

Patient-facing educational content designed to be shown directly during or after the consultation.

**Patient Education Cards** (each one expands on click):
- **What is Lp(a)?** — Explained as the genetic cholesterol that standard statins cannot touch
- **What is hs-CRP?** — Explained as the fire alarm for inflammation inside artery walls
- **What is Vascular Age?** — Why your heart may be biologically older than your birthday suggests
- **What is a CAC Score?** — How coronary artery calcium scoring reveals silent plaque
- **What is ASCVD Risk?** — Your personal 10-year cardiovascular weather forecast

**South Asian Diet Guide:**
- Smart food swaps — Ghee to olive oil, white rice to millets, maida to whole wheat atta, refined sugar to jaggery in moderation
- Heart-protective protein sources — Dal, legumes, nuts, and fish for non-vegetarians
- The Indian Heart Plate — a visual proportion model: half vegetables, a quarter whole grains, a quarter protein
- Heart-protective spices — Turmeric (anti-inflammatory), Ginger (reduces triglycerides), Garlic (lowers blood pressure), Fenugreek (improves insulin sensitivity)

---

## Step 6 — BMI Calculator

Uses South Asian–specific thresholds throughout — not the standard Western values.

**How to use:**
1. Enter weight (kg), height (cm), waist circumference (cm), and sex
2. Click Calculate BMI
3. View:
   - BMI value with South Asian category classification
   - Waist circumference risk assessment — Men above 90 cm or Women above 80 cm flags metabolic risk
   - Comparison table showing Standard vs South Asian thresholds side by side

**Why this matters:**
A South Asian patient with a BMI of 26 would be told "slightly overweight but not obese" by a standard calculator. CalciTrack correctly classifies them as obese — because the metabolic damage from visceral fat accumulation in a South Asian body begins at lower BMI. This changes dietary advice, monitoring frequency, and medication thresholds.

---

## Step 7 — Methodology Tab

A conference and clinical reference tab for presenting the tool to doctors, researchers, or evaluators.

**Contains:**
- The full mathematical formula with step-by-step visual breakdown
- Risk stratification pyramid
- Lp(a) and hs-CRP precision upgrade decision tree
- South Asian lens — standard vs CalciTrack thresholds comparison
- Vascular age calculation walkthrough
- 6-step workflow pipeline overview
- Evidence base summary table with citations

Use this tab when presenting CalciTrack at conferences, departmental meetings, or during clinical evaluation — it gives reviewers a complete, visual walkthrough of the clinical logic without requiring them to use the tool itself.

---

## Demo Mode

CalciTrack includes pre-built clinical demo cases for training, presentations, and demonstrations.

Select a demo case from the sidebar to auto-populate the form with a realistic patient profile. Each case is designed to illustrate a specific pathway through the tool — the South Asian modifier, the Lp(a) upgrade, female enhancers, or the high-risk pathway.

---

## Common Questions

**Can I use CalciTrack without lab values?**
Yes. Lp(a) and hs-CRP inputs default to 0 and are optional. The tool produces a valid risk score from age, sex, blood pressure, and clinical history alone. Lab values add precision — especially for patients in the intermediate range where the upgrade rule matters most.

**What if the patient score is borderline between tiers?**
CalciTrack applies the upgrade rule automatically when lab values are present. For borderline scores without lab values, the INTERMEDIATE result includes a recommendation to obtain Lp(a) and hs-CRP quantitatively before the next visit.

**Can the PDF report be shared directly?**
Yes. The Heart Health Summary Certificate is a formatted PDF that can be downloaded, printed, or emailed. It includes the patient name, risk percentage, tier, vascular age, key risk factors, triage recommendation, and the next screening date.

**Is the WhatsApp referral pre-filled?**
Yes. Clicking the WhatsApp referral button opens WhatsApp with a pre-written message containing the patient's risk result, tier, and clinical flag. The clinician only needs to select the recipient and send.

---

[← Back to Home](Home) | [← Clinical Logic](Clinical-Logic)

---

*CalciTrack · Detect Early · Stratify Precisely · Prevent Effectively*
*Invented by Sai Keerthana Cherukuri · MS4 Clinical Innovation Project*
