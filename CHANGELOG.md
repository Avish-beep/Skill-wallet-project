# Project Changelog

All notable technical updates to the *Analysing Mental Health in Student Ecosystem* project will be documented in this file chronologically.

---

## [Epic 3] Data Visualization (Responsive and Design of Dashboard Completed)
**Date:** October 07, 2026  
**Status:** Completed  

### Responsive Dashboard Architecture & Design Finalization:
- **Completed SkillWallet Task:** *Epic 3 &rarr; Dashboard &rarr; Responsive and Design of Dashboard*.
- **Accurate Project-Specific Description Authored:** Authored official description explaining student cohort summary (101 students), risk stratification (28 high, 36 moderate), within-gender prevalence comparisons, underclassmen transition vulnerability, departmental clustering, and the 90.6% clinical care deficit.
- **Responsive Canvas Layout Implemented:** Built dynamic 16:9 container architecture (1920×1080) with fluid percentage-based sizing, dark slate header with interactive filter pills (`Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`), 4 aligned executive KPI cards, and 6 card-based visual panels with generous padding.
- **Evidence Screenshots Regenerated:** Generated high-resolution 300 DPI evidence images ([`dashboard_overview.png`](file:///C:/Skillwallet/evidence/epic_03/dashboard_overview.png), 685 KB; [`dashboard_treatment.png`](file:///C:/Skillwallet/evidence/epic_03/dashboard_treatment.png), 532 KB) visually demonstrating the responsive layout, verified KPIs, and zero presence of generic template metrics.
- **Exclusion of Invalid Example Fields:** Strict audit verified zero presence of placeholder metrics (*Average Mental Score*, *Sleep Duration Hours*, *Depression Level*, *Attendance Rate*, *Stress Level*, *Heart Rate Variability*, *Study Hours*, and *Academic Performance*).
- **Automated Verification:** Ran [`scripts/verify_epic_03.py`](file:///C:/Skillwallet/scripts/verify_epic_03.py) confirming raw SHA-256 integrity, processed dataset reconciliation (101 rows, 23 columns, 0 nulls, 0 duplicates), valid Tableau XML, evidence existence, and future epic boundaries.

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
