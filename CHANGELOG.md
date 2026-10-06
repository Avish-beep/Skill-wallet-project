# Project Changelog

All notable technical updates to the *Analysing Mental Health in Student Ecosystem* project will be documented in this file chronologically.

---

## [Epic 3] Data Visualization
**Date:** October 07, 2026  
**Status:** Completed  

### Activities & Deliverables:
- **Tableau Workbook Construction (`tableau/student_mental_health_visualizations.twb`):** Authored native Tableau Workbook XML connecting to `data/processed/student_mental_health_processed.csv`, defining metadata, field roles, and calculated fields.
- **10 Unique Worksheets Created:**
  1. *Mental Health Risk Distribution Among Students* (Low: 36.6%, Moderate: 35.6%, High: 27.7%).
  2. *Mental Health Conditions by Gender* (Clustered bars showing within-gender prevalence for depression, anxiety, panic attacks).
  3. *Mental Health Risk Across Age Groups* (Stacked column chart comparing 18–20 and 21–24 cohorts).
  4. *Mental Health Risk by Faculty* (Horizontal stacked bar chart across 7 academic faculties).
  5. *Distribution of Mental Health Condition Count* (Discrete histogram of comorbidity count from 0 to 3).
  6. *Student Mental Health Treatment Gap* (Categorical bar chart showing 90.6% untreated symptomatic students).
  7. *Prevalence of Self-Reported Mental Health Conditions* (Benchmark comparison: Depression 34.7%, Anxiety 33.7%, Panic Attacks 32.7%).
  8. *CGPA and Mental Health Risk* (Boxplot and stripplot showing high academic standing among high-risk students).
  9. *Age and Mental Health Condition Count* (Bar chart of average conditions across ages 18–24).
  10. *Treatment Seeking Across Mental Health Risk Levels* (Stacked bar demonstrating that 78.6% of high-risk students never sought specialist consultation).
- **2 Professional Dashboards Created:**
  1. *Student Mental Health Overview* (Executive 3-tier layout with 3 BAN KPI cards and 6 analytical charts).
  2. *Mental Health Risk & Treatment Dashboard* (Clinical 2 &times; 2 grid focused on campus health center interventions).
- **Calculated Fields Implemented:** Authored 9 Tableau calculations for total student count, risk category percentages, prevalence rates, and treatment gap percentages.
- **Rendering Pipeline & Evidence Generation (`scripts/generate_visualizations.py`):** Generated 12 high-resolution 300 DPI PNG artifacts in `evidence/epic_03/`.
- **Comprehensive Documentation:**
  - `documentation/visualization_report.md`: Full 14-section technical visualization report.
  - `documentation/visualization_dictionary.md`: Matrix mapping chart types, dimensions, measures, purposes, and insights.
  - `tableau/data_source_notes.md`: Updated with worksheet notes, calculated field definitions, and dashboard architectures.
  - `evidence/epic_03/README.md`: Evidence manifest documenting deliverables and validation.
- **Validation & Limitations:** Reconciled respondent counts (N=101) across all views. Highlighted that data reflects self-reported student survey responses rather than clinical diagnoses. Tableau Public publication marked as pending manual authentication.

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
