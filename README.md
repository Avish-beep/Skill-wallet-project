# Analysing Mental Health in Student Ecosystem

## 📌 Project Status

**Current Milestone:** Epic 3 — Data Visualization (Responsive and Design of Dashboard Completed)  
**Completed Epics:** Epic 1 (Data Collection), Epic 2 (Data Preparation), Epic 3 (Data Visualization)  
**Upcoming Epics:** Epic 4–8 (Not Started)  
**Status:** **EPIC 3 COMPLETED**  

---

## 🎯 Project Objective
This project conducts an empirical investigation into psychological distress, academic standing, and mental health intervention outcomes across university students. Through reproducible Python data engineering, Tableau visual intelligence, and a lightweight Flask web portal, the project provides higher education stakeholders with actionable evidence to address campus wellness challenges.

---

## 🏥 Domain
Healthcare / Student Mental Health & Higher Education Analytics

---

## 🛠 Technology Stack
- **Python 3.11.9:** Data engineering, schema auditing, ETL pipelines, and feature derivation (`pandas`, `numpy`, `openpyxl`, `matplotlib`, `seaborn`)
- **Tableau Desktop 2026.1 & Tableau Public:** Interactive visual analytics, calculated fields, worksheets, responsive dashboards, and storytelling
- **Flask 3.1.3:** Web portal embedding interactive Tableau visualizations via Web Component API v3
- **Git 2.55.0 & GitHub:** Version control and portfolio hosting

---

## 📊 Dataset Architecture & Provenance

### 1. Raw Baseline Dataset (Immutable)
- **Location:** `data/raw/Student_Mental_health.csv`
- **Integrity:** SHA-256 Verified (`c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`)
- **Dimensions:** 101 rows &times; 11 survey columns

### 2. Processed Analytical Dataset (Tableau Source)
- **Location:** `data/processed/student_mental_health_processed.csv`
- **Dimensions:** 101 rows &times; 23 analytical columns
- **Completeness:** 100% complete (0 null values, 0 duplicate rows)
- **Data Integrity Standard:** Constructed strictly from verified survey columns. Generic example metrics from placeholder task templates (such as *Average Mental Score*, *Sleep Duration*, *Attendance Rate*, and *Heart Rate Variability*) do not exist in our data and were strictly excluded.

---

## 📈 Current Project Progress

| Epic | Epic Name | Complexity | Estimated Duration | Status | Notes |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **Epic 1** | **Data Collection & Extraction from Database** | Medium | 5 hours | **COMPLETED** | Ingested baseline survey data, validated schema, audited dictionary. |
| **Epic 2** | **Data Preparation** | Medium | 6 hours | **COMPLETED** | ETL pipeline executed, 1 missing value imputed, 12 features engineered. |
| **Epic 3** | **Data Visualization** | High | 8 hours | **COMPLETED** | 10 unique worksheets + 2 responsive dashboards built in Tableau (.twb), 12 evidence PNGs rendered, responsive layout verified. |
| **Epic 4** | Dashboard | High | 6 hours | *Not Started* | Scheduled for next phase |
| **Epic 5** | Story | Medium | 4 hours | *Not Started* | Scheduled for next phase |
| **Epic 6** | Performance Testing | Medium | 4 hours | *Not Started* | Scheduled for next phase |
| **Epic 7** | Web Integration | High | 6 hours | *Not Started* | Scheduled for next phase |
| **Epic 8** | Project Demonstration & Documentation | Medium | 5 hours | *Not Started* | Scheduled for next phase |

---

## 📊 Tableau Visualization Work (Epic 3: Responsive and Design of Dashboard)

### 1. Official Dashboard Description
> The **Student Mental Health Analysis Dashboard** provides an interactive visual overview of self-reported mental-health conditions among 101 surveyed university students. It utilizes validated demographic, academic, mental-health-risk, condition-count, and treatment-seeking fields to help educational stakeholders and wellness administrators identify patterns across gender, age group, and academic faculty.
> 
> - **Executive KPI Cards:** Summarize the student cohort (101 students) and stratify risk tiers (28 high risk, 36 moderate risk, 58 untreated symptomatic students).
> - **Risk Distribution:** Illustrates the proportion of students categorized as Low (36.6%), Moderate (35.6%), and High Risk (27.7%).
> - **Gender Visualization:** Compares self-reported depression, anxiety, and panic attack indicators between female (N=75) and male (N=26) cohorts.
> - **Age-Group & Faculty Views:** Highlight how comorbidity risk is distributed across undergraduate seniority levels (18–20 vs. 21–24) and 7 macro academic disciplines.
> - **Treatment-Gap Visualizations:** Highlight self-reported treatment-seeking patterns, revealing that 90.6% of symptomatic students have not accessed specialist care.
> - **Condition-Count Visualization:** Displays the distribution of concurrent self-reported conditions (0 to 3), detailing comorbidity burdens.

### 2. Dashboards Created (2 Responsive Dashboards)
- **`Student Mental Health Overview`:** Responsive 16:9 layout (1920×1080) featuring interactive filter bar (`Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`), 4 aligned executive KPI cards, and 6 visual panels in a clean card container grid.
- **`Mental Health Risk & Treatment Dashboard`:** Specialized 2 &times; 3 clinical healthcare grid focused on the campus mental health care gap, specialist consultation rates, and comorbidity severity.

### 3. Unique Worksheets Created (10 Worksheets)
1. **Distribution of Mental Health Risk Levels Among Students:** Discrete bar chart (Low: 36.6%, Moderate: 35.6%, High: 27.7%).
2. **Self-Reported Mental Health Conditions by Gender:** Clustered bar chart showing within-gender condition prevalence for females (N=75) and males (N=26).
3. **Mental Health Risk Across Age Groups:** Stacked column chart analyzing comorbidity burdens across underclassmen (18–20) and upperclassmen (21–24).
4. **Mental Health Risk by Faculty:** Horizontal stacked bar chart across 7 academic disciplines.
5. **Distribution of Mental Health Condition Count:** Discrete histogram tracking comorbidity load (0 to 3 concurrent conditions).
6. **Student Mental Health Treatment Gap:** Categorical bar chart quantifying the 90.6% deficit in specialist consultation among symptomatic students.
7. **Prevalence of Self-Reported Conditions:** Benchmark bar chart comparing Depression (34.7%), Anxiety (33.7%), and Panic Attack (32.7%) rates.
8. **CGPA Midpoint and Mental Health Risk:** Boxplot and stripplot showing high academic performance (mean CGPA midpoint 3.45) among high-risk students.
9. **Age and Mental Health Condition Count:** Mean condition count bar chart confirming that vulnerability spans all undergraduate ages (18–24).
10. **Treatment Seeking Across Mental Health Risk Levels:** Stacked bar chart demonstrating that 78.6% of high-risk students have never consulted a clinical specialist.

### 4. Tableau Workbook File
- **Path:** `tableau/student_mental_health_visualizations.twb`

---

## 📂 Repository Structure

```
C:\Skillwallet\
├── data/
│   ├── raw/
│   │   ├── Student_Mental_health.csv       # Ingested baseline survey dataset (immutable)
│   │   └── SOURCE.md                       # Provenance and source audit documentation
│   └── processed/
│       └── student_mental_health_processed.csv # Cleaned & feature-engineered dataset (23 cols)
├── documentation/
│   ├── project_progress.md                 # Epic-by-epic status tracker
│   ├── visualization_report.md             # Comprehensive Epic 3 visualization report
│   ├── visualization_dictionary.md         # Matrix of worksheets, dimensions, measures & insights
│   ├── data_preparation_report.md          # Epic 2 transformation report
│   ├── missing_value_treatment.md          # Methodological justification for Age imputation
│   ├── column_mapping.md                   # Raw to processed field mapping
│   ├── derived_fields.md                   # Logic and formulas for 12 engineered features
│   ├── outlier_analysis.md                 # IQR statistical outlier audit
│   ├── data_validation_report.md           # Schema validation report (Epic 1)
│   └── data_dictionary.md                  # Comprehensive field dictionary
├── evidence/
│   ├── epic_01/
│   │   └── README.md                       # Evidence manifest for Epic 1
│   ├── epic_02/
│   │   └── README.md                       # Evidence manifest for Epic 2
│   └── epic_03/
│       ├── README.md                       # Evidence manifest for Epic 3
│       ├── dashboard_overview.png          # High-resolution render of Dashboard 1
│       ├── dashboard_treatment.png         # High-resolution render of Dashboard 2
│       ├── mental_health_risk.png          # Worksheet 1 render
│       ├── conditions_by_gender.png        # Worksheet 2 render
│       ├── risk_by_age_group.png           # Worksheet 3 render
│       ├── faculty_risk.png                # Worksheet 4 render
│       ├── condition_count.png             # Worksheet 5 render
│       ├── treatment_gap.png               # Worksheet 6 render
│       ├── condition_prevalence.png        # Worksheet 7 render
│       ├── cgpa_risk.png                   # Worksheet 8 render
│       ├── age_condition.png               # Worksheet 9 render
│       └── treatment_by_risk.png           # Worksheet 10 render
├── scripts/
│   ├── generate_visualizations.py          # High-resolution visualization generator
│   ├── generate_tableau_twb.py             # Tableau Workbook XML builder
│   ├── verify_epic_03.py                   # Automated Epic 3 integrity verification script
│   ├── audit_visualization_metrics.py      # Statistical metric verification script
│   ├── prepare_dataset.py                  # Reproducible data preparation pipeline
│   ├── inspect_dataset.py                  # Schema inspection and validation tool
│   └── verify_environment.py               # Virtual environment check
├── tableau/
│   ├── student_mental_health_visualizations.twb # Tableau Workbook file
│   ├── dashboard_design.md                 # Dashboard architecture and layout documentation
│   ├── calculated_fields.md                # Verified calculated fields documentation
│   ├── tableau_setup.md                    # Tableau Desktop setup and publishing guide
│   └── data_source_notes.md                # Data roles, calculated fields, and dashboard specifications
├── flask_app/                              # Web application architecture (Epic 7)
├── .gitignore                              # Git exclusion rules
├── .env.example                            # Template for environment configuration
├── requirements.txt                        # Pinned dependencies
├── CHANGELOG.md                            # Chronological milestone log
└── README.md                               # Project documentation
```

---

## 💻 How to Run & Verify Visualizations (Windows)

Open PowerShell and execute:

```powershell
cd C:\Skillwallet

# Re-generate all high-resolution visualization PNGs
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\generate_visualizations.py"

# Re-build Tableau Workbook XML
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\generate_tableau_twb.py"

# Run automated integrity and reconciliation verification
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\verify_epic_03.py"

# Open in Tableau Desktop 2026.1
& "C:\Program Files\Tableau\Tableau 2026.1\bin\tableau.exe" "C:\Skillwallet\tableau\student_mental_health_visualizations.twb"
```

---

## ⚠️ Epidemiological Disclaimers & Data Limitations
- **Self-Reported Data:** Visualizations represent student responses from a self-administered questionnaire, not clinical DSM-5 diagnoses.
- **Non-Causal Observations:** Academic indicators (e.g. CGPA midpoint) and mental health conditions are evaluated correlationally without causal claims.
- **Cohort Scope:** Observations are based on N=101 university students. Subgroup breakdowns across smaller faculties are descriptive.
