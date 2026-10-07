# Tableau Dashboard Architecture & Layout Design
## Dashboard Suite: Analysing Mental Health in Student Ecosystem

This document defines the formal layout architecture, KPI card definitions, visual hierarchies, and interactive action filters for the two dashboards in **Tableau Desktop 2026.1** and **Tableau Public**.

**Source Data:** `data/processed/student_mental_health_processed.csv` (101 Records, 23 Columns)  
**Strict Integrity Rule:** All metrics are computed exclusively from validated survey columns. Zero synthetic or placeholder fields (no fake mental score, sleep hours, attendance rate, or heart rate variability).

---

### Dashboard 1: Student Mental Health Overview

#### 1. Canvas & Theme Specifications
- **Target Dimensions:** 1920px × 1080px (Responsive 16:9 Desktop Layout)
- **Background Styling:** Neutral Clean Light Theme (`#F8FAFC`)
- **Card Containers:** Pure White Cards (`#FFFFFF`) with 1.2px border (`#CBD5E0`) and 12px inner padding
- **Typography:** Arial / Segoe UI (Standard Tableau Safe Fonts)

#### 2. Visual Layout Structure

```
+-----------------------------------------------------------------------------------------------------------------------+
|  HEADER CONTAINER                                                                                                     |
|  Title: Student Mental Health Overview                                                                                |
|  Subtitle: Self-reported student mental-health survey data (N=101) | Non-causal empirical analysis                     |
+-----------------------------------------------------------------------------------------------------------------------+
|  GLOBAL FILTER BAR (Horizontal Layout Container)                                                                      |
|  [Gender: All v]   [Faculty: All v]   [Age Group: All v]   [Mental Health Risk: All v]                                |
+-----------------------------------------------------------------------------------------------------------------------+
|  TOP ROW: 4 VALIDATED KPI CARDS (Computed strictly from real dataset fields)                                          |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+                       |
|  | TOTAL STUDENTS     |  | HIGH RISK STUDENTS |  | MODERATE RISK      |  | TREATMENT GAP      |                       |
|  | COUNT(User_ID)     |  | Mental_Health_Risk |  | Mental_Health_Risk |  | Untreated          |                       |
|  |                    |  | = High Risk        |  | = Moderate Risk    |  | Symptomatic        |                       |
|  |       101          |  |    28 (27.7%)      |  |    36 (35.6%)      |  |    58 (90.6%)      |                       |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+                       |
+-----------------------------------------------------------------------------------------------------------------------+
|  MIDDLE ROW: DEMOGRAPHIC & RISK STRATIFICATION                                                                        |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
|  | Panel A: Risk Distribution     |  | Panel B: Conditions by Gender  |  | Panel C: Risk Across Age Group |           |
|  | Mental_Health_Risk vs          |  | Gender vs Depression_Flag,     |  | Age_Group vs Mental_Health_Risk|           |
|  | COUNT(User_ID)                 |  | Anxiety_Flag, Panic_Attack_Flag|  | Stacked Column Chart           |           |
|  | (Low: 37, Mod: 36, High: 28)   |  | (Female N=75, Male N=26)       |  | (18-20 vs 21-24)               |           |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
+-----------------------------------------------------------------------------------------------------------------------+
|  BOTTOM ROW: ACADEMIC DISCIPLINES & CARE DEFICIT                                                                      |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
|  | Panel D: Faculty Risk Profile  |  | Panel E: Student Treatment Gap |  | Panel F: Condition Count Dist. |           |
|  | Faculty vs Mental_Health_Risk  |  | Treatment_Gap vs               |  | Condition_Count (0, 1, 2, 3)   |           |
|  | Horizontal Stacked Bars        |  | COUNT(User_ID)                 |  | Discrete Histogram             |           |
|  | (7 Academic Disciplines)       |  | (Untreated 58, Healthy 37, 6)  |  | (0: 37, 1: 36, 2: 18, 3: 10)   |           |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
+-----------------------------------------------------------------------------------------------------------------------+
|  FOOTER: Data Source: student_mental_health_processed.csv | Disclaimer: Self-reported student survey data           |
+-----------------------------------------------------------------------------------------------------------------------+
```

---

### Dashboard 2: Mental Health Risk & Treatment Dashboard

#### 1. Canvas & Focus Specifications
- **Target Dimensions:** 1920px × 1080px (Responsive Healthcare Grid)
- **Primary Stakeholders:** University Healthcare Centers, Counseling Services, Student Welfare Deans
- **Core Mission:** Analyze specialist care-seeking behaviors, treatment barriers, and comorbidity severity.

#### 2. Visual Layout Structure (2 × 3 Grid)

```
+-----------------------------------------------------------------------------------------------------------------------+
|  HEADER: Mental Health Risk & Treatment Dashboard (Care Utilization & Treatment Deficit)                             |
+-----------------------------------------------------------------------------------------------------------------------+
|  ROW 1: TREATMENT-SEEKING BEHAVIOR & CARE GAP                                                                         |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
|  | Panel 1: Treatment Seeking     |  | Panel 2: Treatment Gap Status  |  | Panel 3: Condition Count Dist. |           |
|  | Across Risk Tiers              |  | Pie / Donut Breakdown          |  | Comorbidity Histogram          |           |
|  | Mental_Health_Risk vs          |  | Untreated (57.4%),             |  | 0 Cond: 37 (36.6%)             |           |
|  | Treatment_Sought               |  | Healthy (36.6%),               |  | 1 Cond: 36 (35.6%)             |           |
|  | (Only 6/28 High-Risk sought)   |  | Treated (5.9%)                 |  | 2 Cond: 18, 3 Cond: 10         |           |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
+-----------------------------------------------------------------------------------------------------------------------+
|  ROW 2: CLINICAL BURDEN & DEPARTMENTAL VULNERABILITY                                                                  |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
|  | Panel 4: Conditions by Gender  |  | Panel 5: Risk Distribution     |  | Panel 6: Faculty-wise Risk     |           |
|  | Depression, Anxiety, Panic     |  | Low, Moderate, High Risk       |  | Stacked Horizontal Bars across |           |
|  | by Gender                      |  | Bar Distribution               |  | 7 Academic Faculties           |           |
|  +--------------------------------+  +--------------------------------+  +--------------------------------+           |
+-----------------------------------------------------------------------------------------------------------------------+
|  FOOTER: Self-reported student mental-health survey data (N=101) | Non-causal empirical analysis                      |
+-----------------------------------------------------------------------------------------------------------------------+
```

---

### 3. Action Filters & Interactivity
1. **Interactive Global Filters:**
   - `Gender`: Filters dashboard views between Female (N=75) and Male (N=26).
   - `Faculty`: Filters all worksheets to examine departmental profiles.
   - `Age_Group`: Toggles between Underclassmen (18–20) and Upperclassmen (21–24).
   - `Mental_Health_Risk`: Filters views to isolate High Risk, Moderate Risk, or Low Risk cohorts.
2. **Sheet Cross-Filtering:**
   - Clicking a segment in *Panel A (Risk Distribution)* highlights associated student records across the remaining worksheets.
   - Clicking a faculty in *Panel D (Faculty Risk)* isolates the clinical burden within that discipline.
