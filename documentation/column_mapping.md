# Column Standardization & Mapping Matrix
## Epic 2: Data Preparation

This document records the exact column name transformations executed between the raw survey file and the processed Tableau-ready dataset.

| Original Column (Raw) | Processed Column Name | Transformation Reason |
| :--- | :--- | :--- |
| **`Timestamp`** | **`Timestamp`** | Retained as standard timestamp identifier. |
| **`Choose your gender`** | **`Gender`** | Converted long survey question wording into concise, industry-standard demographic dimension. |
| **`Age`** | **`Age`** | Retained standard column name; cast to integer post-imputation. |
| **`What is your course?`** | **`Course`** | Shortened question phrasing to clean categorical attribute; raw strings preserved in `Course_Raw`. |
| **`Your current year of Study`** | **`Year_of_Study`** | Converted spaced colloquial phrase into standardized snake_case identifier for Tableau pills. |
| **`What is your CGPA?`** | **`CGPA_Range`** | Clarified that values represent ordinal brackets rather than continuous GPAs. |
| **`Marital status`** | **`Marital_Status`** | Standardized spacing to snake_case. |
| **`Do you have Depression?`** | **`Depression`** | Shortened question prompt to clean binary condition name. |
| **`Do you have Anxiety?`** | **`Anxiety`** | Shortened question prompt to clean binary condition name. |
| **`Do you have Panic attack?`** | **`Panic_Attack`** | Shortened question prompt to clean binary condition name with uniform spacing. |
| **`Did you seek any specialist for a treatment?`** | **`Treatment_Sought`** | Condensed long survey question into clear, actionable behavioral healthcare dimension. |

---

### Additional Engineered Features Added
- `User_ID`: Anonymized primary key (`STD_0001` to `STD_0101`) for distinct counting.
- `Course_Raw`: Exact unmodified raw course strings for lineage audit.
- `Faculty`: Higher-level academic discipline grouping (7 faculties).
- `CGPA_Midpoint`: Continuous numeric proxy (1.00 to 3.75) for measure calculation in Tableau.
- `Age_Group`: Binned cohort (`18-20 (Underclassmen)`, `21-24 (Upperclassmen)`).
- `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`, `Treatment_Sought_Flag`: Binary integer flags (1/0).
- `Condition_Count`: Composite sum of conditions (0 to 3).
- `Mental_Health_Risk`: Clinical severity stratification (`Low Risk`, `Moderate Risk`, `High Risk`).
- `Treatment_Gap`: Categorical healthcare status relative to symptoms.
