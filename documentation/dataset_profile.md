# Dataset Profile: Student Mental Health Ecosystem
## Epic 1 — Data Collection & Extraction from Database

---

### 1. Dataset Overview
This dataset contains empirical higher education survey responses capturing undergraduate demographics, academic standing, and mental health challenges. It was collected to investigate the intersection of academic pressure and student psychological well-being.

---

### 2. Source
- **Origin:** University survey repository (`Student_Mental_health.csv`).
- **Storage Location:** `C:\Skillwallet\data\raw\Student_Mental_health.csv`.
- **Ingestion Date:** October 2026.

---

### 3. Number of Records
- **Total Rows:** 101 student observations.

---

### 4. Number of Fields
- **Total Columns:** 11 raw survey fields.

---

### 5. Column Overview & Data Types
1. `Timestamp` (String / Object) — Submission timestamp.
2. `Choose your gender` (String / Categorical) — Student gender (`Female`, `Male`).
3. `Age` (Float64) — Student age in completed years.
4. `What is your course?` (String / Categorical) — Academic course or major (49 unique values).
5. `Your current year of Study` (String / Ordinal) — Class seniority (`year 1`, `year 2`, etc.).
6. `What is your CGPA?` (String / Ordinal) — Grade Point Average ranges (`0 - 1.99` to `3.50 - 4.00`).
7. `Marital status` (String / Binary) — Marital status (`No`, `Yes`).
8. `Do you have Depression?` (String / Binary) — Self-reported depression (`Yes`, `No`).
9. `Do you have Anxiety?` (String / Binary) — Self-reported anxiety (`No`, `Yes`).
10. `Do you have Panic attack?` (String / Binary) — Self-reported panic attacks (`Yes`, `No`).
11. `Did you seek any specialist for a treatment?` (String / Binary) — Care-seeking behavior (`No`, `Yes`).

---

### 6. Missing Values
- `Age`: 1 missing record (row index 43). Missing rate = 0.99%.
- All other 10 columns: 0 missing records (100% complete).

---

### 7. Duplicate Records
- Exactly 0 duplicate rows detected across all 11 columns.

---

### 8. Categorical Distributions
- **Gender:** Female: 75 (74.3%), Male: 26 (25.7%).
- **Marital Status:** Single/Unmarried: 85 (84.2%), Married: 16 (15.8%).
- **Depression Prevalence:** Yes: 35 (34.7%), No: 66 (65.3%).
- **Anxiety Prevalence:** Yes: 34 (33.7%), No: 67 (66.3%).
- **Panic Attacks Prevalence:** Yes: 33 (32.7%), No: 68 (67.3%).
- **Specialist Care Sought:** No: 95 (94.1%), Yes: 6 (5.9%).
- **Academic Standing (CGPA):**
  - `3.50 - 4.00`: 48 students (47.5%)
  - `3.00 - 3.49`: 43 students (42.6%)
  - `2.50 - 2.99`: 4 students (4.0%)
  - `2.00 - 2.49`: 5 students (5.0%)
  - `0 - 1.99`: 1 student (1.0%)

---

### 9. Numerical Summaries (Age)
- **Minimum Age:** 18.0 years
- **Maximum Age:** 24.0 years
- **Mean Age:** 20.53 years
- **Standard Deviation:** 2.50 years
- **Median Age:** 19.0 years

---

### 10. Data Quality Observations
- High overall completeness (>99.9% of data cells populated).
- Standardizing casing in `year_of_study` and trimming whitespace in `cgpa_range` will prevent fragmented headers in Tableau.
- Median imputation for `Age` preserves integer distribution without introducing fractional artifacts.

---

### 11. Suitability for Tableau
- **Dimensions:** Categorical fields (`gender`, `course`, `year_of_study`, `cgpa_range`, condition flags) map directly to Tableau Dimension pills.
- **Measures:** Counting records via `COUNTD()` enables immediate prevalence calculation across demographics.
- **Performance:** Sub-second rendering in Tableau Desktop due to compact file size (< 15 KB).

---

### 12. Limitations
- Lacks the continuous clinical scale scores (`Anxiety Score`, `Depression Score`) and intervention metrics (`Therapy Type`, `Progress Score`) requested in the 18-variable SkillWallet specification.
