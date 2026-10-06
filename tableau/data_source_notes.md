# Tableau Data Source Notes (Epic 2 — Data Preparation & Source Specification)
## Project: Analysing Mental Health in Student Ecosystem

This document defines the schema, field roles, and configuration requirements for connecting **Tableau Desktop 2026.1** and **Tableau Public** to the prepared dataset generated in Epic 2.

---

### 1. Data Connection Specifications

- **Primary Processed Dataset:** `data/processed/student_mental_health_processed.csv`
- **Fallback / Raw Dataset:** `data/raw/Student_Mental_health.csv`
- **Format:** Comma-Separated Values (`.csv`, UTF-8 encoding)
- **Record Count:** 101 rows (100% complete, 0 nulls, 0 duplicate rows)
- **Field Count:** 23 columns (11 standardized raw features + 1 lineage column + 11 engineered analytical features)
- **Recommended Connection Mode:** Tableau Extract (`.hyper`) or Live Text File connection.

---

### 2. Full 23-Field Tableau Role Mapping & Data Types

| # | Field Name | Tableau Data Type | Tableau Role | Default Aggregation | Analytical Purpose & Visualization Usage |
|---|---|---|---|---|---|
| 1 | `User_ID` | String / Text | Dimension | `COUNTD` | Unique respondent identifier (`STD_0001`–`STD_0101`) for granular student tracking and distinct counts. |
| 2 | `Timestamp` | Date & Time | Dimension | `YEAR`, `MONTH` | Survey submission timestamp for response date distributions. |
| 3 | `Gender` | String | Dimension | None | Demographic breakdown (`Female`, `Male`) for comparative equity views. |
| 4 | `Age` | Whole Number | Dimension / Measure | `AVG`, `MEDIAN` | Respondent age (18–24 years; median 19.0 imputed for row index 43). |
| 5 | `Course` | String | Dimension | None | Standardized degree program / major (cleaned casing). |
| 6 | `Year_of_Study` | String | Dimension | None | Standardized academic year label (`year 1`, `year 2`, `year 3`, `year 4`). |
| 7 | `CGPA_Range` | String (Ordinal) | Dimension | None | Academic performance tier (`0 - 1.99`, `2.00 - 2.49`, `2.50 - 2.99`, `3.00 - 3.49`, `3.50 - 4.00`). |
| 8 | `Marital_Status` | String | Dimension | None | Marital status indicator (`No`, `Yes`). |
| 9 | `Depression` | String | Dimension | None | Categorical self-reported depression status (`Yes`, `No`). |
| 10 | `Anxiety` | String | Dimension | None | Categorical self-reported anxiety status (`Yes`, `No`). |
| 11 | `Panic_Attack` | String | Dimension | None | Categorical self-reported panic attack status (`Yes`, `No`). |
| 12 | `Treatment_Sought` | String | Dimension | None | Health-seeking behavior indicator (`Yes`, `No`). |
| 13 | `Course_Raw` | String | Dimension | None | Unmodified raw course strings preserved for data lineage audit. |
| 14 | `Faculty` | String | Dimension | None | Academic discipline grouping (`Engineering`, `Computing & IT`, `Humanities & Social Sciences`, `Islamic Studies & Education`, `Business & Economics`, `Allied Health Sciences`, `Natural Sciences & General`). |
| 15 | `CGPA_Midpoint` | Decimal Number | Measure | `AVG` | Continuous proxy for GPA (1.00, 2.25, 2.75, 3.25, 3.75) enabling scatter plots, boxplots, and trendlines. |
| 16 | `Age_Group` | String (Ordinal) | Dimension | None | Age cohorts (`18-20 (Underclassmen)`, `21-24 (Upperclassmen)`). |
| 17 | `Depression_Flag` | Whole Number | Measure | `SUM`, `AVG` | Binary flag (1 = Yes, 0 = No) for rate calculation (`SUM([Depression_Flag]) / COUNT([User_ID])`). |
| 18 | `Anxiety_Flag` | Whole Number | Measure | `SUM`, `AVG` | Binary flag (1 = Yes, 0 = No) for prevalence calculation. |
| 19 | `Panic_Attack_Flag`| Whole Number | Measure | `SUM`, `AVG` | Binary flag (1 = Yes, 0 = No) for incidence calculation. |
| 20 | `Treatment_Sought_Flag` | Whole Number | Measure | `SUM`, `AVG` | Binary flag (1 = Yes, 0 = No) for treatment rate calculation. |
| 21 | `Condition_Count` | Whole Number | Measure / Dimension | `AVG`, `DISTRIBUTION` | Comorbidity severity index (0 = healthy, 1 = single issue, 2 = dual issue, 3 = triply symptomatic). |
| 22 | `Mental_Health_Risk`| String (Ordinal) | Dimension | None | Risk triage category (`Low Risk` [0 conditions], `Moderate Risk` [1 condition], `High Risk` [2-3 conditions]). |
| 23 | `Treatment_Gap` | String / Dimension | Dimension | None | Categorical healthcare status (`Treatment Gap (Symptomatic, No Treatment)`, `Sought Treatment`, `No Symptoms`). |

---

### 3. Key Tableau Configurations & Visual Best Practices

1. **Default Sort Orders:**
   - `Mental_Health_Risk`: Set manual sort order &rarr; `Low Risk` &rarr; `Moderate Risk` &rarr; `High Risk`.
   - `CGPA_Range`: Set manual sort order &rarr; `0 - 1.99` &rarr; `2.00 - 2.49` &rarr; `2.50 - 2.99` &rarr; `3.00 - 3.49` &rarr; `3.50 - 4.00`.
   - `Year_of_Study`: Set manual sort order &rarr; `year 1` &rarr; `year 2` &rarr; `year 3` &rarr; `year 4`.
   - `Age_Group`: Set manual sort order &rarr; `18-20 (Underclassmen)` &rarr; `21-24 (Upperclassmen)`.

2. **Color Palette Recommendations (Healthcare Theme):**
   - `Mental_Health_Risk`:
     - `Low Risk`: Calm Soft Green (`#2CA02C` or `#48BB78`)
     - `Moderate Risk`: Amber Orange (`#FF7F0E` or `#ED8936`)
     - `High Risk`: Clinical Crimson (`#D62728` or `#E53E3E`)
   - `Gender`:
     - `Female`: Soft Purple (`#9467BD`)
     - `Male`: Steel Blue (`#1F77B4`)

3. **Global Dashboard Interactive Filters:**
   - `Faculty` (Dropdown with 'All')
   - `Gender` (Radio buttons / compact list)
   - `Year_of_Study` (Dropdown)
   - `Mental_Health_Risk` (Checklist / Visual legend filter)
   - `Treatment_Gap` (Dropdown filter)

---

### 4. Calculated Field Formulas for Tableau (Reference for Epic 3)

- **Prevalence Rate (%):**
  `SUM([Depression_Flag]) / COUNT([User_ID])`
- **Comorbidity Rate (%):**
  `COUNT(IF [Condition_Count] >= 2 THEN [User_ID] END) / COUNT([User_ID])`
- **Treatment Gap Count:**
  `COUNT(IF [Treatment_Gap] = 'Treatment Gap (Symptomatic, No Treatment)' THEN [User_ID] END)`
- **Treatment Gap Rate (%):**
  `COUNT(IF [Treatment_Gap] = 'Treatment Gap (Symptomatic, No Treatment)' THEN [User_ID] END) / COUNT(IF [Condition_Count] > 0 THEN [User_ID] END)`

---

### 5. Verification Checklist
- [x] Processed CSV verified without encoding errors (UTF-8).
- [x] Zero null values across all 23 columns.
- [x] Data types align seamlessly with Tableau Desktop 2026.1 and Tableau Public.
- [x] Prepared for immediate import upon authorization to start Epic 3.
