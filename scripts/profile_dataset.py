"""
Dataset Profiling Script
Performs an in-depth audit of the raw dataset without modifying anything.
"""
import os
import pandas as pd
import numpy as np

def profile():
    raw_path = r"C:\Skillwallet\data\raw\Student_Mental_health.csv"
    if not os.path.exists(raw_path):
        print(f"Error: Raw dataset not found at {raw_path}")
        return

    df = pd.read_csv(raw_path)
    print("=" * 60)
    print("RAW DATASET PROFILE: Student Mental health.csv")
    print("=" * 60)
    print(f"Total Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")
    print(f"Duplicate Rows: {df.duplicated().sum()}")
    print("-" * 60)
    
    print("COLUMNS & MISSING VALUES:")
    for idx, col in enumerate(df.columns):
        n_missing = df[col].isna().sum()
        pct_missing = (n_missing / len(df)) * 100
        print(f"  [{idx}] '{col}' | Type: {df[col].dtype} | Nulls: {n_missing} ({pct_missing:.1f}%)")

    print("-" * 60)
    print("CATEGORICAL VALUES & CARDINALITY:")
    for col in df.columns:
        uniques = df[col].dropna().unique()
        if len(uniques) <= 12:
            print(f"\n* '{col}':\n  Values: {list(uniques)}")
        else:
            print(f"\n* '{col}': {len(uniques)} unique values (sample: {list(uniques[:5])})")

    print("-" * 60)
    print("SUMMARY STATISTICS:")
    print(df.describe(include='all').T)
    print("=" * 60)

if __name__ == "__main__":
    profile()
