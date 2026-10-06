# Outlier Analysis & Numerical Validation Report
## Epic 2: Data Preparation

**Date:** October 06, 2026  
**Auditor:** Antigravity Autonomous Development Agent  
**Dataset:** `C:\Skillwallet\data\processed\student_mental_health_processed.csv`  

---

### 1. Methodology
Numerical and ordinal variables were evaluated using the standard **Interquartile Range (IQR)** rule and domain-based boundary checks:
- $Q_1$ (25th percentile), $Q_3$ (75th percentile)
- $IQR = Q_3 - Q_1$
- Valid Statistical Range: $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$
- Domain Boundary Check: Realistic undergraduate population constraints.

---

### 2. Numerical Variable Evaluations

#### A. Age (`Age`)
- **Distribution:** $Q_1 = 18.0$, $Q_3 = 23.0$, $IQR = 5.0$
- **Lower Statistical Bound:** $18.0 - (1.5 \times 5.0) = 10.5$ years
- **Upper Statistical Bound:** $23.0 + (1.5 \times 5.0) = 30.5$ years
- **Empirical Minimum / Maximum:** 18 years / 24 years
- **Outliers Detected:** **0 (Zero)**
- **Domain Assessment:** All observations fall squarely within typical undergraduate college age brackets (18 to 24). No anomalous or extreme values exist.

#### B. Academic Performance Midpoint (`CGPA_Midpoint`)
- **Distribution:** $Q_1 = 3.25$, $Q_3 = 3.75$, $IQR = 0.50$
- **Lower Statistical Bound:** $3.25 - (1.5 \times 0.50) = 2.50$
- **Upper Statistical Bound:** $3.75 + (1.5 \times 0.50) = 4.50$
- **Empirical Range:** 1.00 (`0 - 1.99`) to 3.75 (`3.50 - 4.00`)
- **Statistical Outliers Detected:** **6 records** (4 students at CGPA 1.00; 2 students at CGPA 2.25)
- **Domain Assessment & Action:** **Retained 100% of observations.** These 6 records represent legitimate lower-performing students (e.g. students on academic probation or experiencing severe coursework difficulty). Removing them would introduce catastrophic survival bias and obscure the relationship between mental distress and academic failure.

#### C. Composite Psychiatric Burden (`Condition_Count`)
- **Distribution:** $Q_1 = 0.0$, $Q_3 = 2.0$, $IQR = 2.0$
- **Statistical Range:** $[-3.0, 5.0]$
- **Empirical Range:** 0 to 3 concurrent conditions
- **Outliers Detected:** **0 (Zero)**
- **Domain Assessment:** Bounded naturally between 0 (no condition) and 3 (triple comorbidity).

---

### 3. Conclusion & Treatment Policy
No artificial records, impossible ages, or corrupt numerical values were found. The 6 lower CGPA records represent genuine student segments critical for institutional mental health intervention research and were deliberately preserved.
