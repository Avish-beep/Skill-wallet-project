# Analysing Mental Health in Student Ecosystem

## 📌 Project Status

**Current Epic:** Epic 2 — Data Preparation  
**Task:** Prepare the Data for Visualization  
**Status:** **COMPLETED** (Epic 1 & Epic 2 Completed; Epics 3–8 Not Started)  

---

## 🎯 Project Objective
This project conducts an empirical investigation into psychological distress, academic standing, and mental health intervention outcomes across university students. Through reproducible Python data engineering, Tableau visual intelligence, and a lightweight Flask web portal, the project provides higher education stakeholders with actionable evidence to address campus wellness challenges.

---

## 🏥 Domain
Healthcare / Student Mental Health & Higher Education Analytics

---

## 🛠 Technology Stack
- **Python 3.11.9:** Data engineering, schema auditing, ETL pipelines, and feature derivation (`pandas`, `numpy`, `openpyxl`)
- **Tableau Desktop 2026.1 & Tableau Public:** Interactive visual analytics, calculated fields, dashboards, and storytelling
- **Flask 3.1.3:** Web portal embedding interactive Tableau visualizations via Web Component API v3
- **Git 2.55.0 & GitHub:** Version control and portfolio hosting

---

## 📊 Dataset & ETL Architecture

### 1. Raw Baseline Dataset
- **Location:** `data/raw/Student_Mental_health.csv`
- **Integrity:** Preserved as immutable source (SHA256: `c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`)
- **Dimensions:** 101 rows &times; 11 survey columns

### 2. Processed Analytical Dataset (Epic 2 Deliverable)
- **Location:** `data/processed/student_mental_health_processed.csv`
- **Dimensions:** 101 rows &times; 23 analytical columns
- **Completeness:** 100% complete (0 null values, 0 duplicate rows)
- **Transformations Executed:**
  - Standardized column headers and string casings.
  - Imputed single missing `Age` value (row 43) using cohort median (19.0 years).
  - Derived 12 analytical features including unique keys (`User_ID`), faculty taxonomy (`Faculty`), continuous academic metrics (`CGPA_Midpoint`), clinical condition flags (`Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`), comorbidity index (`Condition_Count`), clinical risk triage (`Mental_Health_Risk`), and support deficit indicator (`Treatment_Gap`).

---

## 🔍 Data Preparation & Feature Engineering Summary

| Feature Category | Engineered Fields | Purpose & Analytical Value |
|---|---|---|
| **Identity & Cohorts** | `User_ID`, `Age_Group` | Granular student distinct counting (`COUNTD`) and age band stratification (18–19, 20–21, 22–24). |
| **Academic Profiling** | `Faculty`, `Study_Year_Num`, `CGPA_Min`, `CGPA_Max`, `CGPA_Midpoint` | Macro academic domain grouping (6 faculties) and continuous GPA quantification for correlation analysis. |
| **Clinical Flags** | `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag` | 0/1 binary numeric variables for direct rate calculation (`SUM(Flag)/COUNT(User_ID)`). |
| **Comorbidity & Triage** | `Condition_Count`, `Mental_Health_Risk` | Severity indexing (0 to 3 conditions) and risk stratification (`None`, `Low`, `Moderate`, `Severe`). |
| **Healthcare Access** | `Treatment_Gap` | Identification of symptomatic students who have not sought professional treatment. |

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
│   ├── data_preparation_report.md          # Comprehensive Epic 2 transformation report
│   ├── missing_value_treatment.md          # Methodological justification for Age imputation
│   ├── column_mapping.md                   # Raw to processed field mapping & data types
│   ├── derived_fields.md                   # Logic and formulas for 12 engineered features
│   ├── outlier_analysis.md                 # IQR statistical outlier audit
│   ├── data_validation_report.md           # Schema validation report (Epic 1)
│   ├── data_dictionary.md                  # Comprehensive field dictionary
│   └── dataset_profile.md                  # Detailed statistical profile of baseline
├── evidence/
│   ├── epic_01/
│   │   └── README.md                       # Evidence manifest for Epic 1
│   └── epic_02/
│       └── README.md                       # Evidence manifest for Epic 2
├── scripts/
│   ├── prepare_dataset.py                  # End-to-end reproducible data preparation pipeline
│   ├── inspect_dataset.py                  # Schema inspection and validation tool
│   └── verify_environment.py               # Virtual environment check
├── tableau/
│   └── data_source_notes.md                # Field roles, color palettes, and Tableau readiness
├── flask_app/                              # Web application architecture (Epic 7)
├── .gitignore                              # Git exclusion rules
├── .env.example                            # Template for environment configuration
├── requirements.txt                        # Pinned dependencies
├── CHANGELOG.md                            # Chronological milestone log
└── README.md                               # Project documentation
```

---

## 📈 Current Progress

| Epic | Epic Name | Status |
| :---: | :--- | :---: |
| **Epic 1** | **Data Collection & Extraction from Database** | **COMPLETED** |
| **Epic 2** | **Data Preparation** | **COMPLETED** |
| Epic 3 | Data Visualization | *Not Started* |
| Epic 4 | Dashboard | *Not Started* |
| Epic 5 | Story | *Not Started* |
| Epic 6 | Performance Testing | *Not Started* |
| Epic 7 | Web Integration | *Not Started* |
| Epic 8 | Project Demonstration & Documentation | *Not Started* |

---

## 💻 How to Run the Pipeline (Windows)

Open PowerShell and execute:

```powershell
cd C:\Skillwallet

# Run the complete data preparation pipeline
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\prepare_dataset.py"

# Inspect dataset schema and quality
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\inspect_dataset.py" "data\processed\student_mental_health_processed.csv"
```

---

## 📊 Tableau Readiness
- The processed dataset (`data/processed/student_mental_health_processed.csv`) is 100% prepared for **Tableau Desktop 2026.1** and **Tableau Public**.
- All categorical fields are cleanly formatted for discrete Dimension pills.
- Continuous numerical fields (`CGPA_Midpoint`, binary flags, `Condition_Count`) are configured for Measure aggregations.
- Field configurations and candidate calculated fields are documented in `tableau/data_source_notes.md`.

---

## 📁 Evidence Files Created for Epic 2
- `data/processed/student_mental_health_processed.csv`
- `scripts/prepare_dataset.py`
- `documentation/data_preparation_report.md`
- `documentation/missing_value_treatment.md`
- `documentation/column_mapping.md`
- `documentation/derived_fields.md`
- `documentation/outlier_analysis.md`
- `tableau/data_source_notes.md`
- `evidence/epic_02/README.md`

---

## 🔮 Next Planned Phase
- **Epic 3 (Data Visualization):** Construction of individual Tableau worksheets and calculated fields once authorized.
