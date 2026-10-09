# Project Presentation Transcript

**Project:** Analysing Mental Health in Student Ecosystem  
**Presenter:** Avishkar Padavi  
**Duration:** 06:24 (6 minutes 24 seconds)  
**Cadence & Accent:** Natural Indian English (`en-IN-PrabhatNeural` at ~130 WPM)

---

### Scene 1: Project Introduction & Student Context (00:00:00 - 00:00:57)

Hello everyone, respected evaluators and faculty members. My name is Avishkar Padavi, and today I am pleased to present my capstone data analytics project titled: Analysing Mental Health in Student Ecosystem. Student mental wellness across university campuses has become one of the most pressing challenges in higher education. Academic pressures, exam competition, and career uncertainties create significant psychological strain. However, many institutions lack empirical, data-driven systems to monitor student distress or evaluate counseling intervention gaps. In this project, I developed an end-to-end analytics workflow using Python for reproducible data preparation, and Tableau Desktop for interactive visual intelligence.

### Scene 2: Problem Statement & Analytical Boundaries (00:00:57 - 00:01:43)

Here in our project framework, we define clear investigative objectives and ethical boundaries. Our study analyzes empirical survey records from one hundred and one university students. I want to emphasize that all responses represent self-reported psychological indicators rather than formal clinical diagnoses. Furthermore, our findings are observational and correlational. In strict accordance with data integrity, we excluded generic template fields such as sleep hours, attendance rate, or stress scores, focusing entirely on authentic, verified survey dimensions.

### Scene 3: Data Engineering Pipeline (Epic 1 & Epic 2) (00:01:43 - 00:02:37)

Moving to our methodology, we established a four-stage reproducible pipeline. In Epic 1, Data Collection, we ingested the immutable survey dataset and validated its SHA-256 checksum. In Epic 2, Data Preparation, we built an automated Python ETL script using pandas. We imputed a single missing age value using the cohort median of nineteen, cleaned CGPA ranges into numeric midpoints, and standardized diverse majors into seven academic faculties. We engineered twelve derived analytical features, including concurrent condition counts and clinical care gap indicators, producing a clean dataset with zero missing cells and zero duplicate rows.

### Scene 4: Tableau Visual Intelligence & Publishing Status (00:02:37 - 00:03:25)

Here is the interactive Tableau visual intelligence section of our website. In our local validated workbook, we developed ten dedicated worksheets and two responsive executive dashboards. Our primary dashboard organizes four key performance indicator cards: total cohort size of one hundred and one students, twenty-eight high-risk students, thirty-six moderate-risk students, and fifty-eight untreated symptomatic students. We have provided a clear status notice: while our local Tableau Desktop workbook is fully verified against our authentic dataset, republishing over the older generic template on Tableau Public remains in progress.

### Scene 5: Key Analytical Findings & The 90.6% Care Gap (00:03:25 - 00:04:22)

Now let us examine our key analytical findings, recalculated directly from the validated dataset. The most critical discovery is the ninety point six percent campus clinical care deficit. Out of sixty-four students reporting at least one mental health condition, fifty-eight have never sought treatment from a psychiatrist or counselor. Only six symptomatic students accessed specialist care. Furthermore, sixty-three point four percent of students experience at least one condition, with twenty-seven point seven percent in the high comorbidity tier. Condition indicators are closely distributed across the cohort: depression at thirty-four point seven percent, anxiety at thirty-three point seven percent, and panic attacks at thirty-two point seven percent.

### Scene 6: Project Story & The High-Achiever Paradox (00:04:22 - 00:05:15)

In our guided Project Story section, we explore six sequential chapters of the student mental health journey. One of our most compelling insights is the high-achiever paradox. Common assumptions suggest that only academically struggling students face mental distress. However, our data demonstrates that high-risk comorbidity students maintain an impressive average CGPA midpoint of three point four five out of four point zero. Top academic performers frequently experience acute anxiety and burnout, concealing their distress behind stellar grades. In addition, comorbidity spans both male and female students across engineering, computing, and humanities departments.

### Scene 7: Presentation Video Player & Chapter Markers (00:05:15 - 00:05:45)

This is our dedicated presentation video walkthrough section on the website. It features an accessible native video player with synchronized WebVTT subtitles, downloadable high-definition MP4 media, and interactive chapter timestamps. Viewers can navigate seamlessly between our introduction, data engineering pipeline, Tableau dashboard review, and policy recommendations.

### Scene 8: Documentation, Live Resources & Conclusion (00:05:45 - 00:06:24)

Finally, our website provides direct links to our GitHub repository, comprehensive data preparation reports, visualization dictionaries, and responsive testing evidence. In conclusion, this project delivers an empirical, transparent foundation for university counseling centers to conduct proactive screenings and eliminate mental health stigma. All source code, automated scripts, and portfolio assets are published under Avishkar Padavi on GitHub. Thank you very much for your time and kind consideration.

