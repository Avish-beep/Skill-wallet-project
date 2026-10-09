# Contributing to Analysing Mental Health in Student Ecosystem

Thank you for your interest in contributing to the **Analysing Mental Health in Student Ecosystem** project. We welcome contributions that preserve empirical rigor, improve accessibility, enhance visualization clarity, and maintain code quality.

---

## 1. Project Overview & Governance Principles

This repository represents an academic capstone portfolio demonstrating end-to-end data analytics on student mental health survey data. All contributions must adhere to these non-negotiable principles:

- **Empirical Ground Truth:** All statistics, charts, and metrics must be calculated directly from the validated dataset (`data/processed/student_mental_health_processed.csv`, N=101 students).
- **Zero Fabrication:** Never introduce placeholder, synthetic, or imaginary metrics (e.g., *Sleep Hours*, *Daily Screen Time*, *Stress Level Score*, *Heart Rate Variability*, *Attendance Rate*).
- **Non-Clinical Observational Framing:** Claims must always reflect self-reported survey indicators, not clinical psychiatric diagnoses.
- **Privacy & Anonymity:** Never commit student PII, credentials, or private records.

---

## 2. Prerequisites & Environment Setup

To work with this project locally on Windows, macOS, or Linux, ensure you have:

- **Node.js:** v20.x or higher (`node -v`)
- **npm:** v10.x or higher (`npm -v`)
- **Python:** v3.11.x or higher (`python --version`)
- **Git:** v2.40.x or higher (`git --version`)
- **Tableau Desktop / Tableau Public:** 2024.1 or higher (for workbook modifications)

### Local Repository Setup (Windows PowerShell)

```powershell
# Clone the repository
git clone https://github.com/Avish-beep/Skill-wallet-project.git
cd Skill-wallet-project

# Activate Python virtual environment
python -m venv venv
& "venv\Scripts\Activate.ps1"

# Install Python requirements
pip install -r requirements.txt
playwright install chromium
```

---

## 3. Development Workflow

### Frontend Web Portfolio (`website/`)

```powershell
cd website

# Install dependencies
npm install

# Run Vite local development server
npm run dev

# Run linter
npm run lint

# Compile production build
npm run build

# Preview production build locally
npm run preview
```

### Reproducible Data Pipeline & Validation Scripts

From the repository root:

```powershell
# 1. Execute reproducible ETL pipeline
& "venv\Scripts\python.exe" "scripts\prepare_dataset.py"

# 2. Verify dataset integrity and Tableau workbook
& "venv\Scripts\python.exe" "scripts\verify_epic_03.py"

# 3. Execute automated multi-viewport responsive test suite
& "venv\Scripts\python.exe" "scripts\test_website_responsive.py"
```

---

## 4. Code Quality & Standards

- **TypeScript Strictness:** Keep strict type-checking enabled in `website/tsconfig.json`. Ensure `tsc -b` passes without errors.
- **Responsive Layout:** Any layout change must be verified across 4 viewports (1920x1080, 1440x900, 768x1024, 390x844) with **0px horizontal scroll / overflow**.
- **Accessible Design:** Ensure semantic HTML, adequate color contrast, alt attributes, and WCAG 2.1 AA compatibility.
- **Relative Path Awareness:** Media and asset paths must respect Vite's base path: `/Skill-wallet-project/`.

---

## 5. Pull Request Guidelines

1. **Create a Feature Branch:** Branch from `main` with a descriptive name (e.g., `feat/accessible-contrast`, `fix/navbar-mobile-padding`).
2. **Commit Messages:** Follow Conventional Commits:
   - `feat:` for new capabilities
   - `fix:` for bug and layout fixes
   - `docs:` for documentation updates
   - `refactor:` for code restructuring
3. **Run Checks Before Opening PR:** Ensure `npm run build` succeeds, responsive tests pass, and `git diff --check` shows no whitespace errors.
4. **Licensing Agreement:** By submitting a pull request, you agree that your original code contributions are licensed under the MIT License, and documentation contributions under CC BY 4.0.
