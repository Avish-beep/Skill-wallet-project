# Deployment & Hosting Verification Report

**Project Title:** Analysing Mental Health in Student Ecosystem
**Author:** Avishkar Padavi
**Execution Timestamp:** 2026-10-09

---

## 1. Hosting Architecture & Verified Status

| Component | Target Environment | Implementation Details | Verified Live Status |
| :--- | :--- | :--- | :---: |
| **Project Website** | GitHub Pages (Static Hosting) | Vite + React + TypeScript + Tailwind CSS bundle built in `website/dist/` | **LIVE (HTTP 200)** |
| **Interactive Analytics**| Tableau Desktop & Cloud | Verified local workbook architecture; Tableau Public connection | **LOCAL VERIFIED / CLOUD OVERWRITE QUEUED** |
| **Presentation Video** | Deployed Web Asset | 1080p Full HD video (06:24, 19.4 MB) served via GitHub Pages | **LIVE (HTTP 200, readyState 4)** |
| **Source Repository** | GitHub | Branch `main` at `https://github.com/Avish-beep/Skill-wallet-project` | **PUSHED & SYNCHRONIZED** |

---

## 2. GitHub Pages CI/CD Workflow Execution

1. **Workflow File:** `.github/workflows/deploy-pages.yml`
   - Actions triggered on `push` to `main` branch.
   - Sets up Node.js v20, runs `npm ci`, compiles production static site via `npm run build`.
   - Uploads `website/dist` directory as GitHub Pages artifact via `actions/upload-pages-artifact@v3`.
   - Deploys automatically via `actions/deploy-pages@v4`.

2. **Base URL Configuration:**
   - Configured in `website/vite.config.ts`: `base: '/Skill-wallet-project/'`.
   - Production target URL: `https://avish-beep.github.io/Skill-wallet-project/`.

3. **Latest Verified Workflow Run:**
   - **Run ID:** `37954443324`
   - **Commit SHA:** `be47d7289032c38fdb6f119f97617af7311decb7`
   - **Conclusion:** `success`
   - **HTTP Status:** `200 OK`
   - **Console Errors:** `0`

---

## 3. Remote Synchronization & Live Verification

- **Git Remote Synchronization:**
  Remote branch `origin/main` is fully synchronized with local `main`.
- **Live Playback Audit:**
  Automated Playwright evaluation on the live GitHub Pages deployment confirmed:
  - Video stream `https://avish-beep.github.io/Skill-wallet-project/video/project_presentation.mp4` loads with `readyState: 4` (`HAVE_ENOUGH_DATA`).
  - WebVTT subtitles `https://avish-beep.github.io/Skill-wallet-project/video/captions.vtt` load with HTTP 200.
  - Multi-viewport layout renders without horizontal overflow across Desktop (1920x1080), Laptop (1440x900), Tablet (768x1024), and Mobile (390x844).
