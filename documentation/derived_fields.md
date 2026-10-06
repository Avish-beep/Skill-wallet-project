# Derived Fields & Feature Engineering Documentation
## Epic 2: Data Preparation

This document records the exact mathematical and categorical formulas used to derive analytical features from raw survey data, ensuring complete transparency and reproducibility.

---

### 1. `User_ID`
- **Purpose:** Unique, anonymized primary key for distinct counting (`COUNTD([User_ID])`) in Tableau.
- **Formula / Logic:** `STD_{row_number:04d}` (Sequential assignment from `STD_0001` to `STD_0101`).
- **Source Columns:** Generated index.

---

### 2. `Age_Group`
- **Purpose:** Binned age cohorts for demographic segmentation.
- **Formula / Logic:**
  ```python
  pd.cut(Age, bins=[17, 20, 25], labels=['18-20 (Underclassmen)', '21-24 (Upperclassmen)'])
  ```
- **Source Columns:** `Age`

---

### 3. `Faculty`
- **Purpose:** Categorizes 49 granular degree majors into 7 institutional higher-education faculties.
- **Formula / Logic:**
  - `Engineering`: If course contains 'engineering', 'koe', 'engin'.
  - `Computing & IT`: If course contains 'bit', 'it', 'computer', 'bcs'.
  - `Humanities & Social Sciences`: If course contains 'law', 'laws', 'human', 'psychology', 'communication', 'kirkhs', 'benl'.
  - `Islamic Studies & Education`: If course contains 'islamic', 'usuluddin', 'fiqh', 'taqwa', 'pendidikan'.
  - `Business & Economics`: If course contains 'economics', 'accounting', 'management', 'business', 'banking', 'econs', 'kenms'.
  - `Allied Health Sciences`: If course contains 'biomedical', 'pharmacy', 'nursing', 'kop', 'medical'.
  - `Natural Sciences & General`: All other disciplines.
- **Source Columns:** `Course`

---

### 4. `CGPA_Midpoint`
- **Purpose:** Continuous numerical proxy enabling scatter plots, average CGPA calculations, and trendlines in Tableau.
- **Formula / Logic:**
  - `'0 - 1.99'` &rarr; `1.00`
  - `'2.00 - 2.49'` &rarr; `2.25`
  - `'2.50 - 2.99'` &rarr; `2.75`
  - `'3.00 - 3.49'` &rarr; `3.25`
  - `'3.50 - 4.00'` &rarr; `3.75`
- **Source Columns:** `CGPA_Range`

---

### 5. `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`, `Treatment_Sought_Flag`
- **Purpose:** Binary 1/0 integer indicators enabling direct rate calculations (`SUM([Flag]) / COUNTD([User_ID])`) without needing Tableau `IF/THEN` statements on strings.
- **Formula / Logic:**
  ```python
  (Column == 'Yes').astype(int)
  ```
- **Source Columns:** `Depression`, `Anxiety`, `Panic_Attack`, `Treatment_Sought`

---

### 6. `Condition_Count`
- **Purpose:** Measures the total concurrent clinical psychiatric load (comorbidity index) per individual.
- **Formula / Logic:**
  ```python
  Condition_Count = Depression_Flag + Anxiety_Flag + Panic_Attack_Flag
  ```
- **Scale:** Discrete integer from 0 (healthy baseline) to 3 (triple comorbidity).
- **Source Columns:** `Depression_Flag`, `Anxiety_Flag`, `Panic_Attack_Flag`

---

### 7. `Mental_Health_Risk`
- **Purpose:** Multidimensional clinical risk severity stratification.
- **Formula / Logic:**
  ```python
  IF Condition_Count == 0 THEN 'Low Risk'
  ELSEIF Condition_Count == 1 THEN 'Moderate Risk'
  ELSEIF Condition_Count >= 2 THEN 'High Risk'
  ```
- **Source Columns:** `Condition_Count`

---

### 8. `Treatment_Gap`
- **Purpose:** Evaluates whether students with diagnosable symptoms received clinical specialist care.
- **Formula / Logic:**
  - `Condition_Count == 0`: `'No Identified Condition'`
  - `Condition_Count > 0 AND Treatment_Sought == 'Yes'`: `'Condition Treated'`
  - `Condition_Count > 0 AND Treatment_Sought == 'No'`: `'Untreated Condition'`
- **Source Columns:** `Condition_Count`, `Treatment_Sought`
