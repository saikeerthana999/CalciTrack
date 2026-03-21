# Evidence Base & Scientific Citations

**CalciTrack — Guideline Mapping and Scientific Foundation**

[← Back to Home](Home)

Every clinical decision, threshold, and algorithm in CalciTrack is grounded in peer-reviewed evidence and international cardiovascular guidelines. This page maps each guideline to its specific application in the tool.

---

## Core Clinical Guidelines

### AHA/ACC 2019 Guideline on Primary Prevention of Cardiovascular Disease

**Citation:** Arnett DK, Blumenthal RS, Albert MA, et al. *2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease*. Circulation. 2019;140(11):e596–e646.

**How it is applied in CalciTrack:**
- Provides the core ASCVD risk stratification framework — LOW, INTERMEDIATE, and HIGH categories
- Defines statin initiation thresholds and intensity recommendations used in triage output
- Establishes the risk-enhancing factors framework — the basis for the +5.0 enhancer scoring
- Defines the intermediate-risk precision marker assessment pathway using Lp(a), hs-CRP, and CAC
- Aligns with the Life's Essential 8 health metrics checklist

---

### CSI Consensus Statement — South Asian Cardiovascular Risk

**Citation:** Enas EA, Mehta J, et al. *Cardiological Society of India Consensus Statement on Management of Dyslipidemia in Indians*. Indian Heart Journal. 2020.

**How it is applied in CalciTrack:**
- Provides the South Asian ethnicity modifier of +2.0 added to the base risk score
- Documents the 5–10 year earlier onset of CAD in South Asian populations
- Establishes the population context for why standard Western calculators underestimate risk
- Informs South Asian–specific lipid management thresholds referenced in clinical output

---

## Precision Biomarker Evidence

### Lp(a) as a Cardiovascular Risk Enhancer

**Citation:** Wilson DP, Jacobson TA, Jones PH, et al. *Use of Lipoprotein(a) in clinical practice: A biomarker whose time has come*. Journal of Clinical Lipidology. 2022.

**Key findings:**
- Lp(a) above 50 mg/dL independently predicts ASCVD events — over and above all other conventional risk factors
- Lp(a) is driven almost entirely by genetic factors and cannot be reduced by diet or conventional statins
- Promotes oxidised phospholipid–mediated plaque formation and thrombosis — two independent mechanisms
- Should prompt reclassification to a higher risk tier in patients who score in the intermediate category
- Particularly prevalent in South Asian populations and frequently undiagnosed

**How it is applied in CalciTrack:**
- Lp(a) above 50 mg/dL triggers automatic INTERMEDIATE → HIGH (UPGRADED) reclassification
- Qualitative checkbox option adds +5.0 when exact value is unavailable
- Numeric lab input enables precise quantitative upgrade
- Lp(a) value and the upgrade flag are printed on the PDF clinical report

---

### hs-CRP and Vascular Inflammation — The CANTOS Trial

**Citation:** Ridker PM, Everett BM, Thuren T, et al. *Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease*. New England Journal of Medicine. 2017;377:1119–1131.

**Key findings:**
- Patients with hs-CRP at or above 2.0 mg/L had significantly elevated cardiovascular event rates
- Anti-inflammatory therapy reduced major adverse cardiac events — independent of lipid lowering
- Established vascular inflammation as a **causal** pathway to cardiac events, not merely an association
- Validates hs-CRP at or above 2.0 mg/L as a clinical threshold for escalating cardiovascular treatment

**How it is applied in CalciTrack:**
- hs-CRP at or above 2.0 mg/L triggers INTERMEDIATE → HIGH (UPGRADED) reclassification
- Numeric lab input for precision triage
- CANTOS evidence cited in the clinical report output
- Informs the recommendation for anti-inflammatory considerations in upgraded-risk patients

---

## South Asian Anthropometric Thresholds

### WHO Asia-Pacific BMI Guidelines

**Citation:** WHO Expert Consultation. *Appropriate body-mass index for Asian populations and its implications for policy and intervention strategies*. Lancet. 2004;363(9403):157–163.

**Key findings:**
- South and Southeast Asian populations develop obesity-related comorbidities at lower BMI than European populations
- The mechanism is body composition — South Asians carry more visceral fat and less muscle mass at equivalent BMI
- Visceral fat is metabolically active, driving insulin resistance and inflammation more aggressively than subcutaneous fat
- Recommended action points for Asian populations: overweight at 23 kg/m² or above, obese at 27.5 kg/m² or above

**How it is applied in CalciTrack:**
- BMI Calculator uses South Asian–adjusted thresholds: Normal below 23, Overweight 23–24.9, Obese 25 or above
- Clinically pragmatic thresholds used rather than the 27.5 cut-off to align with cardiovascular practice guidelines

---

### IDF South Asian Waist Circumference Criteria

**Citation:** International Diabetes Federation. *The IDF Consensus Worldwide Definition of the Metabolic Syndrome*. Brussels: IDF. 2006.

**Key findings:**
- South Asian–specific waist thresholds: Men above 90 cm, Women above 80 cm
- Significantly lower than European criteria (Men above 102 cm, Women above 88 cm)
- Central obesity in South Asians carries substantially higher cardiometabolic risk at smaller waist sizes
- These thresholds are the basis for metabolic syndrome diagnosis in South Asian clinical practice

**How it is applied in CalciTrack:**
- Waist circumference risk assessment in the BMI Calculator uses South Asian thresholds
- Side-by-side comparison table shows Standard vs South Asian thresholds for patient education

---

## Vascular Age Framework

### Vascular Age and Cardiovascular Risk Communication

**Citation:** Grover SA, Lowensteyn I, Joseph L, et al. *Patient Knowledge of Coronary Risk Profile Improves the Effectiveness of Dyslipidemia Therapy*. Archives of Internal Medicine. 2007.

**Key findings:**
- Communicating cardiovascular risk as a biological age — rather than an abstract percentage — significantly improves patient engagement and treatment adherence
- Vascular age framing produces stronger motivation for lifestyle modification than numerical risk alone
- Particularly effective for patients with limited health literacy

**How it is applied in CalciTrack:**
- Vascular Age is calculated using SBP, smoking status, and diabetes as additive modifiers
- Displayed alongside the 10-year risk percentage in Step 1 (Screening)
- Used in Step 2 (What-If Analysis) to show current vs optimised vascular age side by side
- The gap between chronological age and vascular age is the primary patient motivation message

---

## Life's Essential 8

### AHA Life's Essential 8 Framework

**Citation:** Lloyd-Jones DM, Allen NB, Anderson CAM, et al. *Life's Essential 8: Updating and Enhancing the American Heart Association's Cardiovascular Health Score*. Circulation. 2022;146(5):e18–e43.

**Key findings:**
- Eight modifiable health metrics account for the majority of cardiovascular health variance
- Composite scoring across all 8 metrics identifies areas of highest impact for individual patients
- Interactive self-assessment improves patient engagement with preventive care

**How it is applied in CalciTrack:**
- Step 2 includes an interactive Life's Essential 8 checklist with 8 sliders
- Each slider scored 0–100 and combined into a composite health score
- Results guide personalized counselling priorities

---

## Evidence Summary Map

| CalciTrack Feature | Evidence Source | Year |
|---|---|:---:|
| ASCVD Risk Framework | AHA/ACC Primary Prevention Guidelines | 2019 |
| South Asian Risk Modifier (+2.0) | CSI Consensus Statement | 2020 |
| Lp(a) Upgrade Rule (above 50 mg/dL) | Wilson DP et al., J Clin Lipidol | 2022 |
| hs-CRP Upgrade Rule (above 2.0 mg/L) | Ridker PM — CANTOS Trial, NEJM | 2017 |
| South Asian BMI Thresholds | WHO Asia-Pacific Expert Consultation | 2004 |
| Waist Circumference Cutoffs | IDF Consensus — Metabolic Syndrome | 2006 |
| Life's Essential 8 | AHA — Lloyd-Jones DM, Circulation | 2022 |
| Vascular Age Communication | Grover SA et al., Arch Intern Med | 2007 |

---

[← Back to Home](Home) | [User Guide →](User-Guide)

---

*CalciTrack · Detect Early · Stratify Precisely · Prevent Effectively*
*Invented by Sai Keerthana Cherukuri · MS4 Clinical Innovation Project*
