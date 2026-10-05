# Data Dictionary: Student Mental Health in Academic Ecosystem

This data dictionary documents both raw survey columns and derived analytical features produced by the reproducible preprocessing pipeline (`scripts/data_cleaning.py`).

| Column Name | Description | Data Type | Example | Possible Values | Cleaning / Transformation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`student_id`** | Unique anonymized identifier for each student respondent | String | `STD_0001` | `STD_0001` to `STD_0101` | Generated sequential primary key for Tableau aggregation and individual record tracking. |
| **`timestamp`** | Date and time when the survey was submitted | String / DateTime | `8/7/2020 12:02` | ISO-formatted timestamps | Trimmed whitespace, preserved for temporal response patterns. |
| **`gender`** | Self-reported gender of the student | String (Categorical) | `Female` | `Female`, `Male` | Standardized capitalization, stripped trailing spaces from raw `Choose your gender`. |
| **`age`** | Age of the student in completed years | Integer | `19` | `18` - `24` | 1 missing value (row 43) imputed with cohort median (`19`); cast from float64 to integer. |
| **`age_group`** | Age cohort classification | String (Categorical) | `18-20 (Underclassmen)` | `18-20 (Underclassmen)`, `21-24 (Upperclassmen)` | Derived binned categorical feature (`(17, 20]`, `(20, 25]`). |
| **`course`** | Degree program or academic major | String (Categorical) | `Information Technology (BIT)` | 49 unique majors | Normalized typos (`Engin` → `Engineering`, `Mathemathics` → `Mathematics`, `Bit` → `Information Technology (BIT)`). |
| **`faculty`** | Higher-level academic discipline / school | String (Categorical) | `Computing & IT` | `Engineering`, `Computing & IT`, `Humanities & Social Sciences`, `Islamic Studies & Ethics`, `Business & Economics`, `Allied Health Sciences`, `Sciences & General` | Grouped 49 granular courses into 7 standardized institutional faculties. |
| **`year_of_study`** | Academic seniority level | String (Ordinal) | `Year 1` | `Year 1`, `Year 2`, `Year 3`, `Year 4` | Standardized mixed case strings (`year 1`, `Year 1`, `year 2`, etc.) to uniform title case. |
| **`cgpa_range`** | Cumulative Grade Point Average category | String (Ordinal) | `3.00 - 3.49` | `0 - 1.99`, `2.00 - 2.49`, `2.50 - 2.99`, `3.00 - 3.49`, `3.50 - 4.00` | Stripped trailing whitespace (e.g. `'3.50 - 4.00 '` vs `'3.50 - 4.00'`). |
| **`cgpa_midpoint`** | Continuous numerical midpoint of the student's CGPA tier | Float | `3.25` | `1.00`, `2.25`, `2.75`, `3.25`, `3.75` | Derived continuous proxy enabling measure calculations, scatter plots, and trendlines in Tableau. |
| **`marital_status`** | Self-reported marital status | String (Categorical) | `No` | `No`, `Yes` | Standardized capitalization and trimmed spaces. |
| **`depression`** | Indicator of clinical depression symptoms | String (Binary) | `Yes` | `No`, `Yes` | Cleaned from `Do you have Depression?`. |
| **`depression_flag`** | Numeric flag for depression condition | Integer (Binary) | `1` | `0`, `1` | Derived numeric indicator (`1` = Yes, `0` = No) for sum/rate aggregations. |
| **`anxiety`** | Indicator of clinical anxiety symptoms | String (Binary) | `No` | `No`, `Yes` | Cleaned from `Do you have Anxiety?`. |
| **`anxiety_flag`** | Numeric flag for anxiety condition | Integer (Binary) | `0` | `0`, `1` | Derived numeric indicator (`1` = Yes, `0` = No) for sum/rate aggregations. |
| **`panic_attack`** | Indicator of recurring panic attack experiences | String (Binary) | `Yes` | `No`, `Yes` | Cleaned from `Do you have Panic attack?`. |
| **`panic_attack_flag`** | Numeric flag for panic attack experiences | Integer (Binary) | `1` | `0`, `1` | Derived numeric indicator (`1` = Yes, `0` = No) for sum/rate aggregations. |
| **`condition_count`** | Total concurrent mental health conditions | Integer | `2` | `0`, `1`, `2`, `3` | Derived score: `depression_flag + anxiety_flag + panic_attack_flag`. |
| **`mental_health_risk`** | Multidimensional risk severity tier | String (Categorical) | `High Risk` | `Low Risk` (0 conditions), `Moderate Risk` (1 condition), `High Risk` (≥2 conditions) | Derived severity stratification for risk segmentation dashboards. |
| **`treatment_sought`** | Whether student consulted a mental health specialist | String (Binary) | `No` | `No`, `Yes` | Cleaned from `Did you seek any specialist for a treatment?`. |
| **`treatment_sought_flag`**| Numeric flag for specialist consultation | Integer (Binary) | `0` | `0`, `1` | Derived numeric indicator (`1` = Yes, `0` = No). |
| **`treatment_gap`** | Healthcare utilization status relative to need | String (Categorical) | `Untreated Condition` | `No Identified Condition`, `Condition Treated`, `Untreated Condition` | Evaluates whether students with active conditions received specialist care. |
