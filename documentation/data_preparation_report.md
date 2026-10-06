# Data Preparation & ETL Final Audit Report
## Epic 2: Data Preparation — Prepare the Data for Visualization

**Execution Date:** October 06, 2026  
**Pipeline Script:** `scripts/prepare_dataset.py`  
**Execution Environment:** Python 3.11.9 (Pandas 3.0.6, NumPy 2.4.6)  

---

### 1. Objective
Prepare an analysis-ready, clean, and fully validated dataset for Tableau Desktop 2026.1 by correcting data types, standardizing categorical text, handling missing records, validating numerical ranges, and creating justified derived features while preserving 100% of raw data integrity.

---

### 2. Dataset Paths & File Lineage
- **Input (Raw) Dataset:** `C:\Skillwallet\data\raw\Student_Mental_health.csv`
- **Output (Processed) Dataset:** `C:\Skillwallet\data\processed\student_mental_health_processed.csv`
- **Raw File Immutability:** SHA256 checksum verified before and after pipeline execution:  
  `c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a` (Identical; unmodified).

---

### 3. Quantitative Summary Before vs. After

| Metric | Raw Dataset (Before) | Processed Dataset (After) | Change / Delta |
| :--- | :---: | :---: | :---: |
| **Row Count** | 101 | 101 | 0 rows dropped (all observations preserved) |
| **Column Count** | 11 | 23 | +12 engineered analytical columns |
| **Missing Values** | 1 (`Age`, row 43) | 0 | -1 (Imputed using cohort median = 19.0) |
| **Duplicate Complete Rows** | 0 | 0 | 0 duplicates |
| **File Size** | 7.17 KB | 14.28 KB | +7.11 KB (expanded feature schema) |

---

### 4. Data Type Corrections & Column Renames
- `Choose your gender` &rarr; `Gender` (String, stripped & capitalized)
- `Age` &rarr; `Age` (Cast from Float64 with NaN to Clean Integer `int32`)
- `What is your course?` &rarr; `Course` (Standardized title case; raw preserved in `Course_Raw`)
- `Your current year of Study` &rarr; `Year_of_Study` (Standardized to `'Year 1'`, `'Year 2'`, `'Year 3'`, `'Year 4'`)
- `What is your CGPA?` &rarr; `CGPA_Range` (Trimmed trailing whitespace from `'3.50 - 4.00 '`)
- `Marital status` &rarr; `Marital_Status` (String, capitalized)
- `Do you have Depression?` &rarr; `Depression` (String, capitalized)
- `Do you have Anxiety?` &rarr; `Anxiety` (String, capitalized)
- `Do you have Panic attack?` &rarr; `Panic_Attack` (String, capitalized)
- `Did you seek any specialist for a treatment?` &rarr; `Treatment_Sought` (String, capitalized)

---

### 5. Categorical Transformations
- Casing inconsistencies resolved across all text columns.
- Standardized major degree abbreviations (`BIT` &rarr; `Information Technology (BIT)`, `Engine`/`koe` &rarr; `Engineering`, `Mathemathics` &rarr; `Mathematics`).
- Clustered 49 granular degree titles into 7 standardized higher-education academic faculties in `Faculty`.

---

### 6. Numerical Validation & Outlier Findings
- **Age Bounds:** Validated across all 101 students. Values range from 18 to 24 years (mean: 20.51, median: 19.0), perfectly matching university undergraduate distributions.
- **IQR Outlier Check:** 0 outliers found in `Age`; 0 outliers found in `Condition_Count`.
- **Lower CGPA Observations:** 6 students with lower GPAs (`0 - 1.99` and `2.00 - 2.49`) were detected as statistical outliers but deliberately preserved to avoid survival bias.

---

### 7. Derived Features Generated
1. `User_ID`: Anonymized primary key (`STD_0001` to `STD_0101`).
2. `Age_Group`: Demographic cohorts (`18-20 (Underclassmen)`, `21-24 (Upperclassmen)`).
3. `Faculty`: Higher-level discipline categorization (7 faculties).
4. `CGPA_Midpoint`: Continuous numeric midpoint (1.00 to 3.75).
5. `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`, `Treatment_Sought_Flag`: Binary integer indicators (1/0).
6. `Condition_Count`: Total concurrent conditions (0 to 3).
7. `Mental_Health_Risk`: Clinical severity stratification (`Low Risk`, `Moderate Risk`, `High Risk`).
8. `Treatment_Gap`: Utilization status (`Untreated Condition`, `Condition Treated`, `No Identified Condition`).

---

### 8. Final Tableau Readiness
- Processed CSV at `C:\Skillwallet\data\processed\student_mental_health_processed.csv` is 100% prepared to connect to Tableau Desktop 2026.1.
- All column headers are concise and clean for pill dragging.
- Zero null values prevent unexpected data omission in filters or visualizations.
- Dimension and Measure roles are clearly delineated.

---

### 9. Limitations
- Survey data is cross-sectional and self-reported.
- Sleep quality, screen hours, and study duration were not captured in this raw survey wave, as documented in Epic 1.
