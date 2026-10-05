"""
Data Cleaning & Preprocessing Pipeline
Analysing Mental Health in Student Ecosystem
Cleans raw survey data and produces structured, validated output for Tableau and Flask.
"""

import os
import pandas as pd
import numpy as np

def clean_data(raw_file=r"C:\Skillwallet\data\raw\Student_Mental_health.csv",
               output_file=r"C:\Skillwallet\data\processed\student_mental_health_cleaned.csv"):
    print("=" * 60)
    print("STARTING DATA CLEANING PIPELINE")
    print(f"Reading raw data from: {raw_file}")
    
    if not os.path.exists(raw_file):
        raise FileNotFoundError(f"Raw dataset not found at {raw_file}")
        
    df = pd.read_csv(raw_file)
    initial_shape = df.shape
    print(f"Raw records loaded: {initial_shape[0]} rows, {initial_shape[1]} columns")
    
    # 1. Rename columns to standardized clean names
    rename_map = {
        'Timestamp': 'timestamp',
        'Choose your gender': 'gender',
        'Age': 'age',
        'What is your course?': 'course',
        'Your current year of Study': 'year_of_study',
        'What is your CGPA?': 'cgpa_range',
        'Marital status': 'marital_status',
        'Do you have Depression?': 'depression',
        'Do you have Anxiety?': 'anxiety',
        'Do you have Panic attack?': 'panic_attack',
        'Did you seek any specialist for a treatment?': 'treatment_sought'
    }
    df = df.rename(columns=rename_map)
    
    # 2. Check for exact duplicate rows
    n_dupes = df.duplicated().sum()
    print(f"Duplicate rows detected: {n_dupes}")
    if n_dupes > 0:
        df = df.drop_duplicates().reset_index(drop=True)
        print(f"Dropped {n_dupes} duplicate rows.")
        
    # 3. Handle Missing Values
    print("Handling missing values:")
    missing_summary = df.isna().sum()
    for col, count in missing_summary.items():
        if count > 0:
            print(f"  Column '{col}' has {count} missing value(s).")
            
    # Impute missing Age with median of existing ages
    if df['age'].isna().sum() > 0:
        median_age = df['age'].median()
        print(f"  Imputing missing age with median value: {median_age}")
        df['age'] = df['age'].fillna(median_age).astype(int)
    else:
        df['age'] = df['age'].astype(int)
        
    # 4. Standardize Categorical Variables
    # Gender
    df['gender'] = df['gender'].str.strip().str.capitalize()
    
    # Year of Study (e.g. 'year 1', 'Year 1' -> 'Year 1')
    def standardize_year(val):
        if pd.isna(val):
            return val
        val_clean = str(val).strip().lower()
        if '1' in val_clean:
            return 'Year 1'
        elif '2' in val_clean:
            return 'Year 2'
        elif '3' in val_clean:
            return 'Year 3'
        elif '4' in val_clean:
            return 'Year 4'
        return str(val).strip().title()

    df['year_of_study'] = df['year_of_study'].apply(standardize_year)
    
    # CGPA Range (strip whitespace, e.g. '3.50 - 4.00 ' -> '3.50 - 4.00')
    df['cgpa_range'] = df['cgpa_range'].str.strip()
    
    # Standardize Yes/No fields
    binary_cols = ['marital_status', 'depression', 'anxiety', 'panic_attack', 'treatment_sought']
    for b_col in binary_cols:
        df[b_col] = df[b_col].str.strip().str.capitalize()
        
    # Standardize Course names
    df['course_raw'] = df['course']
    df['course'] = df['course'].str.strip().str.title()
    # Normalize common abbreviations and misspellings
    course_replacements = {
        'Bit': 'Information Technology (BIT)',
        'It': 'Information Technology',
        'Bcs': 'Computer Science (BCS)',
        'Engineering': 'Engineering',
        'Engin': 'Engineering',
        'Koe': 'Engineering (KOE)',
        'Kop': 'Pharmacy (KOP)',
        'KIRKHS': 'Islamic Revealed Knowledge (KIRKHS)',
        'Mathemathics': 'Mathematics',
        'Econs': 'Economics',
        'Law': 'Laws'
    }
    for old_val, new_val in course_replacements.items():
        mask = df['course'].str.lower() == old_val.lower()
        df.loc[mask, 'course'] = new_val

    # Group into broad Faculty / Discipline
    def categorize_faculty(course_str):
        c = str(course_str).lower()
        if any(w in c for w in ['engineering', 'koe', 'engin', 'cts']):
            return 'Engineering'
        elif any(w in c for w in ['bit', 'it', 'computer', 'bcs']):
            return 'Computing & IT'
        elif any(w in c for w in ['law', 'laws', 'human sciences', 'psychology', 'communication', 'kirkhs', 'benl', 'irkhs']):
            return 'Humanities & Social Sciences'
        elif any(w in c for w in ['islamic', 'usuluddin', 'kenms', 'fiqh', 'enm', 'taqwa']):
            return 'Islamic Studies & Ethics'
        elif any(w in c for w in ['economics', 'accounting', 'management', 'business', 'banking', 'econs']):
            return 'Business & Economics'
        elif any(w in c for w in ['biomedical', 'pharmacy', 'nursing', 'kop', 'radiography', 'medical']):
            return 'Allied Health Sciences'
        else:
            return 'Sciences & General'

    df['faculty'] = df['course'].apply(categorize_faculty)

    # 5. Derived Features (Supported strictly by actual data)
    # Binary numeric flags for conditions
    df['depression_flag'] = (df['depression'] == 'Yes').astype(int)
    df['anxiety_flag'] = (df['anxiety'] == 'Yes').astype(int)
    df['panic_attack_flag'] = (df['panic_attack'] == 'Yes').astype(int)
    df['treatment_sought_flag'] = (df['treatment_sought'] == 'Yes').astype(int)

    # Total Condition Count (0 to 3)
    df['condition_count'] = df['depression_flag'] + df['anxiety_flag'] + df['panic_attack_flag']

    # Mental Health Risk Category
    conditions = [
        (df['condition_count'] == 0),
        (df['condition_count'] == 1),
        (df['condition_count'] >= 2)
    ]
    choices = ['Low Risk', 'Moderate Risk', 'High Risk']
    df['mental_health_risk'] = np.select(conditions, choices, default='Unknown')

    # Treatment Gap Category
    def compute_treatment_gap(row):
        if row['condition_count'] == 0:
            return 'No Identified Condition'
        elif row['treatment_sought'] == 'Yes':
            return 'Condition Treated'
        else:
            return 'Untreated Condition'

    df['treatment_gap'] = df.apply(compute_treatment_gap, axis=1)

    # CGPA Midpoint (continuous proxy for numeric calculations)
    cgpa_map = {
        '0 - 1.99': 1.00,
        '2.00 - 2.49': 2.25,
        '2.50 - 2.99': 2.75,
        '3.00 - 3.49': 3.25,
        '3.50 - 4.00': 3.75
    }
    df['cgpa_midpoint'] = df['cgpa_range'].map(cgpa_map).fillna(3.00)

    # Age Group
    df['age_group'] = pd.cut(df['age'], bins=[17, 20, 25], labels=['18-20 (Underclassmen)', '21-24 (Upperclassmen)'])

    # Student ID (sequential identifier for student count & anonymized tracking)
    df.insert(0, 'student_id', [f"STD_{i+1:04d}" for i in range(len(df))])

    # 6. Save Processed Dataset
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved to: {output_file}")
    print(f"Final shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("=" * 60)
    return df

if __name__ == '__main__':
    clean_data()
