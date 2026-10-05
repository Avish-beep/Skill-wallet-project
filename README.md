# Analysing Mental Health in Student Ecosystem
### Applied Visual Analytics & Healthcare Informatics

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask 3.1](https://img.shields.io/badge/Flask-3.1.3-green.svg)](https://flask.palletsprojects.com/)
[![Tableau 2026.1](https://img.shields.io/badge/Tableau-2026.1-orange.svg)](https://www.tableau.com/)
[![Git](https://img.shields.io/badge/Version%20Control-Git-red.svg)](https://git-scm.com/)

---

## 📌 Project Overview
This project presents an empirical, end-to-end data analytics study investigating the prevalence, comorbidity, and academic correlates of psychological distress across higher education students. Built under the **SkillWallet — Data Analytics with Tableau** curriculum, the project combines a reproducible Python ETL pipeline, interactive visual analytics in Tableau Desktop 2026.1, and an embedded Flask web portal.

### Key Empirical Findings:
- **62.4%** of surveyed students experience at least one clinical condition (Depression, Anxiety, or Panic Attacks).
- **35.6%** are categorized as **High Risk** (navigating &ge;2 concurrent conditions).
- **90.5% Campus Treatment Gap:** Only 6 of the 63 symptomatic students have ever consulted a mental health specialist.
- **Academic Independence:** High-achieving students (CGPA 3.50–4.00) experience psychological distress rates comparable to average peers.

---

## 🛠 Technology Stack
- **Visual Analytics:** Tableau Desktop 2026.1 & Tableau Public
- **Programming & ETL:** Python 3.11.9 (`pandas`, `numpy`, `openpyxl`, `python-dotenv`)
- **Web Portal:** Flask 3.1.3 (Jinja2, HTML5, CSS3, JavaScript, Tableau Web Component API v3)
- **Version Control:** Git 2.55.0 & GitHub

---

## 📂 Project Structure
```
C:\Skillwallet\
├── data/
│   ├── raw/
│   │   └── Student_Mental_health.csv       # Original survey dataset (N=101)
│   └── processed/
│       └── student_mental_health_cleaned.csv# Cleaned dataset with 12 derived features
├── documentation/
│   ├── project_report.md                   # Complete 22-section academic research report
│   ├── analysis_summary.md                 # Statistical exploratory findings
│   ├── testing_report.md                   # Automated test results (100% pass)
│   ├── performance_testing.md              # Latency & rendering audit
│   ├── skillwallet_task_mapping.md         # 8 Epics & 14 Tasks mapping
│   ├── demo_script.md                      # 5-10 minute presentation script
│   └── viva_questions.md                   # 25 viva questions & comprehensive answers
├── flask_app/
│   ├── app.py                              # Flask application entrypoint
│   ├── templates/
│   │   ├── base.html                       # Global navigation & Tableau API v3 scripts
│   │   ├── index.html                      # Executive dashboard & problem statement
│   │   ├── dashboard.html                  # Interactive Tableau embed container
│   │   ├── insights.html                   # Departmental cross-tab tables
│   │   └── about.html                      # Project background & methodology
│   └── static/
│       ├── css/style.css                   # Responsive academic styling
│       └── js/main.js                      # Responsive scaling & UI helpers
├── scripts/
│   ├── profile_dataset.py                  # Raw dataset audit & quality inspector
│   ├── data_cleaning.py                    # Reproducible ETL & feature engineering pipeline
│   ├── exploratory_analysis.py             # 12-dimension statistical calculator
│   ├── verify_environment.py               # Package & dependency verification
│   └── test_flask_app.py                   # Automated web test suite
├── tableau/
│   ├── visualization_plan.md               # 12-worksheet implementation catalog
│   ├── calculated_fields.md                # Formulas & usage guide for Tableau Desktop
│   ├── dashboard_design.md                 # 4-band responsive layout architecture
│   ├── story_design.md                     # 6-scene analytical narrative structure
│   └── tableau_setup.md                    # Desktop build & publishing walkthrough
├── .gitignore                              # Git exclusion rules
├── .env.example                            # Template for Tableau Public URLs
├── data_dictionary.md                      # Full feature dictionary
├── requirements.txt                        # Pinned Python package dependencies
└── README.md                               # Project documentation
```

---

## 🚀 Setup & Execution Guide (Windows)

### 1. Prerequisites
- Windows 10/11
- Python 3.11.9
- Git 2.55+
- Tableau Desktop 2026.1

### 2. Virtual Environment Setup
Open PowerShell and navigate to the project directory:
```powershell
cd C:\Skillwallet
```

Directly use the configured virtual environment:
```powershell
C:\Skillwallet\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Verify Environment
```powershell
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\verify_environment.py"
```

### 4. Run Data Preprocessing Pipeline
```powershell
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\data_cleaning.py"
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\exploratory_analysis.py"
```

### 5. Launch Flask Web Application
```powershell
& "C:\Skillwallet\venv\Scripts\python.exe" "flask_app\app.py"
```
Open your browser and navigate to: **`http://127.0.0.1:5000`**

### 6. Run Automated Test Suite
```powershell
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\test_flask_app.py"
```

---

## 📊 Tableau Desktop & Tableau Public Integration
1. Launch **Tableau Desktop 2026.1** and connect to `data/processed/student_mental_health_cleaned.csv`.
2. Follow `tableau/visualization_plan.md` and `tableau/calculated_fields.md` to construct the 12 worksheets.
3. Assemble the dashboard following `tableau/dashboard_design.md` and the 6-point narrative story in `tableau/story_design.md`.
4. Click **Server &rarr; Tableau Public &rarr; Save to Tableau Public As...** to publish.
5. Copy your published URL and add it to `C:\Skillwallet\.env`:
   ```ini
   TABLEAU_VIEW_URL=https://public.tableau.com/views/YourWorkbook/Dashboard1
   ```

---

## 🎓 SkillWallet Alignment
This project satisfies all 8 Epics and 14 tasks of the SkillWallet *Data Analytics with Tableau* VIP program. See `documentation/skillwallet_task_mapping.md` for full task tracking.
