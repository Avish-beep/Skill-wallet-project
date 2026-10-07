# Project Changelog

All notable technical updates to the *Analysing Mental Health in Student Ecosystem* project will be documented in this file chronologically.

---

## [Epic 3] Data Visualization (Integrity Validated & Rebuilt)
**Date:** October 07, 2026  
**Status:** Completed  

### Dashboard Data Integrity Correction:
- **Exclusion of Invalid Example Fields:** Conducted a comprehensive audit and removed all references to generic placeholder metrics found in the task template (such as *Average Mental Score*, *Avg. Sleep Duration Hours*, *Avg. Depression Level*, *Avg. Attendance Rate*, *Stress Level*, *Heart Rate Variability*, and *Study Hours*).
- **Rebuilt Dashboard 1 (`Student Mental Health Overview`):**
  - Implemented 4 validated KPI cards strictly computed from real columns: Total Students (101), High Risk Students (28 / 27.7%), Moderate Risk Students (36 / 35.6%), and Treatment Gap Students (58 / 90.6% of symptomatic cohort).
  - Configured 6 analytical panels in a balanced 2 × 3 visual grid (Risk Distribution, Conditions by Gender, Risk by Age Group, Faculty Risk, Treatment Gap, Condition Count).
- **Rebuilt Dashboard 2 (`Mental Health Risk & Treatment Dashboard`):**
  - Constructed dedicated clinical care dashboard with 6 panels covering specialist treatment seeking across risk tiers, treatment gap distribution, comorbidity histogram, gender disparity, risk distribution, and faculty risk.
- **Evidence Screenshots Regenerated:** Regenerated all 12 high-resolution 300 DPI PNG artifacts in `evidence/epic_03/` from the real dataset.
- **Tableau XML Re-authored:** Updated `tableau/student_mental_health_visualizations.twb` ensuring full schema alignment with `data/processed/student_mental_health_processed.csv`.
- **Automated Validation:** Updated and passed `scripts/verify_epic_03.py` confirming zero invalid keywords in XML, dataset reconciliation (101 rows), and future epic boundaries.

### Initial Activities & Deliverables:
- **Tableau Workbook Construction (`tableau/student_mental_health_visualizations.twb`):** Authored native Tableau Workbook XML connecting to `data/processed/student_mental_health_processed.csv`.
- **10 Unique Worksheets Created:** Documented and verified across all demographic, clinical, and academic dimensions.
- **Comprehensive Documentation:** Created `documentation/visualization_report.md`, `documentation/visualization_dictionary.md`, and updated `tableau/data_source_notes.md`.

---

## [Epic 2] Data Preparation
**Date:** October 06, 2026  
**Status:** Completed  

### Activities & Deliverables:
- **Reproducible Pipeline (`scripts/prepare_dataset.py`):** Developed and executed end-to-end data preparation script converting raw baseline data into an analytical-ready dataset without mutating original files.
- **Dataset Generation:** Outputted `data/processed/student_mental_health_processed.csv` (101 records &times; 23 columns, 0 nulls, 0 duplicate rows).
- **Missing Value Imputation:** Addressed single missing entry in `Age` at row index 43 via demographic cohort median imputation (median = 19.0 years); preserved 100% of observations without row dropping.
- **Categorical Standardization:** Standardized string casings across `Gender`, `Course`, `Year_of_Study`, `CGPA_Range`, and binary response flags; trimmed surrounding whitespace.
- **Academic Domain Mapping:** Grouped 43 specific degree programs into 7 standardized higher-education faculties.
- **Feature Engineering (12 Derived Fields):** Generated `User_ID`, `Age_Group`, `Faculty`, `CGPA_Midpoint`, binary flags, `Condition_Count`, `Mental_Health_Risk`, and `Treatment_Gap`.

---

## [Epic 1] Data Collection & Extraction from Database
**Date:** October 06, 2026  
**Status:** Completed  

### Activities & Deliverables:
- **Environment Setup:** Virtual environment verified at `C:\Skillwallet\venv` with Python 3.11.9, Pandas, and NumPy.
- **Directory Structure:** Initialized standardized project structure.
- **Dataset Ingestion & Validation:** Ingested baseline survey dataset (`data/raw/Student_Mental_health.csv`, 101 rows &times; 11 columns, SHA256 verified).
- **Quality Audit:** Developed and ran `scripts/inspect_dataset.py`, generating `documentation/data_validation_report.md` and `documentation/dataset_profile.md`.
