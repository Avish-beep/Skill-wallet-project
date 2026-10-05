# SkillWallet 8 Epic & 14 Task Mapping Matrix
## Module: Data Analytics with Tableau (VIP Program)
## Project: Analysing Mental Health in Student Ecosystem

This document provides a 1-to-1 mapping between the project assets and the 8 Epics and 14 Tasks configured in the live SkillWallet Kanban interface.

---

### Part 1: The 8 Epics Mapping

| Epic # | Epic Name | Requirements | Completed by Agent | Manual Tableau Action | Manual SkillWallet Action | Evidence Required | Current Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EPIC 1** | Data Collection & Extraction from Database | Ingest raw dataset; audit fields; verify schema integrity. | Raw dataset profiled; nulls & datatypes audited via Python. | Connect Tableau Desktop to `student_mental_health_cleaned.csv`. | Move Task 1 & 2 to *To Be Reviewed*. | Raw CSV file, Profiling script output, Data connection screenshot. | **READY FOR SUBMISSION** |
| **EPIC 2** | Data Preparation | Clean data, standardize categorical text, impute missing values, engineer features. | Authored & executed `scripts/data_cleaning.py`; generated `data_dictionary.md`. | Inspect Data Source pane in Tableau Desktop. | Move Task 3 to *To Be Reviewed*. | Processed CSV, Python ETL script, Data dictionary. | **READY FOR SUBMISSION** |
| **EPIC 3** | Data Visualization | Construct at least 8-10 diverse visual worksheets addressing key project questions. | Authored `tableau/visualization_plan.md` & `tableau/calculated_fields.md` (12 charts specified). | Build the 12 worksheets in Tableau Desktop 2026.1. | Move Task 4 to *To Be Reviewed*. | Screenshots of 12 Tableau worksheets; calculated field list. | **CODE READY / MANUAL TABLEAU BUILD** |
| **EPIC 4** | Dashboard | Assemble unified responsive dashboard with KPI row and interactive filters. | Authored `tableau/dashboard_design.md` detailing 4-band layout & filter actions. | Assemble Dashboard 1 in Tableau Desktop (`1400x1050px`). | Move Task 5 to *To Be Reviewed*. | Full-screen dashboard screenshot; layout container schema. | **DESIGN READY / MANUAL TABLEAU ASSEMBLE** |
| **EPIC 5** | Story | Develop narrative storyboard with 5-6 structured analytical scenes. | Authored `tableau/story_design.md` detailing all 6 scenes, insights & captions. | Create Story in Tableau Desktop; insert captions. | Move Task 6 to *To Be Reviewed*. | Story point screenshots; narrative walkthrough. | **DESIGN READY / MANUAL TABLEAU ASSEMBLE** |
| **EPIC 6** | Performance Testing | Record performance benchmarks, evaluate query latency and layout rendering. | Authored `documentation/performance_testing.md` and performance checklist. | Run Tableau Performance Recorder (*Help &rarr; Settings & Performance*). | Move Tasks 7, 8, 9 to *To Be Reviewed*. | Tableau Performance Workbook summary or screenshot. | **DOCUMENTED / MANUAL TABLEAU RUN** |
| **EPIC 7** | Web Integration | Publish to Tableau Public; build web application; embed interactive dashboard. | Authored full Flask application (`flask_app/`), Web Component v3 embed architecture, passing 5/5 tests. | Save to Tableau Public As...; copy URL into `.env`. | Move Tasks 10, 11 to *To Be Reviewed*. | Tableau Public URL; Flask running application screenshot. | **FLASK READY / AWAITING TABLEAU PUBLIC URL** |
| **EPIC 8** | Project Demonstration & Documentation | Project report, demo presentation script, viva prep, and GitHub repository. | Created `project_report.md`, `demo_script.md`, `viva_questions.md`, `README.md`, Git repo configured. | None. | Submit GitHub repo URL and demo video/report to Task 12, 13, 14. | GitHub Repo URL, Final PDF report, Video presentation. | **DOCUMENTATION 100% COMPLETE** |

---

### Part 2: The 14 Tasks Checklist (Verified from SkillWallet Kanban)

| Task # | Task Name | Epic | Artifact / Code File | Technical Status | Required Evidence | Action Required |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Download Dataset & Understand Data | Epic 1 | `data/raw/Student_Mental_health.csv`, `scripts/profile_dataset.py` | **COMPLETED** | Terminal output of `profile_dataset.py` | Move card to In Progress &rarr; Review |
| **2** | Connect to Data Source in Tableau | Epic 1 | `tableau/tableau_setup.md` | **READY** | Screenshot of Tableau Data Source pane | Open Tableau Desktop, connect to cleaned CSV |
| **3** | Prepare Data & Feature Engineering | Epic 2 | `scripts/data_cleaning.py`, `data_dictionary.md` | **COMPLETED** | `student_mental_health_cleaned.csv` + Data Dictionary | Move card to Review |
| **4** | Number of Visualizations (8 Subtasks) | Epic 3 | `tableau/visualization_plan.md`, `tableau/calculated_fields.md` | **SPECIFIED** | 12 Worksheet exports / screenshots | Create worksheets in Tableau Desktop |
| &bull; *4.1*| *Subtask 1: Impact of Factors* | Epic 3 | Worksheet 8 (CGPA vs Risk) | Formula & Guide Ready | Worksheet screenshot | Follow `visualization_plan.md` |
| &bull; *4.2*| *Subtask 2: Gender Disparity* | Epic 3 | Worksheet 6 (100% Stacked Bar) | Formula & Guide Ready | Worksheet screenshot | Follow `visualization_plan.md` |
| &bull; *4.3*| *Subtask 3: Academic Seniority Progression* | Epic 3 | Worksheet 7 (Year of Study) | Formula & Guide Ready | Worksheet screenshot | Follow `visualization_plan.md` |
| &bull; *4.4*| *Subtask 4: Average CGPA Impact* | Epic 3 | Calculated Field `cgpa_midpoint` | Formula & Guide Ready | Worksheet screenshot | Follow `visualization_plan.md` |
| &bull; *4.5*| *Subtask 5: Analyzing Condition Types* | Epic 3 | Worksheet 4 (Prevalence Bars) | Formula & Guide Ready | Worksheet screenshot | Follow `visualization_plan.md` |
| &bull; *4.6*| *Subtask 6: Executive KPI Cards* | Epic 3 | Worksheets 1, 2, 3 (BANs) | Formula & Guide Ready | KPI Cards screenshot | Follow `visualization_plan.md` |
| &bull; *4.7*| *Subtask 7: Mental Health Risk Tiers* | Epic 3 | Worksheet 5 (Risk Donut Chart) | Formula & Guide Ready | Donut Chart screenshot | Follow `visualization_plan.md` |
| &bull; *4.8*| *Subtask 8: Academic Faculty Heatmap*| Epic 3 | Worksheet 9 (Faculty Matrix) | Formula & Guide Ready | Heatmap screenshot | Follow `visualization_plan.md` |
| **5** | Responsive Dashboard Design | Epic 4 | `tableau/dashboard_design.md` | **SPECIFIED** | Full Dashboard 1 screenshot | Assemble sheets in Tableau Desktop |
| **6** | Number of Story Points (6 Scenes) | Epic 5 | `tableau/story_design.md` | **SPECIFIED** | Storyboard screenshots (6 points) | Assemble Story in Tableau Desktop |
| **7** | Amount of Performance Recording | Epic 6 | `documentation/performance_testing.md` | **DOCUMENTED** | Performance Summary sheet | Run Tableau Performance Recorder |
| **8** | Utilization of Performance Recording | Epic 6 | `documentation/performance_testing.md` | **DOCUMENTED** | Optimization report | Review latency metrics |
| **9** | Number of Performance Tests | Epic 6 | `scripts/test_flask_app.py` | **COMPLETED** | 5/5 Automated Test Log | Move card to Review |
| **10**| Publish to Tableau Public | Epic 7 | `tableau/tableau_setup.md` | **AWAITING USER AUTH** | Live `public.tableau.com` link | User logs into Tableau Public |
| **11**| Web Integration (Flask Embedding)| Epic 7 | `flask_app/app.py`, `templates/dashboard.html` | **COMPLETED** | Running web app at `localhost:5000` | Run `python flask_app/app.py` |
| **12**| Record Project Demo Video | Epic 8 | `documentation/demo_script.md` | **SCRIPT READY** | 5-10 minute presentation video | Record presentation using demo script |
| **13**| Project Repository Submission | Epic 8 | `https://github.com/Avish-beep/Skill-wallet-project.git` | **LOCAL GIT READY** | GitHub repository URL | Push to GitHub |
| **14**| Final Project Submission | Epic 8 | `documentation/project_report.md`, `documentation/viva_questions.md` | **COMPLETED** | Project Report & Documentation bundle | Submit final project on SkillWallet |
