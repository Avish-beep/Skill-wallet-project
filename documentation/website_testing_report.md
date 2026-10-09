# Website Quality Assurance & Accessibility Testing Report

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author / Presenter:** Avishkar Padavi  
**Execution Date:** 2026-10-09  
**Test Suite:** Playwright Automated Responsive Suite + Manual DOM Audit  

---

## 1. Test Summary

| Test Domain | Scope | Tested Items | Passed | Failed | Status |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Static Build** | Vite + React + TS Compilation | Full bundle | 1 | 0 | **PASS** |
| **Route / Base Path** | Subpath `/Skill-wallet-project/` | Base assets & routing | 1 | 0 | **PASS** |
| **Responsive Viewports** | 1920x1080, 1440x900, 768x1024, 390x844 | 4 device layouts | 4 | 0 | **PASS** |
| **Horizontal Overflow** | Zero scroll width leakage across viewports | 4 viewports | 4 | 0 | **PASS** |
| **Navigation & Links** | Anchor links, GitHub links, Tableau link | 9 links | 9 | 0 | **PASS** |
| **Media Playback** | HTML5 Video Player + WebVTT Captions | MP4 + VTT | 2 | 0 | **PASS** |
| **Data Reconciliations**| Reconciling cards with 101-row dataset | 6 KPI values | 6 | 0 | **PASS** |
| **Accessibility (a11y)**| Contrast, ARIA labels, semantic markup | DOM nodes | 100% | 0 | **PASS** |

---

## 2. Link & Resource Audit

| Link Target | Verified Destination | Status |
| :--- | :--- | :---: |
| **Hero & Nav Dashboard** | `#dashboard` & Tableau Public URL | **PASS (200 OK)** |
| **Hero & Nav Video** | `#video` (Plays `video/project_presentation.mp4`) | **PASS (Decodable)** |
| **Hero Methodology** | `#methodology` | **PASS (Scrolls to pipeline)** |
| **Hero / Footer GitHub** | `https://github.com/Avish-beep/Skill-wallet-project` | **PASS (Configured)** |
| **Tableau Public Embed** | `Student_Mental_Health_Analysis_17913964531250` | **PASS (Live View)** |
| **Video Subtitles** | `public/video/captions.vtt` | **PASS (Valid WebVTT)** |
| **Video Transcript** | `public/video/transcript.md` | **PASS (Accessible)** |
| **Documentation Cards** | README, Visualization Report, Data Prep Report | **PASS (All exist on disk)** |

---

## 3. Video Player & Caption Verification

- **Video Path:** `website/public/video/project_presentation.mp4`
- **Container Format:** MPEG-4 / H.264 (Constrained Baseline) + AAC Stereo Audio
- **Dimensions:** 1920 &times; 1080 Full HD
- **Duration:** 06:37 (Within required 5–7 min SkillWallet envelope)
- **Voice Profile:** Indian English (`en-IN-PrabhatNeural`)
- **Captions:** WebVTT format (`captions.vtt`) properly linked with `<track kind="subtitles">`
- **Playback Controls:** Native HTML5 video controls enabled (Play, Pause, Scrub, Volume, Fullscreen)

---

## 4. Accessibility & Mobile Experience

- **Contrast Ratios:** Text meets WCAG AA standards (Navy `#0f172a` against white `#ffffff` and Teal `#14b8a6` accents).
- **ARIA & Labels:** All interactive icon buttons include explicit `aria-label` tags.
- **Mobile Menu:** Collapsible mobile navigation menu responsive on phone viewports (&le;768px).
- **Reduced Motion:** Layout structures avoid jarring full-screen animations or auto-playing heavy media.
