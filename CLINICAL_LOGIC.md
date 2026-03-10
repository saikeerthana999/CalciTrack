# Clinical Logic: The CalciTrack Precision Engine

### **Motto: Care Ever, Neglect Never**
### *Start Early, Drive Slowly, Reach Safely*

As the inventor of CalciTrack, I designed this tool to address a specific clinical failure: underestimating cardiovascular risk in South Asian populations. This document outlines the logic I coded into the tool to move beyond standard ASCVD (Atherosclerotic Cardiovascular Disease) scoring.

---

## 1. The South Asian Adjustment (Ethnicity Multiplier)
Most global calculators (like the PCE) are derived from cohorts that do not reflect the Asian Indian phenotype. In my tool, I apply a **1.5x to 2.0x risk multiplier** for South Asian patients, as recommended by the AHA/ACC guidelines for "Risk Enhancing Factors."

* **BMI Threshold:** While the global "overweight" cutoff is $25\text{ kg/m}^2$, I have recalibrated CalciTrack to flag risk at **$23\text{ kg/m}^2$**, reflecting the increased visceral adiposity seen in our community at lower weights.

---

## 2. The Precision Reclassification (The "Upgrade" Logic)
This is the core of the "Drive Slowly" philosophy. Instead of rushing to a binary "High" or "Low" risk, I use specific biomarkers to reclassify patients who fall into the "Intermediate Risk" (5%–7.5%) category.

### **A. Lipoprotein(a) [$Lp(a)$]**
$Lp(a)$ is a genetically determined risk factor that is highly prevalent in South Asians and is not affected by diet or exercise.
* **Logic:** If $Lp(a) > 50\text{ mg/dL}$ (or $> 125\text{ nmol/L}$), the patient is "upgraded" to a higher risk tier.
* **Clinical Impact:** This identifies "silent" genetic risk that standard cholesterol tests miss.

### **B. High-Sensitivity C-Reactive Protein [$hs-CRP$]**
$hs-CRP$ is a marker of systemic inflammation, a key driver of plaque instability.
* **Logic:** If $hs-CRP \ge 2.0\text{ nmol/L}$, it indicates an inflammatory "enhancer."
* **Clinical Impact:** This signals that the patient needs more aggressive preventative measures, even if their LDL appears "normal."

---

## 3. Female-Specific Risk Enhancers
Standard calculators often overlook obstetric and gynecological history. I have ensured CalciTrack asks the questions big hospitals often forget:
* **Preeclampsia/Gestational Diabetes:** History of these conditions doubles long-term CVD risk.
* **PCOS:** Linked to early-onset metabolic syndrome.
* **Early Menopause:** A recognized risk enhancer in my algorithm.

---

##  4. The Triage Output (The "Reach Safely" Protocol)
The tool does not just give a number; it provides a destination.

| Risk Score | Action Level | Referral Protocol |
| :--- | :--- | :--- |
| **Low (<5%)** | Lifestyle Focus | Re-screen in 12 months. |
| **Intermediate (5-7.5%)** | Biomarker Check | Order $Lp(a)$ and $hs-CRP$ for reclassification. |
| **High (>7.5%)** | Specialist Triage | Immediate WhatsApp referral to a cardiologist. |
---

## How I Coded This
The logic is implemented in Python, using a modular approach that enables easy updates as new clinical trials (such as those for $Lp(a)$ inhibitors) are published. By keeping the code open-source, I am ensuring that this precision is **affordable and available** to any health worker with a smartphone.

**Inventor:** **Sai Keerthana Cherukuri** (MS4)

```mermaid
graph TD
    %% Node Definitions
    A[Patient Intake]:::input
    B{Standard ASCVD Scoring}:::decision
    C[Calculate Base Risk %]:::process
    D[Apply South Asian Multiplier]:::process
    E{BMI Check}:::decision
    F[Increase Risk Category]:::process
    G[Maintain Risk Category]:::process
    H{Precision Markers?}:::decision
    I[Evaluate Lp-a & hs-CRP]:::process
    J[PRECISION UPGRADE]:::highrisk
    K[Final Risk Triage]:::process
    L[Automated Referral / WhatsApp]:::output

    %% Relationships
    A --> B
    B --> C
    C --> D
    D --> E
    E -- "BMI >= 23" --> F
    E -- "BMI < 23" --> G
    F --> H
    G --> H
    H -- Yes --> I
    I -- Positive --> J
    I -- Negative --> K
    H -- No --> K
    J --> L
    K --> L

    %% Styling Classes
    classDef input fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef process fill:#f5f5f5,stroke:#616161,stroke-width:1px;
    classDef highrisk fill:#ffcdd2,stroke:#c62828,stroke-width:2px,stroke-dasharray: 5 5;
    classDef output fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px;
