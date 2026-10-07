# Epic 3: Data Visualization Comprehensive Report (Validated & Corrected)
## Project: Analysing Mental Health in Student Ecosystem
**Domain:** Healthcare / Student Mental Health & Higher Education Analytics  
**Tableau Version:** Tableau Desktop 2026.1 / Tableau Public  
**Primary Analytical Dataset:** `C:\Skillwallet\data\processed\student_mental_health_processed.csv` (101 Records, 23 Columns)  

---

### 1. Data Integrity & Exclusion of Unavailable Example Fields

> [!IMPORTANT]
> **Data Integrity Enforcement:**
> All visualizations, dashboards, and KPI metrics in this project are constructed **strictly and exclusively** from the empirical fields present in `data/processed/student_mental_health_processed.csv`.
> 
> The placeholder fields displayed in the generic SkillWallet task screenshots—including:
> - *Average Mental Score*
> - *Avg. Sleep Duration Hours* / *Sleep Duration*
> - *Avg. Depression Level*
> - *Avg. Attendance Rate* / *Attendance Rate*
> - *Stress Level*
> - *Heart Rate Variability*
> - *Study Hours*
> - *Academic Performance*
> 
> **do not exist in our validated dataset and were strictly excluded** from all workbooks, dashboards, and evidence files. Zero synthetic records, fabricated metrics, or imputed external indicators were introduced.

---

### 2. Epic 3 Objective & Scope
The primary objective of Epic 3 (*Task: No of Unique Visualizations*) is to develop a comprehensive, empirically substantiated visual analytics suite in Tableau exploring:
- Student demographic profiles (`Gender`, `Age_Group`, `Faculty`, `Year_of_Study`)
- Self-reported mental health condition prevalence (`Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`)
- Clinical comorbidity severity (`Condition_Count`: 0, 1, 2, 3)
- Risk triage categorization (`Mental_Health_Risk`: `Low Risk`, `Moderate Risk`, `High Risk`)
- Academic performance indicators (`CGPA_Range`, `CGPA_Midpoint`)
- The campus healthcare deficit and treatment-seeking barriers (`Treatment_Gap`, `Treatment_Sought`)

---

### 3. Catalog of Unique Worksheets (10 Worksheets)

| # | Worksheet Name | Chart Type | Dimensions & Measures | Empirical Finding |
|---|---|---|---|---|
| 1 | **Distribution of Mental Health Risk Levels Among Students** | Vertical Bar Chart | Dim: `Mental_Health_Risk`<br>Meas: `COUNTD([User_ID])` | Low Risk: 37 (36.6%), Moderate Risk: 36 (35.6%), High Risk: 28 (27.7%). Total = 101. |
| 2 | **Self-Reported Mental Health Conditions by Gender** | Clustered Bar Chart | Dim: `Gender`<br>Meas: `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag` | Females (N=75): Dep 38.7%, Anx 32.0%, Panic 33.3%. Males (N=26): Dep 23.1%, Anx 38.5%, Panic 30.8%. |
| 3 | **Mental Health Risk Across Age Groups** | 100% Stacked Column Chart | Dims: `Age_Group`, `Mental_Health_Risk`<br>Meas: `COUNTD([User_ID])` | Underclassmen (18–20, N=60) exhibit higher High-Risk rates (31.7%) than upperclassmen (21–24, N=41, 22.0%). |
| 4 | **Mental Health Risk by Faculty** | Horizontal Stacked Bar Chart | Dim: `Faculty` (7 Disciplines)<br>Meas: `COUNTD([User_ID])`<br>Color: `Mental_Health_Risk` | Computing & IT (N=28, 8 High Risk) and Engineering (N=26, 7 High Risk) account for over half of all high-risk students. |
| 5 | **Distribution of Mental Health Condition Count** | Discrete Histogram | Dim: `Condition_Count` (0–3)<br>Meas: `COUNTD([User_ID])` | 0 Conditions: 37 (36.6%), 1 Condition: 36 (35.6%), 2 Conditions: 18 (17.8%), 3 Conditions: 10 (9.9%). |
| 6 | **Student Mental Health Treatment Gap** | Categorical Status Bar Chart | Dim: `Treatment_Gap`<br>Meas: `COUNTD([User_ID])` | Untreated Symptomatic: 58 (57.4% total, 90.6% symptomatic). Healthy: 37 (36.6%). Treated: 6 (5.9%). |
| 7 | **Prevalence of Self-Reported Mental Health Conditions** | Benchmark Comparative Bar | Category: Condition Name<br>Meas: Prevalence % | Depression: 35 (34.7%), Anxiety: 34 (33.7%), Panic Attacks: 33 (32.7%). |
| 8 | **CGPA Midpoint and Mental Health Risk** | Box Plot + Stripplot | Dim: `Mental_Health_Risk`<br>Meas: `CGPA_Midpoint` (1.00–3.75) | High-risk students maintain high academic achievement (mean CGPA midpoint 3.45). Non-causal observation. |
| 9 | **Age and Mental Health Condition Count** | Column Chart of Cohort Means | Dim: `Age` (18–24)<br>Meas: `AVG([Condition_Count])` | Average symptom burden remains persistent (1.00 to 1.17) across all undergraduate student ages. |
| 10 | **Treatment Seeking Across Mental Health Risk Levels** | Stacked Column Chart | Dims: `Mental_Health_Risk`, `Treatment_Sought`<br>Meas: `COUNTD([User_ID])` | Only 6 of 28 (21.4%) high-risk students sought professional care; 0 moderate/low-risk students sought care. |

---

### 4. Dashboards Rebuilt With Real Project Fields

#### Dashboard 1: Student Mental Health Overview
- **Header:** Full title with dataset path attribution and survey data disclaimer.
- **Top Row — 4 Validated KPI Cards:**
  1. **Total Students:** `101` (`COUNTD([User_ID])`) — Full surveyed undergraduate cohort.
  2. **High Risk Students:** `28 (27.7%)` — Students reporting 2 or 3 concurrent conditions.
  3. **Moderate Risk Students:** `36 (35.6%)` — Students reporting 1 clinical condition.
  4. **Treatment Gap Students:** `58 (90.6%)` — Symptomatic students who have never consulted a clinical specialist.
- **Middle Row — Demographic & Risk Stratification:**
  - Panel A: *Distribution of Mental Health Risk Levels Among Students*
  - Panel B: *Self-Reported Mental Health Conditions by Gender*
  - Panel C: *Mental Health Risk Across Age Groups*
- **Bottom Row — Academic Disciplines & Care Deficit:**
  - Panel D: *Mental Health Risk by Faculty*
  - Panel E: *Student Mental Health Treatment Gap*
  - Panel F: *Distribution of Mental Health Condition Count*
- **Interactive Global Filters:** `Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`.
- **Rendered Artifact:** [`evidence/epic_03/dashboard_overview.png`](file:///C:/Skillwallet/evidence/epic_03/dashboard_overview.png)

#### Dashboard 2: Mental Health Risk & Treatment Dashboard
- **Focus:** Dedicated operational analysis of student care-seeking patterns, clinical comorbidity severity, and institutional treatment deficits.
- **Visual Panels (2 × 3 Grid):**
  1. *Treatment Seeking Across Mental Health Risk Levels* (Stacked bar: 22/28 high-risk untreated)
  2. *Student Mental Health Treatment Gap Distribution* (Pie breakdown: 57.4% untreated, 36.6% healthy, 5.9% treated)
  3. *Distribution of Mental Health Condition Count* (Histogram: 0, 1, 2, 3 concurrent conditions)
  4. *Self-Reported Mental Health Conditions by Gender* (Clustered bars)
  5. *Distribution of Mental Health Risk Levels Among Students* (Risk tier distribution)
  6. *Mental Health Risk by Faculty* (Horizontal stacked bars)
- **Rendered Artifact:** [`evidence/epic_03/dashboard_treatment.png`](file:///C:/Skillwallet/evidence/epic_03/dashboard_treatment.png)

---

### 5. Important Epidemiological Disclaimers
1. **Self-Reported Survey Basis:** All condition metrics are derived from self-administered questionnaire items (`Yes`/`No`). They represent self-reported symptoms and must not be interpreted as formal psychiatric diagnoses (such as clinical DSM-5 or ICD-11 classifications).
2. **Non-Causal Associations:** Observed correlations—such as high GPA midpoints among high-risk individuals—are descriptive and correlational. No causal direction is asserted.
3. **Cohort Scope:** Sample size reflects N=101 university students. Subgroup breakdowns across smaller academic faculties (e.g. Business N=5, Allied Health N=7) are reported descriptively.

---

### 6. Technical Files & Reproducibility
- **Tableau Workbook File:** [`tableau/student_mental_health_visualizations.twb`](file:///C:/Skillwallet/tableau/student_mental_health_visualizations.twb)
- **Image Generation Pipeline:** [`scripts/generate_visualizations.py`](file:///C:/Skillwallet/scripts/generate_visualizations.py)
- **Tableau XML Builder:** [`scripts/generate_tableau_twb.py`](file:///C:/Skillwallet/scripts/generate_tableau_twb.py)
- **Automated Validation Script:** [`scripts/verify_epic_03.py`](file:///C:/Skillwallet/scripts/verify_epic_03.py)
