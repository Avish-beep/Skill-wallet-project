# Evidence Manifest: Epic 2 — Data Preparation
## Project: Analysing Mental Health in Student Ecosystem

This manifest documents all artifacts, datasets, transformation pipelines, and analytical reports generated to substantiate full completion of **Epic 2: Data Preparation**.

---

### 1. Ingested & Processed Datasets

| Dataset File | Rows | Columns | Null Values | Status | Description |
|---|---|---|---|---|---|
| `data/raw/Student_Mental_health.csv` | 101 | 11 | 1 (Age) | **Preserved / Immutable** | Original raw baseline survey data (SHA256: `c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`). |
| `data/processed/student_mental_health_processed.csv` | 101 | 23 | 0 (0.0%) | **Final Processed** | Cleaned, standardized, fully imputed, and feature-engineered dataset ready for Tableau visualization. |

---

### 2. ETL & Reproducible Scripts

- **`scripts/prepare_dataset.py`**:
  Deterministic end-to-end Python pipeline executing:
  1. Raw checksum verification and data validation.
  2. Column name standardization (Pythonic snake_case / PascalCase).
  3. Casing normalization and whitespace stripping across all text fields.
  4. Median imputation for missing numeric observations (`Age` = 19.0).
  5. Feature engineering of 12 derived analytical variables (`User_ID`, `Faculty`, `CGPA_Midpoint`, flags, comorbidity metrics).
  6. Quality assertions verifying row count integrity (101 rows), zero null values, and valid data ranges.

---

### 3. Detailed Data Preparation Documentation

The following technical reports provide exhaustive documentation of the data preparation methodology:

1. **`documentation/data_preparation_report.md`**:
   Comprehensive audit containing summary statistics, before-and-after distributions, categorical frequency tables, risk stratification summaries, and pipeline integrity checks.
2. **`documentation/missing_value_treatment.md`**:
   Detailed analysis of the single missing record (`Age` at row 43 / respondent index 43), justification for median imputation (median = 19.0, mode = 18.0, mean = 20.53), and verification of zero data loss.
3. **`documentation/column_mapping.md`**:
   Full mapping table contrasting raw survey headers, processed database names, Tableau display labels, data types, and transformation rules.
4. **`documentation/derived_fields.md`**:
   Mathematical definitions, logical rules, conditional logic, and clinical justification for all 12 engineered features (`User_ID`, `Age_Group`, `Faculty`, `Study_Year_Num`, `CGPA_Min`, `CGPA_Max`, `CGPA_Midpoint`, `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`, `Condition_Count`, `Mental_Health_Risk`, `Treatment_Gap`).
5. **`documentation/outlier_analysis.md`**:
   Statistical IQR (Interquartile Range) evaluations across numeric features confirming zero demographic or clinical anomalies, along with domain validation of academic performance distributions.
6. **`tableau/data_source_notes.md`**:
   Tableau Desktop 2026.1 and Tableau Public field role assignments, default sort configurations, color palette standards, and candidate calculated field formulas.

---

### 4. Verification Checksums

- **Raw Data Hash (Unchanged):**
  `c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`
- **Processed Data Shape:**
  101 rows &times; 23 columns
- **Data Loss Rate:**
  0.0% (all 101 respondents retained)

---

### 5. Epic Status & Governance
- **Epic 1:** Completed
- **Epic 2:** Completed
- **Epics 3–8:** Not Started (Work strictly paused at Epic 2 boundary)
