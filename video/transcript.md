# Project Presentation Transcript

**Project:** Analysing Mental Health in Student Ecosystem  
**Student:** Avishkar Padavi  
**Duration:** 06:37  
**Language:** Indian English (en-IN-PrabhatNeural)

---

### Scene 1: Analysing Mental Health in Student Ecosystem (00:00:00 - 00:00:25)

Hello everyone, respected evaluators and faculty members. My name is Avishkar Padavi, and today I am very excited to present my capstone data analytics project titled: Analysing Mental Health in Student Ecosystem. Across universities today, mental wellness among students has become one of the most pressing concerns. Heavy academic pressure, exam stress, social adjustment, and career uncertainties lead to significant psychological strain. Unfortunately, most college administrations do not have an empirical, data-driven system to track student distress, identify comorbidity risks, or evaluate how effectively campus counseling services are functioning. In this project, our primary goal was to take real survey data, build a clean and reproducible Python ETL pipeline, and create an interactive, responsive visual intelligence dashboard using Tableau Desktop.

### Scene 2: Data Engineering, Architecture & Integrity Standards (00:00:25 - 00:00:50)

Before diving into our charts, let me explain the data engineering behind this project. In Epic 1, Data Collection and Extraction, we ingested the raw survey dataset capturing one hundred and one university students. We audited the dataset and locked it with an SHA-256 checksum to guarantee provenance. Then in Epic 2, Data Preparation, we created an automated pipeline in Python using pandas. We handled missing age values through median imputation, standardized diverse student majors into structured academic faculties, and engineered twelve critical features—such as comorbidity count, risk classification, and clinical treatment gaps. I want to emphasize that we strictly avoided any synthetic metrics or fake fields, ensuring that our final analytical dataset of twenty-three columns is one hundred percent accurate and complete.

### Scene 3: Executive Overview Dashboard (Live Tableau Public) (00:00:50 - 00:01:15)

Now let us look at our first interactive dashboard on Tableau Public: the Student Mental Health Overview Dashboard. This dashboard is designed with a responsive layout container and high-density cards, structured like modern executive healthcare intelligence reports. At the top, we have our four primary KPI cards: First, our total cohort comprises one hundred and one students. Second, twenty-eight students, representing twenty-seven point seven percent, are categorized in the high comorbidity risk tier. Third, thirty-six students, or thirty-five point six percent, fall under moderate risk. And fourth, an alarming fifty-eight students self-report symptomatic distress but have never received any professional medical or psychological treatment. Faculty deans and counselors can use the top interactive filters to slice the data seamlessly across gender, age groups, faculties, and risk levels.

### Scene 4: Clinical Mental Health Risk & Specialist Treatment Gap (00:01:15 - 00:01:40)

Next, we move to our second specialized dashboard: Mental Health Risk and Clinical Treatment Gap. This visualization brings forward the single most shocking insight of our entire investigation. When we analyze students showing active psychological distress, a massive ninety point six percent have never consulted a clinical specialist, psychiatrist, or college counselor. In other words, only six symptomatic students out of sixty-four have ever accessed professional mental health care. This proves that the challenge in student mental health is not just about awareness, but about breaking down social stigma, confidentiality concerns, and institutional barriers to care.

### Scene 5: Cohort Risk Stratification: Low, Moderate, and High Risk (00:01:40 - 00:02:05)

Now let us break down individual worksheets. Here is the Distribution of Mental Health Risk Levels. We systematically grouped students into three distinct risk tiers based on symptom co-occurrence: Students reporting zero conditions are classified as Low Risk, making up thirty-six point six percent of the cohort. Students reporting a single condition are categorized as Moderate Risk, comprising thirty-five point six percent. And students suffering from multiple concurrent conditions—such as co-occurring depression, anxiety, or panic attacks—are placed in the High Risk tier, representing twenty-seven point seven percent. This means that nearly two out of every three students in the campus ecosystem experience some form of mental health distress.

### Scene 6: Within-Gender Self-Reported Conditions Analysis (00:02:05 - 00:02:30)

Here we analyze condition prevalence stratified by gender. Our surveyed cohort includes seventy-five female students and twenty-six male students. To ensure a fair analysis without sample bias, we calculated proportions within each gender group. Among female students, depression is self-reported at thirty-eight point seven percent, anxiety at thirty-two percent, and panic attacks at thirty-three point three percent. Among male students, anxiety is highest at thirty-eight point five percent, with depression and panic attacks both standing at thirty point eight percent. This shows that psychological distress affects both male and female students profoundly across all academic years.

### Scene 7: In-Depth Campus Treatment Deficit: Symptomatic vs. Clinical Consultation (00:02:30 - 00:02:55)

This bar chart illustrates the severity of the Student Treatment Gap. Out of sixty-four students experiencing self-reported psychological symptoms, fifty-eight students remain completely untreated, compared to only six students who sought medical help. From an administration standpoint, this data offers concrete actionable feedback: Simply having a campus counseling office is not enough. Universities must actively conduct anonymous health surveys, promote peer counseling groups, and simplify appointment scheduling so students feel safe reaching out.

### Scene 8: Academic Standing (CGPA Midpoint) Across Mental Health Risk Levels (00:02:55 - 00:03:20)

One of the most eye-opening findings of our analysis is the relationship between academic scores and mental health risk. People often assume that students who suffer from depression or anxiety are those who are failing academically. However, our data completely dispels that myth. As we see in this boxplot and stripplot visualization, students in the High Risk comorbidity group maintain an impressive average CGPA midpoint of three point four five. Similarly, moderate risk students average three point four eight. This clearly proves that high academic performers and honors students frequently experience intense anxiety and burnout, concealing their distress behind top grades.

### Scene 9: Mental Health Risk Across Academic Disciplines & Faculties (00:03:20 - 00:03:45)

Looking at the breakdown across academic faculties: we mapped all student majors into seven primary disciplines: Computing and IT, Engineering, Human Sciences, Biomedical Sciences, Islamic Studies, Economics, and Languages. The data reveals that moderate and high comorbidity risks are widely spread across technical STEM fields as well as humanities programs. This proves that campus wellness programs cannot be limited to just one department; they must be integrated campus-wide.

### Scene 10: Comorbidity Burden: Distribution of Concurrent Conditions (00:03:45 - 00:04:10)

This histogram represents the comorbidity distribution among students. Thirty-seven students reported zero conditions, thirty-six reported exactly one condition, seventeen students reported two concurrent conditions, and eleven students reported suffering from all three conditions simultaneously: depression, anxiety, and panic attacks. Tracking comorbidity is critical because overlapping conditions multiply emotional distress and significantly increase the risk of semester dropouts.

### Scene 11: Risk Trajectory Across Age Groups and Undergraduate Seniority (00:04:10 - 00:04:35)

Examining age groups across undergraduate seniority: we compared younger underclassmen aged eighteen to twenty with senior upperclassmen aged twenty-one to twenty-four. Both groups demonstrate considerable vulnerability. Junior students face the adjustment shock of campus life and independent living, while final-year students face the stress of placement drives, competitive exams, and career uncertainty. Interventions must therefore support students at every stage of their academic journey.

### Scene 12: Conclusion, Actionable Recommendations & Project Verification (00:04:35 - 00:05:00)

To conclude, our project Analysing Mental Health in Student Ecosystem provides a rigorous, transparent, and visually actionable framework for university administrators. Our key recommendations include: implementing anonymous screening tests, launching campus campaigns to dismantle mental health stigma, and providing structured counseling for high-performing students. All project assets—including our reproducible Python ETL pipeline, clean dataset, Tableau workbook, and the live interactive Tableau Public dashboard—are verified, documented, and published. Thank you so much for your time and kind attention.

