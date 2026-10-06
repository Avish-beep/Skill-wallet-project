# Dataset Provenance & Source Audit
## Project: Analysing Mental Health in Student Ecosystem

---

### 1. Dataset Overview
- **Project Domain:** Healthcare & Student Mental Health
- **SkillWallet Module:** Data Analytics with Tableau
- **Curriculum Epic:** Epic 1 — Data Collection & Extraction from Database
- **Current Task:** Downloading the dataset
- **Current Subtask:** Understand the data

---

### 2. Expected SkillWallet Dataset Schema (18 Variables)
As specified by the SkillWallet subtask *Understand the data*, the intended project dataset comprises the following 18 fields:

1. `User ID` – Unique identifier assigned to each individual
2. `Age` – Age of the individual in years
3. `Gender` – Gender of the individual (Male, Female, Other)
4. `Occupation` – Current profession or field of work
5. `Stress Level` – Measured level of stress (Low, Medium, High)
6. `Anxiety Score` – Numerical score indicating anxiety level
7. `Depression Score` – Numerical score indicating depression severity
8. `Sleep Quality` – Quality of sleep (Poor, Average, Good)
9. `Daily Screen Time (hrs)` – Average hours spent on screens per day
10. `Physical Activity Level` – Level of physical activity (Low, Moderate, High)
11. `Social Interaction Score` – Measure of social engagement
12. `Mental Health History` – Whether the individual has prior mental health issues (Yes/No)
13. `Therapy Type` – Type of intervention provided (CBT, Meditation, Counseling, etc.)
14. `Intervention Duration (weeks)` – Duration of the psychological intervention
15. `Progress Score` – Improvement score after intervention
16. `Medication Usage` – Whether medication is being used (Yes/No)
17. `Support System Strength` – Strength of family/friend support (Low, Medium, High)
18. `Work-Life Balance Score` – Score indicating balance between work and personal life

---

### 3. Current Dataset Audit & Candidate Analysis

#### Candidate A: SkillWallet Native Project Resource (Recommended & Authoritative)
- **Source:** Directly attached inside the SkillWallet Task 1 modal (*Downloading the dataset &bull; Understand the data*) or the project *Workspace* tab.
- **Status:** Requires the user to click the download attachment from the authenticated SkillWallet browser tab.
- **Alignment:** 100% matches all 18 variables defined above.

#### Candidate B: Baseline Survey Dataset (`Student_Mental_health.csv`)
- **Source:** Higher education student mental health survey repository.
- **Dimensions:** 101 records &times; 11 survey columns (`Timestamp`, `Choose your gender`, `Age`, `What is your course?`, `Your current year of Study`, `What is your CGPA?`, `Marital status`, `Do you have Depression?`, `Do you have Anxiety?`, `Do you have Panic attack?`, `Did you seek any specialist for a treatment?`).
- **Limitation:** Captures binary diagnostic indicators (Yes/No) and academic standing (CGPA), but lacks the quantitative clinical scores (Anxiety Score, Depression Score, Daily Screen Time, Therapy Type, Progress Score) defined in the 18-variable SkillWallet specification.

---

### 4. Integrity Notice
In strict accordance with project rules (*DO NOT invent data, DO NOT fabricate records, DO NOT select ambiguous datasets without reporting*), both Candidate A (authoritative target) and Candidate B (ingested baseline) are formally documented. When the file from the SkillWallet portal is downloaded into `data/raw/`, `scripts/inspect_dataset.py` will automatically validate and ingest it.
