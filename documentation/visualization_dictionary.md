# Visualization Dictionary & Matrix
## Project: Analysing Mental Health in Student Ecosystem
**Epic 3:** Data Visualization &bull; **Task:** No of Unique Visualizations  

This dictionary formally catalogs each distinct visualization created for the project, detailing its mark type, analytical dimensions, continuous measures, institutional purpose, and primary empirical finding.

---

| Visualization Name | Chart Type | Dimensions | Measures | Institutional Purpose | Key Empirical Insight |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Mental Health Risk Distribution** | Discrete Bar Chart | `Mental_Health_Risk` (Low, Moderate, High) | `Total Students` (`COUNTD([User_ID])`) | Stratify campus student population by aggregate comorbidity burden. | 27.7% (28/101) of students are High Risk (&ge;2 concurrent conditions); 35.6% are Moderate Risk (1 condition). |
| **2. Mental Health Conditions by Gender** | Clustered / Grouped Bar Chart | `Gender` (Female, Male) | `SUM([Depression_Flag])`, `SUM([Anxiety_Flag])`, `SUM([Panic_Attack_Flag])` | Compare gender-specific clinical condition loads to tailor counseling outreach. | Females report higher depression prevalence (38.7% vs 23.1%); anxiety is elevated in both cohorts (32.0% females vs 38.5% males). |
| **3. Mental Health Risk Across Age Groups** | 100% Stacked Column Chart | `Age_Group` (18–20, 21–24), `Mental_Health_Risk` | `COUNTD([User_ID])` | Determine vulnerability variations across student academic seniority stages. | Underclassmen (18–20) experience higher High-Risk rates (31.7%) than upperclassmen (22.0%), reflecting transition friction. |
| **4. Mental Health Risk by Faculty** | Horizontal Stacked Bar Chart | `Faculty` (7 Academic Disciplines), `Mental_Health_Risk` | `COUNTD([User_ID])` | Identify departmental distress concentrations to prioritize embedded counseling. | Computing & IT (N=28, 8 High Risk) and Engineering (N=26, 7 High Risk) contain over half of all high-risk students. |
| **5. Distribution of Condition Count** | Discrete Histogram | `Condition_Count` (0, 1, 2, 3) | `COUNTD([User_ID])` | Assess multiple comorbidity severity across the undergraduate body. | 63.4% of respondents report at least one condition; 9.9% (10 students) report all three conditions concurrently. |
| **6. Student Mental Health Treatment Gap** | Categorical Status Bar Chart | `Treatment_Gap` (Untreated, Healthy, Treated) | `COUNTD([User_ID])` | Quantify unmet psychological support needs on campus. | 90.6% of symptomatic students (58/64) have not consulted a specialist, exposing an acute treatment deficit. |
| **7. Prevalence of Self-Reported Conditions** | Comparative Bar Chart | Condition Name (`Depression`, `Anxiety`, `Panic Attack`) | `Depression Rate %`, `Anxiety Rate %`, `Panic Attack Rate %` | Benchmark the individual frequency of the three tracked clinical conditions. | Conditions show near-equal prevalence: Depression 34.7%, Anxiety 33.7%, and Panic Attacks 32.7%. |
| **8. CGPA and Mental Health Risk** | Box Plot with Distribution Stripplot | `Mental_Health_Risk` (Low, Moderate, High) | `CGPA_Midpoint` (1.00 to 3.75) | Investigate empirical correlation between academic performance and clinical risk. | High-risk students maintain high academic achievement (mean CGPA midpoint 3.45), showing stress is prevalent among top performers. |
| **9. Age and Condition Count** | Column Chart of Cohort Means | `Age` (18 to 24) | `AVG([Condition_Count])` | Track condition burden across individual chronological ages. | Average condition load remains consistently elevated (1.00 to 1.17) across all ages from 18 through 24. |
| **10. Treatment Seeking Across Risk Levels** | Stacked Bar Chart | `Mental_Health_Risk`, `Treatment_Sought` (Yes, No) | `COUNTD([User_ID])` | Examine specialist care-seeking behaviors across clinical risk tiers. | Only 21.4% (6/28) of high-risk students sought care; 0% of moderate-risk students sought care, demonstrating high treatment avoidance. |

---

### Dashboard Matrix

| Dashboard Name | Screen Dimensions | Worksheets Integrated | Key Interactive Filters | Primary Stakeholder |
| :--- | :--- | :--- | :--- | :--- |
| **Student Mental Health Overview** | 1920 &times; 1080 (Responsive) | Worksheets 1, 2, 3, 4, 5, 6 + 3 KPI BAN Cards | `Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk` | University Administration, Provost, Student Welfare Deans |
| **Mental Health Risk & Treatment Dashboard** | 1920 &times; 1080 (Responsive) | Worksheets 2, 4, 5, 6, 10 | `Faculty`, `Mental_Health_Risk`, `Treatment_Sought` | Campus Health Center, Counseling Services, Clinical Psychologists |
