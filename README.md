# Analysing Mental Health in Student Ecosystem

**Student:** Avishkar Padavi  
**Institution / Platform:** SkillWallet — Data Analytics with Tableau  
**Domain:** Healthcare / Student Mental Health & Higher Education Analytics  
**Repository:** [https://github.com/Avish-beep/Skill-wallet-project](https://github.com/Avish-beep/Skill-wallet-project)

---

## 🎯 Executive Summary & Deliverables

This repository contains the end-to-end data engineering and visual analytics assets for the project **"Analysing Mental Health in Student Ecosystem"**. The study investigates self-reported psychological indicators (Depression, Anxiety, Panic Attacks), academic standing (CGPA), and specialist care engagement among university students.

### 📌 Primary Project Deliverables

| Deliverable | Details / Link | Status |
| :--- | :--- | :---: |
| **Tableau Public Dashboard** | [Analysing Mental Health in Student Ecosystem (Tableau Public)](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) | **Verified Live** (HTTP 200) |
| **Project Explanation Video** | Walkthrough of problem statement, data engineering, and Tableau dashboards | Pending User Cloud Upload |
| **Google Drive Demo Folder** | `Analysing Mental Health in Student Ecosystem — Avishkar Padavi` (Anyone with link &rarr; Viewer) | Pending User Cloud Upload |
| **GitHub Source & Evidence** | Reproducible scripts, raw data, processed dataset, Tableau `.twb`, and documentation | Complete & Published |
| **Web Portal / Flask App** | *Not applicable* — strictly Tableau Public, Video, and Repository evidence only | **NOT CREATED / DISABLED** |

> For comprehensive demonstration details and Google Drive setup, refer to [docs/project_demo.md](file:///C:/Skillwallet/docs/project_demo.md).

---

## 📊 Tableau Public Interactive Dashboard

* **Official Live URL:**  
  [https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Key Analytical Views:
1. **Executive Cohort KPIs:**
   - Total Cohort: **101 students**
   - High Comorbidity Risk: **28 students** (27.7%)
   - Moderate Risk: **36 students** (35.6%)
   - Untreated Symptomatic Students: **58 students**
2. **Mental Health Risk Distribution:**
   - Categorized into Low (36.6%), Moderate (35.6%), and High (27.7%) tiers based on validated symptom co-occurrence.
3. **Gender Analysis:**
   - Within-group prevalence across 75 female and 26 male respondents.
4. **Student Mental Health Care Gap:**
   - Visualizing that **90.6%** of students self-reporting symptomatic conditions have never sought consultation from a mental health specialist.
5. **Academic Standing & Comorbidity:**
   - Boxplot and stripplot evaluations of CGPA midpoint (mean 3.45 across high-risk students), demonstrating that high academic achievers experience significant psychological distress.

---

## 📊 Dataset Architecture & Provenance

### 1. Raw Baseline Dataset (Immutable)
- **Path:** `data/raw/Student_Mental_health.csv`
- **Integrity:** SHA-256 Verified (`c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a`)
- **Dimensions:** 101 rows &times; 11 survey columns

### 2. Processed Analytical Dataset (Tableau Source)
- **Path:** `data/processed/student_mental_health_processed.csv`
- **Dimensions:** 101 rows &times; 23 analytical columns
- **Completeness:** 100% complete (0 null values, 0 duplicate rows)
- **Integrity Standard:** Derived strictly from verified survey columns. No synthetic or extraneous template fields were introduced.

---

## 📂 Repository Structure

```
C:\Skillwallet\
├── data/
│   ├── raw/
│   │   ├── Student_Mental_health.csv       # Ingested baseline survey dataset
│   │   └── SOURCE.md                       # Data provenance documentation
│   └── processed/
│       └── student_mental_health_processed.csv # Cleaned & feature-engineered dataset (23 cols)
├── docs/
│   └── project_demo.md                     # Video walkthrough & Google Drive details
├── documentation/
│   ├── project_progress.md                 # Milestone tracking
│   ├── visualization_report.md             # Detailed visual analytics report
│   ├── visualization_dictionary.md         # Field and worksheet matrix
│   ├── data_preparation_report.md          # ETL transformations
│   ├── missing_value_treatment.md          # Imputation methodology
│   ├── column_mapping.md                   # Column transformations
│   ├── derived_fields.md                   # Engineered features documentation
│   ├── outlier_analysis.md                 # Statistical outlier analysis
│   ├── data_validation_report.md           # Schema validation report
│   └── data_dictionary.md                  # Comprehensive dictionary
├── evidence/
│   ├── epic_01/                            # Data collection evidence
│   ├── epic_02/                            # Data preparation evidence
│   └── epic_03/                            # High-resolution dashboard renders
├── scripts/
│   ├── generate_visualizations.py          # Evidence visual generator
│   ├── generate_tableau_twb.py             # Tableau XML builder
│   ├── verify_epic_03.py                   # Automated verification suite
│   ├── audit_visualization_metrics.py      # Statistical verification script
│   └── prepare_dataset.py                  # Reproducible data pipeline
├── tableau/
│   ├── student_mental_health_visualizations.twb # Local Tableau Workbook
│   ├── dashboard_design.md                 # Dashboard architectural layout
│   └── calculated_fields.md                # Calculated fields formulas
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## 💻 How to Run & Verify Locally (Windows)

Open PowerShell in the project directory:

```powershell
cd C:\Skillwallet

# Run data preparation pipeline
python scripts\prepare_dataset.py

# Run validation and metric verification suite
python scripts\verify_epic_03.py

# Open workbook in Tableau Desktop (if installed)
& "C:\Program Files\Tableau\Tableau 2026.1\bin\tableau.exe" "tableau\student_mental_health_visualizations.twb"
```

---

## ⚠️ Epidemiological Disclaimers & Data Limitations
- **Self-Reported Data:** Visualizations represent student responses from a self-administered questionnaire, not clinical DSM-5 diagnoses.
- **Non-Causal Observations:** Academic indicators (e.g. CGPA midpoint) and mental health conditions are evaluated correlationally without causal claims.
- **Cohort Scope:** Observations are based on N=101 university students. Subgroup breakdowns across smaller faculties are descriptive.
