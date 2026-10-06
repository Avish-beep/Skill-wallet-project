"""
Reusable Dataset Inspection & Schema Validator
Analysing Mental Health in Student Ecosystem (SkillWallet Epic 1)
Audits any CSV/Excel file against the 18 expected SkillWallet metadata fields.
"""

import os
import sys
import argparse
import pandas as pd
import numpy as np

EXPECTED_SCHEMA = [
    "User ID",
    "Age",
    "Gender",
    "Occupation",
    "Stress Level",
    "Anxiety Score",
    "Depression Score",
    "Sleep Quality",
    "Daily Screen Time (hrs)",
    "Physical Activity Level",
    "Social Interaction Score",
    "Mental Health History",
    "Therapy Type",
    "Intervention Duration (weeks)",
    "Progress Score",
    "Medication Usage",
    "Support System Strength",
    "Work-Life Balance Score"
]

def inspect(file_path):
    print("=" * 70)
    print("DATASET INTEGRITY & SCHEMA INSPECTION REPORT")
    print("=" * 70)
    
    if not os.path.exists(file_path):
        print(f"[ERROR] Target file does not exist: {file_path}")
        return False

    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_path)[1].lower()
    file_size_kb = os.path.getsize(file_path) / 1024

    print(f"File Name: {file_name}")
    print(f"File Path: {file_path}")
    print(f"File Format: {file_ext}")
    print(f"File Size: {file_size_kb:.2f} KB")

    # Ingestion
    try:
        if file_ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
    except Exception as e:
        print(f"[FATAL] Failed to read dataset: {e}")
        return False

    n_rows, n_cols = df.shape
    print(f"Dimensions: {n_rows} rows x {n_cols} columns")
    print(f"Duplicate Full Rows: {df.duplicated().sum()}")
    print("-" * 70)

    # 1. Schema Validation against SkillWallet Expected Columns
    print("SCHEMA VALIDATION (18 EXPECTED SKILLWALLET FIELDS):")
    found_count = 0
    missing_count = 0
    actual_cols_lower = {str(c).strip().lower(): c for c in df.columns}

    for exp_col in EXPECTED_SCHEMA:
        exp_lower = exp_col.lower()
        if exp_col in df.columns:
            print(f"  [FOUND EXACT]           {exp_col}")
            found_count += 1
        elif exp_lower in actual_cols_lower:
            actual_name = actual_cols_lower[exp_lower]
            print(f"  [FOUND CASE-VARIANT]   {exp_col} -> Actual: '{actual_name}'")
            found_count += 1
        else:
            # Fuzzy check
            fuzzy_matches = [c for c in df.columns if any(token in c.lower() for token in exp_col.lower().split() if len(token) > 3)]
            if fuzzy_matches:
                print(f"  [PARTIAL/DIFFERENT]    {exp_col} -> Potential Match: {fuzzy_matches}")
            else:
                print(f"  [MISSING]              {exp_col}")
            missing_count += 1

    print(f"\nSchema Score: {found_count}/{len(EXPECTED_SCHEMA)} Expected Columns Found")
    print("-" * 70)

    # 2. Detailed Column Profiling
    print("ACTUAL COLUMNS DETAILED AUDIT:")
    for idx, col in enumerate(df.columns):
        col_type = df[col].dtype
        null_count = df[col].isna().sum()
        null_pct = (null_count / n_rows) * 100
        uniques = df[col].dropna().unique()
        n_uniques = len(uniques)

        print(f"\n[{idx+1}] Column: '{col}' | Type: {col_type} | Nulls: {null_count} ({null_pct:.1f}%) | Distinct: {n_uniques}")
        
        # Numeric statistics
        if pd.api.types.is_numeric_dtype(df[col]):
            c_min = df[col].min()
            c_max = df[col].max()
            c_mean = df[col].mean()
            c_std = df[col].std()
            print(f"    Min: {c_min} | Max: {c_max} | Mean: {c_mean:.2f} | Std: {c_std:.2f}")
        else:
            sample_uniques = list(uniques[:6])
            print(f"    Sample Values: {sample_uniques}")

    print("=" * 70)
    return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else r"C:\Skillwallet\data\raw\Student_Mental_health.csv"
    inspect(target)
