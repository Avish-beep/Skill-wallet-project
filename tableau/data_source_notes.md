# Tableau Data Source Notes (Epic 3 — Visual Analytics & Workbook Integration)
## Project: Analysing Mental Health in Student Ecosystem

This document provides complete technical specifications for the Tableau workbook, data connections, calculated fields, individual visualization worksheets, and interactive dashboards created for **Epic 3: Data Visualization**.

---

### 1. Data Connection & Source Specifications

- **Tableau Workbook File:** `tableau/student_mental_health_visualizations.twb`
- **Primary Data Source Path:** `data/processed/student_mental_health_processed.csv`
- **Fallback / Raw Path (Immutable):** `data/raw/Student_Mental_health.csv`
- **Connection Type:** In-memory Text File connection (UTF-8 encoded CSV)
- **Record Count:** 101 records (100% complete, 0 missing values, 0 duplicates)
- **Field Count:** 23 columns (11 standardized raw features + 1 lineage column + 11 engineered features)
- **Target Software:** Tableau Desktop 2026.1 (64-bit) & Tableau Public

---

### 2. Fields Used Across Visualizations

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

### 4. Visualization Worksheets Notes

- **Worksheet 1 (`Mental Health Risk Distribution`):** Uses a clean vertical bar layout with consistent healthcare color palette (`#38A169`, `#DD6B20`, `#E53E3E`).
- **Worksheet 2 (`Mental Health Conditions by Gender`):** Dual clustered bars per condition, annotated with exact within-gender prevalence percentages.
- **Worksheet 3 (`Mental Health Risk Across Age Groups`):** Stacked bar format allowing direct comparison of risk proportions between freshmen/sophomores and seniors.
- **Worksheet 4 (`Mental Health Risk by Faculty`):** Horizontal orientation to accommodate full faculty names cleanly without truncation.
- **Worksheet 5 (`Distribution of Mental Health Condition Count`):** Discrete step histogram from 0 to 3 conditions highlighting the 10 triply symptomatic students.
- **Worksheet 6 (`Student Mental Health Treatment Gap`):** Highlights the acute contrast between the 58 untreated symptomatic students and only 6 treated students.
- **Worksheet 7 (`Prevalence of Self-Reported Conditions`):** Benchmark view comparing Depression (34.7%), Anxiety (33.7%), and Panic Attack (32.7%).
- **Worksheet 8 (`CGPA and Mental Health Risk`):** Boxplot with overlaid student jitter showing median and mean GPA midpoints across risk tiers.
- **Worksheet 9 (`Age and Mental Health Condition Count`):** Bar chart of mean conditions per student age confirming uniform vulnerability across age groups.
- **Worksheet 10 (`Treatment Seeking Across Mental Health Risk Levels`):** Stacked bar demonstrating that 78.6% of high-risk students never sought specialist consultation.

---

### 5. Dashboard Notes

- **Dashboard 1: `Student Mental Health Overview`**
  - **Structure:** 3-tier hierarchy (Top: BAN KPI cards; Middle: Risk & Demographics; Bottom: Academics & Care Gap).
  - **Filters:** Interactive dropdowns for `Gender`, `Age_Group`, `Faculty`, and `Mental_Health_Risk` configured for cross-sheet filtering.
  - **Dimensions:** 1920 &times; 1080 responsive canvas.
- **Dashboard 2: `Mental Health Risk & Treatment Dashboard`**
  - **Structure:** 2 &times; 2 clinical grid focusing specifically on campus health intervention metrics.
  - **Target Audience:** Campus counseling staff, medical clinic directors, student welfare committees.

---

### 6. Verification & Rendering Checklist
- [x] Processed dataset connected without schema mismatch.
- [x] All 10 worksheets configured with verified calculations.
- [x] Tableau Workbook XML (`tableau/student_mental_health_visualizations.twb`) generated and validated.
- [x] 12 high-resolution evidence artifacts (10 worksheets + 2 dashboards) rendered in `evidence/epic_03/`.
- [x] Zero fabricated fields or external datasets used.
