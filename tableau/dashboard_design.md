# Tableau Dashboard Architecture & Responsive Design Documentation
## Task: Responsive and Design of Dashboard (Epic 3)
**Project Title:** Analysing Mental Health in Student Ecosystem  
**Target Platform:** Tableau Desktop 2026.1 / Tableau Public  
**Primary Dataset:** `C:\Skillwallet\data\processed\student_mental_health_processed.csv` (101 Rows, 23 Columns)  

---

### 1. Accurate Project-Specific Dashboard Description

> **Official Dashboard Description:**
> The **Student Mental Health Analysis Dashboard** provides an interactive overview of self-reported mental-health conditions among 101 surveyed students. It utilizes validated demographic, academic, mental-health-risk, condition-count, and treatment-seeking fields to help educational stakeholders and wellness administrators identify patterns across gender, age group, and academic faculty.
> 
> - **Executive KPI Cards:** Summarize the student cohort (101 students) and stratify risk tiers (28 high risk, 36 moderate risk, 58 untreated symptomatic students).
> - **Risk Distribution:** Illustrates the proportion of students categorized as Low (36.6%), Moderate (35.6%), and High Risk (27.7%).
> - **Gender Visualization:** Compares self-reported depression, anxiety, and panic attack indicators between female (N=75) and male (N=26) cohorts.
> - **Age-Group & Faculty Views:** Highlight how comorbidity risk is distributed across undergraduate seniority levels (18–20 vs. 21–24) and 7 macro academic disciplines.
> - **Treatment-Gap Visualizations:** Highlight self-reported treatment-seeking patterns, revealing that 90.6% of symptomatic students have not accessed specialist care.
> - **Condition-Count Visualization:** Displays the distribution of concurrent self-reported conditions (0 to 3), detailing comorbidity burdens.
> 
> *Epidemiological Disclaimer: This project is based entirely on self-reported student mental-health survey data. Survey responses reflect self-reported symptoms and do not represent formal psychiatric diagnoses. All observed associations are correlational and non-causal.*

---

### 2. Canvas & Responsive Layout Architecture

- **Dashboard Canvas Dimensions:** 1920px × 1080px (Responsive 16:9 Desktop & Tablet Grid)
- **Tableau Layout Type:** Range Layout (`minwidth='1280'`, `minheight='720'`, `maxwidth='1920'`, `maxheight='1080'`)
- **Responsive Approach:** 
  - Dynamic percentage-based horizontal and vertical layout containers ensure fluid resizing across standard laptops, high-resolution monitors, and projection screens.
  - Generous internal padding (10–14px per card) prevents overlapping chart marks, cramped labels, or clipped text headers.
  - Automatic wrapping in mobile/phone view automatically stacks KPI cards into a 2×2 grid and analytical views into a vertical scroll stream.

---

### 3. Visual Layout Structure (Dashboard 1: Student Mental Health Overview)

```
+-------------------------------------------------------------------------------------------------------------------------------+
|  HEADER CONTAINER (Dark Slate #1E293B, Height: ~60px)                                                                        |
|  Title: Student Mental Health Overview                                                                                        |
|  Subtitle: Interactive Visual Intelligence Dashboard | Survey Cohort Analysis (N=101)                                         |
|  [▼ Filter: Gender]      [▼ Filter: Age Group]      [▼ Filter: Faculty]      [▼ Filter: Risk Tier]                            |
+-------------------------------------------------------------------------------------------------------------------------------+
|  TOP KPI CONTAINER (4 Aligned Equal-Width Cards, Height: ~110px)                                                              |
|  +------------------------+  +------------------------+  +------------------------+  +------------------------+               |
|  | TOTAL STUDENTS         |  | HIGH RISK STUDENTS     |  | MODERATE RISK          |  | TREATMENT GAP          |               |
|  |         101            |  |      28 (27.7%)        |  |      36 (35.6%)        |  |      58 (90.6%)        |               |
|  | Full Cohort (COUNTD)   |  | ≥2 Conditions          |  | 1 Condition            |  | Symptomatic Untreated  |               |
|  +------------------------+  +------------------------+  +------------------------+  +------------------------+               |
+-------------------------------------------------------------------------------------------------------------------------------+
|  ROW 1 PANELS: DEMOGRAPHIC & RISK STRATIFICATION (Height: ~380px)                                                             |
|  +----------------------------+  +----------------------------------------------------+  +----------------------------+       |
|  | Panel 1: Risk Distribution |  | Panel 2: Self-Reported Conditions by Gender        |  | Panel 3: Risk by Age Group |       |
|  | Low: 37 (36.6%)            |  | Clustered Bars (Depression, Anxiety, Panic Attack) |  | Stacked 100% Columns       |       |
|  | Moderate: 36 (35.6%)       |  | Female (N=75) vs Male (N=26)                       |  | Underclassmen (18-20) vs   |       |
|  | High: 28 (27.7%)           |  | With exact within-gender prevalence labels         |  | Upperclassmen (21-24)      |       |
|  +----------------------------+  +----------------------------------------------------+  +----------------------------+       |
+-------------------------------------------------------------------------------------------------------------------------------+
|  ROW 2 PANELS: ACADEMIC DISCIPLINES & CARE DEFICIT (Height: ~380px)                                                           |
|  +----------------------------------------------------+  +----------------------------+  +----------------------------+       |
|  | Panel 4: Mental Health Risk by Faculty             |  | Panel 5: Treatment Gap     |  | Panel 6: Condition Count   |       |
|  | Horizontal Stacked Bars across 7 Disciplines       |  | Untreated Symptomatic: 58  |  | Discrete Histogram (0-3)   |       |
|  | (Highest in Computing & IT and Engineering)        |  | Healthy: 37, Treated: 6    |  | 0: 37, 1: 36, 2: 18, 3: 10 |       |
|  +----------------------------------------------------+  +----------------------------+  +----------------------------+       |
+-------------------------------------------------------------------------------------------------------------------------------+
|  FOOTER: Data Source: student_mental_health_processed.csv | Validated N=101 | Non-Causal Descriptive Research                  |
+-------------------------------------------------------------------------------------------------------------------------------+
```

---

### 4. Visual Layout Structure (Dashboard 2: Mental Health Risk & Treatment Dashboard)

- **Grid Architecture:** 2 &times; 3 balanced clinical grid.
- **Header:** Slate container with quick filters for `Mental_Health_Risk`, `Treatment_Sought`, and `Faculty`.
- **Top Row:**
  - Panel 1: *Treatment Seeking Across Risk Tiers* (Stacked bars: 22/28 high-risk students untreated).
  - Panel 2: *Treatment Gap Distribution* (Pie breakdown: 57.4% untreated, 36.6% healthy, 5.9% treated).
  - Panel 3: *Condition Count Distribution* (Histogram: 0, 1, 2, 3 concurrent conditions).
- **Bottom Row:**
  - Panel 4: *Self-Reported Conditions by Gender* (Clustered bars).
  - Panel 5: *Mental Health Risk Distribution* (Bar chart).
  - Panel 6: *Mental Health Risk by Faculty* (Horizontal stacked bars).

---

### 5. Color Strategy & Typography
- **Background Canvas:** Soft Slate Clean Gray (`#F0F4F8`).
- **Containers & Cards:** Clean White (`#FFFFFF`) with subtle border lines (`#CBD5E1`) and 1.2px thickness.
- **Risk Severity Palette:**
  - `Low Risk`: `#38A169` (Calm Forest Green)
  - `Moderate Risk`: `#DD6B20` (Amber / Warm Orange)
  - `High Risk`: `#E53E3E` (Clinical Crimson Red)
- **Gender Disaggregation:**
  - `Female`: `#805AD5` (Royal Purple)
  - `Male`: `#3182CE` (Steel Blue)
- **Condition Palette:**
  - `Depression`: `#2B6CB0` (Deep Blue)
  - `Anxiety`: `#D69E2E` (Warm Mustard)
  - `Panic Attack`: `#C53030` (Crimson)
- **Typography:** Standard cross-platform sans-serif (`DejaVu Sans`, `Arial`, `Helvetica`).
  - Dashboard Title: 18pt Bold White
  - Panel Titles: 10pt Bold Slate (`#0F172A`)
  - Big Numbers (BANs): 24pt Bold
  - Axis & Tick Labels: 8–9pt Regular Slate (`#334155`)

---

### 6. Accessibility & Readability Considerations
1. **High Contrast Ratios:** All text elements exceed WCAG AA 4.5:1 contrast requirements against their card backgrounds.
2. **Dual Encoding:** Key metrics feature both direct numeric values and percentage annotations to avoid reliance on tooltips alone.
3. **No Overlapping Text:** Margins and tick mark rotations are explicitly spaced to prevent label truncation.
4. **Zero 3D or Distorted Charts:** Standard 2D Cartesian and horizontal representations maintain visual truth and ratio fidelity.

---

### 7. Interactive Dashboard Actions
1. **Interactive Global Filters:**
   - `Gender`: Disaggregates all views by Female (N=75) and Male (N=26).
   - `Age_Group`: Filters between Underclassmen (18–20) and Upperclassmen (21–24).
   - `Faculty`: Isolates students belonging to specific academic disciplines.
   - `Mental_Health_Risk`: Filters views to highlight High Risk, Moderate Risk, or Low Risk cohorts.
2. **Cross-Filtering:** Selecting a risk segment in Panel 1 cross-highlights associated students in the Gender, Age, and Faculty views.

---

### 8. Data Source & Integrity Verification
- **Verified Data Path:** `data/processed/student_mental_health_processed.csv` (101 Rows, 23 Columns, 0 Nulls, 0 Duplicates).
- **Excluded Metrics:** Placeholder task template metrics (*Average Mental Score*, *Sleep Duration*, *Attendance Rate*, *Stress Level*, *Heart Rate Variability*, *Study Hours*, and *Academic Performance*) **do not exist in our dataset and were strictly excluded**.
