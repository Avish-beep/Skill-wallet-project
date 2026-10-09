# Deployment & Hosting Verification Report

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author:** Avishkar Padavi  
**Execution Timestamp:** 2026-10-09  

---

## 1. Hosting Architecture

| Component | Target Environment | Implementation Details | Current Status |
| :--- | :--- | :--- | :---: |
| **Project Website** | GitHub Pages (Static Hosting) | Vite + React + TypeScript + Tailwind CSS bundle built in `website/dist/` | **Ready for Pages deployment** |
| **Interactive Analytics**| Tableau Public Cloud | Live visual dashboard (`AnalysingMentalHealthinStudentEcosystem`) | **LIVE & EMBEDDED** |
| **Presentation Video** | Local & Website Media | 1080p Full HD video (20.0 MB) bundled in `video/` and `website/public/video/` | **VERIFIED ON DISK** |
| **Source Repository** | GitHub | Branch `main` at `https://github.com/Avish-beep/Skill-wallet-project` | **COMMITTED LOCALLY** |

---

## 2. GitHub Pages Configuration

1. **Workflow File:** `.github/workflows/deploy-pages.yml`
   - Actions triggered on `push` to `main` branch.
   - Sets up Node.js v20, runs `npm ci`, compiles production static site via `npm run build`.
   - Uploads `website/dist` directory as GitHub Pages artifact via `actions/upload-pages-artifact@v3`.
   - Deploys automatically via `actions/deploy-pages@v4`.

2. **Base URL Configuration:**
   - Configured in `website/vite.config.ts`: `base: '/Skill-wallet-project/'`.
   - Production target URL: `https://avish-beep.github.io/Skill-wallet-project/`.

---

## 3. Deployment Blocker & Security Status

- **Local Git Repository State:**  
  All commits, website source files, video media assets, and documentation are committed cleanly to local branch `main`.
- **Remote Push Blocker:**  
  When executing `git push origin main`, GitHub returns HTTP 403 Forbidden:  
  `remote: Permission to Avish-beep/Skill-wallet-project.git denied to padaviavishkar374-beep.`  
  *Cause:* The active Windows Credential Manager session holds tokens for GitHub account `padaviavishkar374-beep`, whereas repository owner is `Avish-beep`.  
  *Remedy:* Once the user authorizes `Avish-beep` in Git Credential Manager or grants contributor permissions to `padaviavishkar374-beep`, the branch pushes immediately and the GitHub Actions Pages workflow triggers automatically.
