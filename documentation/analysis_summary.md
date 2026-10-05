# Exploratory Data Analysis Report: Student Mental Health Ecosystem

**Cohort Size:** 101 Students  
**Data Source:** Anonymized Higher Education Survey (`Student_Mental_health.csv`)  
**Date Processed:** October 2026

---

## Executive Statistical Summary

### 1. Stress Level Distribution
- **Dataset Status:** *Direct Likert Scale Not Available in Dataset.*
- **Closest Valid Analysis / Proxy:** Evaluation of Panic Attacks and Concurrent Multi-Condition Burden (`condition_count`), which serve as empirical behavioral proxies for acute stress manifestations.
- **Acute Stress (Panic Attacks):** 33 students (32.7%).
- **Multi-Condition Load (≥2 Conditions):** 28 students (27.7%).

### 2. Anxiety Distribution
- **Dataset Status:** *Available (`anxiety` / `anxiety_flag`).*
- **Anxiety Prevalence:** 34 of 101 students (33.7%).
- **Gender Breakdown:**
  - Female: 24/75 (32.0%)
  - Male: 10/26 (38.5%)

### 3. Mental Health Risk Stratification
- **Dataset Status:** *Available (Derived composite metric from clinical indicators).*
- **Low Risk:** 37 students (36.6%)
- **Moderate Risk:** 36 students (35.6%)
- **High Risk:** 28 students (27.7%)

### 4. Sleep Quality
- **Dataset Status:** *Not Available in Dataset.*
- **Recommendation:** Future survey waves should integrate the Pittsburgh Sleep Quality Index (PSQI) or average sleep hours per night.

### 5. Study Hours
- **Dataset Status:** *Not Available in Dataset.*
- **Closest Valid Analysis:** Year of study and academic major intensity proxies. Study hours variable was not captured in this survey wave.

### 6. Screen Time
- **Dataset Status:** *Not Available in Dataset.*
- **Recommendation:** Digital wellness tracking modules should capture daily device screen hours.

### 7. Academic Performance (CGPA)
- **Dataset Status:** *Available (`cgpa_range`, `cgpa_midpoint`).*
- **Cohort Mean CGPA Midpoint:** 3.36 (Standard Deviation: 0.58)
- **CGPA Range Distribution:**
  - `3.50 - 4.00`: 48 students (47.5%)
  - `3.00 - 3.49`: 43 students (42.6%)
  - `2.50 - 2.99`: 4 students (4.0%)
  - `0 - 1.99`: 4 students (4.0%)
  - `2.00 - 2.49`: 2 students (2.0%)
- **Depression Prevalence by Academic Standing:**
  - `0 - 1.99`: 0/4 (0.0% depressed)
  - `2.00 - 2.49`: 0/2 (0.0% depressed)
  - `2.50 - 2.99`: 3/4 (75.0% depressed)
  - `3.00 - 3.49`: 19/43 (44.2% depressed)
  - `3.50 - 4.00`: 13/48 (27.1% depressed)

### 8. Social Interaction
- **Dataset Status:** *Not Available in Dataset.*
- **Closest Valid Analysis:** Marital status (`marital_status`) is available as a proxy for primary interpersonal relationship status. Married students: 16 (15.8%).

### 9. Mood
- **Dataset Status:** *Direct Mood Diary Not Available.*
- **Closest Valid Analysis:** Depression indicator (`depression`). Prevalence: 35 students (34.7%).

### 10. Burnout
- **Dataset Status:** *Maslach Burnout Inventory (MBI) Not Available.*
- **Closest Valid Analysis:** Comorbidity score (`condition_count == 3` - having Depression, Anxiety, and Panic Attacks concurrently). Total experiencing severe comorbidity: 10 students (9.9%).

### 11. Demographic Profiles
- **Dataset Status:** *Available (`gender`, `age`, `course`, `faculty`, `year_of_study`).*
- **Gender Distribution:** Female: 75 (74.3%), Male: 26 (25.7%)
- **Age Range:** 18 to 24 years (Mean: 20.5, Median: 19)
- **Academic Seniority:**
  - Year 1: 43 students (42.6%)
  - Year 2: 26 students (25.7%)
  - Year 3: 24 students (23.8%)
  - Year 4: 8 students (7.9%)
- **Faculty Distribution:**
  - Computing & IT: 28 students (27.7%)
  - Engineering: 27 students (26.7%)
  - Humanities & Social Sciences: 14 students (13.9%)
  - Sciences & General: 13 students (12.9%)
  - Allied Health Sciences: 8 students (7.9%)
  - Islamic Studies & Ethics: 7 students (6.9%)
  - Business & Economics: 4 students (4.0%)

### 12. Lifestyle Patterns & Health-Seeking Behavior
- **Dataset Status:** *Available (`treatment_sought`, `treatment_gap`).*
- **Specialist Consultation Rate:** 6 of 101 students (5.9%)
- **Students with ≥1 Mental Health Condition:** 64 (63.4%)
- **Critical Treatment Gap:** 58 students with active symptoms have NOT sought specialist treatment (90.6% of affected cohort)!
