# Tableau Data Source Notes (Epic 3 — Visual Analytics & Workbook Integration)
## Project: Analysing Mental Health in Student Ecosystem

This document provides complete technical specifications for the Tableau workbook, data connections, calculated fields, individual visualization worksheets, and interactive dashboards created for **Epic 3: Data Visualization**.

**Validated Source Dataset:** `data/processed/student_mental_health_processed.csv` (101 Records, 23 Columns)  
**Strict Integrity Rule:** All metrics are derived exclusively from actual survey columns. Generic example metrics (Average Mental Score, Sleep Duration, Attendance Rate, Heart Rate Variability) do not exist in our dataset and are strictly excluded.

---

### 1. Data Connection & Source Specifications

- **Tableau Workbook File:** `tableau/student_mental_health_visualizations.twb`
- **Primary Data Source Path:** `data/processed/student_mental_health_processed.csv`
- **Fallback / Raw Path (Immutable):** `data/raw/Student_Mental_health.csv` (SHA-256: `c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`)
- **Connection Type:** In-memory Text File connection (UTF-8 encoded CSV)
- **Record Count:** 101 records (100% complete, 0 missing values, 0 duplicates)
- **Field Count:** 23 columns (11 standardized raw features + 1 lineage column + 11 engineered features)
- **Target Software:** Tableau Desktop 2026.1 (64-bit) & Tableau Public

---

### 2. Validated Fields Used Across Visualizations

| Field Name | Data Type | Tableau Role | Used In Worksheets | Analytical Function |
|---|---|---|---|---|
| `User_ID` | String | Dimension | WS 1–10, Dashboards | Granular student primary key (`COUNTD([User_ID])`). |
| `Gender` | String | Dimension | WS 2, Filters, Dashboards | Demographic disaggregation (`Female`, `Male`). |
| `Age` | Integer | Dimension / Measure | WS 9, Dashboards | Chronological respondent age (18–24). |
| `Age_Group` | String | Dimension (Ordinal) | WS 3, Filters, Dashboards | Binned cohorts (`18-20 (Underclassmen)`, `21-24 (Upperclassmen)`). |
| `Faculty` | String | Dimension | WS 4, Filters, Dashboards | 7 macro academic disciplines. |
| `Course` | String | Dimension | Detail / Tooltips | Standardized degree programs (43 majors). |
| `Year_of_Study` | String | Dimension | Filters / Detail | Standardized study year (`year 1`–`year 4`). |
| `CGPA_Range` | String | Dimension (Ordinal) | Detail / Tooltips | Ordinal grade categories. |
| `CGPA_Midpoint` | Real (Float) | Measure | WS 8 | Continuous proxy for GPA (1.00–3.75). |
| `Depression_Flag` | Integer | Measure | WS 2, WS 7, Dashboards | Binary condition indicator (1/0). |
| `Anxiety_Flag` | Integer | Measure | WS 2, WS 7, Dashboards | Binary condition indicator (1/0). |
| `Panic_Attack_Flag`| Integer | Measure | WS 2, WS 7, Dashboards | Binary condition indicator (1/0). |
| `Condition_Count` | Integer | Measure / Dimension | WS 5, WS 9, Dashboards | Comorbidity sum (0–3 concurrent conditions). |
| `Mental_Health_Risk`| String | Dimension (Ordinal) | WS 1, 3, 4, 8, 10, Filters | Clinical risk classification (`Low Risk`, `Moderate Risk`, `High Risk`). |
| `Treatment_Gap` | String | Dimension | WS 6, Dashboards | Status: `Untreated Condition`, `No Identified Condition`, `Condition Treated`. |
| `Treatment_Sought` | String | Dimension | WS 10, Dashboards | Professional healthcare seeking (`Yes`, `No`). |

---

### 3. Tableau Calculated Fields Created

The following calculated fields are embedded within `tableau/student_mental_health_visualizations.twb`:

1. **`[Total_Students_Calc]`**:
   ```tableau
   COUNTD([User_ID])
   ```
2. **`[High_Risk_Count_Calc]`**:
   ```tableau
   COUNTD(IF [Mental_Health_Risk] = 'High Risk' THEN [User_ID] END)
   ```
3. **`[High_Risk_Pct_Calc]`**:
   ```tableau
   [High_Risk_Count_Calc] / [Total_Students_Calc]
   ```
4. **`[Moderate_Risk_Count_Calc]`**:
   ```tableau
   COUNTD(IF [Mental_Health_Risk] = 'Moderate Risk' THEN [User_ID] END)
   ```
5. **`[Treatment_Gap_Count_Calc]`**:
   ```tableau
   COUNTD(IF [Treatment_Gap] = 'Untreated Condition' THEN [User_ID] END)
   ```
6. **`[Treatment_Gap_Pct_Calc]`**:
   ```tableau
   [Treatment_Gap_Count_Calc] / COUNTD(IF [Condition_Count] > 0 THEN [User_ID] END)
   ```
7. **`[Depression_Rate_Calc]`**:
   ```tableau
   SUM([Depression_Flag]) / [Total_Students_Calc]
   ```
8. **`[Anxiety_Rate_Calc]`**:
   ```tableau
   SUM([Anxiety_Flag]) / [Total_Students_Calc]
   ```
9. **`[Panic_Rate_Calc]`**:
   ```tableau
   SUM([Panic_Attack_Flag]) / [Total_Students_Calc]
   ```

---

### 4. Dashboards Architecture (Rebuilt & Validated)

- **Dashboard 1: `Student Mental Health Overview`**
  - **4 Top KPI Cards:** Total Students (101), High Risk Students (28 / 27.7%), Moderate Risk Students (36 / 35.6%), Treatment Gap Students (58 / 90.6% symptomatic).
  - **6 Visual Panels (2 × 3 Grid):**
    - Panel A: *Distribution of Mental Health Risk Levels Among Students*
    - Panel B: *Self-Reported Mental Health Conditions by Gender*
    - Panel C: *Mental Health Risk Across Age Groups*
    - Panel D: *Mental Health Risk by Faculty*
    - Panel E: *Student Mental Health Treatment Gap*
    - Panel F: *Distribution of Mental Health Condition Count*
  - **Filters:** Interactive dropdowns for `Gender`, `Age_Group`, `Faculty`, and `Mental_Health_Risk`.
  - **Dimensions:** 1920 &times; 1080 responsive canvas.

- **Dashboard 2: `Mental Health Risk & Treatment Dashboard`**
  - **6 Clinical Panels:** Focused specifically on specialist consultation rates, treatment gap status, comorbidity severity, and departmental risk distribution.
  - **Target Audience:** Campus counseling staff, medical clinic directors, student welfare deans.

---

### 5. Verification Checklist
- [x] Processed dataset connected without schema mismatch (101 rows, 23 columns).
- [x] Zero invalid example fields present in workbook, XML, or visualizations.
- [x] All 10 worksheets configured with verified calculations.
- [x] Tableau Workbook XML (`tableau/student_mental_health_visualizations.twb`) generated and validated.
- [x] 12 high-resolution evidence artifacts (10 worksheets + 2 dashboards) rendered in `evidence/epic_03/`.
- [x] Full data reconciliation verified (101 total student records).
