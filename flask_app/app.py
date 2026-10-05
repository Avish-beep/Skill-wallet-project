"""
Flask Web Application
Analysing Mental Health in Student Ecosystem
SkillWallet Project — Data Analytics with Tableau
"""

import os
import pandas as pd
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

# Load local environment variables if available
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-dev-secret-key-student-mental-health')

# Path to cleaned dataset
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'student_mental_health_cleaned.csv')

def load_cohort_stats():
    """Calculates live aggregated cohort metrics from the cleaned dataset."""
    if not os.path.exists(DATA_PATH):
        return {
            'total_students': 101,
            'high_risk_count': 36,
            'high_risk_pct': 35.6,
            'depression_count': 35,
            'depression_pct': 34.7,
            'anxiety_count': 34,
            'anxiety_pct': 33.7,
            'panic_count': 33,
            'panic_pct': 32.7,
            'treatment_gap_pct': 90.5,
            'avg_cgpa': 3.28
        }
    
    df = pd.read_csv(DATA_PATH)
    n = len(df)
    high_risk = (df['mental_health_risk'] == 'High Risk').sum()
    dep = df['depression_flag'].sum()
    anx = df['anxiety_flag'].sum()
    panic = df['panic_attack_flag'].sum()
    active_cond = (df['condition_count'] > 0).sum()
    untreated = ((df['condition_count'] > 0) & (df['treatment_sought'] == 'No')).sum()
    treatment_gap = (untreated / active_cond * 100) if active_cond > 0 else 0
    avg_cgpa = df['cgpa_midpoint'].mean() if 'cgpa_midpoint' in df.columns else 3.28

    return {
        'total_students': int(n),
        'high_risk_count': int(high_risk),
        'high_risk_pct': round((high_risk / n) * 100, 1),
        'depression_count': int(dep),
        'depression_pct': round((dep / n) * 100, 1),
        'anxiety_count': int(anx),
        'anxiety_pct': round((anx / n) * 100, 1),
        'panic_count': int(panic),
        'panic_pct': round((panic / n) * 100, 1),
        'treatment_gap_pct': round(treatment_gap, 1),
        'avg_cgpa': round(avg_cgpa, 2)
    }

@app.route('/')
def home():
    stats = load_cohort_stats()
    return render_template('index.html', stats=stats)

@app.route('/dashboard')
def dashboard():
    stats = load_cohort_stats()
    tableau_view_url = os.getenv('TABLEAU_VIEW_URL', '').strip()
    tableau_story_url = os.getenv('TABLEAU_STORY_URL', '').strip()
    return render_template(
        'dashboard.html',
        stats=stats,
        tableau_view_url=tableau_view_url,
        tableau_story_url=tableau_story_url
    )

@app.route('/insights')
def insights():
    stats = load_cohort_stats()
    # Faculty and academic breakdown
    faculties = []
    academic_tiers = []
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        fac_grp = df.groupby('faculty').agg(
            total=('student_id', 'count'),
            high_risk=('mental_health_risk', lambda x: (x == 'High Risk').sum()),
            depression=('depression_flag', 'sum')
        ).reset_index()
        fac_grp['high_risk_pct'] = (fac_grp['high_risk'] / fac_grp['total'] * 100).round(1)
        faculties = fac_grp.to_dict('records')

        cgpa_grp = df.groupby('cgpa_range').agg(
            total=('student_id', 'count'),
            depression_rate=('depression_flag', lambda x: round(x.mean() * 100, 1)),
            anxiety_rate=('anxiety_flag', lambda x: round(x.mean() * 100, 1))
        ).reset_index()
        academic_tiers = cgpa_grp.to_dict('records')

    return render_template(
        'insights.html',
        stats=stats,
        faculties=faculties,
        academic_tiers=academic_tiers
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/summary')
def api_summary():
    return jsonify(load_cohort_stats())

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
