# Analysing Mental Health in Student Ecosystem

**Student:** Avishkar Padavi  
**Institution:** Indira College of Engineering and Management  
**Platform / Module:** SkillWallet — Data Analytics with Tableau  
**Domain:** Healthcare Analytics / Student Mental Health  
**Repository:** [https://github.com/Avish-beep/Skill-wallet-project](https://github.com/Avish-beep/Skill-wallet-project)  
**Tableau Public Dashboard:** [Live Tableau Public Dashboard](https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
**Website (GitHub Pages):** [https://avish-beep.github.io/Skill-wallet-project/](https://avish-beep.github.io/Skill-wallet-project/)  

---

## 🎯 Executive Summary & Verified Deliverables

This capstone project conducts an empirical investigation into psychological distress, academic standing, and mental health intervention outcomes across university students. Through reproducible Python data engineering, Tableau visual intelligence, an accessible static web portfolio, and a full narrated video walkthrough, the project delivers actionable insights for campus wellness administration.

### 📌 Primary Project Deliverables

| Deliverable | Details / Resource | Status |
| :--- | :--- | :---: |
| **Interactive Tableau Public Dashboard** | [Analysing Mental Health in Student Ecosystem](https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) | **Verified Live** (HTTP 200) |
| **Project Presentation Video** | 1080p Full HD presentation (06:37) with Indian English narration (`video/project_presentation.mp4`) | **Verified on Disk** (20.0 MB) |
| **Project Portfolio Website** | Vite + React + TypeScript + Tailwind CSS with responsive embed & scrollytelling (`website/`) | **Built & Verified** |
| **Automated Deployment Workflow** | GitHub Actions Pages workflow (`.github/workflows/deploy-pages.yml`) | **Configured** |
| **Analytical Dataset & ETL** | 101 rows &times; 23 analytical columns (`data/processed/student_mental_health_processed.csv`) | **SHA-256 Validated** |
| **Automated Verification Suite** | Epic 3 integrity tests + Playwright multi-viewport responsive testing suite | **100% Passed** |

---

## 📊 Tableau Visual Intelligence & Core Views

The final workbook (`tableau/student_mental_health_visualizations.twb`) features **10 unique worksheets** and **2 responsive dashboards** connected strictly to the validated 101-row dataset:

### 1. Executive Cohort KPIs:
- **Total Surveyed Cohort:** 101 students
- **High Comorbidity Risk:** 28 students (27.7%)
- **Moderate Risk:** 36 students (35.6%)
- **Untreated Symptomatic Students:** 58 students (90.6% clinical care gap)

### 2. Analytical Findings:
- **The Specialist Care Deficit:** 58 of 64 symptomatic students have never accessed professional counseling or psychiatric treatment.
- **Academic High-Achiever Distress:** High-risk comorbidity students maintain a mean CGPA midpoint of **3.45 / 4.0**, proving that academic high achievers experience acute psychological strain.
- **Within-Gender Prevalence:** Depression, anxiety, and panic attacks are distributed across female (N=75) and male (N=26) cohorts across all 7 academic faculties.

---

## 🎥 Project Presentation Video (06:37)

A complete academic screen walkthrough narrated in natural Indian English (`en-IN-PrabhatNeural`):
- **Video File:** [`video/project_presentation.mp4`](file:///C:/Skillwallet/video/project_presentation.mp4) (1080p Full HD @ 40fps, 20.0 MB)
- **Thumbnail:** [`video/thumbnail.png`](file:///C:/Skillwallet/video/thumbnail.png)
- **Narration Script:** [`video/script.md`](file:///C:/Skillwallet/video/script.md)
- **Scene Plan:** [`video/scene_plan.md`](file:///C:/Skillwallet/video/scene_plan.md)
- **Transcript:** [`video/transcript.md`](file:///C:/Skillwallet/video/transcript.md)
- **Captions:** WebVTT [`video/captions.vtt`](file:///C:/Skillwallet/video/captions.vtt) & SubRip [`video/captions.srt`](file:///C:/Skillwallet/video/captions.srt)

---

## 📂 Repository Structure

```
C:\Skillwallet\
├── .github/
│   └── workflows/
│       └── deploy-pages.yml                # Automated GitHub Pages CI/CD workflow
├── data/
│   ├── raw/
│   │   ├── Student_Mental_health.csv       # Ingested baseline survey (SHA-256 verified)
│   │   └── SOURCE.md                       # Data provenance audit
│   └── processed/
│       └── student_mental_health_processed.csv # Clean analytical dataset (101 rows x 23 cols)
├── documentation/
│   ├── project_development_procedure.md    # Comprehensive step-by-step procedure
│   ├── performance_testing_report.md       # Bundle, ETL, and embed performance metrics
│   ├── website_testing_report.md           # Playwright responsive & accessibility audit
│   ├── deployment_report.md                # Hosting and configuration verification
│   ├── project_progress.md                 # Epic-by-epic milestone tracker
│   ├── visualization_report.md             # Detailed visual analytics report
│   └── data_preparation_report.md          # ETL transformations and formulas
├── evidence/
│   ├── epic_03/                            # 12 high-resolution dashboard & chart renders
│   └── website_responsive/                 # Playwright multi-viewport evidence screenshots
├── scripts/
│   ├── prepare_dataset.py                  # Reproducible Python ETL pipeline
│   ├── verify_epic_03.py                   # Automated Epic 3 integrity verification script
│   ├── test_website_responsive.py          # Playwright headless responsive testing suite
│   ├── generate_indian_voice_video.py      # Indian English neural voiceover video generator
│   └── build_video_docs.py                 # Captions, transcript, and scene plan builder
├── tableau/
│   ├── student_mental_health_visualizations.twb # Local Tableau Desktop Workbook
│   └── dashboard_design.md                 # Layout containers & responsive specifications
├── video/
│   ├── project_presentation.mp4            # Final 06:37 Full HD presentation video (20 MB)
│   ├── thumbnail.png                       # Video poster image
│   ├── captions.vtt                        # WebVTT subtitle track
│   ├── captions.srt                        # SubRip subtitle track
│   ├── transcript.md                       # Spoken transcript
│   ├── script.md                           # Full presentation script
│   └── scene_plan.md                       # Scene breakdown with timestamps
├── website/                                # Vite + React + TypeScript + Tailwind CSS app
│   ├── src/App.tsx                         # Single-page application with dashboard & story
│   ├── dist/                               # Production static bundle for GitHub Pages
│   └── vite.config.ts                      # Base path configured for GitHub Pages
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## 💻 Local Execution & Reproduction Commands (Windows)

Open PowerShell and execute:

```powershell
cd C:\Skillwallet

# 1. Run reproducible ETL pipeline
& "venv\Scripts\python.exe" "scripts\prepare_dataset.py"

# 2. Run data integrity & Tableau XML verification
& "venv\Scripts\python.exe" "scripts\verify_epic_03.py"

# 3. Run automated responsive website test suite
& "venv\Scripts\python.exe" "scripts\test_website_responsive.py"

# 4. Build and preview static website
cd website
npm run build
npm run preview
```

---

## ⚠️ Epidemiological Disclaimers & Data Limitations
- **Self-Reported Data:** Visualizations represent student survey responses, not formal clinical DSM-5 diagnoses.
- **Non-Causal Observations:** Academic indicators (CGPA midpoint) and mental health conditions are evaluated correlationally without causal claims.
- **Cohort Scope:** Observations are based on N=101 university students. Subgroup breakdowns across smaller faculties are descriptive.
