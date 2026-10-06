# Analysing Mental Health in Student Ecosystem

## 📌 Project Status

**Current Epic:** Epic 1 — Data Collection & Extraction from Database  
**Task:** Downloading the dataset &bull; Understand the data  
**Status:** **IN PROGRESS** *(Baseline ingested & validated; awaiting exact 18-variable SkillWallet resource file)*  

---

## 🎯 Project Objective
This project conducts an empirical investigation into psychological distress, academic standing, and mental health intervention outcomes across university students. Through reproducible Python data engineering, Tableau visual intelligence, and a lightweight Flask web portal, the project provides higher education stakeholders with actionable evidence to address campus wellness challenges.

---

## 🏥 Domain
Healthcare / Student Mental Health & Higher Education Analytics

---

## 🛠 Technology Stack
- **Python 3.11.9:** Data engineering, schema auditing, and ETL pipelines (`pandas`, `numpy`, `openpyxl`)
- **Tableau Desktop 2026.1 & Tableau Public:** Interactive visual analytics, calculated fields, dashboards, and storytelling
- **Flask 3.1.3:** Web portal embedding interactive Tableau visualizations via Web Component API v3
- **Git 2.55.0 & GitHub:** Version control and portfolio hosting

---

## 📊 Dataset & Provenance

### Expected Schema (18 Variables from SkillWallet Specification)
As defined in the SkillWallet subtask *Understand the data*:
`User ID`, `Age`, `Gender`, `Occupation`, `Stress Level`, `Anxiety Score`, `Depression Score`, `Sleep Quality`, `Daily Screen Time (hrs)`, `Physical Activity Level`, `Social Interaction Score`, `Mental Health History`, `Therapy Type`, `Intervention Duration (weeks)`, `Progress Score`, `Medication Usage`, `Support System Strength`, `Work-Life Balance Score`.

### Dataset Ingestion & Status
1. **Ingested Baseline Dataset:** `data/raw/Student_Mental_health.csv` (101 verified observations &times; 11 survey columns). Captures self-reported depression, anxiety, panic attacks, CGPA standing, and academic major.
2. **Authoritative SkillWallet Resource:** When downloaded from the authenticated SkillWallet Task 1 modal into `data/raw/`, the automated script `scripts/inspect_dataset.py` validates its full 18-column schema.

---

## 🔍 Data Validation Summary
- **Total Records Audited:** 101 rows, 11 columns
- **Duplicate Full Rows:** 0 (0.0%)
- **Missing Values:** 1 record in `Age` (0.99%, imputed with cohort median 19.0); all other columns 100% complete.
- **Categorical Casing:** Identified mixed-case strings in `year_of_study` and trailing whitespace in `cgpa_range`.
- **Validation Script:** Executed via `scripts/inspect_dataset.py` with full results documented in `documentation/data_validation_report.md`.

---

## 📂 Repository Structure

```
C:\Skillwallet\
├── data/
│   ├── raw/
│   │   ├── Student_Mental_health.csv       # Ingested baseline survey dataset
│   │   └── SOURCE.md                       # Provenance and source audit documentation
│   └── processed/                          # Destination for cleaned datasets (Epic 2)
├── documentation/
│   ├── project_progress.md                 # Epic-by-epic status tracker
│   ├── data_validation_report.md           # Schema and data quality validation results
│   ├── data_dictionary.md                  # Comprehensive 18-variable field dictionary
│   └── dataset_profile.md                  # Detailed statistical profile of the dataset
├── evidence/
│   └── epic_01/
│       └── README.md                       # Evidence manifest for Epic 1 submission
├── scripts/
│   ├── inspect_dataset.py                  # Reusable dataset inspection & schema validation script
│   └── verify_environment.py               # Python virtual environment check
├── tableau/
│   └── data_source_notes.md                # Data role classifications & Tableau readiness
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
| **Epic 1** | **Data Collection & Extraction from Database** | **IN PROGRESS** |
| Epic 2 | Data Preparation | *Not Started* |
| Epic 3 | Data Visualization | *Not Started* |
| Epic 4 | Dashboard | *Not Started* |
| Epic 5 | Story | *Not Started* |
| Epic 6 | Performance Testing | *Not Started* |
| Epic 7 | Web Integration | *Not Started* |
| Epic 8 | Project Demonstration & Documentation | *Not Started* |

---

## 💻 How to Run Dataset Inspection (Windows)

Open PowerShell and execute:

```powershell
cd C:\Skillwallet

# Inspect the dataset against the 18 expected SkillWallet fields
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\inspect_dataset.py" "data\raw\Student_Mental_health.csv"

# Verify environment packages
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\verify_environment.py"
```

---

## 📊 Tableau Readiness
- The dataset format (`.csv`) is 100% compatible with **Tableau Desktop 2026.1**.
- Text columns map directly to discrete Dimension pills; numerical fields map to Measure pills.
- Documented in detail in `tableau/data_source_notes.md`.

---

## 📁 Evidence Files Created for Epic 1
- `data/raw/SOURCE.md`
- `documentation/data_validation_report.md`
- `documentation/data_dictionary.md`
- `documentation/dataset_profile.md`
- `tableau/data_source_notes.md`
- `scripts/inspect_dataset.py`
- `evidence/epic_01/README.md`

---

## 🔮 Future Work (Planned Epics)
- **Epic 2 (Data Preparation):** Data cleaning, categorical standardization, handling missing records, and derived feature engineering.
- **Epic 3 (Data Visualization):** Construction of individual Tableau worksheets and calculated fields.
- **Epic 4 & 5 (Dashboard & Story):** Multi-sheet interactive dashboard with global filters and 6-scene storyboard.
- **Epic 6, 7 & 8:** Performance recording, Flask web portal deployment, and project demonstration.
