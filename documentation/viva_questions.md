# 25 Essential Viva Questions & Comprehensive Answers
## Project: Analysing Mental Health in Student Ecosystem

---

### Section 1: Tableau & Visual Analytics

#### Q1: What is the difference between a Dimension and a Measure in Tableau?
**Answer:** In Tableau, a **Dimension** contains qualitative, categorical values (such as `gender`, `faculty`, or `year_of_study`) that slice, segment, and categorize data. A **Measure** contains quantifiable, numerical values (such as `student_id` count, condition counts, or percentages) that can be aggregated via `SUM`, `AVG`, `COUNTD`, or `MEDIAN`.

#### Q2: What is the difference between a Discrete and a Continuous field in Tableau?
**Answer:** Discrete fields (blue pills) create distinct headers, buckets, or categorical rows/columns. Continuous fields (green pills) create an unbroken axis or scale across a continuous domain (such as our continuous `cgpa_midpoint` axis).

#### Q3: Why did you use a Donut Chart instead of a standard Pie Chart?
**Answer:** A Donut Chart uses a dual-axis circle overlay with a hollow center. This hollow center provides high-value real estate to display a central summary metric (e.g. Total Students or % High Risk) while reducing cognitive load and visual clutter compared to a solid pie chart.

#### Q4: How did you implement cross-filtering across the dashboard?
**Answer:** In Tableau Desktop, we enabled **"Use as Filter"** on the primary summary worksheets (such as the Risk Donut and CGPA bars) which creates underlying Dashboard Filter Actions. Clicking a mark dynamically passes the selected dimension value to all other worksheets on the canvas.

#### Q5: What is a Tableau Story, and how does it differ from a Dashboard?
**Answer:** A Dashboard presents multiple related worksheets on a single interactive screen for exploratory analysis. A Tableau Story is a sequential series of "Story Points" (scenes) arranged chronologically to guide the user through a narrative argument, presenting context, discovery, and recommendations step-by-step.

---

### Section 2: Calculated Fields & Metrics

#### Q6: How did you calculate the High Risk student rate in Tableau?
**Answer:** We created a calculated field using conditional logic and distinct counting:
```tableau
SUM(IF [mental_health_risk] = 'High Risk' THEN 1 ELSE 0 END) / COUNTD([student_id])
```
Formatted as a percentage to one decimal place.

#### Q7: What is `COUNTD()` and why was it used instead of `COUNT()`?
**Answer:** `COUNTD()` computes the count of distinct values. Because each student has a unique `student_id`, using `COUNTD([student_id])` prevents duplicate counting even if the underlying data connection or join replicates rows across categories.

#### Q8: What is the formula for the Campus Treatment Gap Rate?
**Answer:**
```tableau
SUM(IF [condition_count] > 0 AND [treatment_sought] = 'No' THEN 1 ELSE 0 END) 
/ 
SUM(IF [condition_count] > 0 THEN 1 ELSE 0 END)
```
This isolates students who have at least one active condition and calculates the percentage who have never consulted a specialist.

---

### Section 3: Data Cleaning & Preprocessing

#### Q9: How did you handle missing values in the dataset?
**Answer:** During profiling, we identified a single missing value in the `Age` column. Because the distribution was slightly skewed with ages ranging from 18 to 24, we imputed the missing value using the cohort median of 19.0 rather than the mean, preserving integer age integrity.

#### Q10: Why did you clean and standardize the CGPA range column?
**Answer:** The raw survey contained inconsistent string entries such as `'3.50 - 4.00 '` with a trailing space alongside `'3.50 - 4.00'`. Without string trimming, Tableau would treat these as two separate categorical buckets, splitting the highest-performing student cohort.

#### Q11: What is the `cgpa_midpoint` derived feature and why was it necessary?
**Answer:** The raw CGPA data was captured as categorical ordinal brackets (`3.00 - 3.49`). To compute cohort-wide averages, trendlines, and scatter plot correlations, we calculated the mathematical midpoint for each bracket (e.g. 3.25 for `3.00 - 3.49`), creating a continuous numeric proxy.

#### Q12: Did you invent or fabricate any student records?
**Answer:** Absolutely not. We strictly preserved all 101 empirical survey records. All derived features (`condition_count`, `mental_health_risk`, `faculty`) were programmatically engineered from verified existing survey columns without any artificial data synthesis.

---

### Section 4: Python & Flask Web Integration

#### Q13: What role does Python play in your project pipeline?
**Answer:** Python serves as the foundational data engineering layer. Using `pandas` and `numpy`, it executes the automated audit (`profile_dataset.py`), the cleaning pipeline (`data_cleaning.py`), and the statistical analysis calculations (`exploratory_analysis.py`), outputting a validated dataset for Tableau and Flask.

#### Q14: How does Flask communicate with the cleaned dataset?
**Answer:** In `flask_app/app.py`, a helper function `load_cohort_stats()` loads `data/processed/student_mental_health_cleaned.csv` using Pandas, calculates live aggregate rates (prevalence, risk tiers, treatment gap), and injects them into the Jinja2 context templates.

#### Q15: How is the Tableau visualization embedded in Flask?
**Answer:** We utilize the modern **Tableau Web Component API v3** script (`<script type="module" src="https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js">`). On the `/dashboard` page, a `<tableau-viz>` component dynamically embeds the published Tableau Public URL configured via the `.env` environment variable.

#### Q16: What happens if the Tableau Public URL is not configured yet in Flask?
**Answer:** The application includes a fallback architecture. If `TABLEAU_VIEW_URL` is empty, Flask gracefully displays an informative, professional integration placeholder that details the exact step-by-step procedure to publish in Tableau Desktop and update `.env`.

---

### Section 5: Version Control & Git

#### Q17: What files are excluded in your `.gitignore` and why?
**Answer:** Our `.gitignore` strictly excludes the Python virtual environment (`venv/`), Python cache files (`__pycache__/`, `*.pyc`), environment secrets (`.env`), editor settings (`.vscode/`, `.idea/`), and temporary Tableau cache/log files (`*.log`, `*.tmp`). This ensures credentials and massive binary files are never exposed to GitHub.

#### Q18: Why is it critical not to commit `.env` files to GitHub?
**Answer:** `.env` files often contain sensitive secrets, API keys, database credentials, or private configuration. Exposing them in public repositories creates severe security vulnerabilities. Instead, we commit `.env.example` as a sanitized template.

---

### Section 6: Project Findings & Clinical Insights

#### Q19: What is the most critical statistical insight from your study?
**Answer:** The **90.5% Treatment Gap**: While 62.4% (63 students) suffer from mental health conditions, only 6 students sought specialist care. 57 symptomatic students navigate distress completely unsupported.

#### Q20: Does high academic performance protect students against depression?
**Answer:** No. Our cross-tabulation of CGPA tiers against mental health risk reveals that students in the top honors bracket (`3.50 - 4.00`) experience depression (33.3%) and anxiety (31.0%) at rates almost identical to lower GPA brackets, disproving the myth that academic success prevents psychiatric distress.

#### Q21: What is "comorbidity" and how prevalent is it in your cohort?
**Answer:** Comorbidity is the simultaneous presence of two or more distinct medical or psychological conditions. In our cohort, 35.6% of students have two or more conditions, and 15.8% (16 students) experience all three: Depression, Anxiety, and Panic Attacks simultaneously.

#### Q22: Which academic faculties demonstrated the highest risk concentration?
**Answer:** Technical disciplines with intense, project-heavy deliverables—specifically Engineering and Computing & Information Technology—exhibited the highest proportions of High-Risk students.

---

### Section 7: Performance Testing & SkillWallet Alignment

#### Q23: How do you measure rendering performance in Tableau Desktop?
**Answer:** Using the native Performance Recorder via **Help &rarr; Settings and Performance &rarr; Start Performance Recording**. After interacting with filters, stopping the recording generates a diagnostic workbook measuring data engine query latency, layout computing time, and rendering time in milliseconds.

#### Q24: What are the 8 Epics in the SkillWallet Data Analytics module?
**Answer:**
1. Data Collection & Extraction from Database
2. Data Preparation
3. Data Visualization
4. Dashboard
5. Story
6. Performance Testing
7. Web Integration
8. Project Demonstration & Documentation

#### Q25: What institutional recommendations do you propose based on this project?
**Answer:**
1. Establish confidential, walk-in triage counseling centers during exam seasons.
2. Embed mental health literacy and de-stigmatization campaigns during undergraduate orientation.
3. Deploy dedicated student welfare counselors into high-stress academic faculties (Engineering & IT).
