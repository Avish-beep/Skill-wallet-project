# Epic 3 — Data Visualization Evidence Manifest (Validated & Corrected)
## Project: Analysing Mental Health in Student Ecosystem
**Epic:** Data Visualization  
**Task:** No of Unique Visualizations  
**Date:** October 07, 2026  

This manifest documents all visual artifacts, Tableau workbook configurations, image evidence, and validation checks completed for **Epic 3: Data Visualization**, strictly validated against the real student mental health dataset.

---

### 1. Data Integrity & Exclusion of Unavailable Example Fields

> [!IMPORTANT]
> **Zero Synthetic / Placeholder Metrics:**
> All evidence artifacts below are built **strictly and exclusively** from the empirical columns present in `data/processed/student_mental_health_processed.csv` (101 student records, 23 columns).
>
> Generic example fields from the SkillWallet task template—including:
> - *Average Mental Score*
> - *Avg. Sleep Duration Hours* / *Sleep Duration*
> - *Avg. Depression Level*
> - *Avg. Attendance Rate* / *Attendance Rate*
> - *Stress Level*
> - *Heart Rate Variability*
> - *Study Hours*
> - *Academic Performance*
>
> **do not exist in our validated dataset and were completely excluded**. All evidence screenshots were generated directly from the real data.

---

### 2. Tableau Workbook & Deliverables Summary

- **Tableau Workbook File:** `tableau/student_mental_health_visualizations.twb`
- **Dataset Connected:** `data/processed/student_mental_health_processed.csv` (101 Rows, 23 Columns, 0 Nulls, 0 Duplicates)
- **Total Unique Worksheets Created:** 10
- **Total Dashboards Created:** 2
- **Evidence Images Generated:** 12 High-Resolution PNGs (300 DPI)

---

### 3. Rebuilt Dashboards Created

1. **`Student Mental Health Overview`**
   - **File:** `evidence/epic_03/dashboard_overview.png`
   - **Composition:** 4 Validated KPI cards (Total Students: 101, High Risk: 28, Moderate Risk: 36, Treatment Gap: 58) + 6 analytic panels (Risk Distribution, Conditions by Gender, Risk by Age Group, Faculty Risk, Treatment Gap, Condition Count).
   - **Interactive Filters:** `Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`.
2. **`Mental Health Risk & Treatment Dashboard`**
   - **File:** `evidence/epic_03/dashboard_treatment.png`
   - **Composition:** 2 &times; 3 clinical grid focusing on treatment seeking across risk levels, treatment gap status, comorbidity severity, gender disparity, risk distribution, and faculty risk.

---

### 4. Worksheets & Evidence Artifact Catalog

| # | Worksheet Name | Evidence Image File | Mark Type | Primary Dimensions & Measures | Key Empirical Finding |
|---|---|---|---|---|---|
| 1 | **Distribution of Mental Health Risk Levels Among Students** | `evidence/epic_03/mental_health_risk.png` | Bar Chart | `Mental_Health_Risk`, `Total Students` | 28 High Risk (27.7%), 36 Moderate Risk (35.6%), 37 Low Risk (36.6%). |
| 2 | **Self-Reported Mental Health Conditions by Gender** | `evidence/epic_03/conditions_by_gender.png` | Clustered Bar | `Gender`, `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag` | Higher depression prevalence in females (38.7% vs 23.1%); anxiety elevated in both cohorts. |
| 3 | **Mental Health Risk Across Age Groups** | `evidence/epic_03/risk_by_age_group.png` | Stacked Column | `Age_Group`, `Mental_Health_Risk`, `Total Students` | Underclassmen (18–20) exhibit 31.7% high risk vs 22.0% in upperclassmen. |
| 4 | **Mental Health Risk by Faculty** | `evidence/epic_03/faculty_risk.png` | Horizontal Stacked Bar | `Faculty`, `Mental_Health_Risk`, `Total Students` | Computing & IT (N=28) and Engineering (N=26) have the largest volume of high-risk students. |
| 5 | **Distribution of Mental Health Condition Count** | `evidence/epic_03/condition_count.png` | Discrete Histogram | `Condition_Count`, `Total Students` | 63.4% report &ge;1 condition; 9.9% (10 students) report all 3 conditions concurrently. |
| 6 | **Student Mental Health Treatment Gap** | `evidence/epic_03/treatment_gap.png` | Categorical Bar | `Treatment_Gap`, `Total Students` | 58/64 symptomatic students (90.6%) have not sought specialist consultation. |
| 7 | **Prevalence of Self-Reported Conditions** | `evidence/epic_03/condition_prevalence.png` | Benchmark Bar | Condition Name, Prevalence % | Near-even distribution: Depression 34.7%, Anxiety 33.7%, Panic Attacks 32.7%. |
| 8 | **CGPA Midpoint and Mental Health Risk** | `evidence/epic_03/cgpa_risk.png` | Boxplot + Stripplot | `Mental_Health_Risk`, `CGPA_Midpoint` | High-risk students maintain high academic achievement (mean CGPA midpoint 3.45). |
| 9 | **Age and Condition Count** | `evidence/epic_03/age_condition.png` | Bar Chart (Mean) | `Age`, `AVG([Condition_Count])` | Vulnerability is persistent across all undergraduate ages (18–24). |
| 10 | **Treatment Seeking Across Risk Levels** | `evidence/epic_03/treatment_by_risk.png` | Stacked Bar | `Mental_Health_Risk`, `Treatment_Sought` | 78.6% of high-risk students have never sought specialist help. |

---

### 5. Validation Performed
- [x] Processed dataset loaded successfully with 101 rows and 23 columns.
- [x] XML schema for `tableau/student_mental_health_visualizations.twb` validated without syntax errors.
- [x] All 12 visualization images generated and verified in `evidence/epic_03/`.
- [x] Reconciled all student counts to 101 respondents.
- [x] Visualizations strictly labeled as survey self-reported data without clinical causal claims.
- [x] Verified zero invalid example fields in XML, script, or screenshots.

---

### 6. Tableau Public Publishing Status
**Status:** **Tableau Public publication pending authentication.**  
*Note: Local Tableau workbook (`.twb`) and complete rendering artifacts are ready. Direct publishing to Tableau Public requires manual browser authentication via your friend's credentials.*
