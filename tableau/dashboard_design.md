# Tableau Dashboard Architecture & Layout Design
## Dashboard Title: Analysing Mental Health in Student Ecosystem

### Canvas Specifications
- **Target Dimensions:** 1400px width × 1050px height (Fixed Desktop / Academic Presentation Layout)
- **Background Styling:** Neutral Slate Clean Light Theme (`#F8FAFC`)
- **Card Containers:** Pure White Cards (`#FFFFFF`) with 1px border (`#E2E8F0`) and 8px inner padding
- **Typography:** Arial / Segoe UI (Standard Tableau Safe Fonts)

---

### Layout Hierarchy

```
+---------------------------------------------------------------------------------------------------+
|  HEADER CONTAINER                                                                                 |
|  Title: Analysing Mental Health in Student Ecosystem                                              |
|  Subtitle: An Empirical Study of Psychological Distress, Academic Tiers, and Healthcare Gaps      |
+---------------------------------------------------------------------------------------------------+
|  GLOBAL FILTER BAR (Horizontal Layout Container)                                                  |
|  [Gender: All v]   [Faculty: All v]   [Year of Study: All v]   [Academic Standing: All v]         |
+---------------------------------------------------------------------------------------------------+
|  EXECUTIVE KPI ROW (5 Equal Column Cards)                                                         |
|  +-------------+  +-------------+  +-------------+  +-------------+  +-------------+              |
|  | TOTAL       |  | HIGH RISK   |  | DEPRESSION  |  | ANXIETY     |  | TREATMENT   |              |
|  | STUDENTS    |  | COHORT      |  | PREVALENCE  |  | PREVALENCE  |  | GAP RATE    |              |
|  |    101      |  | 36 (35.6%)  |  | 35 (34.7%)  |  | 34 (33.7%)  |  | 57 (90.5%)  |              |
|  +-------------+  +-------------+  +-------------+  +-------------+  +-------------+              |
+---------------------------------------------------------------------------------------------------+
|  SECTION 1: OVERALL MENTAL HEALTH & RISK STRATIFICATION                                           |
|  +---------------------------------------------+  +---------------------------------------------+  |
|  | [Worksheet 5] Risk Tier Distribution        |  | [Worksheet 4] Clinical Condition Burden     |  |
|  | Donut Chart (Low vs Moderate vs High Risk)  |  | Horizontal Bars (Depression, Anxiety, Panic)|  |
|  +---------------------------------------------+  +---------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
|  SECTION 2: ACADEMIC CORRELATIONS & SENIORITY PROGRESSION                                         |
|  +---------------------------------------------+  +---------------------------------------------+  |
|  | [Worksheet 8] CGPA Tiers vs Risk Profile    |  | [Worksheet 7] Year of Study Progression     |  |
|  | Stacked 100% Bar by Academic Standing       |  | Multi-condition Average Burden by Class     |  |
|  +---------------------------------------------+  +---------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
|  SECTION 3: CARE UTILIZATION & COMORBIDITY SEVERITY                                               |
|  +---------------------------------------------+  +---------------------------------------------+  |
|  | [Worksheet 10] Comorbidity Overlap Matrix   |  | [Worksheet 11] The Campus Treatment Gap     |  |
|  | Severity Histogram (0, 1, 2, 3 Conditions)  |  | Symptomatic Students Seeking vs Untreated   |  |
|  +---------------------------------------------+  +---------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
|  SECTION 4: DEMOGRAPHIC & FACULTY RISK CLUSTERING                                                 |
|  +---------------------------------------------+  +---------------------------------------------+  |
|  | [Worksheet 6] Gender Vulnerability Profile  |  | [Worksheet 9] Faculty Distress Heatmap      |  |
|  | Diverging Gender Comparison                 |  | Matrix: Faculty Discipline vs Condition %   |  |
|  +---------------------------------------------+  +---------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
|  FOOTER / DATA SOURCE ATTRIBUTION                                                                 |
|  Data Source: Cleaned Survey Dataset (N=101) | SkillWallet VIP Data Analytics Project             |
+---------------------------------------------------------------------------------------------------+
```

---

### Dashboard Interactivity & Action Filters
1. **Global Quick Filters:**
   - `gender` (Single value dropdown / multiple)
   - `faculty` (Multiple dropdown)
   - `year_of_study` (Compact checklist)
   - `cgpa_range` (Multiple dropdown)
2. **Dashboard Filter Actions (Cross-Highlighting):**
   - **Action 1 (Filter by Risk Tier):** Clicking a segment on the Donut Chart (e.g. *High Risk*) filters all academic and faculty worksheets to display only High Risk students.
   - **Action 2 (Filter by Academic Standing):** Selecting a CGPA tier (e.g. *3.50 - 4.00*) updates the Care Utilization and Faculty views for that honors cohort.
   - **Action 3 (Faculty Drill-Down):** Clicking a discipline on the Faculty Heatmap isolates that department's specific mental health profile.
