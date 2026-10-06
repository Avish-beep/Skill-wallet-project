# Data Validation & Integrity Audit Report
## Epic 1: Data Collection & Extraction from Database

**Evaluation Date:** October 06, 2026  
**Auditor:** Antigravity Autonomous Development Agent  
**Tool:** `scripts/inspect_dataset.py` (Python 3.11 / Pandas 3.0.6)  

---

### 1. Schema Validation against SkillWallet Specification (18 Fields)

| # | Expected SkillWallet Field | Status in Ingested Baseline | Actual Column Name | Discrepancy / Alignment Notes |
| :-: | :--- | :--- | :--- | :--- |
| **1** | `User ID` | **MISSING** | — | Unique user identifier absent in raw survey; synthetic key required if using Candidate B. |
| **2** | `Age` | **FOUND EXACT** | `Age` | Integer values ranging from 18 to 24 years. |
| **3** | `Gender` | **PRESENT (VARIANT)** | `Choose your gender` | Binary categories (`Female`, `Male`). |
| **4** | `Occupation` | **MISSING** | `What is your course?` | Major/degree recorded rather than professional occupation. |
| **5** | `Stress Level` | **MISSING** | — | No Likert stress scale; panic attack acts as behavioral stress proxy. |
| **6** | `Anxiety Score` | **PRESENT (VARIANT)** | `Do you have Anxiety?` | Binary indicator (`Yes`/`No`) rather than continuous clinical score. |
| **7** | `Depression Score` | **PRESENT (VARIANT)** | `Do you have Depression?` | Binary indicator (`Yes`/`No`) rather than continuous clinical score. |
| **8** | `Sleep Quality` | **MISSING** | — | Sleep quality variable not captured in baseline survey. |
| **9** | `Daily Screen Time (hrs)`| **MISSING** | — | Daily screen time not captured in baseline survey. |
| **10**| `Physical Activity Level`| **MISSING** | — | Exercise/physical activity not captured in baseline survey. |
| **11**| `Social Interaction Score`| **MISSING**| — | Interpersonal engagement score not captured in baseline survey. |
| **12**| `Mental Health History` | **MISSING** | — | Longitudinal history not captured in baseline survey. |
| **13**| `Therapy Type` | **MISSING** | — | Specific therapeutic modality (CBT, counseling) not captured. |
| **14**| `Intervention Duration (weeks)`| **MISSING**| — | Intervention duration not captured in baseline survey. |
| **15**| `Progress Score` | **MISSING** | — | Clinical progress score not captured in baseline survey. |
| **16**| `Medication Usage` | **MISSING** | — | Pharmacotherapy usage not captured in baseline survey. |
| **17**| `Support System Strength` | **MISSING** | — | Social support strength not captured in baseline survey. |
| **18**| `Work-Life Balance Score` | **MISSING** | — | Work-life balance score not captured in baseline survey. |

---

### 2. Empirical Data Quality Metrics (Baseline Dataset)

| Quality Dimension | Measured Value | Threshold / Tolerance | Quality Status |
| :--- | :--- | :--- | :--- |
| **Total Rows** | 101 records | &ge; 100 records | **PASS** |
| **Duplicate Complete Rows** | 0 duplicates (0.0%) | 0 duplicates | **PASS** |
| **Missing Values (Age)** | 1 record (row index 43, 0.99%) | < 5% | **FLAGGED (Resolved by median imputation)** |
| **Missing Values (Other)** | 0 records across 10 columns | 0% | **PASS** |
| **Invalid Ages** | Min: 18, Max: 24 (Mean: 20.53) | 16–100 years | **PASS** |
| **String Inconsistencies** | Mixed casing in `year_of_study` | Strict case uniformity | **FLAGGED (Requires standard title casing)** |
| **Whitespace Inconsistencies**| Trailing spaces in `cgpa_range` | Zero trailing spaces | **FLAGGED (Requires string strip)** |

---

### 3. Conclusion & Recommendation
The baseline survey provides a functional preliminary dataset for academic exploratory analysis, but only directly matches 1 of the 18 expected SkillWallet clinical fields. To fulfill the SkillWallet subtask without ambiguity, the official dataset file attached to the SkillWallet task card should be downloaded into `data/raw/` and validated.
