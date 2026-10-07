# Visualization Dictionary & Matrix (Validated)
## Project: Analysing Mental Health in Student Ecosystem
**Epic 3:** Data Visualization &bull; **Task:** No of Unique Visualizations  
**Validated Source Dataset:** `data/processed/student_mental_health_processed.csv` (101 Rows, 23 Columns)  

> [!NOTE]
> All visualizations below are constructed strictly from verified empirical columns in the processed dataset. Unavailable example metrics (such as Average Mental Score, Sleep Duration, Attendance Rate, and Heart Rate Variability) were strictly excluded.

---

### Worksheets Matrix

| # | Visualization Name | Chart Type | Dimensions | Measures | Institutional Purpose | Key Empirical Insight |
|---|---|---|---|---|---|---|
| **1** | **Distribution of Mental Health Risk Levels Among Students** | Vertical Bar Chart | `Mental_Health_Risk` (Low, Moderate, High) | `COUNTD([User_ID])` | Quantify aggregate risk stratification across student body. | 27.7% (28/101) High Risk; 35.6% (36/101) Moderate Risk; 36.6% (37/101) Low Risk. Total = 101. |
| **2** | **Self-Reported Mental Health Conditions by Gender** | Clustered Bar Chart | `Gender` (Female N=75, Male N=26) | `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag` | Evaluate gender differences in self-reported clinical symptoms. | Females report higher depression rate (38.7% vs 23.1%); anxiety is elevated in both cohorts (32.0% females vs 38.5% males). |
| **3** | **Mental Health Risk Across Age Groups** | 100% Stacked Column | `Age_Group` (18–20, 21–24), `Mental_Health_Risk` | `COUNTD([User_ID])` | Assess vulnerability progression across student seniority stages. | Underclassmen (18–20) experience higher High-Risk proportion (31.7%) than upperclassmen (22.0%). |
| **4** | **Mental Health Risk by Faculty** | Horizontal Stacked Bar | `Faculty` (7 Disciplines), `Mental_Health_Risk` | `COUNTD([User_ID])` | Identify departmental distress concentrations to prioritize embedded counseling. | Computing & IT (N=28, 8 High Risk) and Engineering (N=26, 7 High Risk) contain over half of all high-risk students. |
| **5** | **Distribution of Mental Health Condition Count** | Discrete Histogram | `Condition_Count` (0, 1, 2, 3) | `COUNTD([User_ID])` | Measure comorbidity load across individual students. | 63.4% of respondents report &ge;1 condition; 9.9% (10 students) report all 3 conditions concurrently. |
| **6** | **Student Mental Health Treatment Gap** | Categorical Status Bar | `Treatment_Gap` (Untreated, Healthy, Treated) | `COUNTD([User_ID])` | Quantify the campus psychological treatment deficit. | 90.6% of symptomatic students (58/64) have not consulted a specialist, exposing an acute care deficit. |
| **7** | **Prevalence of Self-Reported Mental Health Conditions** | Comparative Bar Chart | Condition Name (`Depression`, `Anxiety`, `Panic Attack`) | Prevalence % | Benchmark individual condition frequencies across the full cohort. | Conditions show near-equal prevalence: Depression 34.7%, Anxiety 33.7%, Panic Attacks 32.7%. |
| **8** | **CGPA Midpoint and Mental Health Risk** | Box Plot with Stripplot | `Mental_Health_Risk` (Low, Moderate, High) | `CGPA_Midpoint` (1.00–3.75) | Investigate empirical correlation between academic performance and clinical risk. | High-risk students maintain high academic achievement (mean CGPA midpoint 3.45). Non-causal observation. |
| **9** | **Age and Mental Health Condition Count** | Column Chart of Cohort Means | `Age` (18 to 24) | `AVG([Condition_Count])` | Track average condition burden across chronological ages. | Average condition burden remains consistently elevated (1.00 to 1.17) across all ages from 18 through 24. |
| **10**| **Treatment Seeking Across Mental Health Risk Levels** | Stacked Column Chart | `Mental_Health_Risk`, `Treatment_Sought` (Yes, No) | `COUNTD([User_ID])` | Analyze professional healthcare utilization across clinical risk tiers. | Only 21.4% (6/28) of high-risk students sought care; 0% of moderate-risk students sought care. |

---

### Dashboards Matrix

| Dashboard Name | Screen Dimensions | Components Integrated | Key Interactive Filters | Primary Stakeholder |
| :--- | :--- | :--- | :--- | :--- |
| **Student Mental Health Overview** | 1920 &times; 1080 (Responsive) | **4 Real KPI Cards** (Total: 101, High Risk: 28, Moderate: 36, Treatment Gap: 58) + **6 Analytical Panels** (Worksheets 1, 2, 3, 4, 5, 6) | `Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk` | University Administration, Provost, Student Welfare Deans |
| **Mental Health Risk & Treatment Dashboard** | 1920 &times; 1080 (Responsive) | **6 Clinical Panels** (Worksheets 10, 6, 5, 2, 1, 4) focused on specialist consultation, treatment barriers, comorbidity, and faculty risk | `Faculty`, `Mental_Health_Risk`, `Treatment_Sought` | Campus Health Center, Counseling Services, Clinical Psychologists |
