# Tableau Calculated Fields Documentation
## Project: Analysing Mental Health in Student Ecosystem

All calculated field formulas documented below are verified to work directly in **Tableau Desktop 2026.1** and **Tableau Public** against the validated processed dataset (`data/processed/student_mental_health_processed.csv`).

**Data Integrity Standard:** All formulas rely exclusively on validated empirical survey columns. No synthetic metrics (no fake sleep duration, attendance rate, or stress score).

---

### 1. `Total Students (Denominator)`
- **Purpose:** Produces an accurate distinct count of students regardless of worksheet aggregation level.
- **Formula:**
  ```tableau
  COUNTD([User_ID])
  ```
- **Data Dependency:** `[User_ID]`
- **Where Used:** All Executive KPI Cards, Tooltips, Percentage Calculations, Baseline Denominators.

---

### 2. `High Risk Student Count`
- **Purpose:** Aggregates students with high-severity psychiatric load (≥2 concurrent conditions).
- **Formula:**
  ```tableau
  COUNTD(IF [Mental_Health_Risk] = 'High Risk' THEN [User_ID] END)
  ```
- **Data Dependency:** `[Mental_Health_Risk]`, `[User_ID]`
- **Where Used:** Executive KPI Row, Risk Breakdown cards, Alert tooltips.
- **Value:** 28 students (27.7% of cohort).

---

### 3. `High Risk Percentage`
- **Purpose:** Measures the cohort proportion meeting high clinical risk criteria.
- **Formula:**
  ```tableau
  [High Risk Student Count] / [Total Students]
  ```
- **Data Dependency:** `[High Risk Student Count]`, `[Total Students]`
- **Formatting:** Percentage, 1 decimal place (`27.7%`)
- **Where Used:** Header BAN KPI, Comparative Faculty Heatmap.

---

### 4. `Moderate Risk Student Count`
- **Purpose:** Aggregates students with single condition load requiring early intervention.
- **Formula:**
  ```tableau
  COUNTD(IF [Mental_Health_Risk] = 'Moderate Risk' THEN [User_ID] END)
  ```
- **Data Dependency:** `[Mental_Health_Risk]`, `[User_ID]`
- **Formatting:** Whole number
- **Value:** 36 students (35.6% of cohort).

---

### 5. `Treatment Gap Student Count`
- **Purpose:** Identifies symptomatic students who have NOT received specialist treatment.
- **Formula:**
  ```tableau
  COUNTD(IF [Treatment_Gap] = 'Untreated Condition' THEN [User_ID] END)
  ```
- **Data Dependency:** `[Treatment_Gap]`, `[User_ID]`
- **Value:** 58 students (57.4% of total cohort; 90.6% of symptomatic students).

---

### 6. `Treatment Gap Rate (%)`
- **Purpose:** Calculates the percentage of symptomatic students left untreated.
- **Formula:**
  ```tableau
  [Treatment Gap Student Count] / COUNTD(IF [Condition_Count] > 0 THEN [User_ID] END)
  ```
- **Data Dependency:** `[Treatment Gap Student Count]`, `[Condition_Count]`, `[User_ID]`
- **Formatting:** Percentage, 1 decimal place (`90.6%`)
- **Where Used:** KPI Card, Mental Health Risk & Treatment Dashboard.

---

### 7. `Depression Prevalence Rate (%)`
- **Purpose:** Calculates the percentage of filtered students reporting depression symptoms.
- **Formula:**
  ```tableau
  SUM([Depression_Flag]) / [Total Students]
  ```
- **Data Dependency:** `[Depression_Flag]`, `[User_ID]`
- **Formatting:** Percentage, 1 decimal place (`34.7%`)
- **Where Used:** Condition Prevalence Bar Chart, Demographic Cross-Tabs.

---

### 8. `Anxiety Prevalence Rate (%)`
- **Purpose:** Calculates the percentage of filtered students reporting anxiety symptoms.
- **Formula:**
  ```tableau
  SUM([Anxiety_Flag]) / [Total Students]
  ```
- **Data Dependency:** `[Anxiety_Flag]`, `[User_ID]`
- **Formatting:** Percentage, 1 decimal place (`33.7%`)
- **Where Used:** Condition Prevalence Bar Chart, Gender Comparison.

---

### 9. `Panic Attack Prevalence Rate (%)`
- **Purpose:** Calculates the percentage of students experiencing panic attacks.
- **Formula:**
  ```tableau
  SUM([Panic_Attack_Flag]) / [Total Students]
  ```
- **Data Dependency:** `[Panic_Attack_Flag]`, `[User_ID]`
- **Formatting:** Percentage, 1 decimal place (`32.7%`)
- **Where Used:** Condition Prevalence Bar Chart, Gender Comparison.
