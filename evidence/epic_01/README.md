# Evidence Manifest: Epic 1 — Data Collection & Extraction from Database
## Project: Analysing Mental Health in Student Ecosystem

This manifest lists the artifacts that substantiate completion of Epic 1 and the *Understand the Data* subtask.

---

### Artifact Index

1. **Dataset Schema & Source Documentation:**
   - `data/raw/SOURCE.md`: Details dataset provenance, origin, and schema comparison.
   - `data_dictionary.md`: Complete field definitions for the 18 expected variables.

2. **Data Profiling & Inspection Scripts:**
   - `scripts/inspect_dataset.py`: Reusable Python script for inspecting any incoming dataset against the 18-column specification.
   - `documentation/dataset_profile.md`: Full structural audit report.

3. **Validation & Quality Audit:**
   - `documentation/data_validation_report.md`: Formal verification of column presence, missing values, duplicates, and ranges.

4. **Tableau Compatibility Assessment:**
   - `tableau/data_source_notes.md`: Documents dimension/measure classifications and readiness for Tableau Desktop 2026.1.

5. **Progress & Governance:**
   - `documentation/project_progress.md`: Tracks Epic 1 status.
   - `CHANGELOG.md`: Chronological log of Epic 1 activities.
