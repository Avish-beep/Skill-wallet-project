# Dataset Licensing, Provenance & Usage Terms

**Project:** Analysing Mental Health in Student Ecosystem
**Author / Maintainer:** Avishkar Padavi
**Date:** October 2026

---

## 1. Dataset Overview & Provenance

This repository utilizes an observational higher-education mental health survey dataset containing self-reported psychological indicators and academic metrics from university students.

| Attribute | Baseline Raw Dataset | Engineered Processed Dataset |
| :--- | :--- | :--- |
| **File Path** | `data/raw/Student_Mental_health.csv` | `data/processed/student_mental_health_processed.csv` |
| **Record Count** | 101 observations | 101 observations |
| **Column Count** | 11 survey columns | 23 analytical & engineered features |
| **Missing Values** | 1 missing age cell (row 43) | 0 missing values (cohort median imputed) |
| **Duplicate Rows** | 0 duplicates | 0 duplicates |
| **Raw SHA-256** | `c0d1300dd5225b42603847a9ffec01c77f0a39dd118d0e74f1ec5be3d0663f0a` | `7074465dfecf265b44fc476be2687dc9f6c77098e9a26391a27e361c4bb587e9` |

---

## 2. Licensing Notice & Scope

> **IMPORTANT LEGAL NOTICE:**
> **The root repository MIT License does NOT grant rights to this survey dataset.**
> Dataset licensing and upstream redistribution permissions require separate verification from the original survey publishers.

- **Primary Source Context:** Ingested as a baseline empirical survey on student mental health within higher education.
- **Original Source Attribution:** The survey questionnaire records self-reported responses regarding depression, anxiety, panic attacks, academic CGPA range, and specialist treatment consultation.
- **Upstream License Status:** Upstream terms of the raw survey distribution remain unverified under an explicit public domain or open data license.

---

## 3. Privacy, Anonymity & Data Protection

Student mental health responses involve sensitive individual disclosures. In accordance with responsible research standards:

1. **No Personally Identifiable Information (PII):** The dataset does not contain names, student registration numbers, phone numbers, email addresses, IP addresses, or geographic coordinates.
2. **Aggregated Analytical Presentation:** The public website ([https://avish-beep.github.io/Skill-wallet-project/](https://avish-beep.github.io/Skill-wallet-project/)) and presentation materials display exclusively aggregate cohort statistics, distributions, and cross-tabulations (e.g., condition rates, comorbidity tiers, faculty breakdowns).
3. **No Individual Profiling:** Individual row-level survey submissions are never singled out, profiled, or deanonymized.

---

## 4. Permitted Use & Redistribution Policy

- **Academic & Educational Demonstration:** The data is processed and presented solely for educational evaluation within the SkillWallet curriculum and student capstone portfolio demonstration.
- **No Commercial Exploitation:** The dataset may not be used for commercial profiling, targeted marketing, or automated clinical assessment.
- **Non-Clinical Disclaimer:** These survey records represent observational, self-reported screening indicators, not clinical psychiatric diagnoses according to DSM-5 or ICD-11 criteria.
- **Redistribution Rights:** If upstream data ownership or licensing conditions require withdrawal of raw or processed row-level records, downstream users must reproduce the findings using local authorized copies via `scripts/prepare_dataset.py`.

---

## 5. Contact & Inquiries

For questions regarding dataset provenance, research methodology, or licensing clarification, please open an issue in the GitHub repository:
[https://github.com/Avish-beep/Skill-wallet-project/issues](https://github.com/Avish-beep/Skill-wallet-project/issues)
