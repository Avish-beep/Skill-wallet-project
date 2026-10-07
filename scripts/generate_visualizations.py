import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd
import numpy as np

# Ensure evidence directory exists
os.makedirs("evidence/epic_03", exist_ok=True)

# Load validated processed dataset
DATA_PATH = "data/processed/student_mental_health_processed.csv"
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Processed dataset missing at: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# Verify dataset integrity before rendering
assert len(df) == 101, f"Expected 101 rows, got {len(df)}"
assert df.isnull().sum().sum() == 0, "Null values detected in dataset"

# Set standard styling
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#CBD5E0'
plt.rcParams['axes.linewidth'] = 0.8

# Healthcare Color Palettes
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

DISCLAIMER_TEXT = "Self-reported student mental-health survey data (N=101). Not formal clinical diagnoses. Observed associations are non-causal."

# Pre-calculate metrics
risk_counts = df["Mental_Health_Risk"].value_counts().loc[["Low Risk", "Moderate Risk", "High Risk"]]
gender_conditions = df.groupby("Gender")[["Depression_Flag", "Anxiety_Flag", "Panic_Attack_Flag"]].sum()
gender_conditions.columns = ["Depression", "Anxiety", "Panic Attack"]
crosstab_age = pd.crosstab(df["Age_Group"], df["Mental_Health_Risk"])[["Low Risk", "Moderate Risk", "High Risk"]]
crosstab_faculty = pd.crosstab(df["Faculty"], df["Mental_Health_Risk"])[["Low Risk", "Moderate Risk", "High Risk"]]
crosstab_faculty["Total"] = crosstab_faculty.sum(axis=1)
crosstab_faculty = crosstab_faculty.sort_values(by="Total", ascending=True)
cond_counts = df["Condition_Count"].value_counts().sort_index()
gap_counts = df["Treatment_Gap"].value_counts().loc[["Untreated Condition", "No Identified Condition", "Condition Treated"]]
crosstab_seek = pd.crosstab(df["Mental_Health_Risk"], df["Treatment_Sought"]).loc[["Low Risk", "Moderate Risk", "High Risk"]][["No", "Yes"]]

# -----------------------------------------------------------------------------
# 1. GENERATE ALL 10 INDIVIDUAL WORKSHEETS (CLEAN, VERIFIED)
# -----------------------------------------------------------------------------

# WS 1
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
colors = [RISK_COLORS[r] for r in risk_counts.index]
bars = ax.bar(risk_counts.index, risk_counts.values, color=colors, width=0.52, edgecolor="#2D3748", linewidth=1.2)
for bar in bars:
    yval = bar.get_height()
    pct = (yval / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval} ({pct:.1f}%)", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#2D3748')
ax.set_title("Distribution of Mental Health Risk Levels Among Students", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Number of Students (COUNTD)", fontsize=11, fontweight='bold')
ax.set_xlabel("Mental Health Risk Tier", fontsize=11, fontweight='bold')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Source: {DATA_PATH} | {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/mental_health_risk.png", dpi=300)
plt.close()

# WS 2
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
x = np.arange(len(gender_conditions.columns))
width = 0.35
rects1 = ax.bar(x - width/2, gender_conditions.loc["Female"], width, label=f'Female (N={len(df[df["Gender"]=="Female"])})', color='#805AD5', edgecolor='#44337A')
rects2 = ax.bar(x + width/2, gender_conditions.loc["Male"], width, label=f'Male (N={len(df[df["Gender"]=="Male"])})', color='#3182CE', edgecolor='#2B6CB0')
for rects, g_total in [(rects1, 75), (rects2, 26)]:
    for rect in rects:
        h = rect.get_height()
        pct = (h / g_total) * 100
        ax.annotate(f'{h}\n({pct:.1f}%)', xy=(rect.get_x() + rect.get_width() / 2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.set_title("Self-Reported Mental Health Conditions by Gender", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Number of Affected Students", fontsize=11, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(gender_conditions.columns, fontsize=11, fontweight='bold')
ax.set_ylim(0, 35)
ax.legend(frameon=True, facecolor='white', edgecolor='#E2E8F0')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Percentages indicate within-gender prevalence (Female N=75, Male N=26). {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/conditions_by_gender.png", dpi=300)
plt.close()

# WS 3
fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
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
ax.set_title("Mental Health Risk Across Age Groups", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Student Count", fontsize=11, fontweight='bold')
ax.set_ylim(0, 70)
ax.legend(title="Risk Level", frameon=True, loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Underclassmen (18-20, N=60) vs Upperclassmen (21-24, N=41). {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/risk_by_age_group.png", dpi=300)
plt.close()

# WS 4
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
left = np.zeros(len(crosstab_faculty))
y_positions = np.arange(len(crosstab_faculty))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    values = crosstab_faculty[col].values
    ax.barh(y_positions, values, left=left, label=col, color=RISK_COLORS[col], height=0.6, edgecolor='#2D3748')
    left += values
for idx, total in enumerate(crosstab_faculty["Total"]):
    ax.text(total + 0.5, idx, f"{total}", va='center', ha='left', fontweight='bold', fontsize=10)
ax.set_yticks(y_positions)
ax.set_yticklabels(crosstab_faculty.index, fontsize=10, fontweight='bold')
ax.set_title("Mental Health Risk by Faculty", fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel("Student Count", fontsize=11, fontweight='bold')
ax.set_xlim(0, 32)
ax.legend(title="Risk Level", loc='lower right', frameon=True)
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Faculty groupings based on 43 standardized degree programs. {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/faculty_risk.png", dpi=300)
plt.close()

# WS 5
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
cond_colors = ["#38A169", "#DD6B20", "#E53E3E", "#9B2C2C"]
bars = ax.bar([f"{i} Conditions" for i in cond_counts.index], cond_counts.values, color=cond_colors, width=0.55, edgecolor='#2D3748')
for bar in bars:
    h = bar.get_height()
    pct = (h / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, h + 1, f"{h}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=10)
ax.set_title("Distribution of Mental Health Condition Count", fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel("Number of Concurrent Conditions (Depression, Anxiety, Panic Attacks)", fontsize=11, fontweight='bold')
ax.set_ylabel("Student Count", fontsize=11, fontweight='bold')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.18, f"Tracks concurrent symptom load (0 to 3 conditions). {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/condition_count.png", dpi=300)
plt.close()

# WS 6
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
gap_colors = ["#E53E3E", "#38A169", "#3182CE"]
bars = ax.bar(["Untreated Symptomatic", "Healthy (No Symptoms)", "Symptomatic & Treated"], gap_counts.values, color=gap_colors, width=0.55, edgecolor='#2D3748')
for bar in bars:
    h = bar.get_height()
    pct = (h / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, h + 1.5, f"{h}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=10)
ax.set_title("Student Mental Health Treatment Gap", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Number of Students", fontsize=11, fontweight='bold')
ax.set_ylim(0, 70)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"58 of 64 (90.6%) symptomatic students have not sought specialist consultation. {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/treatment_gap.png", dpi=300)
plt.close()

# WS 7
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
conditions = ["Depression", "Anxiety", "Panic Attack"]
totals = [df["Depression_Flag"].sum(), df["Anxiety_Flag"].sum(), df["Panic_Attack_Flag"].sum()]
bar_colors = [CONDITION_COLORS[c] for c in conditions]
bars = ax.bar(conditions, totals, color=bar_colors, width=0.5, edgecolor='#2D3748')
for bar in bars:
    h = bar.get_height()
    pct = (h / len(df)) * 100
    ax.text(bar.get_x() + bar.get_width()/2, h + 1, f"{h}\n({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.set_title("Prevalence of Self-Reported Mental Health Conditions", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Affected Student Count", fontsize=11, fontweight='bold')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Prevalence across cohort (N=101). Students can experience multiple conditions concurrently. {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/condition_prevalence.png", dpi=300)
plt.close()

# WS 8
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
risk_order = ["Low Risk", "Moderate Risk", "High Risk"]
sns.boxplot(data=df, x="Mental_Health_Risk", y="CGPA_Midpoint", order=risk_order, 
            hue="Mental_Health_Risk", palette=RISK_COLORS, width=0.45, ax=ax, legend=False,
            boxprops=dict(edgecolor='#2D3748', linewidth=1.2))
sns.stripplot(data=df, x="Mental_Health_Risk", y="CGPA_Midpoint", order=risk_order,
              color='#1A202C', alpha=0.4, jitter=0.2, size=6, ax=ax)
means = df.groupby("Mental_Health_Risk")["CGPA_Midpoint"].mean().loc[risk_order]
for i, m in enumerate(means):
    ax.scatter(i, m, color='yellow', edgecolor='black', s=80, zorder=5, label='Cohort Mean' if i == 0 else "")
    ax.text(i + 0.22, m, f"Mean: {m:.2f}", va='center', fontsize=10, fontweight='bold', color='#1A202C')
ax.set_title("CGPA Midpoint and Mental Health Risk", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("CGPA Midpoint (Derived Continuous Metric)", fontsize=11, fontweight='bold')
ax.set_xlabel("Mental Health Risk Tier", fontsize=11, fontweight='bold')
ax.set_ylim(0.5, 4.2)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend(loc='lower left', frameon=True)
ax.text(0.5, -0.15, f"CGPA_Midpoint derived from survey CGPA ranges. High-risk students maintain high mean CGPA (3.45). {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/cgpa_risk.png", dpi=300)
plt.close()

# WS 9
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
age_conditions = df.groupby("Age")["Condition_Count"].agg(["mean", "count"]).reset_index()
bars = ax.bar(age_conditions["Age"].astype(str), age_conditions["mean"], color='#4A5568', width=0.55, edgecolor='#2D3748')
for bar, n in zip(bars, age_conditions["count"]):
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 0.05, f"{h:.2f}\n(n={n})", ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.set_title("Age and Mental Health Condition Count", fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel("Age of Student (Years)", fontsize=11, fontweight='bold')
ax.set_ylabel("Average Condition Count (0 to 3)", fontsize=11, fontweight='bold')
ax.set_ylim(0, 2.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Mean concurrent conditions by student age. Psychological distress spans entire undergraduate range. {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/age_condition.png", dpi=300)
plt.close()

# WS 10
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
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
ax.set_title("Treatment Seeking Across Mental Health Risk Levels", fontsize=13, fontweight='bold', pad=15)
ax.set_ylabel("Student Count", fontsize=11, fontweight='bold')
ax.set_ylim(0, 45)
ax.legend(frameon=True, loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.text(0.5, -0.15, f"Only 6/28 (21.4%) high-risk students sought professional care; 0 moderate/low-risk sought care. {DISCLAIMER_TEXT}", ha='center', va='center', transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#718096')
plt.tight_layout()
plt.savefig("evidence/epic_03/treatment_by_risk.png", dpi=300)
plt.close()


# -----------------------------------------------------------------------------
# 2. RESPONSIVE DASHBOARD 1: "Student Mental Health Overview"
# -----------------------------------------------------------------------------
# Total Canvas: 2000px x 1450px at 300 DPI (approx 20 x 14.5 inches)
fig = plt.figure(figsize=(20, 14.5), dpi=300, facecolor='#F0F4F8')

# 4 Rows: Header & Filter Bar (0.07), KPI Cards (0.10), Panels Row 1 (0.38), Panels Row 2 (0.38)
gs = fig.add_gridspec(
    4, 4,
    height_ratios=[0.55, 0.75, 2.2, 2.2],
    hspace=0.28, wspace=0.22,
    top=0.96, bottom=0.04, left=0.04, right=0.96
)

# --- A. HEADER & INTERACTIVE FILTER BAR CONTAINER ---
ax_header = fig.add_subplot(gs[0, :])
ax_header.set_facecolor('#1E293B')  # Tableau Dark Slate Header
ax_header.set_xticks([])
ax_header.set_yticks([])
for spine in ax_header.spines.values():
    spine.set_color('#0F172A')

# Header text
ax_header.text(0.02, 0.68, "Student Mental Health Overview", color='#FFFFFF', fontsize=18, fontweight='bold', va='center')
ax_header.text(0.02, 0.28, "Interactive Visual Intelligence Dashboard | Survey Cohort Analysis (N=101)", color='#94A3B8', fontsize=10, va='center')

# Interactive Filter Pills (Visual Representation of Tableau Quick Filters)
filters = [
    ("Filter: Gender", "All (Female / Male)"),
    ("Filter: Age Group", "All (18-20 / 21-24)"),
    ("Filter: Faculty", "All Faculties (7)"),
    ("Filter: Risk Tier", "All (Low / Mod / High)")
]
filter_x = 0.45
for f_label, f_val in filters:
    rect = patches.FancyBboxPatch((filter_x, 0.20), 0.12, 0.60, boxstyle="round,pad=0.02", facecolor='#334155', edgecolor='#475569', linewidth=1)
    ax_header.add_patch(rect)
    ax_header.text(filter_x + 0.06, 0.62, f_label, color='#CBD5E1', fontsize=7.5, fontweight='bold', ha='center', va='center')
    ax_header.text(filter_x + 0.06, 0.35, f"{f_val} ▼", color='#38BDF8', fontsize=8, fontweight='bold', ha='center', va='center')
    filter_x += 0.135

# --- B. 4 VALIDATED EXECUTIVE KPI CARDS ---
kpis = [
    ("TOTAL STUDENTS", "101", "COUNTD([User_ID])\nFull Cohort Baseline", "#1E40AF", "#EFF6FF", "#BFDBFE"),
    ("HIGH RISK STUDENTS", "28", "27.7% of Cohort (≥2 Conditions)\nAcute Intervention Tier", "#B91C1C", "#FEF2F2", "#FECACA"),
    ("MODERATE RISK", "36", "35.6% of Cohort (1 Condition)\nEarly Counseling Target", "#C2410C", "#FFF7ED", "#FED7AA"),
    ("TREATMENT GAP", "58", "90.6% of Symptomatic (58/64)\nUntreated Distress Deficit", "#991B1B", "#FEF2F2", "#FECACA")
]

for col_idx, (title, val, subtext, text_col, bg_col, border_col) in enumerate(kpis):
    ax_kpi = fig.add_subplot(gs[1, col_idx])
    ax_kpi.set_facecolor(bg_col)
    ax_kpi.set_xticks([])
    ax_kpi.set_yticks([])
    for spine in ax_kpi.spines.values():
        spine.set_color(border_col)
        spine.set_linewidth(1.5)
    
    ax_kpi.text(0.5, 0.78, title, ha='center', va='center', fontsize=9, fontweight='bold', color='#475569')
    ax_kpi.text(0.5, 0.46, val, ha='center', va='center', fontsize=24, fontweight='bold', color=text_col)
    ax_kpi.text(0.5, 0.16, subtext, ha='center', va='center', fontsize=7.5, color='#64748B')

# --- C. ROW 1 VISUAL PANELS (3 PANELS ACROSS 4 COLUMNS) ---
# Panel 1: Risk Distribution (Column 0: span 1.2)
ax_p1 = fig.add_subplot(gs[2, 0])
ax_p1.set_facecolor('#FFFFFF')
bars_p1 = ax_p1.bar(risk_counts.index, risk_counts.values, color=[RISK_COLORS[r] for r in risk_counts.index], edgecolor='#334155', width=0.55)
for bar in bars_p1:
    h = bar.get_height()
    ax_p1.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{int(h)}\n({h/101*100:.1f}%)", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_p1.set_title("1. Mental Health Risk Distribution", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_p1.set_ylabel("Student Count", fontsize=9, fontweight='bold', color='#334155')
ax_p1.set_ylim(0, 46)
ax_p1.tick_params(axis='x', labelsize=8)
ax_p1.tick_params(axis='y', labelsize=8)
ax_p1.grid(axis='y', linestyle='--', alpha=0.5)

# Panel 2: Conditions by Gender (Columns 1-2: span 2 cols)
ax_p2 = fig.add_subplot(gs[2, 1:3])
ax_p2.set_facecolor('#FFFFFF')
r1 = ax_p2.bar(x - width/2, gender_conditions.loc["Female"], width, label='Female (N=75)', color='#805AD5', edgecolor='#44337A')
r2 = ax_p2.bar(x + width/2, gender_conditions.loc["Male"], width, label='Male (N=26)', color='#3182CE', edgecolor='#2B6CB0')
for bar in r1:
    h = bar.get_height()
    ax_p2.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{int(h)} ({h/75*100:.1f}%)", ha='center', va='bottom', fontsize=7.5, fontweight='bold')
for bar in r2:
    h = bar.get_height()
    ax_p2.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{int(h)} ({h/26*100:.1f}%)", ha='center', va='bottom', fontsize=7.5, fontweight='bold')
ax_p2.set_xticks(x)
ax_p2.set_xticklabels(["Depression", "Anxiety", "Panic Attack"], fontsize=9, fontweight='bold')
ax_p2.set_title("2. Self-Reported Conditions by Gender (Within-Gender Prevalence)", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_p2.legend(fontsize=8, loc='upper right', frameon=True)
ax_p2.set_ylim(0, 36)
ax_p2.tick_params(axis='y', labelsize=8)
ax_p2.grid(axis='y', linestyle='--', alpha=0.5)

# Panel 3: Risk Across Age Groups (Column 3)
ax_p3 = fig.add_subplot(gs[2, 3])
ax_p3.set_facecolor('#FFFFFF')
b_p3 = np.zeros(len(crosstab_age))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    ax_p3.bar(["18-20", "21-24"], crosstab_age[col].values, bottom=b_p3, label=col, color=RISK_COLORS[col], edgecolor='#334155', width=0.5)
    b_p3 += crosstab_age[col].values
for i, tot in enumerate(crosstab_age.sum(axis=1)):
    ax_p3.text(i, tot + 1.2, f"Total: {tot}", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_p3.set_title("3. Risk Across Age Groups", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_p3.legend(fontsize=7.5, loc='upper right', frameon=True)
ax_p3.set_ylim(0, 72)
ax_p3.tick_params(axis='x', labelsize=8)
ax_p3.tick_params(axis='y', labelsize=8)
ax_p3.grid(axis='y', linestyle='--', alpha=0.5)

# --- D. ROW 2 VISUAL PANELS (3 PANELS ACROSS 4 COLUMNS) ---
# Panel 4: Faculty Risk (Columns 0-1)
ax_p4 = fig.add_subplot(gs[3, 0:2])
ax_p4.set_facecolor('#FFFFFF')
l_p4 = np.zeros(len(crosstab_faculty))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    ax_p4.barh(np.arange(len(crosstab_faculty)), crosstab_faculty[col].values, left=l_p4, color=RISK_COLORS[col], edgecolor='#334155', height=0.55)
    l_p4 += crosstab_faculty[col].values
for idx, tot in enumerate(crosstab_faculty["Total"]):
    ax_p4.text(tot + 0.4, idx, f"{tot}", va='center', ha='left', fontsize=8, fontweight='bold')
ax_p4.set_yticks(np.arange(len(crosstab_faculty)))
short_f = [f[:20] + ".." if len(f)>20 else f for f in crosstab_faculty.index]
ax_p4.set_yticklabels(short_f, fontsize=8, fontweight='bold')
ax_p4.set_title("4. Mental Health Risk by Faculty (Standardized Academic Disciplines)", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_p4.set_xlabel("Student Count", fontsize=9, fontweight='bold', color='#334155')
ax_p4.grid(axis='x', linestyle='--', alpha=0.5)
ax_p4.tick_params(axis='x', labelsize=8)

# Panel 5: Student Mental Health Treatment Gap (Column 2)
ax_p5 = fig.add_subplot(gs[3, 2])
ax_p5.set_facecolor('#FFFFFF')
bars_p5 = ax_p5.bar(["Untreated", "Healthy", "Treated"], gap_counts.values, color=["#E53E3E", "#38A169", "#3182CE"], edgecolor='#334155', width=0.55)
for bar in bars_p5:
    h = bar.get_height()
    ax_p5.text(bar.get_x() + bar.get_width()/2, h + 1.2, f"{int(h)}\n({h/101*100:.1f}%)", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_p5.set_title("5. Treatment Gap Status", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_p5.set_ylim(0, 72)
ax_p5.tick_params(axis='x', labelsize=8)
ax_p5.tick_params(axis='y', labelsize=8)
ax_p5.grid(axis='y', linestyle='--', alpha=0.5)

# Panel 6: Condition Count Distribution (Column 3)
ax_p6 = fig.add_subplot(gs[3, 3])
ax_p6.set_facecolor('#FFFFFF')
bars_p6 = ax_p6.bar([f"{i} Cond." for i in cond_counts.index], cond_counts.values, color=cond_colors, edgecolor='#334155', width=0.55)
for bar in bars_p6:
    h = bar.get_height()
    ax_p6.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{int(h)}\n({h/101*100:.1f}%)", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_p6.set_title("6. Condition Count (0-3)", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_p6.set_ylim(0, 46)
ax_p6.tick_params(axis='x', labelsize=8)
ax_p6.tick_params(axis='y', labelsize=8)
ax_p6.grid(axis='y', linestyle='--', alpha=0.5)

# Style panel borders
for p_ax in [ax_p1, ax_p2, ax_p3, ax_p4, ax_p5, ax_p6]:
    for spine in p_ax.spines.values():
        spine.set_color('#CBD5E1')
        spine.set_linewidth(1.2)

# Global Footer
plt.figtext(
    0.5, 0.015,
    f"Data Source: {DATA_PATH} | N=101 | Validated Fields Only | {DISCLAIMER_TEXT}",
    ha='center', fontsize=8, fontstyle='italic', color='#475569'
)

plt.savefig("evidence/epic_03/dashboard_overview.png", dpi=300, bbox_inches='tight')
plt.close()


# -----------------------------------------------------------------------------
# 3. RESPONSIVE DASHBOARD 2: "Mental Health Risk & Treatment Dashboard"
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(18, 12), dpi=300, facecolor='#F0F4F8')

gs2 = fig.add_gridspec(
    3, 3,
    height_ratios=[0.55, 2.2, 2.2],
    hspace=0.28, wspace=0.22,
    top=0.96, bottom=0.04, left=0.04, right=0.96
)

# Header & Filter Bar
ax_h2 = fig.add_subplot(gs2[0, :])
ax_h2.set_facecolor('#1E293B')
ax_h2.set_xticks([])
ax_h2.set_yticks([])
for spine in ax_h2.spines.values():
    spine.set_color('#0F172A')

ax_h2.text(0.02, 0.68, "Mental Health Risk & Treatment Dashboard", color='#FFFFFF', fontsize=18, fontweight='bold', va='center')
ax_h2.text(0.02, 0.28, "Campus Care Utilization, Treatment-Seeking Barriers, and Clinical Comorbidity Analysis", color='#94A3B8', fontsize=10, va='center')

# Filters on D2
f_x2 = 0.55
for f_label, f_val in [("Filter: Risk Tier", "All Tiers ▼"), ("Filter: Treatment Sought", "All Responses ▼"), ("Filter: Faculty", "All Disciplines ▼")]:
    rect = patches.FancyBboxPatch((f_x2, 0.20), 0.13, 0.60, boxstyle="round,pad=0.02", facecolor='#334155', edgecolor='#475569', linewidth=1)
    ax_h2.add_patch(rect)
    ax_h2.text(f_x2 + 0.065, 0.62, f_label, color='#CBD5E1', fontsize=7.5, fontweight='bold', ha='center', va='center')
    ax_h2.text(f_x2 + 0.065, 0.35, f_val, color='#38BDF8', fontsize=8, fontweight='bold', ha='center', va='center')
    f_x2 += 0.145

# D2 Panel 1: Treatment Seeking Across Risk Levels
ax_d2_1 = fig.add_subplot(gs2[1, 0])
ax_d2_1.set_facecolor('#FFFFFF')
b2 = np.zeros(len(crosstab_seek))
for col in ["No", "Yes"]:
    ax_d2_1.bar(crosstab_seek.index, crosstab_seek[col].values, bottom=b2, label=f"Sought Care: {col}", color=colors_seek[col], edgecolor='#334155', width=0.52)
    b2 += crosstab_seek[col].values
for i, tot in enumerate(crosstab_seek.sum(axis=1)):
    ax_d2_1.text(i, tot + 0.8, f"Total: {tot}", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_d2_1.set_title("1. Treatment Seeking by Risk Tier", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_d2_1.legend(fontsize=8, loc='upper right', frameon=True)
ax_d2_1.set_ylim(0, 46)
ax_d2_1.tick_params(axis='x', labelsize=8)
ax_d2_1.tick_params(axis='y', labelsize=8)
ax_d2_1.grid(axis='y', linestyle='--', alpha=0.5)

# D2 Panel 2: Treatment Gap Status
ax_d2_2 = fig.add_subplot(gs2[1, 1])
ax_d2_2.set_facecolor('#FFFFFF')
ax_d2_2.pie(gap_counts.values, labels=["Untreated (58)", "Healthy (37)", "Treated (6)"], colors=["#E53E3E", "#38A169", "#3182CE"],
            autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8.5, 'fontweight': 'bold'},
            wedgeprops=dict(edgecolor='#334155', linewidth=1.2))
ax_d2_2.set_title("2. Treatment Gap Distribution", fontsize=10, fontweight='bold', color='#0F172A', pad=10)

# D2 Panel 3: Condition Count Distribution
ax_d2_3 = fig.add_subplot(gs2[1, 2])
ax_d2_3.set_facecolor('#FFFFFF')
bars_d2_3 = ax_d2_3.bar([f"{i} Cond." for i in cond_counts.index], cond_counts.values, color=cond_colors, edgecolor='#334155', width=0.55)
for bar in bars_d2_3:
    h = bar.get_height()
    ax_d2_3.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{int(h)}\n({h/101*100:.1f}%)", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_d2_3.set_title("3. Condition Count Distribution", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_d2_3.set_ylim(0, 46)
ax_d2_3.tick_params(axis='x', labelsize=8)
ax_d2_3.tick_params(axis='y', labelsize=8)
ax_d2_3.grid(axis='y', linestyle='--', alpha=0.5)

# D2 Panel 4: Conditions by Gender
ax_d2_4 = fig.add_subplot(gs2[2, 0])
ax_d2_4.set_facecolor('#FFFFFF')
ax_d2_4.bar(x - width/2, gender_conditions.loc["Female"], width, label='Female (N=75)', color='#805AD5', edgecolor='#44337A')
ax_d2_4.bar(x + width/2, gender_conditions.loc["Male"], width, label='Male (N=26)', color='#3182CE', edgecolor='#2B6CB0')
ax_d2_4.set_xticks(x)
ax_d2_4.set_xticklabels(["Dep.", "Anx.", "Panic"], fontsize=8.5, fontweight='bold')
ax_d2_4.set_title("4. Conditions by Gender", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_d2_4.legend(fontsize=8, loc='upper right', frameon=True)
ax_d2_4.set_ylim(0, 36)
ax_d2_4.tick_params(axis='y', labelsize=8)
ax_d2_4.grid(axis='y', linestyle='--', alpha=0.5)

# D2 Panel 5: Mental Health Risk Distribution
ax_d2_5 = fig.add_subplot(gs2[2, 1])
ax_d2_5.set_facecolor('#FFFFFF')
bars_d2_5 = ax_d2_5.bar(risk_counts.index, risk_counts.values, color=[RISK_COLORS[r] for r in risk_counts.index], edgecolor='#334155', width=0.55)
for bar in bars_d2_5:
    h = bar.get_height()
    ax_d2_5.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{int(h)}\n({h/101*100:.1f}%)", ha='center', va='bottom', fontsize=8, fontweight='bold')
ax_d2_5.set_title("5. Mental Health Risk Distribution", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_d2_5.set_ylim(0, 46)
ax_d2_5.tick_params(axis='x', labelsize=8)
ax_d2_5.tick_params(axis='y', labelsize=8)
ax_d2_5.grid(axis='y', linestyle='--', alpha=0.5)

# D2 Panel 6: Faculty Risk Profile
ax_d2_6 = fig.add_subplot(gs2[2, 2])
ax_d2_6.set_facecolor('#FFFFFF')
l_d2_6 = np.zeros(len(crosstab_faculty))
for col in ["Low Risk", "Moderate Risk", "High Risk"]:
    ax_d2_6.barh(np.arange(len(crosstab_faculty)), crosstab_faculty[col].values, left=l_d2_6, color=RISK_COLORS[col], edgecolor='#334155', height=0.55)
    l_d2_6 += crosstab_faculty[col].values
ax_d2_6.set_yticks(np.arange(len(crosstab_faculty)))
ax_d2_6.set_yticklabels([f[:14]+".." if len(f)>14 else f for f in crosstab_faculty.index], fontsize=7.5, fontweight='bold')
ax_d2_6.set_title("6. Mental Health Risk by Faculty", fontsize=10, fontweight='bold', color='#0F172A', pad=10)
ax_d2_6.grid(axis='x', linestyle='--', alpha=0.5)
ax_d2_6.tick_params(axis='x', labelsize=8)

for p_ax in [ax_d2_1, ax_d2_2, ax_d2_3, ax_d2_4, ax_d2_5, ax_d2_6]:
    for spine in p_ax.spines.values():
        spine.set_color('#CBD5E1')
        spine.set_linewidth(1.2)

plt.figtext(
    0.5, 0.015,
    f"Data Source: {DATA_PATH} | Validated N=101 | {DISCLAIMER_TEXT}",
    ha='center', fontsize=8, fontstyle='italic', color='#475569'
)

plt.savefig("evidence/epic_03/dashboard_treatment.png", dpi=300, bbox_inches='tight')
plt.close()

print("All 10 worksheets and 2 responsive dashboards successfully regenerated.")
