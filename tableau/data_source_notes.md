# Tableau Data Source Notes (Epic 1 — Pre-Connection Assessment)
## Project: Analysing Mental Health in Student Ecosystem

This document evaluates the schema requirements for **Tableau Desktop 2026.1** based on the 18 expected metadata fields specified in the SkillWallet *Understand the Data* subtask.

---

### 1. Target Data Connection
- **Expected Source Format:** Delimited text file (`.csv`) or Excel workbook (`.xlsx`).
- **Connection Type:** In-memory extract (recommended for maximum interactive responsiveness).
- **Target Location:** `C:\Skillwallet\data\raw\`

---

### 2. Expected Field Mapping & Tableau Data Types

| Expected Field | Expected Tableau Role | Tableau Data Type | Suitability & Analytical Purpose |
| :--- | :--- | :--- | :--- |
| **User ID** | Dimension | String / Text | Granular distinct identifier for counting unique individuals (`COUNTD([User ID])`). |
| **Age** | Dimension / Measure | Whole Number | Demographic segmentation and age cohort distribution analysis. |
| **Gender** | Dimension | String / Categorical | Demographic slicing (`Male`, `Female`, `Other`). |
| **Occupation** | Dimension | String / Categorical | Segmenting student vs. professional subgroups. |
| **Stress Level** | Dimension (Ordinal) | String / Ordinal | Key categorical risk factor (`Low`, `Medium`, `High`). |
| **Anxiety Score** | Measure | Continuous Number | Quantitative clinical score for calculating cohort averages and distribution boxplots. |
| **Depression Score** | Measure | Continuous Number | Quantitative clinical score for correlation analysis against screen time and sleep. |
| **Sleep Quality** | Dimension (Ordinal) | String / Ordinal | Lifestyle indicator (`Poor`, `Average`, `Good`). |
| **Daily Screen Time (hrs)** | Measure | Continuous Number | Primary behavioral predictor for scatter plots and trendlines. |
| **Physical Activity Level** | Dimension (Ordinal) | String / Ordinal | Health behavior categorization (`Low`, `Moderate`, `High`). |
| **Social Interaction Score** | Measure | Continuous Number | Interpersonal wellness metric. |
| **Mental Health History** | Dimension (Binary) | String (`Yes`/`No`) | Pre-existing vulnerability filter. |
| **Therapy Type** | Dimension | String / Categorical | Treatment modality segmentation (`CBT`, `Meditation`, `Counseling`, etc.). |
| **Intervention Duration (weeks)** | Measure / Dimension | Whole Number | Time dimension evaluating dosage/exposure of clinical interventions. |
| **Progress Score** | Measure | Continuous Number | Primary post-intervention clinical outcome metric. |
| **Medication Usage** | Dimension (Binary) | String (`Yes`/`No`) | Pharmacological intervention indicator. |
| **Support System Strength** | Dimension (Ordinal) | String (`Low`, `Medium`, `High`) | Social buffering dimension. |
| **Work-Life Balance Score** | Measure | Continuous Number | Environmental stress balance metric. |

---

### 3. Fields Requiring Attention During Ingestion
- **Ordinal Scales:** Fields like `Stress Level`, `Sleep Quality`, and `Support System Strength` will require custom manual sorting (e.g. Low &rarr; Medium &rarr; High) in Tableau rather than default alphabetical sorting.
- **Score Bounds:** Numerical score fields (`Anxiety Score`, `Depression Score`, `Progress Score`) should be validated for defined clinical range minimums and maximums (e.g. 0–21 or 1–10).
- **Text Trimming:** Categorical text fields must be stripped of leading and trailing whitespace to prevent fragmented dimension headers.

---

### 4. Potential Global Dashboard Filters
1. `Gender`
2. `Occupation`
3. `Stress Level`
4. `Sleep Quality`
5. `Therapy Type`
6. `Mental Health History`

---

### 5. Candidate Calculated Fields (For Future Epic 3 & 4)
- **`Cohort Size`**: `COUNTD([User ID])`
- **`Average Progress by Therapy`**: `AVG([Progress Score])`
- **`Screen Time Category`**: `IF [Daily Screen Time (hrs)] > 6 THEN 'High' ELSEIF [Daily Screen Time (hrs)] >= 3 THEN 'Moderate' ELSE 'Low' END`
- **`High Anxiety Indicator`**: `IF [Anxiety Score] >= 10 THEN 1 ELSE 0 END`
