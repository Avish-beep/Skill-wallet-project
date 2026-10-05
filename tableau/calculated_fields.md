# Tableau Calculated Fields Documentation
## Project: Analysing Mental Health in Student Ecosystem

All calculated field formulas documented below are verified to work directly in **Tableau Desktop 2026.1** against the processed schema (`student_mental_health_cleaned.csv`).

---

### 1. `Total Students (Denominator)`
- **Purpose:** Produces an accurate distinct count of students regardless of worksheet aggregation level.
- **Formula:**
  ```tableau
  COUNTD([student_id])
  ```
- **Data Dependency:** `[student_id]`
- **Where Used:** All Executive KPI Cards, Tooltips, Percentage Calculations, Donut Chart Centers.

---

### 2. `High Risk Student Count`
- **Purpose:** Aggregates students with high-severity psychiatric load (≥2 conditions).
- **Formula:**
  ```tableau
  SUM(IF [mental_health_risk] = 'High Risk' THEN 1 ELSE 0 END)
  ```
- **Data Dependency:** `[mental_health_risk]`
- **Where Used:** Executive KPI Row, Risk Breakdown cards, Alert tooltips.

---

### 3. `High Risk Percentage`
- **Purpose:** Measures the cohort proportion meeting high clinical risk criteria.
- **Formula:**
  ```tableau
  SUM(IF [mental_health_risk] = 'High Risk' THEN 1 ELSE 0 END) / COUNTD([student_id])
  ```
- **Data Dependency:** `[mental_health_risk]`, `[student_id]`
- **Formatting:** Percentage, 1 decimal place (`35.6%`)
- **Where Used:** Header BAN KPI, Comparative Faculty Heatmap.

---

### 4. `Depression Prevalence Rate`
- **Purpose:** Calculates the percentage of filtered students reporting clinical depression.
- **Formula:**
  ```tableau
  SUM([depression_flag]) / COUNTD([student_id])
  ```
- **Data Dependency:** `[depression_flag]`, `[student_id]`
- **Formatting:** Percentage, 1 decimal place (`34.7%`)
- **Where Used:** Condition Prevalence Bar Chart, Demographic Cross-Tabs.

---

### 5. `Anxiety Prevalence Rate`
- **Purpose:** Calculates the percentage of filtered students reporting clinical anxiety.
- **Formula:**
  ```tableau
  SUM([anxiety_flag]) / COUNTD([student_id])
  ```
- **Data Dependency:** `[anxiety_flag]`, `[student_id]`
- **Formatting:** Percentage, 1 decimal place (`33.7%`)
- **Where Used:** Condition Prevalence Bar Chart, Age Trend Area Chart.

---

### 6. `Panic Attack Prevalence Rate`
- **Purpose:** Calculates the percentage of students experiencing recurrent panic attacks.
- **Formula:**
  ```tableau
  SUM([panic_attack_flag]) / COUNTD([student_id])
  ```
- **Data Dependency:** `[panic_attack_flag]`, `[student_id]`
- **Formatting:** Percentage, 1 decimal place (`32.7%`)
- **Where Used:** Condition Prevalence Bar Chart, Stress Proxy Analytics.

---

### 7. `Campus Treatment Gap Rate (%)`
- **Purpose:** Calculates the proportion of symptomatic students who have NOT received specialist treatment.
- **Formula:**
  ```tableau
  SUM(IF [condition_count] > 0 AND [treatment_sought] = 'No' THEN 1 ELSE 0 END) 
  / 
  SUM(IF [condition_count] > 0 THEN 1 ELSE 0 END)
  ```
- **Data Dependency:** `[condition_count]`, `[treatment_sought]`
- **Formatting:** Percentage, 1 decimal place (`90.5%`)
- **Where Used:** Crisis KPI Card, Care Utilization Bar Chart, Policy Recommendations.

---

### 8. `Comorbidity Classification`
- **Purpose:** Granular multi-morbid categorization for student psychiatric burden.
- **Formula:**
  ```tableau
  IF [condition_count] = 0 THEN 'Healthy Baseline'
  ELSEIF [condition_count] = 1 THEN 'Single Condition'
  ELSEIF [condition_count] = 2 THEN 'Dual Comorbidity'
  ELSEIF [condition_count] = 3 THEN 'Triple Comorbidity (Severe)'
  ELSE 'Other'
  END
  ```
- **Data Dependency:** `[condition_count]`
- **Where Used:** Comorbidity Matrix, Student Persona Segmentation.

---

### 9. `Academic Tier (CGPA Classification)`
- **Purpose:** Groups student academic performance into standardized academic honors tiers.
- **Formula:**
  ```tableau
  IF [cgpa_range] = '3.50 - 4.00' THEN 'First Class / Dean’s List'
  ELSEIF [cgpa_range] = '3.00 - 3.49' THEN 'Upper Second Class'
  ELSEIF [cgpa_range] = '2.50 - 2.99' THEN 'Lower Second Class'
  ELSEIF [cgpa_range] = '2.00 - 2.49' THEN 'Third Class'
  ELSE 'Academic Probation (<2.00)'
  END
  ```
- **Data Dependency:** `[cgpa_range]`
- **Where Used:** Academic Performance Analysis, Dual-Axis CGPA charts.

---

### 10. `Risk Alert Color Indicator`
- **Purpose:** Drives dynamic UI alert badges on Tableau dashboards.
- **Formula:**
  ```tableau
  IF [mental_health_risk] = 'High Risk' THEN '#EF4444'
  ELSEIF [mental_health_risk] = 'Moderate Risk' THEN '#F59E0B'
  ELSE '#10B981'
  END
  ```
- **Data Dependency:** `[mental_health_risk]`
- **Where Used:** Custom shape cards, Color shelf in Tableau Worksheets.
