# Epic 3: Data Visualization Comprehensive Report
## Project: Analysing Mental Health in Student Ecosystem
**Domain:** Healthcare / Student Mental Health & Higher Education Analytics  
**Tableau Version:** Tableau Desktop 2026.1 / Tableau Public  
**Analytical Dataset:** `data/processed/student_mental_health_processed.csv` (101 Records, 23 Columns)  

---

### 1. Epic 3 Objective
The primary objective of Epic 3 (*Task: No of Unique Visualizations*) is to develop a comprehensive suite of distinct, empirically validated visualizations in Tableau exploring the distribution of mental health risk, clinical symptom prevalence, academic performance correlates, and healthcare utilization deficits across university undergraduates. The visualizations are designed to provide institutional decision-makers with clear, actionable insights while maintaining strict epidemiological caution regarding self-reported survey data.

---

### 2. Dataset & Technical Environment
- **Data Source:** `C:\Skillwallet\data\processed\student_mental_health_processed.csv`
- **Data Quality:** 101 rows, 23 columns, 0 nulls, 0 duplicate rows.
- **Tableau Software:** Tableau Desktop 2026.1 (64-bit) & Tableau Public.
- **Workbook File:** `tableau/student_mental_health_visualizations.twb` (Native Tableau Workbook XML).
- **Evidence Rendering Pipeline:** `scripts/generate_visualizations.py` (High-resolution 300 DPI artifacts).

---

### 3. Catalog of Unique Worksheets (10 Worksheets)

#### Worksheet 1: Mental Health Risk Distribution Among Students
- **Chart Type:** Discrete Bar Chart / Frequency Distribution
- **Dimensions:** `Mental_Health_Risk` (`Low Risk`, `Moderate Risk`, `High Risk`)
- **Measures:** `Total Students` (`COUNTD([User_ID])`)
- **Color Scheme:** Low Risk (`#38A169` Green), Moderate Risk (`#DD6B20` Amber), High Risk (`#E53E3E` Crimson)
- **Purpose:** Quantify the high-level psychological vulnerability across the entire student population.
- **Key Observations:**
  - Low Risk (0 conditions): 37 students (36.6%)
  - Moderate Risk (1 condition): 36 students (35.6%)
  - High Risk (&ge;2 conditions): 28 students (27.7%)
  - Over 63.3% of the surveyed cohort reports at least one concurrent psychological condition.

#### Worksheet 2: Mental Health Conditions by Gender
- **Chart Type:** Clustered / Grouped Bar Chart
- **Dimensions:** `Gender` (`Female` N=75, `Male` N=26)
- **Measures:** `SUM([Depression_Flag])`, `SUM([Anxiety_Flag])`, `SUM([Panic_Attack_Flag])`
- **Purpose:** Compare condition prevalence between male and female students to inform demographic support programming.
- **Key Observations:**
  - Female respondents report: Depression 29 (38.7%), Anxiety 24 (32.0%), Panic Attacks 25 (33.3%).
  - Male respondents report: Depression 6 (23.1%), Anxiety 10 (38.5%), Panic Attacks 8 (30.8%).
  - Females report a noticeably higher within-group prevalence of self-reported depression (38.7% vs 23.1%), whereas anxiety is elevated across both genders (32.0% females vs 38.5% males).

#### Worksheet 3: Mental Health Risk Across Age Groups
- **Chart Type:** 100% Stacked Column Chart
- **Dimensions:** `Age_Group` (`18-20 (Underclassmen)`, `21-24 (Upperclassmen)`), `Mental_Health_Risk`
- **Measures:** `COUNTD([User_ID])`
- **Purpose:** Evaluate whether developmental/academic seniority influences mental health risk.
- **Key Observations:**
  - 18–20 Age Group (N=60): 21 Low Risk (35.0%), 20 Moderate Risk (33.3%), 19 High Risk (31.7%).
  - 21–24 Age Group (N=41): 16 Low Risk (39.0%), 16 Moderate Risk (39.0%), 9 High Risk (22.0%).
  - Underclassmen (ages 18–20) display a higher proportion of High Risk comorbidity (31.7% vs 22.0%), highlighting university transition shock.

#### Worksheet 4: Mental Health Risk by Faculty
- **Chart Type:** Horizontal Stacked Bar Chart
- **Dimensions:** `Faculty` (7 Academic Disciplines), `Mental_Health_Risk`
- **Measures:** `COUNTD([User_ID])`
- **Purpose:** Identify departmental distress clusters across campus disciplines.
- **Key Observations:**
  - Computing & IT (N=28): 8 High Risk, 12 Moderate Risk, 8 Low Risk (71.4% symptomatic).
  - Engineering (N=26): 7 High Risk, 10 Moderate Risk, 9 Low Risk (65.4% symptomatic).
  - Humanities & Social Sciences (N=14): 5 High Risk, 4 Moderate Risk, 5 Low Risk (64.3% symptomatic).
  - Natural Sciences & General (N=13): 5 High Risk, 5 Moderate Risk, 3 Low Risk (76.9% symptomatic).
  - High risk is concentrated in high-enrollment STEM programs (Computing and Engineering account for 15 out of 28 high-risk students).

#### Worksheet 5: Distribution of Mental Health Condition Count
- **Chart Type:** Discrete Histogram / Comorbidity Distribution
- **Dimensions:** `Condition_Count` (0, 1, 2, 3)
- **Measures:** `COUNTD([User_ID])`
- **Purpose:** Detail the exact clinical comorbidity burden across students.
- **Key Observations:**
  - 0 conditions: 37 students (36.6%)
  - 1 condition: 36 students (35.6%)
  - 2 conditions: 18 students (17.8%)
  - 3 conditions (triply symptomatic): 10 students (9.9%)
  - Approximately 1 in 10 students reports experiencing depression, anxiety, and panic attacks simultaneously.

#### Worksheet 6: Student Mental Health Treatment Gap
- **Chart Type:** Categorical Status Bar Chart
- **Dimensions:** `Treatment_Gap` (`Untreated Condition`, `No Identified Condition`, `Condition Treated`)
- **Measures:** `COUNTD([User_ID])`
- **Purpose:** Quantify the magnitude of unaddressed psychological distress on campus.
- **Key Observations:**
  - Untreated Condition: 58 students (57.4% of total; 90.6% of symptomatic students).
  - No Identified Condition: 37 students (36.6% of total).
  - Condition Treated: 6 students (5.9% of total; 9.4% of symptomatic students).
  - Demonstrates an overwhelming 90.6% treatment deficit among students reporting distress.

#### Worksheet 7: Prevalence of Self-Reported Mental Health Conditions
- **Chart Type:** Benchmark Bar Chart
- **Dimensions:** Condition Category (`Depression`, `Anxiety`, `Panic Attack`)
- **Measures:** Prevalence Percentage (`SUM([Flag]) / [Total Students]`)
- **Purpose:** Benchmark the comparative prevalence rates of the three tracked conditions.
- **Key Observations:**
  - Depression: 35 / 101 (34.7%)
  - Anxiety: 34 / 101 (33.7%)
  - Panic Attacks: 33 / 101 (32.7%)
  - Remarkably balanced distribution across all three symptom categories, indicating widespread multi-factorial stress.

#### Worksheet 8: CGPA and Mental Health Risk
- **Chart Type:** Box Plot with Distribution Stripplot & Mean Points
- **Dimensions:** `Mental_Health_Risk` (`Low Risk`, `Moderate Risk`, `High Risk`)
- **Measures:** `CGPA_Midpoint` (1.00 to 3.75)
- **Purpose:** Investigate the relationship between academic achievement and mental health risk.
- **Key Observations:**
  - Low Risk: Mean CGPA = 3.26, Median = 3.25 (IQR = 0.50).
  - Moderate Risk: Mean CGPA = 3.40, Median = 3.25 (IQR = 0.50).
  - High Risk: Mean CGPA = 3.45, Median = 3.50 (IQR = 0.50, range 2.75–3.75).
  - High-risk students maintain high academic standing (mean 3.45), demonstrating that academic success does not protect against acute psychological distress. Non-causal observation.

#### Worksheet 9: Age and Mental Health Condition Count
- **Chart Type:** Column Chart of Mean Condition Load by Age
- **Dimensions:** `Age` (18 to 24)
- **Measures:** `AVG([Condition_Count])` with cohort counts
- **Purpose:** Trace condition load progression across student chronological ages.
- **Key Observations:**
  - Mean condition count remains relatively steady across all age cohorts: 18 (1.00), 19 (1.09), 20 (1.17), 21 (1.00), 22 (1.00), 23 (1.08), 24 (1.17).
  - Confirms that mental health concerns affect students throughout their entire university trajectory.

#### Worksheet 10: Treatment Seeking Across Mental Health Risk Levels
- **Chart Type:** Segmented Stacked Column Chart
- **Dimensions:** `Mental_Health_Risk`, `Treatment_Sought` (`Yes` / `No`)
- **Measures:** `COUNTD([User_ID])`
- **Purpose:** Analyze healthcare access barriers stratified by clinical severity.
- **Key Observations:**
  - Low Risk: 0 / 37 sought treatment (0.0%).
  - Moderate Risk: 0 / 36 sought treatment (0.0%).
  - High Risk: 6 / 28 sought treatment (21.4%).
  - 78.6% of students in the highest risk category have never consulted a clinical specialist, demonstrating extreme stigma or access friction.

---

### 4. Interactive Dashboards

#### Dashboard 1: Student Mental Health Overview
- **Layout Architecture:** Executive 3-tier hierarchy (1920 &times; 1080 responsive grid):
  - **Header / KPIs:** 
    - Total Students: `101`
    - High-Risk Students: `28 (27.7%)`
    - Symptomatic Care Gap: `58 (90.6%)`
  - **Middle Row (Demographics & Risk):**
    - Mental Health Risk Distribution
    - Mental Health Conditions by Gender
    - Mental Health Risk Across Age Groups
  - **Bottom Row (Academic & Institutional):**
    - Faculty-wise Mental Health Risk
    - Student Mental Health Treatment Gap
    - Distribution of Condition Count
- **Interactive Global Filters:** `Gender`, `Age_Group`, `Faculty`, `Mental_Health_Risk`.

#### Dashboard 2: Mental Health Risk & Treatment Dashboard
- **Layout Architecture:** Specialized 2 &times; 2 clinical healthcare grid:
  - Top Left: Campus Care Deficit Donut / Distribution
  - Top Right: Treatment Seeking Across Risk Levels
  - Bottom Left: Comorbidity Severity Histogram (0–3 Conditions)
  - Bottom Right: Conditions by Gender Clustered Comparison
- **Purpose:** Equips campus healthcare centers with direct operational evidence for counseling triage and mental health awareness campaigns.

---

### 5. Data Limitations & Epidemiological Disclaimers
1. **Self-Reported Nature:** All mental health indicators are derived from student self-administered survey questions. They represent self-reported symptoms and do not constitute formal DSM-5 or ICD-11 psychiatric diagnoses.
2. **Sample Size (N=101):** The cohort reflects a single institutional survey sample. Subgroup analyses in smaller faculties (e.g. Business N=5, Allied Health N=7) should be interpreted descriptively.
3. **Correlation vs. Causation:** Observed associations (such as high GPA among high-risk students) represent empirical correlations. No causal inferences are claimed or implied.
4. **CGPA Midpoint Proxy:** The CGPA variable was surveyed as discrete brackets (e.g. `3.50 - 4.00`) and mapped to midpoint numeric approximations (`3.75`).

---

### 6. Reproducibility Instructions
To reproduce all 10 visualizations, dashboards, and evidence artifacts:
```powershell
cd C:\Skillwallet

# 1. Generate all visualization evidence artifacts (PNGs)
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\generate_visualizations.py"

# 2. Generate the Tableau Workbook XML file
& "C:\Skillwallet\venv\Scripts\python.exe" "scripts\generate_tableau_twb.py"

# 3. Open in Tableau Desktop 2026.1
& "C:\Program Files\Tableau\Tableau 2026.1\bin\tableau.exe" "C:\Skillwallet\tableau\student_mental_health_visualizations.twb"
```
