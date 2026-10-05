# Performance Testing & Optimization Audit
## Project: Analysing Mental Health in Student Ecosystem

This document audits the computational overhead, query efficiency, and rendering characteristics of both the data pipeline and Tableau visual assets.

---

### 1. Dataset Characteristics & Storage Footprint
- **Raw Dataset Size:** 7.17 KB (`Student_Mental_health.csv`, 101 records, 11 columns)
- **Processed Dataset Size:** 13.9 KB (`student_mental_health_cleaned.csv`, 101 records, 23 columns)
- **Memory Footprint in Pandas:** < 0.1 MB (Instantaneous in-memory processing)
- **ETL Execution Latency:** ~ 0.08 seconds (Executed via `scripts/data_cleaning.py`)

---

### 2. Tableau Component Architecture Audit
- **Worksheet Count:** 12 Visual Worksheets + 3 BAN KPI Sheets
- **Calculated Fields Count:** 10 Structured Calculated Fields (Documented in `tableau/calculated_fields.md`)
- **Global Dashboard Filters:** 4 Quick Filters (`gender`, `faculty`, `year_of_study`, `cgpa_range`)
- **Dashboard Layout Containers:** 6 Logical Nested Grid Containers (Header, Filter Bar, KPI Row, 2 Main Analytics Grids, Footer)
- **Story Points:** 6 Sequential Narrative Scenes

---

### 3. Rendering & Query Performance Observations
- **Data Source Engine:** In-memory Hyper Extract / Text File Connection.
- **Filter Response Latency:** < 50ms expected response time due to compact cohort size (N=101).
- **Calculated Field Complexity:** All formulas utilize simple boolean logic (`IF/THEN`), counting (`COUNTD`), and single-dimension aggregations (`SUM/AVG`). Zero recursive table calculations or nested LOD expressions are required, ensuring maximum rendering speed.
- **Web App Embed Latency:** HTML page load < 45ms locally; Tableau Web Component v3 script asynchronously fetched from `public.tableau.com` CDN.

---

### 4. Empirical Performance Recording (Tableau Desktop)
To capture exact rendering benchmarks inside Tableau Desktop 2026.1:

| Metric | Status / Measurement | Benchmark Standard |
| :--- | :--- | :--- |
| **Data Engine Query Time** | **MANUAL TABLEAU CHECK REQUIRED** | Recommended < 0.2s |
| **Computing Layout Time** | **MANUAL TABLEAU CHECK REQUIRED** | Recommended < 0.5s |
| **Geocoding / Rendering Time** | **MANUAL TABLEAU CHECK REQUIRED** | Recommended < 0.3s |
| **Total Dashboard Render Time**| **MANUAL TABLEAU CHECK REQUIRED** | Recommended < 1.5s |

> **How to execute the manual check in Tableau Desktop:**  
> Navigate to: **Help &rarr; Settings and Performance &rarr; Start Performance Recording**.  
> Interact with the filters on the Dashboard, then click **Help &rarr; Settings and Performance &rarr; Stop Performance Recording**. Tableau will automatically generate a performance workbook detailing millisecond-level execution timings.
