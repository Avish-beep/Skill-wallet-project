# Tableau Visualization Implementation Plan
## Project: Analysing Mental Health in Student Ecosystem

This visualization plan is formulated **strictly from the empirical columns** present in `student_mental_health_cleaned.csv` (101 verified survey records). Every visualization has been mapped with its visual mark type, dimensions, measures, filters, and analytical intent.

---

### Visualization Catalog (12 Valid Visualizations)

#### 1. Total Student Cohort (Executive KPI Card)
- **Chart Type:** Big Number / KPI Card with BAN (Big-Ass Number) format
- **Dimensions:** None
- **Measures:** `COUNTD([student_id])`
- **Filters:** Academic Year, Gender, Faculty (Global)
- **Formatting:** 36pt Bold, Navy (`#1E293B`), Centered, Subtitle: "Total Survey Respondents"
- **Purpose & Expected Insight:** Provides the baseline denominator for all prevalence calculations across the student ecosystem.

#### 2. High-Risk Student Population (Executive KPI Card)
- **Chart Type:** KPI Card with Alert Indicator
- **Dimensions:** None
- **Measures:** `SUM(IF [mental_health_risk] = 'High Risk' THEN 1 ELSE 0 END)`
- **Calculated Metric:** `% High Risk = SUM(IF [mental_health_risk] = 'High Risk' THEN 1 ELSE 0 END) / COUNTD([student_id])`
- **Formatting:** Bold Red/Amber (`#E11D48`), Subtitle: "% of Total Cohort"
- **Purpose & Expected Insight:** Immediately surfaces the acute burden: 35.6% (36 students) suffer from 2 or more concurrent clinical conditions.

#### 3. Campus Treatment Gap (Crisis KPI Card)
- **Chart Type:** KPI Card with Warning Icon
- **Dimensions:** None
- **Measures:** `SUM(IF [treatment_gap] = 'Untreated Condition' THEN 1 ELSE 0 END)`
- **Calculated Metric:** `% Untreated = [Untreated Count] / SUM(IF [condition_count] > 0 THEN 1 ELSE 0 END)`
- **Formatting:** Orange/Coral (`#F97316`), Subtitle: "Affected Students Untreated (90.5%)"
- **Purpose & Expected Insight:** Highlights that of the 63 students with mental health conditions, 57 have never consulted a specialist.

#### 4. Clinical Condition Prevalence (Comparative Bar Chart)
- **Chart Type:** Grouped Horizontal Bar Chart
- **Dimensions:** Measure Names (`Depression`, `Anxiety`, `Panic Attack`)
- **Measures:** `SUM([depression_flag])`, `SUM([anxiety_flag])`, `SUM([panic_attack_flag])`
- **Labels:** Absolute Count + Percentage of Total Cohort
- **Color:** Soft Indigo (`#6366F1`)
- **Purpose & Expected Insight:** Quantifies individual condition burdens (Depression: 34.7%, Anxiety: 33.7%, Panic Attacks: 32.7%).

#### 5. Mental Health Risk Stratification (Donut / Pie Chart)
- **Chart Type:** Donut Chart (Dual Axis Pie with inner white circle)
- **Dimensions:** `mental_health_risk` (`Low Risk`, `Moderate Risk`, `High Risk`)
- **Measures:** `COUNTD([student_id])`
- **Color Palette:** Green (`#10B981` - Low), Amber (`#F59E0B` - Moderate), Crimson (`#EF4444` - High)
- **Purpose & Expected Insight:** Visualizes the proportion of students across risk tiers (Low: 37.6%, Moderate: 26.7%, High: 35.6%).

#### 6. Gender-Based Vulnerability Breakdown (100% Stacked Bar Chart)
- **Chart Type:** 100% Stacked Bar Chart
- **Dimensions (Rows):** `gender` (Female, Male)
- **Dimensions (Color):** `mental_health_risk`
- **Measures (Columns):** `COUNTD([student_id])` with Quick Table Calculation (`Percent of Total`, Compute Using: `mental_health_risk`)
- **Purpose & Expected Insight:** Evaluates whether female or male students bear disproportionate vulnerability. Female respondents (75/101) exhibit high condition loads requiring targeted campus outreach.

#### 7. Academic Seniority Progression (Year of Study Risk Analysis)
- **Chart Type:** Grouped Column Chart with Trend Line
- **Dimensions (Columns):** `year_of_study` (`Year 1`, `Year 2`, `Year 3`, `Year 4`)
- **Measures (Rows):** `AVG([condition_count])` and `COUNTD([student_id])`
- **Color:** `mental_health_risk`
- **Purpose & Expected Insight:** Demonstrates that Year 1 transition stress and Year 3 pre-graduation pressure represent peak vulnerability windows.

#### 8. Academic Performance (CGPA Tiers) vs. Mental Health Risk
- **Chart Type:** Stacked Bar Chart with Dual-Axis Average CGPA Line
- **Dimensions (Columns):** `cgpa_range` (`0 - 1.99`, `2.00 - 2.49`, `2.50 - 2.99`, `3.00 - 3.49`, `3.50 - 4.00`)
- **Measures (Rows):** `COUNTD([student_id])` by `mental_health_risk`
- **Secondary Axis:** `AVG([cgpa_midpoint])`
- **Purpose & Expected Insight:** Directly analyzes the correlation between academic outcomes and mental health distress, revealing significant condition prevalence even among top academic achievers (`3.50 - 4.00`).

#### 9. Faculty / Academic Discipline Risk Heatmap
- **Chart Type:** Highlight Table / Heatmap
- **Dimensions (Rows):** `faculty`
- **Dimensions (Columns):** Measure Names (`Depression Rate`, `Anxiety Rate`, `Panic Attack Rate`, `High Risk %`)
- **Measures (Color & Text):** Calculated prevalence percentages
- **Color Palette:** Sequential Red-Gold Palette
- **Purpose & Expected Insight:** Identifies specific academic faculties (e.g. Engineering, Computing & IT) with heightened distress clusters to inform departmental counseling.

#### 10. Comorbidity Severity Distribution (Bar Histogram)
- **Chart Type:** Vertical Discrete Frequency Histogram
- **Dimensions (Columns):** `condition_count` (`0`, `1`, `2`, `3` conditions)
- **Measures (Rows):** `COUNTD([student_id])`
- **Color Gradient:** Green (0) to Dark Red (3)
- **Purpose & Expected Insight:** Details the severity distribution: 16 students suffer from all three conditions simultaneously (severe comorbidity).

#### 11. The Care Utilization Breakdown (Specialist Consultation)
- **Chart Type:** Diverging / Segmented Bar Chart
- **Dimensions (Rows):** `mental_health_risk`
- **Dimensions (Color):** `treatment_sought` (`Yes`, `No`)
- **Measures (Columns):** `COUNTD([student_id])`
- **Purpose & Expected Insight:** Proves that even in the `High Risk` category, fewer than 15% of students have accessed specialist clinical support.

#### 12. Age Distribution & Condition Onset (Area / Step Chart)
- **Chart Type:** Area Chart
- **Dimensions (Columns):** `age` (`18` to `24`)
- **Measures (Rows):** `SUM([depression_flag])`, `SUM([anxiety_flag])`, `SUM([panic_attack_flag])`
- **Color Palette:** Distinct 3-color palette
- **Purpose & Expected Insight:** Maps symptom onset across undergraduate age cohorts, with the age 18-20 cohort demonstrating rapid onset spikes.
