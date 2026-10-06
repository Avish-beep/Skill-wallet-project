# Project Changelog

All notable technical updates to the *Analysing Mental Health in Student Ecosystem* project will be documented in this file chronologically.

---

## [Epic 2] Data Preparation
**Date:** October 06, 2026  
**Status:** Completed  

### Activities & Deliverables:
- **Reproducible Pipeline (`scripts/prepare_dataset.py`):** Developed and executed end-to-end data preparation script converting raw baseline data into an analytical-ready dataset without mutating original files.
- **Dataset Generation:** Outputted `data/processed/student_mental_health_processed.csv` (101 records &times; 23 columns, 0 nulls, 0 duplicate rows).
- **Missing Value Imputation:** Addressed single missing entry in `Age` at row index 43 via demographic cohort median imputation (median = 19.0 years); preserved 100% of observations without row dropping.
- **Categorical Standardization:** Standardized string casings across `Gender`, `Course`, `Year_of_Study`, `CGPA_Range`, and binary response flags; trimmed surrounding whitespace.
- **Academic Domain Mapping:** Grouped 43 specific degree programs into 6 standardized higher-education faculties (`Computing & IT`, `Engineering`, `Healthcare & Sciences`, `Humanities & Social Sciences`, `Business & Economics`, `Islamic Studies`).
- **Feature Engineering (12 Derived Fields):**
  - Generated unique respondent primary key (`User_ID`: `STU_001`–`STU_101`).
  - Derived demographic age cohort (`Age_Group`: `18-19`, `20-21`, `22-24`).
  - Extracted numeric study level (`Study_Year_Num`: 1–4).
  - Decomposed GPA ranges into numeric bounds and continuous midpoint metric (`CGPA_Min`, `CGPA_Max`, `CGPA_Midpoint`).
  - Engineered numeric binary indicators for conditions (`Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`).
  - Computed composite comorbidity score (`Condition_Count`: 0–3) and clinical triage categorization (`Mental_Health_Risk`: `None`, `Low`, `Moderate`, `Severe`).
  - Formulated unmet mental health support gap indicator (`Treatment_Gap`).
- **Documentation & Analysis:**
  - `documentation/data_preparation_report.md`: Complete before/after transformation audit and summary statistics.
  - `documentation/missing_value_treatment.md`: Formal justification and impact evaluation for missing value handling.
  - `documentation/column_mapping.md`: Comprehensive dictionary mapping 11 raw headers to 23 processed fields and Tableau roles.
  - `documentation/derived_fields.md`: Detailed mathematical definitions and clinical rationale for all 12 engineered features.
  - `documentation/outlier_analysis.md`: Statistical IQR outlier assessment verifying data integrity.
  - `tableau/data_source_notes.md`: Updated Tableau Desktop 2026.1 and Tableau Public data connection specifications.
  - `evidence/epic_02/README.md`: Evidence manifest cataloging all Epic 2 audit artifacts.

---

## [Epic 1] Data Collection & Extraction from Database
**Date:** October 06, 2026  
**Status:** Completed  

### Activities & Deliverables:
- **Environment Setup:** Virtual environment verified at `C:\Skillwallet\venv` with Python 3.11.9, Pandas, and NumPy.
- **Directory Structure:** Initialized standardized project structure with `data/raw/`, `data/processed/`, `scripts/`, `documentation/`, `evidence/epic_01/`, `tableau/`, and `flask_app/`.
- **Dataset Ingestion & Validation:** Ingested baseline survey dataset (`data/raw/Student_Mental_health.csv`, 101 rows &times; 11 columns, SHA256 verified).
- **Quality Audit:** Developed and ran `scripts/inspect_dataset.py`, generating `documentation/data_validation_report.md` and `documentation/dataset_profile.md`.
- **Documentation:** Prepared comprehensive field dictionary (`documentation/data_dictionary.md`) and evidence manifest (`evidence/epic_01/README.md`).
