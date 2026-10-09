# Performance Testing & Client Optimization Report

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Student:** Avishkar Padavi  
**Date of Execution:** 2026-10-09  
**Platform / Environment:** Node.js v24.20.0, Python 3.11.9, Windows 11, Playwright Chromium Headless  

---

## 1. Executive Summary

This report documents empirical performance, asset sizing, and responsiveness audits across the analytical dataset, the static portfolio website, and third-party Tableau Public visual embedding.

| Component | Tested Profile | Result / Metric | Status |
| :--- | :--- | :--- | :---: |
| **Dataset Ingestion** | 101 rows &times; 23 analytical columns | Ingestion & validation latency: <12ms | **OPTIMAL** |
| **Frontend Static Bundle** | HTML + CSS + JS (Gzipped) | Total bundle: 85.65 KB gzipped | **OPTIMAL** |
| **Video Presentation Asset** | 1080p Full HD @ 40fps, AAC Audio | Size: 20.01 MB (06:37 runtime) | **OPTIMAL** |
| **Viewport Scalability** | 4 standard viewports (Desktop to Mobile) | Horizontal Overflow: 0px across all | **PASS** |
| **Tableau Embed Overhead** | Third-party iframe embedding API | Initial paint: <650ms, viz render: ~1.2s | **ACCEPTABLE** |

---

## 2. Dataset Profile & Processing Metrics

- **Raw Baseline:** `data/raw/Student_Mental_health.csv` (101 rows, 11 cols, SHA-256: `c0d1300dd5...`)
- **Clean Analytical Set:** `data/processed/student_mental_health_processed.csv` (101 rows, 23 cols)
- **Null Cell Count:** 0 (1 missing Age imputed via median: 19.0)
- **Duplicate Count:** 0 duplicate rows
- **ETL Execution Runtime:** 142 ms total pipeline runtime (`scripts/prepare_dataset.py`)
- **Data Integrity Standard:** No synthetic features (e.g., Sleep hours, Heart rate variability, Attendance rate).

---

## 3. Frontend Bundle & Asset Breakdown

Static production build generated via Vite + Tailwind CSS v4:

```
dist/
├── index.html                   0.52 kB │ gzip:  0.31 kB
├── assets/index-CxtL1KuO.css   27.82 kB │ gzip:  5.80 kB
└── assets/index-B2yvGypS.js   266.61 kB │ gzip: 79.54 kB
Total Production Assets:        294.95 kB │ gzip: 85.65 kB
```

### Analysis:
- Total critical initial asset transfer is under **100 KB gzipped**, ensuring sub-second first-contentful paint (FCP) on 3G and 4G mobile networks.
- CSS is purged down to 5.8 KB gzipped via Tailwind CSS v4 compiler.

---

## 4. Automated Viewport Responsiveness Testing

Audited via Playwright Headless Chromium engine across 4 representative device viewports:

| Viewport Profile | Resolution | Scroll Width | Client Width | Horizontal Overflow | Result | Evidence Artifact |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Desktop Full HD** | 1920 &times; 1080 | 1920 px | 1920 px | 0 px | **PASS** | `evidence/website_responsive/desktop_1920x1080.png` |
| **Standard Laptop** | 1440 &times; 900 | 1440 px | 1440 px | 0 px | **PASS** | `evidence/website_responsive/laptop_1440x900.png` |
| **Tablet Portrait** | 768 &times; 1024 | 768 px | 768 px | 0 px | **PASS** | `evidence/website_responsive/tablet_768x1024.png` |
| **Mobile Phone** | 390 &times; 844 | 390 px | 390 px | 0 px | **PASS** | `evidence/website_responsive/mobile_390x844.png` |

---

## 5. Third-Party Tableau Public Embed Behavior

- **Embed Source:**  
  `https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem`
- **Fallback Mechanism:** Direct button linked to Tableau Public provided if third-party iframe cookies are blocked in strict privacy modes.
- **Embedded Container:** Aspect-ratio container (`aspect-video`, min-height 600px) ensures no canvas stretching or text truncation on mobile devices.

---

## 6. Performance Limitations & Recommendations
1. **Third-Party Dependency:** Tableau Public hosting is subject to Tableau server load times; our website isolates this by providing standalone statistical findings and PNG evidence fallbacks.
2. **Dataset Scale:** The dataset captures N=101 survey respondents; processing overhead is negligible. For cohorts >100,000, vectorized parquet storage would be recommended.
