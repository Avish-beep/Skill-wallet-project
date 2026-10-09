# End-to-End Project Development Procedure

**Project Title:** Analysing Mental Health in Student Ecosystem
**Domain:** Healthcare Analytics / Higher Education Mental Health
**Student Developer:** Avishkar Padavi
**Institution:** Indira College of Engineering and Management
**Curriculum Module:** Data Analytics with Tableau (SkillWallet)

---

## 1. Project Overview & Clinical Objectives
This capstone investigates self-reported mental health distress (Depression, Anxiety, Panic Attacks), academic standing (CGPA), and institutional treatment engagement across higher education students. Through Python data engineering, Tableau visual intelligence, and an accessible portfolio website, the project quantifies campus mental health vulnerability and care gaps.

---

## 2. Dataset Acquisition & Schema Inspection
- **Baseline File:** `data/raw/Student_Mental_health.csv`
- **Integrity Validation:** SHA-256 Checksum (`c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`)
- **Survey Dimensions:** 101 student observations &times; 11 survey columns capturing timestamps, gender, age, course of study, current academic year, CGPA grade brackets, marital status, and self-reported depression, anxiety, panic attack, and specialist treatment indicators.

---

## 3. Data Cleaning & Feature Engineering Pipeline
Implemented reproducibly in `scripts/prepare_dataset.py`:
1. **Missing Value Treatment:** Imputed 1 single missing `Age` value using cohort median (19.0).
2. **Standardization:** Stripped whitespace and normalized string formatting for all categorical fields.
3. **Faculty Aggregation:** Categorized 43 raw degree programs into 7 macro academic faculties:
   - Computing & IT (N=28)
   - Engineering (N=26)
   - Humanities & Social Sciences (N=14)
   - Natural Sciences & General (N=13)
   - Islamic Studies & Education (N=8)
   - Allied Health Sciences (N=7)
   - Business & Economics (N=5)
4. **Numeric CGPA Midpoint:** Mapped discrete string CGPA ranges (`3.50 - 4.00`, `3.00 - 3.49`, etc.) into statistical midpoints (`3.75`, `3.25`).
5. **Feature Engineering (12 Derived Features):**
   - Binary Condition Flags (`Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`, `Treatment_Sought_Flag`)
   - `Condition_Count`: Total concurrent symptoms per student (0 to 3).
   - `Mental_Health_Risk`: Low Risk (0 conditions, 36.6%), Moderate Risk (1 condition, 35.6%), High Risk (&ge;2 conditions, 27.7%).
   - `Treatment_Gap`: Categorical care deficit highlighting that 58 of 64 symptomatic students never consulted a specialist.

---

## 4. Tableau Visual Intelligence & Worksheets
Constructed in Tableau Desktop (`tableau/student_mental_health_visualizations.twb`):
1. **Distribution of Mental Health Risk Levels:** Discrete bar chart showing population risk tiers.
2. **Self-Reported Conditions by Gender:** Clustered bar chart showing within-gender condition prevalence for females (N=75) and males (N=26).
3. **Mental Health Risk Across Age Groups:** Stacked bar chart analyzing comorbidity burdens across underclassmen (18–20) and upperclassmen (21–24).
4. **Mental Health Risk by Faculty:** Horizontal stacked bar chart across 7 academic disciplines.
5. **Distribution of Condition Count:** Comorbidity histogram (0, 1, 2, 3 conditions).
6. **Student Mental Health Treatment Gap:** Categorical bar chart quantifying the 90.6% specialist consultation care deficit.
7. **Prevalence of Self-Reported Conditions:** Benchmark bar chart comparing Depression (34.7%), Anxiety (33.7%), and Panic Attack (32.7%) rates.
8. **CGPA Midpoint and Mental Health Risk:** Boxplot and stripplot demonstrating high academic performance (mean 3.45) among high-distress students.
9. **Age and Condition Count:** Bar chart showing condition load across undergraduate ages (18–24).
10. **Treatment Seeking Across Risk Levels:** Stacked chart showing 78.6% of high-risk students have never sought treatment.

---

## 5. Dashboards & Responsive Architecture
- **Dashboard 1: Student Mental Health Overview:** Responsive 16:9 layout featuring 4 executive KPI cards, 6 visual panels, and multi-tier interactive filters (`Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`).
- **Dashboard 2: Mental Health Risk & Treatment Dashboard:** Specialized 2 &times; 3 healthcare grid focused on the campus clinical treatment gap and comorbidity severity.

---

## 6. Web Application & Portfolio Integration
- **Framework:** Vite + React + TypeScript + Tailwind CSS v4 + Lucide Icons.
- **Tableau Public Integration:** Responsive iframe embedding with third-party cookie fallback.
- **Scrollytelling:** Interactive 6-scene story section highlighting the investigation progression.
- **Responsive Testing:** Automated Playwright test suite verifying 1920x1080, 1440x900, 768x1024, and 390x844 viewports with 0px horizontal overflow.

---

## 7. Video Presentation Production
- **Duration:** 06:24 (6 minutes 24 seconds).
- **Format:** 1080p Full HD @ 30fps MPEG-4 / AAC audio.
- **Narration:** Indian English Neural Voice (`en-IN-PrabhatNeural` at `-14%` rate) providing humanized, confident academic narration.
- **Subtitles & Text:** Synchronized WebVTT (`captions.vtt`), SubRip (`captions.srt`), transcript (`transcript.md`), and scene plan (`scene_plan.md`).

---

## 8. Licensing & Repository Governance
- **Software Code:** Standard MIT License (`LICENSE`) covering original application code and scripts.
- **Documentation:** Creative Commons Attribution 4.0 International (`LICENSE-DOCS`) covering written analysis and narrative scripts.
- **Dataset Audit:** Comprehensive provenance and non-commercial academic usage terms (`DATA_LICENSE.md`).
- **Attribution Notices:** Third-party dependency notices (`THIRD_PARTY_NOTICES.md`).
- **Community Standards:** Contributor guidelines (`CONTRIBUTING.md`), Code of Conduct (`CODE_OF_CONDUCT.md`), Security policy (`SECURITY.md`), and Citation metadata (`CITATION.cff`).

---

## 9. Verification & Local Setup Commands (Windows)
```powershell
cd C:\Skillwallet

# Run data preparation pipeline
& "venv\Scripts\python.exe" "scripts\prepare_dataset.py"

# Verify Epic 3 data integrity & workbook XML
& "venv\Scripts\python.exe" "scripts\verify_epic_03.py"

# Run automated responsive website test suite
& "venv\Scripts\python.exe" "scripts\test_website_responsive.py"

# Build static portfolio website
cd website
npm run build
```
