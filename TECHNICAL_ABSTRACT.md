# Technical Abstract: CalciTrack
### **Project Title:** CalciTrack: A Mobile Clinical Decision Support Engine for Precision Cardiovascular Triage in South Asian Populations
**Author:** Sai Keerthana Cherukuri (MS4)  
**Keywords:** `South Asian CVD` • `Precision Medicine` • `mHealth` • `Clinical Informatics`

---

## 1. The Problem: The Clinical Gap
South Asian populations carry a disproportionately high burden of **Atherosclerotic Cardiovascular Disease (ASCVD)**, often manifesting **5–10 years earlier** than in Western cohorts. 

> [!WARNING]
> **The Failure of Standard Models:** Current global risk calculators (PCE, SCORE) frequently underestimate this risk, failing to account for unique metabolic phenotypes and genetic markers like $Lp(a)$. This leads to missed early interventions and high-cost emergency room admissions.

---

## 2. The Solution: Innovation
**CalciTrack** is an open-source, mobile-optimized clinical engine designed to **"Democratize Precision Cardiology."** It shifts high-complexity screening from tertiary hospitals directly to the point-of-service—bringing the "Specialist Logic" to the patient's doorstep.

---

## 3. Technical Architecture: The Logic
The tool implements a multi-stage triage algorithm designed for the Indian phenotype:

### **A. Recalibration & Thresholds**
| Metric | Standard (Western) | CalciTrack (South Asian) |
| :--- | :--- | :--- |
| **Risk Multiplier** | 1.0x | **1.5x – 2.0x** |
| **BMI Overweight** | $25\text{ kg/m}^2$ | **$23\text{ kg/m}^2$** |

### **B. Precision Reclassification**
The engine automates "Upgrade" logic for intermediate-risk patients based on high-sensitivity biomarkers:
* **Lipoprotein(a):** Upgrade if $Lp(a) > 50\text{ mg/dL}$
* **Inflammation:** Upgrade if $hs\text{-}CRP \ge 2.0\text{ mg/L}$

### **C. Gender-Specific Logic**
Integrates Obstetric and Gynecological history as **hard-coded risk enhancers**:
* Preeclampsia / Eclampsia
* Gestational Diabetes Mellitus (GDM)
* Polycystic Ovary Syndrome (PCOS)

---

## 4. Philosophy: Start Early, Drive Slowly, Reach Safely
1.  **Start Early:** Decentralized screening enables detection in the 2nd and 3rd decades of life.
2.  **Drive Slowly:** Precision markers provide a definitive diagnosis, reducing "ER anxiety" and unnecessary hospital load.
3.  **Reach Safely:** Automated referral pipelines ensure patients reach specialized care before an acute event occurs.

---

## 5. Impact & Scalability
By treating **"Platform as a Product,"** CalciTrack is built for low-resource environments:
* **Affordable:** Zero-cost licensing for community health workers.
* **Portable:** Operates on low-end mobile hardware.
* **Accessible:** Multilingual interface for diverse regional deployment.

CalciTrack ensures that precision medicine is no longer a corporate luxury, but a community standard.
