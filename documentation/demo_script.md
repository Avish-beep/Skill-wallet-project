# 5–10 Minute Academic Presentation Script
## Project: Analysing Mental Health in Student Ecosystem

**Presenter:** Project Lead / Student Researcher  
**Target Audience:** Evaluators, Mentors, and Academic Examiners  
**Estimated Time:** 8 Minutes  

---

### Minute 0:00 – 1:00 | 1. Introduction & Domain Scope
> *"Respected evaluators and peers, good morning. Today, I am proud to present our project: **Analysing Mental Health in Student Ecosystem**, executed under the SkillWallet Data Analytics with Tableau curriculum.*
> 
> *Student mental health is one of the most pressing yet under-addressed challenges in higher education today. Our objective was not merely to observe symptoms, but to construct a reproducible analytical pipeline connecting Python data engineering, Tableau visual intelligence, and a responsive Flask web application to uncover real, actionable institutional patterns."*

---

### Minute 1:00 – 2:00 | 2. Problem Statement & Research Objectives
> *"Universities invest heavily in infrastructure, yet students frequently experience silent psychiatric distress. The primary problem we tackled is twofold: first, the widespread misconception that mental distress only affects students who struggle academically; and second, the profound institutional blind spot regarding the disparity between clinical need and actual healthcare utilization."*

---

### Minute 2:00 – 3:00 | 3. Dataset Discovery & Profiling
> *"We utilized an empirical survey dataset comprising 101 university student respondents across 11 raw survey fields. Using our Python profiling script, we audited the data for integrity. We found zero duplicate records, detected a single missing value in the age column, and identified formatting inconsistencies across categorical fields like CGPA and academic year."*

---

### Minute 3:00 – 4:00 | 4. Python Data Preparation Pipeline
> *"To ensure academic reproducibility, we authored `scripts/data_cleaning.py`. The pipeline imputes the missing age using the cohort median of 19, standardizes text casing, and engineers 12 verified features. Crucially, we engineered a `condition_count` metric and stratified students into three clinically grounded risk categories: Low, Moderate, and High Risk. We also generated a continuous CGPA midpoint proxy enabling numeric correlations without altering raw survey truths."*

---

### Minute 4:00 – 5:30 | 5. Tableau Visualizations & Calculated Fields
> *(Transition to Tableau Desktop / Dashboard)*
> *"Moving to visual analytics in Tableau Desktop 2026.1, we built 12 specialized worksheets governed by 10 custom calculated fields. 
> 
> Here you see our executive BAN KPI cards:
> - Out of 101 students, **35 suffer from Depression**, **34 from Anxiety**, and **33 experience acute Panic Attacks**.
> - Looking at our Donut Chart, **35.6% of the cohort is categorized as High Risk**, meaning they suffer from multiple conditions simultaneously.
> - Our 100% stacked bar chart illustrates gender disparities, while our faculty heatmap identifies heightened distress concentrations within Engineering and Computing disciplines."*

---

### Minute 5:30 – 6:30 | 6. Dashboard Interactivity & Tableau Story
> *"Our unified dashboard is built on a responsive 4-band container architecture. It features interactive global filters for gender, faculty, study year, and academic standing, allowing dynamic cross-filtering.
> 
> Furthermore, we structured our findings into a 6-scene analytical Tableau Story. Scene 4 specifically challenges prevailing assumptions by plotting CGPA against mental health risk: students in the top honors band (3.50 to 4.00) experience anxiety and depression at rates identical to or higher than lower tiers, proving that academic success is no shield against mental illness."*

---

### Minute 6:30 – 7:30 | 7. Flask Web Integration
> *(Transition to browser showing `http://127.0.0.1:5000`)*
> *"To democratize access to these insights, we developed a production-ready Flask web application. Our Flask backend parses processed cohort data dynamically to render live KPI cards on the home page. On the `/dashboard` route, the Tableau dashboard is embedded via the official Tableau Web Component API v3, providing seamless, responsive interactive analytics across mobile, tablet, and desktop devices."*

---

### Minute 7:30 – 8:30 | 8. The Core Finding: The 90.5% Treatment Gap
> *"The single most critical takeaway from our empirical study is the **Campus Treatment Gap**. 
> 
> While 63 out of 101 students report at least one clinical condition, **only 6 students sought specialist consultation**. Over **90.5% of symptomatic students** navigate their distress in complete isolation. This empirical finding provides decisive evidence for campus administrations to actively de-stigmatize mental healthcare and deploy walk-in counseling triage."*

---

### Minute 8:30 – 9:00 | 9. Conclusion & Q&A
> *"In summary, our project has fulfilled all 8 Epics and 14 tasks of the SkillWallet curriculum, maintaining complete data integrity from raw ingestion to web deployment. Thank you for your time, and I welcome your questions."*
