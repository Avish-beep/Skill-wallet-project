# Analysing Mental Health in Student Ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg?style=flat-square)](LICENSE)
[![Documentation: CC BY 4.0](https://img.shields.io/badge/Documentation-CC%20BY%204.0-blue.svg?style=flat-square)](LICENSE-DOCS)
[![GitHub Actions: Deploy Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-success?style=flat-square&logo=github)](https://avish-beep.github.io/Skill-wallet-project/)
[![Dataset: Validated](https://img.shields.io/badge/Dataset%20Audit-N%3D101%20%7C%2023%20Cols-emerald?style=flat-square)](data/processed/student_mental_health_processed.csv)
[![Tableau Desktop](https://img.shields.io/badge/Tableau%20Desktop-2026.1-orange?style=flat-square&logo=tableau)](tableau/student_mental_health_visualizations.twb)

---

## 📌 Executive Summary

**Analysing Mental Health in Student Ecosystem** is an empirical data analytics and visual intelligence capstone project developed by **Avishkar Padavi** at **Indira College of Engineering and Management** as part of the **SkillWallet Data Analytics with Tableau** curriculum.

The project investigates self-reported psychological distress, academic standing, and clinical care gaps among higher-education students. By integrating reproducible Python ETL engineering, advanced Tableau Desktop visualization, an accessible React web portfolio deployed on GitHub Pages, and a natural narrated video walkthrough, this repository delivers evidence-based insights for campus health administration.

- **Primary Repository:** [https://github.com/Avish-beep/Skill-wallet-project](https://github.com/Avish-beep/Skill-wallet-project)
- **Live Deployed Portfolio:** [https://avish-beep.github.io/Skill-wallet-project/](https://avish-beep.github.io/Skill-wallet-project/)
- **Published Tableau Public View:** [AnalysingMentalHealthinStudentEcosystem](https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🎯 Problem Statement & Research Objectives

Higher education environments impose severe academic, economic, and developmental pressures on students. However, university wellness programs often allocate resources reactively without empirical data on symptom prevalence, academic correlation, or care accessibility.

### Key Research Questions
1. **Prevalence & Comorbidity:** What are the empirical prevalence rates of self-reported depression, anxiety, and panic attacks, and how frequently do these conditions co-occur?
2. **The Treatment Gap:** What proportion of symptomatic students seek professional psychiatric or psychological counseling?
3. **The High-Achiever Paradox:** Does high academic achievement (CGPA) insulate students from psychological distress, or does comorbidity persist across top academic tiers?
4. **Disciplinary & Gender Dynamics:** How do symptom rates vary across academic faculties and between male and female student cohorts?

---

## 👤 Author Information

- **Student / Author:** Avishkar Padavi
- **Institution:** Indira College of Engineering and Management, Pune
- **Domain:** Healthcare Analytics / Student Mental Health
- **Curriculum:** SkillWallet — Data Analytics with Tableau

---

## 📂 Dataset Overview & Provenance

The empirical foundation consists of higher-education student survey records capturing demographic profiles, academic standing, self-reported mental health conditions, and treatment-seeking behavior.

### Verified Dataset Profile
- **Raw Survey Data:** `data/raw/Student_Mental_health.csv`
  - Ingested observations: **101 rows × 11 survey columns**
  - SHA-256 Hash: `c0d1300dd5225b42603847a9ffec01c77f0a39dd118d0e74f1ec5be3d0663f0a`
- **Processed Analytical Data:** `data/processed/student_mental_health_processed.csv`
  - Engineered observations: **101 rows × 23 analytical features**
  - SHA-256 Hash: `7074465dfecf265b44fc476be2687dc9f6c77098e9a26391a27e361c4bb587e9`
  - Missing Values: **0** (single missing Age entry in row 43 imputed via cohort median of 19.0)
  - Duplicate Records: **0** (100% unique student survey records)

---

## ⚙️ Data Preparation & Feature Engineering

Data engineering was executed via an automated, reproducible Python pipeline (`scripts/prepare_dataset.py`) preserving raw source immutability.

### 12 Engineered Features
1. `User_ID`: Standardized unique respondent identifier (`STU_001` through `STU_101`).
2. `Age_Imputed`: Handled single missing age via demographic median imputation (`19.0`).
3. `Age_Group`: Binned cohort stratification (`18-20` and `21-25`).
4. `Gender_Clean`: Standardized binary string formatting (`Female`: 75, `Male`: 26).
5. `Faculty`: Categorized 43 distinct courses into 7 higher-education faculties:
   - Computing & IT (28), Engineering (26), Humanities (14), Sciences (13), Business & Management (9), Allied Health (8), Law (3).
6. `CGPA_Range_Clean`: Sanitized academic grading boundaries.
7. `CGPA_Midpoint`: Continuous numeric representation of CGPA ranges (e.g., `3.75` for `3.50 - 4.00`).
8. `Depression_Flag`: Binary numeric indicator (1 = Yes, 0 = No).
9. `Anxiety_Flag`: Binary numeric indicator (1 = Yes, 0 = No).
10. `Panic_Attack_Flag`: Binary numeric indicator (1 = Yes, 0 = No).
11. `Condition_Count`: Total concurrent conditions per student (0 to 3).
12. `Mental_Health_Risk`: Clinical comorbidity tier:
    - **Low Risk (0 conditions):** 37 students (36.6%)
    - **Moderate Risk (1 condition):** 36 students (35.6%)
    - **High Risk (2–3 conditions):** 28 students (27.7%)
13. `Treatment_Gap`: Categorized care accessibility (`Treated`: 6, `Untreated`: 58, `No Condition`: 37).

---

## 📈 Key Analytical Findings

1. **The 90.6% Campus Care Deficit:**
   Out of 64 students exhibiting at least one self-reported condition, **58 students (90.6%)** have never consulted a psychiatrist, counselor, or mental health specialist. Only 6 symptomatic students accessed professional support.
2. **Broad Tri-Condition Prevalence:**
   Condition prevalence across the 101 surveyed respondents is evenly elevated:
   - **Depression:** 34.7% (35 students)
   - **Anxiety:** 33.7% (34 students)
   - **Panic Attacks:** 32.7% (33 students)
3. **Severe Comorbid Burden:**
   63.4% of all surveyed students experience at least one condition. 18 students experience two concurrent conditions, and 10 students suffer from all three conditions simultaneously.
4. **The High-Achiever Paradox:**
   Students in the highest comorbidity risk tier (2–3 concurrent conditions) maintain an average CGPA midpoint of **3.45 out of 4.0**, dispelling the misconception that mental health distress is confined to academically struggling students.
5. **Cross-Disciplinary Reach:**
   Psychological distress is distributed across all 7 mapped faculties, led by Computing & IT (28 students) and Engineering (26 students), proving that student wellness interventions must be university-wide.

---

## 📊 Tableau Visual Intelligence & Dashboards

The native Tableau Desktop workbook (`tableau/student_mental_health_visualizations.twb`) contains **10 individual worksheets** and **2 responsive dashboards**:

### Visual Worksheets Catalogue
- `WS01`: Condition Prevalence Rates (Horizontal Bar Chart)
- `WS02`: Risk Stratification Breakdown (Donut / Segmented Chart)
- `WS03`: Specialist Treatment Gap (Diverging Bar / Distribution)
- `WS04`: Gender-Condition Cross-Tabulation (Grouped Bars)
- `WS05`: Faculty-Level Risk Distribution (Stacked 100% Bar Chart)
- `WS06`: CGPA Midpoint vs. Risk Tier (Box / Whisker Comparison)
- `WS07`: Academic Year Progression Analysis (Bar Chart)
- `WS08`: Comorbidity Count Distribution (Histogram)
- `WS09`: Treatment Gap by Gender (Comparative Matrix)
- `WS10`: Executive Cohort KPI Tiles

### Tableau Public Publication Status
- **Local Source of Truth:** `tableau/student_mental_health_visualizations.twb` is 100% verified against the authentic 101-student dataset.
- **Tableau Public Cloud State:** The published URL currently displays the legacy template. The local workbook awaits cloud save overwrite. The portfolio website includes a clear reconciliation panel alerting viewers to this status.

---

## 🎥 Presentation Video & Walkthrough (06:24)

An academic project demonstration narrated in natural Indian English:

- **Video File:** [`video/project_presentation.mp4`](file:///C:/Skillwallet/video/project_presentation.mp4) (mirrored in `website/public/video/`)
- **Duration:** **06:24** (384.45 seconds)
- **Resolution & Format:** 1080p Full HD (1920 × 1080), H.264 / AAC, 19.4 MB
- **Narration Engine:** Microsoft Azure Neural Speech (`en-IN-PrabhatNeural` at `-14%` conversational pace)
- **Captions:** WebVTT ([`video/captions.vtt`](file:///C:/Skillwallet/video/captions.vtt)) & SubRip ([`video/captions.srt`](file:///C:/Skillwallet/video/captions.srt))
- **Documentation:** [`video/script.md`](file:///C:/Skillwallet/video/script.md), [`video/transcript.md`](file:///C:/Skillwallet/video/transcript.md), and [`video/scene_plan.md`](file:///C:/Skillwallet/video/scene_plan.md)
- **Thumbnail Poster:** [`video/thumbnail.png`](file:///C:/Skillwallet/video/thumbnail.png)

---

## 🌐 Web Portfolio & Deployment

The portfolio website is built with **React 19**, **TypeScript**, **Vite**, and **Tailwind CSS**, featuring:
- Live KPI executive counter cards
- Methodological pipeline provenance audit
- Verified Tableau dashboard architecture preview
- Interactive 6-chapter scrollytelling walkthrough
- Responsive video player with subtitle switching and chapters
- Zero horizontal scroll across all desktop, laptop, tablet, and mobile viewports

- **Live URL:** [https://avish-beep.github.io/Skill-wallet-project/](https://avish-beep.github.io/Skill-wallet-project/) (HTTP 200)
- **Automated CI/CD:** GitHub Actions workflow [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml) triggers on every push to `main`.

---

## 📁 Repository Directory Structure

```
C:\Skillwallet\
├── .github/
│   └── workflows/
│       └── deploy-pages.yml             # GitHub Actions automated Pages deployment
├── data/
│   ├── raw/
│   │   ├── Student_Mental_health.csv    # Ingested baseline survey (SHA-256 verified)
│   │   └── SOURCE.md                    # Data provenance audit
│   └── processed/
│       └── student_mental_health_processed.csv # Clean analytical dataset (101 rows x 23 cols)
├── documentation/
│   ├── project_development_procedure.md # Step-by-step methodology log
│   ├── performance_testing_report.md    # Bundle and ETL benchmarks
│   ├── website_testing_report.md        # Playwright audit & accessibility tests
│   ├── deployment_report.md             # Hosting and deployment verification
│   ├── project_progress.md              # Milestone progress tracker
│   ├── visualization_report.md          # In-depth visual analytics report
│   └── data_preparation_report.md       # ETL logic and formulas
├── evidence/
│   ├── dashboard_overview.png           # Validated Tableau Desktop 16:9 canvas render
│   ├── website_responsive/              # Multi-viewport evidence screenshots
│   └── walkthrough_frames/              # 8 High-definition website screen captures
├── scripts/
│   ├── prepare_dataset.py               # Reproducible Python ETL pipeline
│   ├── verify_epic_03.py                # Dataset & Tableau workbook integrity checker
│   ├── test_website_responsive.py       # Automated multi-viewport responsive testing suite
│   ├── verify_live_pages.py             # Playwright live deployment verification script
│   └── build_natural_walkthrough_video.py # Narration synthesis & video assembly script
├── tableau/
│   ├── student_mental_health_visualizations.twb # Local Tableau Desktop workbook
│   └── dashboard_design.md              # Layout containers & responsive specifications
├── video/
│   ├── project_presentation.mp4         # Final 06:24 Full HD presentation video (19.4 MB)
│   ├── thumbnail.png                    # High-res video poster
│   ├── captions.vtt                     # WebVTT subtitle track
│   ├── captions.srt                     # SubRip subtitle track
│   ├── transcript.md                    # Spoken transcript
│   ├── script.md                        # Full presentation script
│   └── scene_plan.md                    # Scene breakdown with timestamps
├── website/                             # React + Vite + TypeScript web application
│   ├── src/App.tsx                      # Single-page portfolio application
│   ├── public/video/                    # Static media bundle for production
│   ├── dist/                            # Production static build
│   └── vite.config.ts                   # Base URL configuration
├── LICENSE                              # MIT License (Original Software Code)
├── LICENSE-DOCS                         # CC BY 4.0 License (Original Documentation)
├── DATA_LICENSE.md                      # Dataset provenance and usage terms
├── THIRD_PARTY_NOTICES.md               # Upstream software and asset licenses
├── CONTRIBUTING.md                      # Contributor guidelines and workflow
├── CODE_OF_CONDUCT.md                   # Contributor Covenant 2.1
├── SECURITY.md                          # Vulnerability reporting and privacy policy
├── CITATION.cff                         # Academic Citation File Format
├── requirements.txt                     # Python dependencies
└── README.md                            # Comprehensive project overview
```

---

## 💻 Local Installation & Reproduction Commands

### Prerequisites
- Node.js v20+
- Python 3.11+
- Windows PowerShell / Linux Bash

### Execution Steps

```powershell
cd C:\Skillwallet

# 1. Activate Python virtual environment & install requirements
python -m venv venv
& "venv\Scripts\Activate.ps1"
pip install -r requirements.txt
playwright install chromium

# 2. Run reproducible ETL pipeline (validates SHA-256 and outputs clean CSV)
& "venv\Scripts\python.exe" "scripts\prepare_dataset.py"

# 3. Verify dataset reconciliation and Tableau workbook XML
& "venv\Scripts\python.exe" "scripts\verify_epic_03.py"

# 4. Execute automated responsive testing suite across 4 viewports
& "venv\Scripts\python.exe" "scripts\test_website_responsive.py"

# 5. Build and preview static portfolio website
cd website
npm install
npm run build
npm run preview
```

---

## 🛠️ Technology Stack

| Domain | Technologies |
| :--- | :--- |
| **Data Engineering** | Python 3.11, Pandas 3.0, NumPy 2.4 |
| **Visual Analytics** | Tableau Desktop 2026.1, Tableau Public Cloud |
| **Frontend Web** | React 19, TypeScript, Vite 8, Tailwind CSS 4, Lucide React |
| **Testing & Automation** | Playwright for Python, Oxlint, GitHub Actions CI/CD |
| **Audio & Video** | FFmpeg, Microsoft Azure Neural Speech (`en-IN-PrabhatNeural`) |
| **Hosting & CI/CD** | GitHub Pages, GitHub Actions |

---

## 📄 Licensing & Attribution Summary

- **Software Code:** Licensed under the [MIT License](LICENSE) &copy; 2026 Avishkar Padavi. Covers original TypeScript, React, Python, and build scripts.
- **Documentation & Narrative:** Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-DOCS) &copy; 2026 Avishkar Padavi.
- **Survey Dataset:** Governed by terms detailed in [DATA_LICENSE.md](DATA_LICENSE.md). The root MIT License does not apply to third-party survey records.
- **Third-Party Dependencies:** Fully acknowledged in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- **Academic Citation:** Refer to [CITATION.cff](CITATION.cff) for standard citation formats.

---

## ⚠️ Epidemiological Disclaimers & Known Limitations

1. **Self-Reported Screening:** Data represents self-reported survey responses from university students, not formal clinical DSM-5 diagnoses.
2. **Observational & Non-Causal:** Academic performance (CGPA) and mental health indicators are evaluated correlationally without causal claims.
3. **Tableau Public Cloud Overwrite:** The local workbook (`tableau/student_mental_health_visualizations.twb`) is verified; manual cloud overwrite to update the Tableau Public URL remains pending author authorization.
