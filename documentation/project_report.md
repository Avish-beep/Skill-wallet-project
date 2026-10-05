# Academic Project Report: Analysing Mental Health in Student Ecosystem

**Academic Domain:** Healthcare & Student Wellness Analytics  
**Curriculum Track:** SkillWallet — Data Analytics with Tableau  
**Technology Stack:** Tableau Desktop 2026.1 &bull; Python 3.11.9 &bull; Flask 3.1.3 &bull; GitHub  
**Author:** Academic Project Cohort  
**Date:** October 2026  

---

## 1. Title
**Analysing Mental Health in Student Ecosystem: An Empirical Investigation of Psychological Vulnerabilities, Academic Correlations, and the Campus Treatment Gap**

---

## 2. Abstract
This study investigates the prevalence and structural correlates of psychological distress among university students using an empirical cohort of 101 surveyed undergraduates. Through rigorous data preprocessing in Python and interactive visual analytics in Tableau Desktop 2026.1, we evaluate the distribution of depression, anxiety, and panic attacks across academic tiers, faculties, and demographic strata. The investigation reveals that 62.4% of surveyed students suffer from at least one diagnosable condition, with 35.6% categorized as High Risk (&ge;2 concurrent conditions). Crucially, the study exposes an alarming **90.5% campus treatment gap**, demonstrating that nine out of ten symptomatic students navigate psychiatric distress without specialist intervention. Findings are synthesized into an integrated Flask web dissemination portal.

---

## 3. Introduction
Mental health challenges among tertiary students represent a growing public health crisis globally. The transition to higher education introduces substantial academic, interpersonal, and financial stressors. While universities invest in counseling infrastructure, utilization rates remain surprisingly low. Visual analytics and reproducible data pipelines provide higher education leadership with transparent, actionable evidence to drive institutional reform.

---

## 4. Problem Statement
Higher education institutions frequently lack empirical visibility into the real burden of student mental health. Prevailing assumptions suggest that mental health distress is primarily restricted to academically struggling students. Furthermore, without quantitative tracking of comorbidity and treatment-seeking patterns, universities cannot accurately resource their psychological support centers.

---

## 5. Objectives
1. **Clean & Validate Survey Data:** Build a reproducible Python pipeline to standardize categorical responses and handle missing data.
2. **Quantify Condition Prevalence:** Measure the individual and joint rates of Depression, Anxiety, and Panic Attacks.
3. **Analyze Demographic & Academic Correlates:** Evaluate whether academic seniority, gender, faculty, or CGPA moderate psychological distress.
4. **Expose the Healthcare Utilization Gap:** Measure the proportion of symptomatic students accessing mental health specialists.
5. **Develop an Integrated Dissemination System:** Construct a 12-worksheet Tableau dashboard, a 6-scene analytical story, and an embedding Flask application.

---

## 6. Domain Context
This investigation operates at the intersection of **Healthcare Informatics** and **Higher Education Institutional Analytics**, adhering to strict anonymization, ethical data handling, and evidence-based clinical classifications.

---

## 7. Dataset Description
The analysis utilizes verified survey data comprising 101 student observations across 11 raw survey fields (`Timestamp`, `Choose your gender`, `Age`, `What is your course?`, `Your current year of Study`, `What is your CGPA?`, `Marital status`, `Do you have Depression?`, `Do you have Anxiety?`, `Do you have Panic attack?`, `Did you seek any specialist for a treatment?`).

---

## 8. Data Dictionary
*(Abridged Summary — see `data_dictionary.md` for full specification)*
- `student_id`: Unique anonymized identifier (`STD_0001` to `STD_0101`).
- `gender`: Female (74.3%) / Male (25.7%).
- `age`: 18 to 24 years (mean: 20.5 years).
- `faculty`: 7 categorized institutional faculties.
- `cgpa_range`: Standardized academic tiers (`0 - 1.99` to `3.50 - 4.00`).
- `depression_flag`, `anxiety_flag`, `panic_attack_flag`: Binary condition indicators (1/0).
- `condition_count`: Composite psychiatric burden score (0 to 3).
- `mental_health_risk`: Clinical risk stratification (Low, Moderate, High Risk).
- `treatment_gap`: Healthcare status relative to clinical need.

---

## 9. Data Collection
Survey responses were gathered through standard digital questionnaire instruments administered across diverse degree disciplines. Data was stored in comma-separated format (`Student_Mental_health.csv`).

---

## 10. Data Cleaning
Executed via `scripts/data_cleaning.py`:
- 1 missing age record was imputed using cohort median (19.0).
- Trimmed whitespace discrepancies in CGPA strings (e.g. `'3.50 - 4.00 '`).
- Standardized mixed-case seniority labels (`year 1`, `Year 1` &rarr; `Year 1`).
- Corrected course abbreviations (`BIT` &rarr; `Information Technology (BIT)`).

---

## 11. Data Preparation & Feature Engineering
Engineered 12 derived variables:
1. `condition_count` = sum of binary condition flags.
2. `mental_health_risk` = stratification into Low (0), Moderate (1), and High (&ge;2) risk.
3. `cgpa_midpoint` = numerical proxy for academic grade performance.
4. `treatment_gap` = classification into Treated, Untreated, or Healthy Baseline.

---

## 12. Exploratory Analysis Findings
- **High-Risk Burden:** 36 students (35.6%) experience &ge;2 concurrent conditions.
- **Depression:** 35 students (34.7%).
- **Anxiety:** 34 students (33.7%).
- **Panic Attacks:** 33 students (32.7%).
- **Triple Comorbidity:** 16 students (15.8%) suffer from all 3 conditions simultaneously.
- **Academic Independence:** High-achieving students (CGPA 3.50–4.00) show severe condition prevalence rates equivalent to average students.

---

## 13. Visualization Methodology
Constructed 12 dedicated visual worksheets adhering to visual encoding best practices:
- Donut chart for risk tier proportions.
- Grouped bars for condition prevalence.
- 100% stacked bars for gender disparity.
- Heatmaps for faculty-level risk clustering.

---

## 14. Dashboard Design
Structured across 4 logical visual bands:
1. Header & Global Interactive Filter Bar (`gender`, `faculty`, `year_of_study`, `cgpa_range`).
2. Executive BAN KPI Row.
3. Section 1 (Overall Risk & Clinical Burden) & Section 2 (Academic Correlations).
4. Section 3 (Comorbidity & Treatment Gap) & Section 4 (Faculty Heatmap).

---

## 15. Tableau Story Narrative
Structured into 6 chronological scenes:
- Scene 1: Ecosystem Overview & Scope
- Scene 2: The Triad of Psychological Burden
- Scene 3: Demographic Profiles & Seniority Vulnerability
- Scene 4: Academic Rigor vs. Mental Health
- Scene 5: The Critical Treatment Gap
- Scene 6: Institutional Strategic Interventions

---

## 16. Key Insights & Institutional Recommendations
1. **The Treatment Void:** 90.5% of students with active mental health conditions have never seen a specialist.
2. **De-Stigmatize Care:** Introduce mandatory, confidential mental health check-ins during orientation.
3. **High-Stress Faculty Resources:** Allocate targeted mental health liaison officers to Engineering and IT departments.

---

## 17. Flask Web Integration
A lightweight web portal (`flask_app/app.py`) was constructed to host the visual analytics. Features include:
- Home page with live KPI cards calculated directly from `data/processed/`.
- Embedded Tableau dashboard container leveraging the Tableau Web Component API v3.
- Departmental cross-tab tables and REST API summary endpoint (`/api/summary`).

---

## 18. Performance Testing
- Processed dataset footprint is 13.9 KB.
- Sub-second pipeline execution.
- Web component loads asynchronously with minimal browser resource consumption.

---

## 19. Testing & Validation
100% pass rate achieved across all test scripts (`scripts/verify_environment.py`, `scripts/test_flask_app.py`).

---

## 20. Limitations
- Cross-sectional survey design precludes making causal inferences.
- Self-reported survey data may introduce recall bias.
- Sleep quality, screen time, and study hours were not captured in this survey wave.

---

## 21. Future Scope
- Deploy longitudinal pulse tracking across multiple academic semesters.
- Integrate wearable biometric data (sleep trackers, heart rate variability).
- Expand sample size to include cross-institutional comparisons.

---

## 22. Conclusion
This study provides decisive evidence that mental health distress is widespread across university students, crossing demographic and academic boundaries. Addressing the 90.5% treatment gap requires decisive, de-stigmatized institutional support systems.
