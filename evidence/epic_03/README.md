# Epic 3 — Data Visualization Evidence Manifest
## Task: Responsive and Design of Dashboard
**Project:** Analysing Mental Health in Student Ecosystem  
**Target Platform:** Tableau Desktop 2026.1 / Tableau Public  
**Date:** October 07, 2026  

This manifest documents the final responsive dashboard design, visual analytics worksheets, evidence artifacts, and verification results for **Epic 3: Data Visualization (Responsive and Design of Dashboard)**.

---

### 1. Accurate Project-Specific Dashboard Description

> **Dashboard Overview:**  
> The **Student Mental Health Analysis Dashboard** provides an interactive visual overview of self-reported mental-health conditions among 101 surveyed university students. It utilizes validated demographic, academic, mental-health-risk, condition-count, and treatment-seeking fields to help educational stakeholders and wellness administrators identify patterns across gender, age group, and academic faculty.
> 
> - **Executive KPI Cards:** Summarize the student cohort (101 students) and stratify risk tiers (28 high risk, 36 moderate risk, 58 untreated symptomatic students).
> - **Risk Distribution:** Illustrates the proportion of students categorized as Low (36.6%), Moderate (35.6%), and High Risk (27.7%).
> - **Gender Visualization:** Compares self-reported depression, anxiety, and panic attack indicators between female (N=75) and male (N=26) cohorts.
> - **Age-Group & Faculty Views:** Highlight how comorbidity risk is distributed across undergraduate seniority levels (18–20 vs. 21–24) and 7 macro academic disciplines.
> - **Treatment-Gap Visualizations:** Highlight self-reported treatment-seeking patterns, revealing that 90.6% of symptomatic students have not accessed specialist care.
> - **Condition-Count Visualization:** Displays the distribution of concurrent self-reported conditions (0 to 3), detailing comorbidity burdens.
> 
> *Epidemiological Disclaimer: This project is based entirely on self-reported student mental-health survey data. Survey responses reflect self-reported symptoms and do not represent formal psychiatric diagnoses. All observed associations are correlational and non-causal.*

---

### 2. Exclusion of Unavailable Example Fields

> [!IMPORTANT]
> **Strict Data Integrity:**
> Generic placeholder metrics displayed in the course assignment screenshots—including:
> - *Average Mental Score*
> - *Avg. Sleep Duration Hours* / *Sleep Duration*
> - *Avg. Depression Level*
> - *Avg. Attendance Rate* / *Attendance Rate*
> - *Stress Level*
> - *Heart Rate Variability*
> - *Study Hours*
> - *Academic Performance*
> 
> **do not exist in our validated dataset and were strictly excluded** from all workbooks, dashboards, and evidence files. All visual components are generated exclusively from `data/processed/student_mental_health_processed.csv`.

---

### 3. Responsive Dashboard Suite

1. **`Student Mental Health Overview`**
   - **Evidence File:** `evidence/epic_03/dashboard_overview.png` (High-Resolution 300 DPI, 685 KB)
   - **Responsive Features:** Dynamic 16:9 container architecture (1920×1080), dark slate header with interactive filter pills (`Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`), 4 aligned executive KPI cards, and a 2×3 card-based visual panel grid.
   - **4 KPI Cards:** Total Students (101), High Risk Students (28 / 27.7%), Moderate Risk Students (36 / 35.6%), Treatment Gap Students (58 / 90.6% of symptomatic).
   - **6 Analytical Panels:**
     1. Distribution of Mental Health Risk Levels Among Students
     2. Self-Reported Mental Health Conditions by Gender
     3. Mental Health Risk Across Age Groups
     4. Mental Health Risk by Faculty
     5. Student Mental Health Treatment Gap
     6. Distribution of Mental Health Condition Count

2. **`Mental Health Risk & Treatment Dashboard`**
   - **Evidence File:** `evidence/epic_03/dashboard_treatment.png` (High-Resolution 300 DPI, 532 KB)
   - **Focus:** Dedicated operational analysis of care utilization, comorbidity severity, and treatment barriers.
   - **6 Clinical Panels:**
     1. Treatment Seeking Across Risk Tiers
     2. Student Mental Health Treatment Gap Distribution
     3. Distribution of Mental Health Condition Count
     4. Self-Reported Conditions by Gender
     5. Mental Health Risk Distribution
     6. Mental Health Risk by Faculty

---

### 4. Worksheets Catalog & Evidence Artifacts

| # | Worksheet Name | Evidence Image File | Mark Type | Primary Dimensions & Measures | Key Empirical Finding |
|---|---|---|---|---|---|
| 1 | **Distribution of Mental Health Risk Levels Among Students** | `evidence/epic_03/mental_health_risk.png` | Bar Chart | `Mental_Health_Risk`, `COUNTD([User_ID])` | 28 High Risk (27.7%), 36 Moderate Risk (35.6%), 37 Low Risk (36.6%). |
| 2 | **Self-Reported Mental Health Conditions by Gender** | `evidence/epic_03/conditions_by_gender.png` | Clustered Bar | `Gender`, `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag` | Higher depression in females (38.7% vs 23.1%); anxiety elevated in both cohorts. |
| 3 | **Mental Health Risk Across Age Groups** | `evidence/epic_03/risk_by_age_group.png` | Stacked Column | `Age_Group`, `Mental_Health_Risk`, `COUNTD([User_ID])` | Underclassmen (18–20) exhibit 31.7% high risk vs 22.0% in upperclassmen. |
| 4 | **Mental Health Risk by Faculty** | `evidence/epic_03/faculty_risk.png` | Horizontal Stacked Bar | `Faculty`, `Mental_Health_Risk`, `COUNTD([User_ID])` | Computing & IT (N=28) and Engineering (N=26) have largest volume of high-risk students. |
| 5 | **Distribution of Mental Health Condition Count** | `evidence/epic_03/condition_count.png` | Discrete Histogram | `Condition_Count`, `COUNTD([User_ID])` | 63.4% report &ge;1 condition; 9.9% (10 students) report all 3 conditions concurrently. |
| 6 | **Student Mental Health Treatment Gap** | `evidence/epic_03/treatment_gap.png` | Categorical Bar | `Treatment_Gap`, `COUNTD([User_ID])` | 58/64 symptomatic students (90.6%) have not sought specialist consultation. |
| 7 | **Prevalence of Self-Reported Conditions** | `evidence/epic_03/condition_prevalence.png` | Benchmark Bar | Condition Name, Prevalence % | Near-even distribution: Depression 34.7%, Anxiety 33.7%, Panic Attacks 32.7%. |
| 8 | **CGPA Midpoint and Mental Health Risk** | `evidence/epic_03/cgpa_risk.png` | Boxplot + Stripplot | `Mental_Health_Risk`, `CGPA_Midpoint` | High-risk students maintain high academic achievement (mean CGPA midpoint 3.45). |
| 9 | **Age and Condition Count** | `evidence/epic_03/age_condition.png` | Bar Chart (Mean) | `Age`, `AVG([Condition_Count])` | Vulnerability is persistent across all undergraduate ages (18–24). |
| 10 | **Treatment Seeking Across Mental Health Risk Levels** | `evidence/epic_03/treatment_by_risk.png` | Stacked Bar | `Mental_Health_Risk`, `Treatment_Sought` | 78.6% of high-risk students have never sought specialist consultation. |

---

### 5. Verification Checksums & Test Results
- **Raw Data SHA-256 (Immutable):** `c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`
- **Processed Dataset:** 101 rows, 23 columns, 0 nulls, 0 duplicate rows
- **Tableau XML File:** `tableau/student_mental_health_visualizations.twb` (Validated well-formed XML)
- **Automated Validation:** `scripts/verify_epic_03.py` &rarr; **ALL INTEGRITY CHECKS PASSED**

---

### 6. Tableau Public Publishing Status
**Status:** **Tableau Public publication pending authentication.**  
*Note: Direct publishing requires manual browser authentication via your friend's credentials.*
