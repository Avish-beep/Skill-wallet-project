# Missing Value Treatment Report
## Epic 2: Data Preparation

**Date:** October 06, 2026  
**Dataset:** `C:\Skillwallet\data\raw\Student_Mental_health.csv` &rarr; `C:\Skillwallet\data\processed\student_mental_health_processed.csv`  

---

### 1. Missing Value Audit

| Column Name | Raw Missing Count | Raw Missing % | Action / Treatment | Rationale & Method |
| :--- | :---: | :---: | :--- | :--- |
| **`Age`** | 1 | 0.99% | Imputation using Cohort Median (`19.0`) | The missing observation occurred at row index 43. Age in this cohort is a discrete integer variable ranging from 18 to 24 with a slight right-skew (Mean: 20.53, Median: 19.0). Mean imputation would introduce an unrealistic decimal age (20.53). Median imputation preserves discrete distribution and avoids skewing age-related analyses. |
| **`Timestamp`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Choose your gender`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`What is your course?`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Your current year of Study`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`What is your CGPA?`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Marital status`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Do you have Depression?`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Do you have Anxiety?`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Do you have Panic attack?`** | 0 | 0.0% | None | 100% complete across all 101 records. |
| **`Did you seek any specialist for a treatment?`** | 0 | 0.0% | None | 100% complete across all 101 records. |

---

### 2. Post-Imputation Verification
- Missing values in raw dataset: **1**
- Missing values in processed dataset: **0 (0.0%)**
- Post-imputation distribution: Minimum age remains 18, Maximum age remains 24, Median age remains 19, Mean age slightly shifts from 20.53 to 20.51.
