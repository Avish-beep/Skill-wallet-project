import pandas as pd

df = pd.read_csv("data/processed/student_mental_health_processed.csv")
print("=== 1. RISK DISTRIBUTION ===")
print(df["Mental_Health_Risk"].value_counts())

print("\n=== 2. CONDITIONS BY GENDER ===")
print(df.groupby("Gender")[["Depression_Flag", "Anxiety_Flag", "Panic_Attack_Flag"]].sum())
print("Gender Totals:\n", df["Gender"].value_counts())

print("\n=== 3. RISK BY AGE GROUP ===")
print(pd.crosstab(df["Age_Group"], df["Mental_Health_Risk"]))

print("\n=== 4. FACULTY RISK ===")
print(pd.crosstab(df["Faculty"], df["Mental_Health_Risk"]))

print("\n=== 5. CONDITION COUNT ===")
print(df["Condition_Count"].value_counts().sort_index())

print("\n=== 6. TREATMENT GAP ===")
print(df["Treatment_Gap"].value_counts())

print("\n=== 7. OVERALL PREVALENCE ===")
for col in ["Depression_Flag", "Anxiety_Flag", "Panic_Attack_Flag"]:
    total = df[col].sum()
    pct = df[col].mean() * 100
    print(f"{col}: {total} ({pct:.1f}%)")

print("\n=== 8. CGPA BY RISK ===")
print(df.groupby("Mental_Health_Risk")["CGPA_Midpoint"].agg(["count", "mean", "median", "std", "min", "max"]))

print("\n=== 9. AGE BY CONDITION COUNT ===")
print(df.groupby("Condition_Count")["Age"].agg(["count", "mean", "median", "min", "max"]))

print("\n=== 10. TREATMENT SOUGHT BY RISK ===")
print(pd.crosstab(df["Mental_Health_Risk"], df["Treatment_Sought"]))
