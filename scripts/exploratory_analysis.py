"""
Exploratory Data Analysis Script
Analysing Mental Health in Student Ecosystem
Evaluates all 12 analytical dimensions strictly against available columns.
"""
import os
import pandas as pd
import numpy as np

def run_analysis(input_file=r"C:\Skillwallet\data\processed\student_mental_health_cleaned.csv",
                 output_report=r"C:\Skillwallet\documentation\analysis_summary.md"):
    print("=" * 60)
    print("RUNNING EXPLORATORY DATA ANALYSIS")
    df = pd.read_csv(input_file)
    n_students = len(df)
    print(f"Total Student Cohort Analyzed: {n_students}")
    
    os.makedirs(os.path.dirname(output_report), exist_ok=True)
    
    lines = []
    lines.append("# Exploratory Data Analysis Report: Student Mental Health Ecosystem\n")
    lines.append(f"**Cohort Size:** {n_students} Students  ")
    lines.append(f"**Data Source:** Anonymized Higher Education Survey (`Student_Mental_health.csv`)  ")
    lines.append(f"**Date Processed:** October 2026\n")
    lines.append("---\n")
    lines.append("## Executive Statistical Summary\n")

    # 1. Stress level distribution
    lines.append("### 1. Stress Level Distribution")
    lines.append("- **Dataset Status:** *Direct Likert Scale Not Available in Dataset.*")
    lines.append("- **Closest Valid Analysis / Proxy:** Evaluation of Panic Attacks and Concurrent Multi-Condition Burden (`condition_count`), which serve as empirical behavioral proxies for acute stress manifestations.")
    panic_count = df['panic_attack_flag'].sum()
    panic_pct = (panic_count / n_students) * 100
    lines.append(f"- **Acute Stress (Panic Attacks):** {panic_count} students ({panic_pct:.1f}%).")
    lines.append(f"- **Multi-Condition Load (≥2 Conditions):** {(df['condition_count'] >= 2).sum()} students ({((df['condition_count'] >= 2).sum()/n_students)*100:.1f}%).\n")

    # 2. Anxiety distribution
    lines.append("### 2. Anxiety Distribution")
    lines.append("- **Dataset Status:** *Available (`anxiety` / `anxiety_flag`).*")
    anx_count = df['anxiety_flag'].sum()
    anx_pct = (anx_count / n_students) * 100
    lines.append(f"- **Anxiety Prevalence:** {anx_count} of {n_students} students ({anx_pct:.1f}%).")
    lines.append(f"- **Gender Breakdown:**")
    for g, grp in df.groupby('gender'):
        g_anx = grp['anxiety_flag'].sum()
        lines.append(f"  - {g}: {g_anx}/{len(grp)} ({g_anx/len(grp)*100:.1f}%)")
    lines.append("")

    # 3. Mental health risk
    lines.append("### 3. Mental Health Risk Stratification")
    lines.append("- **Dataset Status:** *Available (Derived composite metric from clinical indicators).*")
    risk_dist = df['mental_health_risk'].value_counts()
    for r_lvl, count in risk_dist.items():
        lines.append(f"- **{r_lvl}:** {count} students ({count/n_students*100:.1f}%)")
    lines.append("")

    # 4. Sleep quality
    lines.append("### 4. Sleep Quality")
    lines.append("- **Dataset Status:** *Not Available in Dataset.*")
    lines.append("- **Recommendation:** Future survey waves should integrate the Pittsburgh Sleep Quality Index (PSQI) or average sleep hours per night.\n")

    # 5. Study hours
    lines.append("### 5. Study Hours")
    lines.append("- **Dataset Status:** *Not Available in Dataset.*")
    lines.append("- **Closest Valid Analysis:** Year of study and academic major intensity proxies. Study hours variable was not captured in this survey wave.\n")

    # 6. Screen time
    lines.append("### 6. Screen Time")
    lines.append("- **Dataset Status:** *Not Available in Dataset.*")
    lines.append("- **Recommendation:** Digital wellness tracking modules should capture daily device screen hours.\n")

    # 7. Academic performance (CGPA)
    lines.append("### 7. Academic Performance (CGPA)")
    lines.append("- **Dataset Status:** *Available (`cgpa_range`, `cgpa_midpoint`).*")
    lines.append(f"- **Cohort Mean CGPA Midpoint:** {df['cgpa_midpoint'].mean():.2f} (Standard Deviation: {df['cgpa_midpoint'].std():.2f})")
    lines.append("- **CGPA Range Distribution:**")
    cgpa_dist = df['cgpa_range'].value_counts()
    for r, count in cgpa_dist.items():
        lines.append(f"  - `{r}`: {count} students ({count/n_students*100:.1f}%)")
    lines.append("- **Depression Prevalence by Academic Standing:**")
    for r, grp in df.groupby('cgpa_range'):
        dep_rate = grp['depression_flag'].mean() * 100
        lines.append(f"  - `{r}`: {grp['depression_flag'].sum()}/{len(grp)} ({dep_rate:.1f}% depressed)")
    lines.append("")

    # 8. Social interaction
    lines.append("### 8. Social Interaction")
    lines.append("- **Dataset Status:** *Not Available in Dataset.*")
    lines.append("- **Closest Valid Analysis:** Marital status (`marital_status`) is available as a proxy for primary interpersonal relationship status. Married students: " +
                 f"{(df['marital_status'] == 'Yes').sum()} ({(df['marital_status'] == 'Yes').sum()/n_students*100:.1f}%).\n")

    # 9. Mood
    lines.append("### 9. Mood")
    lines.append("- **Dataset Status:** *Direct Mood Diary Not Available.*")
    lines.append("- **Closest Valid Analysis:** Depression indicator (`depression`). Prevalence: " +
                 f"{df['depression_flag'].sum()} students ({df['depression_flag'].mean()*100:.1f}%).\n")

    # 10. Burnout
    lines.append("### 10. Burnout")
    lines.append("- **Dataset Status:** *Maslach Burnout Inventory (MBI) Not Available.*")
    lines.append("- **Closest Valid Analysis:** Comorbidity score (`condition_count == 3` - having Depression, Anxiety, and Panic Attacks concurrently). " +
                 f"Total experiencing severe comorbidity: {(df['condition_count'] == 3).sum()} students ({((df['condition_count'] == 3).sum()/n_students)*100:.1f}%).\n")

    # 11. Demographics
    lines.append("### 11. Demographic Profiles")
    lines.append("- **Dataset Status:** *Available (`gender`, `age`, `course`, `faculty`, `year_of_study`).*")
    lines.append(f"- **Gender Distribution:** Female: {(df['gender'] == 'Female').sum()} ({(df['gender'] == 'Female').sum()/n_students*100:.1f}%), " +
                 f"Male: {(df['gender'] == 'Male').sum()} ({(df['gender'] == 'Male').sum()/n_students*100:.1f}%)")
    lines.append(f"- **Age Range:** {df['age'].min()} to {df['age'].max()} years (Mean: {df['age'].mean():.1f}, Median: {df['age'].median():.0f})")
    lines.append("- **Academic Seniority:**")
    for yr, count in df['year_of_study'].value_counts().items():
        lines.append(f"  - {yr}: {count} students ({count/n_students*100:.1f}%)")
    lines.append("- **Faculty Distribution:**")
    for fac, count in df['faculty'].value_counts().items():
        lines.append(f"  - {fac}: {count} students ({count/n_students*100:.1f}%)")
    lines.append("")

    # 12. Lifestyle patterns & Treatment seeking
    lines.append("### 12. Lifestyle Patterns & Health-Seeking Behavior")
    lines.append("- **Dataset Status:** *Available (`treatment_sought`, `treatment_gap`).*")
    t_sought = df['treatment_sought_flag'].sum()
    lines.append(f"- **Specialist Consultation Rate:** {t_sought} of {n_students} students ({t_sought/n_students*100:.1f}%)")
    active_conditions = (df['condition_count'] > 0).sum()
    untreated = ((df['condition_count'] > 0) & (df['treatment_sought'] == 'No')).sum()
    lines.append(f"- **Students with ≥1 Mental Health Condition:** {active_conditions} ({active_conditions/n_students*100:.1f}%)")
    lines.append(f"- **Critical Treatment Gap:** {untreated} students with active symptoms have NOT sought specialist treatment ({untreated/active_conditions*100:.1f}% of affected cohort)!")
    lines.append("")

    with open(output_report, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
        
    print(f"Analysis summary successfully written to {output_report}")
    print("=" * 60)

if __name__ == '__main__':
    run_analysis()
