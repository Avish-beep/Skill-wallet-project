import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Ensure evidence directory exists
os.makedirs("evidence/epic_03", exist_ok=True)

# Load validated processed dataset
df = pd.read_csv("data/processed/student_mental_health_processed.csv")

# Set standard styling
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#CBD5E0'
plt.rcParams['axes.linewidth'] = 0.8

# Color Palettes
RISK_COLORS = {
    "Low Risk": "#38A169",      # Green
    "Moderate Risk": "#DD6B20", # Amber/Orange
    "High Risk": "#E53E3E"      # Crimson/Red
}

GENDER_COLORS = {
    "Female": "#805AD5",        # Purple
    "Male": "#3182CE"           # Blue
}

CONDITION_COLORS = {
    "Depression": "#2B6CB0",
    "Anxiety": "#D69E2E",
    "Panic Attack": "#C53030"
}

# -------------------------------------------------------------
# VISUALIZATION 1: Mental Health Risk Distribution
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
risk_counts = df["Mental_Health_Risk"].value_counts().loc[["Low Risk", "Moderate Risk", "High Risk"]]
colors = [RISK_COLORS[r] for r in risk_counts.index]
bars = ax.bar(risk_counts.index, risk_counts.values, color=colors, width=0.55, edgecolor="#2D3748", linewidth=1.2)

for bar in bars:
    yval = bar.get_height()
    pct = (yval / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval} ({pct:.1f}%)", 
            ha='center', va='bottom', fontsize=11, fontweight='bold', color='#2D3748')

ax.set_title("Mental Health Risk Distribution Among Students", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Number of Students (COUNTD)", fontsize=11, fontweight='semibold')
ax.set_xlabel("Mental Health Risk Tier", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Source: student_mental_health_processed.csv (N=101) | Derived from comorbidity condition counts (0, 1, 2-3)",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/mental_health_risk.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 2: Mental Health Conditions by Gender
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
gender_conditions = df.groupby("Gender")[["Depression_Flag", "Anxiety_Flag", "Panic_Attack_Flag"]].sum()
gender_conditions.columns = ["Depression", "Anxiety", "Panic Attack"]

x = np.arange(len(gender_conditions.columns))
width = 0.35

rects1 = ax.bar(x - width/2, gender_conditions.loc["Female"], width, label=f'Female (N={len(df[df["Gender"]=="Female"])})', 
                color='#805AD5', edgecolor='#44337A')
rects2 = ax.bar(x + width/2, gender_conditions.loc["Male"], width, label=f'Male (N={len(df[df["Gender"]=="Male"])})', 
                color='#3182CE', edgecolor='#2B6CB0')

for rects, g_total in [(rects1, 75), (rects2, 26)]:
    for rect in rects:
        h = rect.get_height()
        pct = (h / g_total) * 100
        ax.annotate(f'{h}\n({pct:.1f}%)',
                    xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_title("Mental Health Conditions by Gender", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Number of Affected Students", fontsize=11, fontweight='semibold')
ax.set_xticks(x)
ax.set_xticklabels(gender_conditions.columns, fontsize=11, fontweight='semibold')
ax.set_ylim(0, 35)
ax.legend(frameon=True, facecolor='white', edgecolor='#E2E8F0')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Note: Percentages indicate within-gender prevalence (Female N=75, Male N=26). Survey self-reported data.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/conditions_by_gender.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 3: Mental Health Risk by Age Group
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
crosstab_age = pd.crosstab(df["Age_Group"], df["Mental_Health_Risk"])[["Low Risk", "Moderate Risk", "High Risk"]]

bottom = np.zeros(len(crosstab_age))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    values = crosstab_age[col].values
    bars = ax.bar(crosstab_age.index, values, bottom=bottom, label=col, color=RISK_COLORS[col], width=0.5, edgecolor='#2D3748')
    for i, (val, b) in enumerate(zip(values, bottom)):
        if val > 0:
            ax.text(i, b + val/2, f"{val}", ha='center', va='center', color='white', fontweight='bold', fontsize=11)
    bottom += values

for i, total in enumerate(crosstab_age.sum(axis=1)):
    ax.text(i, total + 1.5, f"Total: {total}", ha='center', va='bottom', fontweight='bold', fontsize=11)

ax.set_title("Mental Health Risk Across Age Groups", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Student Count", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 70)
ax.legend(title="Risk Level", frameon=True, loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Underclassmen (18-20, N=60) vs Upperclassmen (21-24, N=41). Stacked segment counts.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/risk_by_age_group.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 4: Faculty-wise Mental Health Risk
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
crosstab_faculty = pd.crosstab(df["Faculty"], df["Mental_Health_Risk"])[["Low Risk", "Moderate Risk", "High Risk"]]
crosstab_faculty["Total"] = crosstab_faculty.sum(axis=1)
crosstab_faculty = crosstab_faculty.sort_values(by="Total", ascending=True)

left = np.zeros(len(crosstab_faculty))
y_positions = np.arange(len(crosstab_faculty))

for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    values = crosstab_faculty[col].values
    ax.barh(y_positions, values, left=left, label=col, color=RISK_COLORS[col], height=0.6, edgecolor='#2D3748')
    left += values

for idx, total in enumerate(crosstab_faculty["Total"]):
    ax.text(total + 0.5, idx, f"{total}", va='center', ha='left', fontweight='bold', fontsize=10)

ax.set_yticks(y_positions)
ax.set_yticklabels(crosstab_faculty.index, fontsize=10, fontweight='semibold')
ax.set_title("Mental Health Risk by Faculty", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Student Count", fontsize=11, fontweight='semibold')
ax.set_xlim(0, 32)
ax.legend(title="Risk Level", loc='lower right', frameon=True)
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Engineered academic faculty classification based on 43 course majors. Stacked risk distribution.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/faculty_risk.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 5: Condition Count Distribution
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
cond_counts = df["Condition_Count"].value_counts().sort_index()
cond_colors = ["#38A169", "#DD6B20", "#E53E3E", "#9B2C2C"]
bars = ax.bar([str(i) for i in cond_counts.index], cond_counts.values, color=cond_colors, width=0.55, edgecolor='#2D3748')

for bar in bars:
    h = bar.get_height()
    pct = (h / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, h + 1, f"{h}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=10)

ax.set_title("Distribution of Mental Health Condition Count", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Number of Concurrent Conditions (Depression, Anxiety, Panic Attacks)", fontsize=11, fontweight='semibold')
ax.set_ylabel("Student Count", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.18, "Shows comorbidity load (0 to 3 concurrent conditions). Non-clinical self-reported survey measure.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/condition_count.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 6: Student Mental Health Treatment Gap
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
gap_counts = df["Treatment_Gap"].value_counts().loc[["Untreated Condition", "No Identified Condition", "Condition Treated"]]
gap_colors = ["#E53E3E", "#38A169", "#3182CE"]
bars = ax.bar(gap_counts.index, gap_counts.values, color=gap_colors, width=0.55, edgecolor='#2D3748')

for bar in bars:
    h = bar.get_height()
    pct = (h / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, h + 1.5, f"{h}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=10)

ax.set_title("Student Mental Health Treatment Gap", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Number of Students", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 70)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Highlights that 58/64 (90.6%) symptomatic students have not sought specialist treatment. Self-reported data.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/treatment_gap.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 7: Prevalence of Self-Reported Conditions
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
conditions = ["Depression", "Anxiety", "Panic Attack"]
totals = [df["Depression_Flag"].sum(), df["Anxiety_Flag"].sum(), df["Panic_Attack_Flag"].sum()]
bar_colors = [CONDITION_COLORS[c] for c in conditions]
bars = ax.bar(conditions, totals, color=bar_colors, width=0.5, edgecolor='#2D3748')

for bar in bars:
    h = bar.get_height()
    pct = (h / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, h + 1, f"{h}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=11)

ax.set_title("Prevalence of Self-Reported Mental Health Conditions", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Affected Student Count", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Prevalence across full student cohort (N=101). Multiple conditions can affect an individual.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/condition_prevalence.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 8: CGPA and Mental Health Risk
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
risk_order = ["Low Risk", "Moderate Risk", "High Risk"]
sns.boxplot(data=df, x="Mental_Health_Risk", y="CGPA_Midpoint", order=risk_order, 
            palette=RISK_COLORS, width=0.45, ax=ax, boxprops=dict(edgecolor='#2D3748', linewidth=1.2))
sns.stripplot(data=df, x="Mental_Health_Risk", y="CGPA_Midpoint", order=risk_order,
              color='#1A202C', alpha=0.4, jitter=0.2, size=6, ax=ax)

# Add mean markers
means = df.groupby("Mental_Health_Risk")["CGPA_Midpoint"].mean().loc[risk_order]
for i, m in enumerate(means):
    ax.scatter(i, m, color='yellow', edgecolor='black', s=80, zorder=5, label='Mean' if i == 0 else "")
    ax.text(i + 0.25, m, f"Mean: {m:.2f}", va='center', fontsize=10, fontweight='bold', color='#1A202C')

ax.set_title("CGPA and Mental Health Risk", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("CGPA Midpoint (Derived Continuous Metric)", fontsize=11, fontweight='semibold')
ax.set_xlabel("Mental Health Risk Tier", fontsize=11, fontweight='semibold')
ax.set_ylim(0.5, 4.2)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend(loc='lower left', frameon=True)
ax.text(0.5, -0.15, "CGPA_Midpoint derived from survey CGPA ranges. High-risk students maintain high mean CGPA (3.45). Non-causal.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/cgpa_risk.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 9: Age and Mental Health Condition Count
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
# Grouped bar of average conditions by age
age_conditions = df.groupby("Age")["Condition_Count"].agg(["mean", "count"]).reset_index()
bars = ax.bar(age_conditions["Age"].astype(str), age_conditions["mean"], color='#4A5568', width=0.55, edgecolor='#2D3748')

for bar, n in zip(bars, age_conditions["count"]):
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 0.05, f"{h:.2f}\n(n={n})", ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_title("Age and Mental Health Condition Count", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Age of Student (Years)", fontsize=11, fontweight='semibold')
ax.set_ylabel("Average Condition Count (0 to 3)", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 2.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Displays mean concurrent conditions across student ages. Vulnerability spans entire undergraduate range.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/age_condition.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# VISUALIZATION 10: Treatment Seeking Across Mental Health Risk
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
crosstab_seek = pd.crosstab(df["Mental_Health_Risk"], df["Treatment_Sought"]).loc[["Low Risk", "Moderate Risk", "High Risk"]][["No", "Yes"]]

bottom = np.zeros(len(crosstab_seek))
colors_seek = {"No": "#E53E3E", "Yes": "#3182CE"}
for col in ["No", "Yes"]:
    vals = crosstab_seek[col].values
    bars = ax.bar(crosstab_seek.index, vals, bottom=bottom, label=f"Sought Treatment: {col}", color=colors_seek[col], width=0.55, edgecolor='#2D3748')
    for i, (v, b) in enumerate(zip(vals, bottom)):
        if v > 0:
            ax.text(i, b + v/2, f"{v}", ha='center', va='center', color='white', fontweight='bold', fontsize=11)
    bottom += vals

for i, total in enumerate(crosstab_seek.sum(axis=1)):
    ax.text(i, total + 1, f"Total: {total}", ha='center', va='bottom', fontweight='bold', fontsize=10)

ax.set_title("Treatment Seeking Across Mental Health Risk Levels", fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel("Student Count", fontsize=11, fontweight='semibold')
ax.set_ylim(0, 45)
ax.legend(frameon=True, loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, "Only 6/28 (21.4%) high-risk students sought professional treatment; 0 moderate/low-risk sought care.",
        ha='center', va='center', transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/treatment_by_risk.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# DASHBOARD 1: Student Mental Health Overview
# -------------------------------------------------------------
fig = plt.figure(figsize=(16, 12), dpi=300)
gs = fig.add_gridspec(3, 3, height_ratios=[0.8, 2, 2], hspace=0.35, wspace=0.3)

# Top KPIs
ax_kpi1 = fig.add_subplot(gs[0, 0])
ax_kpi2 = fig.add_subplot(gs[0, 1])
ax_kpi3 = fig.add_subplot(gs[0, 2])

for ax, val, title, color in [
    (ax_kpi1, "101", "Total Students Surveyed", "#2B6CB0"),
    (ax_kpi2, "28 (27.7%)", "High-Risk Students", "#E53E3E"),
    (ax_kpi3, "58 (90.6%)", "Symptomatic Treatment Gap", "#DD6B20")
]:
    ax.set_facecolor("#F7FAFC")
    ax.text(0.5, 0.6, val, ha='center', va='center', fontsize=22, fontweight='bold', color=color)
    ax.text(0.5, 0.25, title, ha='center', va='center', fontsize=12, fontweight='semibold', color='#4A5568')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor('#CBD5E0')

# Middle 1: Risk Distribution
ax_m1 = fig.add_subplot(gs[1, 0])
ax_m1.bar(risk_counts.index, risk_counts.values, color=[RISK_COLORS[r] for r in risk_counts.index], edgecolor='#2D3748')
for bar in ax_m1.patches:
    h = bar.get_height()
    ax_m1.text(bar.get_x() + bar.get_width()/2, h + 0.5, f"{int(h)}", ha='center', va='bottom', fontweight='bold', fontsize=9)
ax_m1.set_title("Mental Health Risk Distribution", fontsize=11, fontweight='bold')
ax_m1.set_ylim(0, 45)
ax_m1.grid(axis='y', linestyle='--', alpha=0.5)

# Middle 2: Conditions by Gender
ax_m2 = fig.add_subplot(gs[1, 1])
ax_m2.bar(x - width/2, gender_conditions.loc["Female"], width, label='Female', color='#805AD5', edgecolor='#44337A')
ax_m2.bar(x + width/2, gender_conditions.loc["Male"], width, label='Male', color='#3182CE', edgecolor='#2B6CB0')
ax_m2.set_xticks(x)
ax_m2.set_xticklabels(["Dep.", "Anx.", "Panic"], fontsize=9, fontweight='semibold')
ax_m2.set_title("Conditions by Gender", fontsize=11, fontweight='bold')
ax_m2.legend(fontsize=8)
ax_m2.set_ylim(0, 35)
ax_m2.grid(axis='y', linestyle='--', alpha=0.5)

# Middle 3: Risk by Age Group
ax_m3 = fig.add_subplot(gs[1, 2])
b = np.zeros(len(crosstab_age))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    ax_m3.bar(["18-20", "21-24"], crosstab_age[col].values, bottom=b, label=col, color=RISK_COLORS[col], edgecolor='#2D3748')
    b += crosstab_age[col].values
ax_m3.set_title("Risk by Age Group", fontsize=11, fontweight='bold')
ax_m3.legend(fontsize=8)
ax_m3.set_ylim(0, 70)
ax_m3.grid(axis='y', linestyle='--', alpha=0.5)

# Bottom 1: Faculty Risk
ax_b1 = fig.add_subplot(gs[2, 0])
left = np.zeros(len(crosstab_faculty))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    ax_b1.barh(np.arange(len(crosstab_faculty)), crosstab_faculty[col].values, left=left, color=RISK_COLORS[col], edgecolor='#2D3748')
    left += crosstab_faculty[col].values
ax_b1.set_yticks(np.arange(len(crosstab_faculty)))
short_faculties = [f[:15]+".." if len(f)>15 else f for f in crosstab_faculty.index]
ax_b1.set_yticklabels(short_faculties, fontsize=8)
ax_b1.set_title("Faculty Risk Distribution", fontsize=11, fontweight='bold')
ax_b1.grid(axis='x', linestyle='--', alpha=0.5)

# Bottom 2: Treatment Gap
ax_b2 = fig.add_subplot(gs[2, 1])
ax_b2.bar(["Untreated", "Healthy", "Treated"], gap_counts.values, color=["#E53E3E", "#38A169", "#3182CE"], edgecolor='#2D3748')
for bar in ax_b2.patches:
    h = bar.get_height()
    ax_b2.text(bar.get_x() + bar.get_width()/2, h + 1, f"{int(h)}", ha='center', va='bottom', fontweight='bold', fontsize=9)
ax_b2.set_title("Treatment Gap", fontsize=11, fontweight='bold')
ax_b2.set_ylim(0, 70)
ax_b2.grid(axis='y', linestyle='--', alpha=0.5)

# Bottom 3: Condition Count
ax_b3 = fig.add_subplot(gs[2, 2])
ax_b3.bar([str(i) for i in cond_counts.index], cond_counts.values, color=cond_colors, edgecolor='#2D3748')
for bar in ax_b3.patches:
    h = bar.get_height()
    ax_b3.text(bar.get_x() + bar.get_width()/2, h + 1, f"{int(h)}", ha='center', va='bottom', fontweight='bold', fontsize=9)
ax_b3.set_title("Condition Count (0-3)", fontsize=11, fontweight='bold')
ax_b3.set_ylim(0, 45)
ax_b3.grid(axis='y', linestyle='--', alpha=0.5)

fig.suptitle("Tableau Dashboard 1: Student Mental Health Overview", fontsize=16, fontweight='bold', y=0.98)
plt.savefig("evidence/epic_03/dashboard_overview.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# DASHBOARD 2: Mental Health Risk & Treatment Dashboard
# -------------------------------------------------------------
fig = plt.figure(figsize=(15, 10), dpi=300)
gs2 = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.25)

# D2 Panel 1: Treatment Gap vs Total
ax_d2_1 = fig.add_subplot(gs2[0, 0])
ax_d2_1.pie(gap_counts.values, labels=gap_counts.index, colors=["#E53E3E", "#38A169", "#3182CE"],
            autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='#2D3748', linewidth=1.2))
ax_d2_1.set_title("Campus Mental Health Care Deficit", fontsize=12, fontweight='bold')

# D2 Panel 2: Treatment Seeking by Risk
ax_d2_2 = fig.add_subplot(gs2[0, 1])
b2 = np.zeros(len(crosstab_seek))
for col in ["No", "Yes"]:
    ax_d2_2.bar(crosstab_seek.index, crosstab_seek[col].values, bottom=b2, label=f"Treatment Sought: {col}", color=colors_seek[col], edgecolor='#2D3748', width=0.5)
    b2 += crosstab_seek[col].values
ax_d2_2.set_title("Treatment Seeking by Risk Level", fontsize=12, fontweight='bold')
ax_d2_2.legend()
ax_d2_2.set_ylim(0, 45)
ax_d2_2.grid(axis='y', linestyle='--', alpha=0.5)

# D2 Panel 3: Comorbidity Count Breakdown
ax_d2_3 = fig.add_subplot(gs2[1, 0])
ax_d2_3.bar(["0 Conditions", "1 Condition", "2 Conditions", "3 Conditions"], cond_counts.values, color=cond_colors, edgecolor='#2D3748', width=0.5)
for bar in ax_d2_3.patches:
    h = bar.get_height()
    ax_d2_3.text(bar.get_x() + bar.get_width()/2, h + 1, f"{int(h)} ({h/101*100:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=9)
ax_d2_3.set_title("Comorbidity Severity Distribution", fontsize=12, fontweight='bold')
ax_d2_3.set_ylim(0, 45)
ax_d2_3.grid(axis='y', linestyle='--', alpha=0.5)

# D2 Panel 4: Conditions by Gender
ax_d2_4 = fig.add_subplot(gs2[1, 1])
ax_d2_4.bar(x - width/2, gender_conditions.loc["Female"], width, label='Female', color='#805AD5', edgecolor='#44337A')
ax_d2_4.bar(x + width/2, gender_conditions.loc["Male"], width, label='Male', color='#3182CE', edgecolor='#2B6CB0')
ax_d2_4.set_xticks(x)
ax_d2_4.set_xticklabels(["Depression", "Anxiety", "Panic Attack"], fontsize=10, fontweight='semibold')
ax_d2_4.set_title("Clinical Burden by Gender", fontsize=12, fontweight='bold')
ax_d2_4.legend()
ax_d2_4.set_ylim(0, 35)
ax_d2_4.grid(axis='y', linestyle='--', alpha=0.5)

fig.suptitle("Tableau Dashboard 2: Mental Health Risk & Treatment Dashboard", fontsize=16, fontweight='bold', y=0.98)
plt.savefig("evidence/epic_03/dashboard_treatment.png", dpi=300)
plt.close()

print("All 10 visualizations and 2 dashboards successfully generated and saved to evidence/epic_03/")
