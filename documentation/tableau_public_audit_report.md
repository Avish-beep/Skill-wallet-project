# Tableau Public Audit & Live Reconciliation Report

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author:** Avishkar Padavi  
**Audit Timestamp:** 2026-10-09 18:02 IST  
**Live URL Tested:** [https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem](https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  

---

## 1. Direct Visual Inspection of Live Tableau Public View

Using automated headless Chromium rendering (`evidence/tableau_public_live_check.png`), the live publication was inspected against the local validated workbook:

### ⚠️ Critical Findings:
- **Publication Ownership:** Published under author profile **Avishkar Padavi**.
- **Live Content Status:** The current live Tableau Public link (`Student_Mental_Health_Analysis_17913964531250`) currently hosts the **OLD TEMPLATE WORKBOOK** containing invalid synthetic placeholder fields:
  - `KPI - Avg Anxiety` (Score: 52.59)
  - `KPI - Avg Depression` (Score: 48.09)
  - `KPI - Avg Screen Time` (7.0 hrs)
  - `Stress Level Distribution` (High: 49, Low: 44, Medium: 107)
  - `Sleep Quality vs Stress Level`
  - `Ranked Therapy Efficacy` (CBT, Counseling, Meditation)
- **Data Integrity Violation:** These fields **DO NOT EXIST** in our validated project dataset (`student_mental_health_processed.csv`, N=101). They belong to a generic mock template.

---

## 2. Comparison with Local Validated Workbook

| Metric / Attribute | Live Tableau Public (Current) | Local Validated Workbook (`tableau/student_mental_health_visualizations.twb`) |
| :--- | :--- | :--- |
| **Cohort Size** | Mock counts (sums to 200) | **101 students** (Verified N=101) |
| **KPI 1** | Avg Anxiety score (52.59) | **Total Students: 101** |
| **KPI 2** | Avg Depression score (48.09) | **High Risk Students: 28 (27.7%)** |
| **KPI 3** | Avg Screen Time (7.0 hrs) | **Moderate Risk Students: 36 (35.6%)** |
| **KPI 4** | None / Generic card | **Treatment Gap: 58 (90.6% untreated symptomatic)** |
| **Visual Charts** | Sleep quality, therapy efficacy, screen time | **Risk distribution, Within-gender conditions, CGPA boxplot, Care gap** |
| **Dataset Source** | Generic mock generator | **data/processed/student_mental_health_processed.csv** |

---

## 3. Required Action & Republishing Guide

Tableau Desktop 2026.1 has been launched with the validated workbook:  
`C:\Skillwallet\tableau\student_mental_health_visualizations.twb`

### Steps to Complete Live Republishing:
1. In Tableau Desktop, select **Server** &rarr; **Tableau Public** &rarr; **Save to Tableau Public As...**
2. Sign in with the authorized account for **Avishkar Padavi**.
3. Name the workbook: `Student_Mental_Health_Analysis_17913964531250` (to overwrite) or create a clean published view.
4. Once republished, the live URL will immediately reflect the verified 101-student dataset.
5. In accordance with strict project rules, until the user performs this quick sign-in in Tableau Desktop, our documentation transparently identifies this discrepancy.
