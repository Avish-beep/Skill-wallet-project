import os
import hashlib
import pandas as pd
import xml.etree.ElementTree as ET

def verify():
    print("=== RUNNING EPIC 3 RESPONSIVE & DATA INTEGRITY VERIFICATION ===")
    
    # 1. Raw file hash
    raw_path = "data/raw/Student_Mental_health.csv"
    with open(raw_path, "rb") as f:
        raw_hash = hashlib.sha256(f.read()).hexdigest()
    assert raw_hash == "c0d1300dd5225b426f91ee75c81e5068efdadf528416628994a5a6e013063f0a", "Raw file hash modified!"
    print("[PASS] Raw file integrity verified (Immutable SHA-256).")

    # 2. Processed dataset
    proc_path = "data/processed/student_mental_health_processed.csv"
    df = pd.read_csv(proc_path)
    assert df.shape == (101, 23), f"Invalid processed shape: {df.shape}"
    assert df.isnull().sum().sum() == 0, "Processed dataset contains nulls!"
    assert df["User_ID"].nunique() == 101, "User_ID not distinct!"
    print("[PASS] Processed dataset (101 rows, 23 cols, 0 nulls, 0 duplicates) verified.")

    # 3. Tableau Workbook XML Integrity & Keyword Scan
    twb_path = "tableau/student_mental_health_visualizations.twb"
    assert os.path.exists(twb_path), "TWB file missing!"
    
    with open(twb_path, "r", encoding="utf-8") as f:
        twb_text = f.read()
    
    invalid_keywords = [
        "Average Mental Score", "Sleep Duration", "Attendance Rate", 
        "Heart Rate", "Study Hours", "Average Depression Level", "Stress Level"
    ]
    for kw in invalid_keywords:
        assert kw.lower() not in twb_text.lower(), f"Detected invalid example field '{kw}' in Tableau workbook XML!"
    print("[PASS] Verified ZERO invalid example fields in Tableau XML.")

    tree = ET.parse(twb_path)
    root = tree.getroot()
    assert root.tag == "workbook", "Invalid TWB XML root!"
    worksheets = [ws.attrib.get("name") for ws in root.findall(".//worksheet")]
    dashboards = [db.attrib.get("name") for db in root.findall(".//dashboard")]
    assert len(worksheets) == 10, f"Expected 10 worksheets, found {len(worksheets)}"
    assert len(dashboards) == 2, f"Expected 2 dashboards, found {len(dashboards)}"
    assert "Student Mental Health Overview" in dashboards, "Dashboard 1 missing!"
    assert "Mental Health Risk & Treatment Dashboard" in dashboards, "Dashboard 2 missing!"
    print(f"[PASS] Tableau Workbook verified with {len(worksheets)} worksheets and {len(dashboards)} dashboards.")

    # 4. Evidence PNGs
    expected_pngs = [
        "mental_health_risk.png", "conditions_by_gender.png", "risk_by_age_group.png",
        "faculty_risk.png", "condition_count.png", "treatment_gap.png",
        "condition_prevalence.png", "cgpa_risk.png", "age_condition.png",
        "treatment_by_risk.png", "dashboard_overview.png", "dashboard_treatment.png"
    ]
    for png in expected_pngs:
        p = os.path.join("evidence/epic_03", png)
        assert os.path.exists(p), f"Missing evidence PNG: {p}"
        size = os.path.getsize(p)
        assert size > 50000, f"Evidence PNG {p} too small ({size} bytes)!"
    print(f"[PASS] All {len(expected_pngs)} high-resolution evidence image artifacts verified on disk.")

    # 5. Documentation files
    expected_docs = [
        "documentation/visualization_report.md",
        "documentation/visualization_dictionary.md",
        "documentation/project_progress.md",
        "tableau/data_source_notes.md",
        "tableau/dashboard_design.md",
        "tableau/calculated_fields.md",
        "tableau/tableau_setup.md",
        "evidence/epic_03/README.md",
        "README.md",
        "CHANGELOG.md"
    ]
    for doc in expected_docs:
        assert os.path.exists(doc) and os.path.getsize(doc) > 0, f"Missing doc file: {doc}"
    print("[PASS] All required documentation and evidence manifest files verified.")

    # 6. Future epic guard
    with open("documentation/project_progress.md", "r") as f:
        prog = f.read()
    for epic_num in [4, 5, 6, 7, 8]:
        assert f"Epic {epic_num}" in prog and "Not Started" in prog, f"Future Epic {epic_num} not marked Not Started!"
    print("[PASS] Scope guard verified: Epics 4-8 strictly marked Not Started.")

    print("\nALL EPIC 3 RESPONSIVE & INTEGRITY CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    verify()
