# Project Changelog

All notable technical updates to the *Analysing Mental Health in Student Ecosystem* project will be documented in this file chronologically.

---

## [Epic 1] Data Collection & Extraction from Database
**Date:** October 06, 2026  
**Status:** In Progress (Awaiting exact SkillWallet source dataset file)  

### Activities & Findings:
- **Environment Setup:** Virtual environment verified at `C:\Skillwallet\venv` with Python 3.11.9, Pandas, and NumPy.
- **Directory Structure:** Initialized standardized project structure with `data/raw/`, `data/processed/`, `scripts/`, `documentation/`, `evidence/epic_01/`, `tableau/`, and `flask_app/`.
- **Schema Alignment Audit:** Analyzed the 18 expected metadata columns provided by the SkillWallet subtask *"Understand the data"*.
- **Dataset Identification & Comparison:** Audited local environment and public datasets against the 18 required fields. Identified ambiguity between the 11-column survey dataset and the 18-column clinical intervention schema specified in the SkillWallet portal.
- **Reporting:** Flagged dataset candidate ambiguity for user verification per dataset integrity rules.
