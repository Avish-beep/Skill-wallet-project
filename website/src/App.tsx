import { useState } from 'react';
import {
  LayoutDashboard,
  Database,
  FileText,
  ExternalLink,
  CheckCircle,
  AlertCircle,
  BarChart3,
  Activity,
  BookOpen,
  ShieldCheck,
  ChevronRight,
  Menu,
  X,
  Play,
  Download
} from 'lucide-react';

function GithubIcon({ className = "w-4 h-4 mr-1.5" }: { className?: string }) {
  return (
    <svg className={className} fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
      <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
    </svg>
  );
}

const TABLEAU_VIEW_URL = "https://public.tableau.com/views/Student_Mental_Health_Analysis_17913964531250/AnalysingMentalHealthinStudentEcosystem?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link";

export default function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeStoryScene, setActiveStoryScene] = useState(0);

  const BASE_URL = import.meta.env.BASE_URL;

  const storyScenes = [
    {
      title: "1. Problem & Population Context",
      subtitle: "N = 101 Empirical University Student Cohort",
      image: `${BASE_URL}evidence/dashboard_overview.png`,
      desc: "Investigating psychological distress across higher education students. Out of 101 surveyed respondents, 75 identify as female and 26 as male across 7 academic disciplines.",
      stat: "101 Total Surveyed Students",
      tag: "Baseline Population"
    },
    {
      title: "2. Comorbidity Burden & Risk Stratification",
      subtitle: "Zero to Three Concurrent Conditions",
      image: `${BASE_URL}evidence/mental_health_risk.png`,
      desc: "Students were stratified into 3 tiers based on concurrent self-reported symptom counts. 36.6% are Low Risk (0 conditions), 35.6% are Moderate Risk (1 condition), and 27.7% are High Risk (2-3 conditions).",
      stat: "27.7% High Comorbidity Risk",
      tag: "Clinical Stratification"
    },
    {
      title: "3. Within-Gender Condition Prevalence",
      subtitle: "Depression (34.7%), Anxiety (33.7%), Panic Attacks (32.7%)",
      image: `${BASE_URL}evidence/conditions_by_gender.png`,
      desc: "Within the female cohort (N=75), depression is 38.7%, anxiety 32.0%, and panic attacks 33.3%. In the male cohort (N=26), anxiety leads at 38.5%, with depression and panic attacks at 30.8% each.",
      stat: "Broad Cross-Gender Impact",
      tag: "Gender Analysis"
    },
    {
      title: "4. The 90.6% Campus Care Deficit",
      subtitle: "58 Untreated Symptomatic Students vs. 6 Treated",
      image: `${BASE_URL}evidence/treatment_gap.png`,
      desc: "Among 64 students self-reporting at least one clinical condition, 58 (90.6%) have never consulted a psychiatrist, psychologist, or campus counselor. Only 6 students ever received treatment.",
      stat: "90.6% Treatment Gap",
      tag: "Critical Care Deficit"
    },
    {
      title: "5. Academic Standing & The High-Achiever Paradox",
      subtitle: "Mean CGPA Midpoint: 3.45 in High Risk Group",
      image: `${BASE_URL}evidence/cgpa_risk.png`,
      desc: "Challenging the stereotype that only failing students struggle with mental health: High-risk students hold a mean CGPA midpoint of 3.45/4.0. Top academic performers frequently conceal severe distress.",
      stat: "3.45 Avg CGPA in High Risk",
      tag: "Academic Paradox"
    },
    {
      title: "6. Departmental & Faculty Distribution",
      subtitle: "Risk Distributed Across STEM & Humanities",
      image: `${BASE_URL}evidence/faculty_risk.png`,
      desc: "Comorbidity is prevalent across all 7 mapped faculties, led by Computing & IT (28 students) and Engineering (26 students), proving institutional wellness must be campus-wide.",
      stat: "7 Academic Disciplines",
      tag: "Departmental Insights"
    }
  ];

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 flex flex-col font-sans overflow-x-hidden">
      {/* Top Header / Navigation */}
      <header className="sticky top-0 z-50 bg-slate-900 border-b border-slate-800 text-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="bg-teal-500 text-slate-950 p-2 rounded-lg font-bold flex items-center justify-center">
              <Activity className="w-5 h-5" aria-hidden="true" />
            </div>
            <div>
              <span className="font-bold text-lg tracking-tight text-white block leading-tight">Student Mental Health Analytics</span>
              <span className="text-xs text-slate-400 block">Avishkar Padavi &bull; Capstone Portfolio</span>
            </div>
          </div>

          <nav className="hidden lg:flex items-center space-x-6 text-sm font-medium">
            <a href="#overview" className="text-slate-300 hover:text-teal-400 transition-colors">Overview</a>
            <a href="#methodology" className="text-slate-300 hover:text-teal-400 transition-colors">Methodology</a>
            <a href="#dashboard" className="text-slate-300 hover:text-teal-400 transition-colors">Tableau Dashboard</a>
            <a href="#findings" className="text-slate-300 hover:text-teal-400 transition-colors">Key Findings</a>
            <a href="#story" className="text-slate-300 hover:text-teal-400 transition-colors">Project Story</a>
            <a href="#video" className="text-slate-300 hover:text-teal-400 transition-colors">Presentation Video</a>
            <a href="#docs" className="text-slate-300 hover:text-teal-400 transition-colors">Documentation</a>
            <a
              href="https://github.com/Avish-beep/Skill-wallet-project"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center px-3 py-1.5 rounded-md bg-slate-800 text-teal-400 hover:bg-slate-700 border border-slate-700 transition"
              aria-label="GitHub Repository"
            >
              <GithubIcon className="w-4 h-4 mr-1.5" />
              GitHub
            </a>
          </nav>

          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="lg:hidden p-2 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 focus:outline-none"
            aria-label="Toggle Navigation Menu"
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Dropdown */}
        {mobileMenuOpen && (
          <div className="lg:hidden bg-slate-900 border-b border-slate-800 px-4 pt-2 pb-4 space-y-2 text-sm">
            <a href="#overview" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Overview</a>
            <a href="#methodology" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Methodology</a>
            <a href="#dashboard" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Tableau Dashboard</a>
            <a href="#findings" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Key Findings</a>
            <a href="#story" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Project Story</a>
            <a href="#video" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Presentation Video</a>
            <a href="#docs" onClick={() => setMobileMenuOpen(false)} className="block py-2 text-slate-300 hover:text-teal-400">Documentation</a>
            <a
              href="https://github.com/Avish-beep/Skill-wallet-project"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center py-2 text-teal-400 hover:underline"
            >
              <GithubIcon className="w-4 h-4 mr-1.5" /> View on GitHub
            </a>
          </div>
        )}
      </header>

      {/* Hero Section */}
      <section id="overview" className="bg-gradient-to-b from-slate-900 via-slate-900 to-slate-800 text-white py-20 px-4 sm:px-6 lg:px-8 border-b border-slate-800">
        <div className="max-w-7xl mx-auto">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal-950/80 border border-teal-500/30 text-teal-300 text-xs font-semibold mb-6">
            <ShieldCheck className="w-4 h-4" aria-hidden="true" />
            Empirical Healthcare Analytics &bull; Verified N=101 Student Cohort
          </div>
          <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-white max-w-4xl leading-tight">
            Analysing Mental Health in Student Ecosystem
          </h1>
          <p className="mt-5 text-lg sm:text-xl text-slate-300 max-w-3xl leading-relaxed">
            Exploring self-reported student mental-health patterns through reproducible Python data preparation, interactive Tableau visual analytics, and evidence-based clinical gap reporting.
          </p>

          <div className="mt-8 flex flex-wrap gap-4">
            <a
              href="#dashboard"
              className="inline-flex items-center px-6 py-3 rounded-lg bg-teal-500 text-slate-950 font-semibold hover:bg-teal-400 shadow-md transition"
            >
              <LayoutDashboard className="w-5 h-5 mr-2" aria-hidden="true" />
              View Live Dashboard
            </a>
            <a
              href="#video"
              className="inline-flex items-center px-6 py-3 rounded-lg bg-slate-800 text-white border border-slate-700 font-semibold hover:bg-slate-700 transition"
            >
              <Play className="w-5 h-5 mr-2 text-teal-400" aria-hidden="true" />
              Watch Video Presentation (06:24)
            </a>
            <a
              href="#methodology"
              className="inline-flex items-center px-6 py-3 rounded-lg bg-transparent text-slate-300 hover:text-white border border-slate-700 hover:border-slate-500 transition"
            >
              <BookOpen className="w-5 h-5 mr-2" aria-hidden="true" />
              Explore Methodology
            </a>
            <a
              href="https://github.com/Avish-beep/Skill-wallet-project"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center px-6 py-3 rounded-lg bg-transparent text-slate-300 hover:text-white border border-slate-700 hover:border-slate-500 transition"
            >
              <GithubIcon className="w-5 h-5 mr-2" />
              Source Code
            </a>
          </div>

          {/* Project Truth Scorecards */}
          <div className="mt-12 grid grid-cols-2 sm:grid-cols-4 gap-4 max-w-4xl">
            <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-xl">
              <span className="text-xs font-semibold text-slate-400 block uppercase tracking-wider">Cohort Size</span>
              <span className="text-2xl font-bold text-white mt-1 block">101 Students</span>
              <span className="text-xs text-teal-400 mt-1 block">0 missing &bull; 0 duplicates</span>
            </div>
            <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-xl">
              <span className="text-xs font-semibold text-slate-400 block uppercase tracking-wider">High Risk Tiers</span>
              <span className="text-2xl font-bold text-amber-400 mt-1 block">28 (27.7%)</span>
              <span className="text-xs text-slate-300 mt-1 block">&ge;2 concurrent conditions</span>
            </div>
            <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-xl">
              <span className="text-xs font-semibold text-slate-400 block uppercase tracking-wider">Care Deficit</span>
              <span className="text-2xl font-bold text-rose-400 mt-1 block">90.6%</span>
              <span className="text-xs text-slate-300 mt-1 block">58 of 64 symptomatic untreated</span>
            </div>
            <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-xl">
              <span className="text-xs font-semibold text-slate-400 block uppercase tracking-wider">High Risk CGPA</span>
              <span className="text-2xl font-bold text-teal-300 mt-1 block">3.45 / 4.0</span>
              <span className="text-xs text-slate-300 mt-1 block">High achievers distressed</span>
            </div>
          </div>
        </div>
      </section>

      {/* Problem Statement & Research Boundaries */}
      <section className="py-16 px-4 sm:px-6 lg:px-8 bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <span className="text-teal-600 font-semibold text-sm uppercase tracking-wider">Investigative Framework</span>
              <h2 className="text-3xl font-bold text-slate-900 mt-2">Problem Statement & Research Scope</h2>
              <p className="mt-4 text-slate-600 leading-relaxed">
                Higher education environments impose acute academic, economic, and developmental pressures. While universities allocate resources to academic tutoring, institutional support for mental health remains disconnected from empirical population analytics.
              </p>
              <div className="mt-6 space-y-4">
                <div className="flex items-start">
                  <CheckCircle className="w-5 h-5 text-teal-600 mt-0.5 mr-3 flex-shrink-0" />
                  <div>
                    <h3 className="font-semibold text-slate-800">What This Project Answers</h3>
                    <p className="text-sm text-slate-600 mt-0.5">Empirical distribution of self-reported depression, anxiety, and panic attacks; quantification of the campus clinical care gap; correlation with academic CGPA midpoint across 7 academic disciplines.</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <AlertCircle className="w-5 h-5 text-amber-500 mt-0.5 mr-3 flex-shrink-0" />
                  <div>
                    <h3 className="font-semibold text-slate-800">Observational Boundaries & Data Integrity</h3>
                    <p className="text-sm text-slate-600 mt-0.5">Survey responses are self-reported indicators, not formal clinical DSM-5 diagnoses. Claims are observational, not causal. Generic template metrics like sleep hours, heart rate variability, or attendance do not exist in this survey and are strictly excluded.</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-2xl p-6 shadow-sm">
              <h3 className="font-bold text-slate-900 text-lg flex items-center mb-4">
                <Database className="w-5 h-5 text-teal-600 mr-2" />
                Validated Analytical Data Profile
              </h3>
              <div className="space-y-3 text-sm">
                <div className="flex justify-between py-2 border-b border-slate-200">
                  <span className="text-slate-500">Student Observations (Rows):</span>
                  <span className="font-semibold text-slate-800">101</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-200">
                  <span className="text-slate-500">Engineered Analytical Features (Cols):</span>
                  <span className="font-semibold text-slate-800">23</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-200">
                  <span className="text-slate-500">Missing / Null Values:</span>
                  <span className="font-semibold text-emerald-600">0 (Imputed via Age Median)</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-200">
                  <span className="text-slate-500">Duplicate Records:</span>
                  <span className="font-semibold text-emerald-600">0 (100% Unique Survey Records)</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-200">
                  <span className="text-slate-500">Raw SHA-256 Hash:</span>
                  <span className="font-mono text-xs text-slate-600">c0d1300dd5...63f0a</span>
                </div>
                <div className="flex justify-between py-2">
                  <span className="text-slate-500">Preprocessing Pipeline:</span>
                  <span className="font-mono text-xs text-teal-700 bg-teal-50 px-2 py-0.5 rounded">scripts/prepare_dataset.py</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Methodology Visual Pipeline */}
      <section id="methodology" className="py-16 px-4 sm:px-6 lg:px-8 bg-slate-50 border-b border-slate-200">
        <div className="max-w-7xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="text-teal-600 font-semibold text-sm uppercase tracking-wider">End-to-End Pipeline</span>
            <h2 className="text-3xl font-bold text-slate-900 mt-2">Analytical Methodology & Provenance</h2>
            <p className="mt-3 text-slate-600">
              A transparent, reproducible data engineering workflow from immutable survey ingestion to interactive visual intelligence.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm relative">
              <div className="w-10 h-10 rounded-lg bg-blue-50 text-blue-600 font-bold flex items-center justify-center mb-4">1</div>
              <h3 className="font-bold text-slate-900 mb-2">1. Ingestion & Audit</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Ingested immutable baseline CSV (101 rows x 11 survey columns). Verified SHA-256 hash. Audited data types, distributions, and null values.
              </p>
              <div className="mt-4 text-xs font-mono text-blue-700 bg-blue-50/70 p-2 rounded">
                Epic 1: Data Collection
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm relative">
              <div className="w-10 h-10 rounded-lg bg-teal-50 text-teal-600 font-bold flex items-center justify-center mb-4">2</div>
              <h3 className="font-bold text-slate-900 mb-2">2. ETL & Engineering</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Imputed 1 missing age using median (19.0). Cleaned CGPA ranges. Mapped 43 courses into 7 macro faculties. Engineered 12 features including condition counts and care gaps.
              </p>
              <div className="mt-4 text-xs font-mono text-teal-700 bg-teal-50/70 p-2 rounded">
                Epic 2: Data Preparation
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm relative">
              <div className="w-10 h-10 rounded-lg bg-indigo-50 text-indigo-600 font-bold flex items-center justify-center mb-4">3</div>
              <h3 className="font-bold text-slate-900 mb-2">3. Visual Intelligence</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Constructed 10 individual worksheets and 2 responsive executive dashboards in Tableau Desktop. Standardized card grids and multi-tier filters.
              </p>
              <div className="mt-4 text-xs font-mono text-indigo-700 bg-indigo-50/70 p-2 rounded">
                Epic 3: Data Visualization
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm relative">
              <div className="w-10 h-10 rounded-lg bg-emerald-50 text-emerald-600 font-bold flex items-center justify-center mb-4">4</div>
              <h3 className="font-bold text-slate-900 mb-2">4. Web & Video Delivery</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Deployed interactive Tableau Public view, published static responsive portfolio on GitHub Pages, and generated narrated presentation video.
              </p>
              <div className="mt-4 text-xs font-mono text-emerald-700 bg-emerald-50/70 p-2 rounded">
                Epic 4-8: Demonstration
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Tableau Dashboard Embed Section */}
      <section id="dashboard" className="py-16 px-4 sm:px-6 lg:px-8 bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row md:items-end justify-between mb-8">
            <div>
              <span className="text-teal-600 font-semibold text-sm uppercase tracking-wider">Visual Intelligence & Deployment</span>
              <h2 className="text-3xl font-bold text-slate-900 mt-1">Student Mental Health Analytical Dashboard</h2>
              <p className="text-slate-600 mt-2 max-w-2xl text-sm">
                Derived from the validated 101-student dataset across 23 features. Below is the verified workbook architecture developed in Tableau Desktop 2026.1 alongside the live Tableau Public connection.
              </p>
            </div>
            <div className="mt-4 md:mt-0 flex flex-wrap gap-3">
              <a
                href={TABLEAU_VIEW_URL}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center px-4 py-2 rounded-lg bg-teal-600 text-white font-medium hover:bg-teal-500 shadow-sm text-sm transition"
              >
                <ExternalLink className="w-4 h-4 mr-2" />
                Open Current View on Tableau Public
              </a>
            </div>
          </div>

          {/* Publication Status & Reconciliation Card */}
          <div className="mb-6 bg-amber-50/90 border border-amber-200 rounded-xl p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 text-xs text-amber-900">
            <div className="flex items-start gap-3">
              <AlertCircle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
              <div>
                <strong className="font-semibold block text-amber-950">Tableau Public Publication Notice:</strong>
                <span>The local Tableau Desktop workbook (<code>tableau/student_mental_health_visualizations.twb</code>) is 100% verified against our authentic 101-student dataset. Cloud overwrite to replace the older generic template on Tableau Public is currently queued.</span>
              </div>
            </div>
            <span className="bg-amber-200/80 text-amber-900 px-3 py-1 rounded-full font-mono text-[11px] whitespace-nowrap self-start sm:self-center font-bold">
              Local: Validated (N=101) &bull; Cloud: Pending Overwrite
            </span>
          </div>

          {/* Validated Local Dashboard Evidence Preview */}
          <div className="bg-slate-900 rounded-2xl overflow-hidden shadow-xl border border-slate-800">
            <div className="bg-slate-950 px-4 py-3 flex items-center justify-between border-b border-slate-800 text-xs text-slate-400">
              <div className="flex items-center space-x-2">
                <span className="w-3 h-3 rounded-full bg-emerald-500 inline-block"></span>
                <span className="w-3 h-3 rounded-full bg-amber-500 inline-block"></span>
                <span className="w-3 h-3 rounded-full bg-blue-500 inline-block"></span>
                <span className="ml-2 font-mono text-slate-300">Verified Architecture &bull; Student Mental Health Overview (16:9 Canvas)</span>
              </div>
              <span className="text-emerald-400 font-semibold hidden sm:inline">&bull; 4 Verified KPIs &bull; 6 Core Panels</span>
            </div>

            <div className="relative w-full bg-slate-950 p-2 sm:p-4 flex items-center justify-center">
              <img
                src={`${BASE_URL}evidence/dashboard_overview.png`}
                alt="Validated Student Mental Health Overview Dashboard in Tableau"
                className="w-full rounded-lg shadow-lg object-contain max-h-[640px]"
              />
            </div>

            <div className="p-4 bg-slate-900 border-t border-slate-800 flex flex-col sm:flex-row justify-between items-center text-xs text-slate-400 gap-2">
              <span>Includes interactive multi-tier filters: <strong>Gender</strong>, <strong>Age Group</strong>, <strong>Faculty (7)</strong>, and <strong>Risk Tier (3)</strong>.</span>
              <span className="text-teal-400 font-mono">student_mental_health_visualizations.twb</span>
            </div>
          </div>
        </div>
      </section>

      {/* Key Analytical Findings */}
      <section id="findings" className="py-16 px-4 sm:px-6 lg:px-8 bg-slate-50 border-b border-slate-200">
        <div className="max-w-7xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="text-teal-600 font-semibold text-sm uppercase tracking-wider">Reproducible Statistics</span>
            <h2 className="text-3xl font-bold text-slate-900 mt-2">Key Analytical Findings</h2>
            <p className="mt-3 text-slate-600">
              Direct statistical extractions from the validated 101-student analytical dataset.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-rose-600 bg-rose-50 px-2.5 py-1 rounded-full">Primary Deficit</span>
                <span className="text-2xl font-black text-rose-600">90.6%</span>
              </div>
              <h3 className="font-bold text-slate-900 text-lg">The Specialist Care Deficit</h3>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                58 out of 64 students exhibiting at least one self-reported condition have never consulted a psychiatrist, psychologist, or counselor. Only 6 symptomatic students accessed care.
              </p>
              <div className="mt-4 pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                Symptomatic Cohort: 64 | Untreated: 58 | Treated: 6
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full">Risk Stratification</span>
                <span className="text-2xl font-black text-amber-600">63.4%</span>
              </div>
              <h3 className="font-bold text-slate-900 text-lg">Vulnerable Student Cohort</h3>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                63.4% of all surveyed students experience at least one condition: 35.6% Moderate Risk (1 condition) and 27.7% High Risk (&ge;2 conditions). Only 36.6% report zero conditions.
              </p>
              <div className="mt-4 pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                Low Risk: 37 (36.6%) | Moderate: 36 (35.6%) | High: 28 (27.7%)
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-teal-600 bg-teal-50 px-2.5 py-1 rounded-full">Academic Paradox</span>
                <span className="text-2xl font-black text-teal-600">3.45</span>
              </div>
              <h3 className="font-bold text-slate-900 text-lg">High Academic Achiever Distress</h3>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                High-risk comorbidity students maintain an average CGPA midpoint of 3.45 out of 4.0, dispelling the assumption that mental health distress is confined to struggling students.
              </p>
              <div className="mt-4 pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                Mean CGPA Midpoint: High Risk (3.45) vs Low Risk (3.26)
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded-full">Condition Rates</span>
                <span className="text-2xl font-black text-indigo-600">34.7%</span>
              </div>
              <h3 className="font-bold text-slate-900 text-lg">Tri-Condition Prevalence</h3>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                Condition indicators are closely distributed across the cohort: Depression at 34.7% (35 students), Anxiety at 33.7% (34 students), and Panic Attacks at 32.7% (33 students).
              </p>
              <div className="mt-4 pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                Depression: 35 | Anxiety: 34 | Panic Attacks: 33
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-purple-600 bg-purple-50 px-2.5 py-1 rounded-full">Comorbidity</span>
                <span className="text-2xl font-black text-purple-600">28</span>
              </div>
              <h3 className="font-bold text-slate-900 text-lg">Severe Comorbid Burden</h3>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                18 students suffer from two concurrent conditions, while 10 students suffer from all three conditions concurrently (depression, anxiety, and panic attacks).
              </p>
              <div className="mt-4 pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                0 conditions: 37 | 1: 36 | 2: 18 | 3: 10
              </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md transition">
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-600 bg-slate-100 px-2.5 py-1 rounded-full">Faculties</span>
                <span className="text-2xl font-black text-slate-700">7</span>
              </div>
              <h3 className="font-bold text-slate-900 text-lg">Cross-Disciplinary Reach</h3>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                Computing & IT (28 students) and Engineering (26 students) form over 53% of the surveyed cohort, but comorbidity is documented across all humanities and science faculties.
              </p>
              <div className="mt-4 pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                Computing: 28 | Engineering: 26 | Humanities: 14 | Sciences: 13
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Project Story / Scrollytelling Section */}
      <section id="story" className="py-16 px-4 sm:px-6 lg:px-8 bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="text-teal-600 font-semibold text-sm uppercase tracking-wider">Guided Analytical Narrative</span>
            <h2 className="text-3xl font-bold text-slate-900 mt-2">Project Story & Scrollytelling</h2>
            <p className="mt-3 text-slate-600">
              Step through the 6 chapters of the student mental health analytical journey.
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            {/* Story Navigation Tabs */}
            <div className="lg:col-span-4 space-y-2">
              {storyScenes.map((scene, idx) => (
                <button
                  key={idx}
                  onClick={() => setActiveStoryScene(idx)}
                  className={`w-full text-left p-4 rounded-xl border transition flex items-center justify-between ${
                    activeStoryScene === idx
                      ? 'bg-slate-900 text-white border-slate-900 shadow-md'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  <div>
                    <span className="text-xs font-semibold uppercase tracking-wider block opacity-75">{scene.tag}</span>
                    <span className="font-bold text-sm block mt-0.5">{scene.title}</span>
                  </div>
                  <ChevronRight className={`w-4 h-4 flex-shrink-0 ${activeStoryScene === idx ? 'text-teal-400' : 'text-slate-400'}`} />
                </button>
              ))}
            </div>

            {/* Active Story Scene Display */}
            <div className="lg:col-span-8 bg-slate-50 border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
              <div className="p-4 sm:p-6 bg-slate-900 text-white flex justify-between items-center">
                <div>
                  <span className="text-teal-400 font-semibold text-xs tracking-wider uppercase block">{storyScenes[activeStoryScene].tag}</span>
                  <h3 className="text-xl font-bold text-white mt-1">{storyScenes[activeStoryScene].title}</h3>
                  <span className="text-xs text-slate-300">{storyScenes[activeStoryScene].subtitle}</span>
                </div>
                <div className="text-right">
                  <span className="text-xs text-slate-400 block uppercase">Key Stat</span>
                  <span className="text-base font-bold text-teal-400">{storyScenes[activeStoryScene].stat}</span>
                </div>
              </div>

              <div className="p-4 bg-slate-950 flex justify-center items-center">
                <img
                  src={storyScenes[activeStoryScene].image}
                  alt={storyScenes[activeStoryScene].title}
                  className="max-h-[420px] rounded-lg shadow-md object-contain border border-slate-800"
                />
              </div>

              <div className="p-6 bg-white border-t border-slate-200">
                <p className="text-slate-700 text-sm leading-relaxed">{storyScenes[activeStoryScene].desc}</p>
                <div className="mt-4 flex justify-between items-center text-xs text-slate-500">
                  <span>Scene {activeStoryScene + 1} of {storyScenes.length}</span>
                  <div className="space-x-2">
                    <button
                      onClick={() => setActiveStoryScene(Math.max(0, activeStoryScene - 1))}
                      disabled={activeStoryScene === 0}
                      className="px-3 py-1 bg-slate-100 rounded text-slate-700 disabled:opacity-40"
                    >
                      Previous
                    </button>
                    <button
                      onClick={() => setActiveStoryScene(Math.min(storyScenes.length - 1, activeStoryScene + 1))}
                      disabled={activeStoryScene === storyScenes.length - 1}
                      className="px-3 py-1 bg-teal-600 text-white rounded disabled:opacity-40"
                    >
                      Next
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Project Presentation Video Section */}
      <section id="video" className="py-16 px-4 sm:px-6 lg:px-8 bg-slate-900 text-white border-b border-slate-800">
        <div className="max-w-7xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="text-teal-400 font-semibold text-sm uppercase tracking-wider">Video Walkthrough & Narration</span>
            <h2 className="text-3xl font-bold text-white mt-2">End-to-End Project Presentation Video</h2>
            <p className="mt-3 text-slate-300 text-sm">
              Full 6-minute 24-second academic walkthrough with natural Indian English narration by Avishkar Padavi.
            </p>
          </div>

          <div className="max-w-4xl mx-auto bg-slate-950 rounded-2xl overflow-hidden border border-slate-800 shadow-2xl">
            <div className="relative aspect-video bg-black flex items-center justify-center">
              <video
                controls
                poster={`${BASE_URL}video/thumbnail.png`}
                className="w-full h-full object-contain"
              >
                <source src={`${BASE_URL}video/project_presentation.mp4`} type="video/mp4" />
                <track src={`${BASE_URL}video/captions.vtt`} kind="subtitles" srcLang="en" label="English" default />
                Your browser does not support HTML5 video playback.
              </video>
            </div>

            <div className="p-6 bg-slate-900 border-t border-slate-800">
              <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                <div>
                  <h3 className="font-bold text-white text-lg">Analysing Mental Health in Student Ecosystem &bull; Presentation Walkthrough</h3>
                  <p className="text-xs text-slate-400 mt-1">
                    Duration: 06:24 &bull; Resolution: 1080p Full HD &bull; Voice: Indian English (en-IN-PrabhatNeural)
                  </p>
                </div>
                <div className="flex gap-3">
                  <a
                    href={`${BASE_URL}video/project_presentation.mp4`}
                    download="Analysing_Mental_Health_Avishkar_Padavi.mp4"
                    className="inline-flex items-center px-3.5 py-2 rounded-lg bg-teal-500 text-slate-950 font-semibold hover:bg-teal-400 text-xs transition"
                  >
                    <Download className="w-4 h-4 mr-1.5" />
                    Download MP4 (20 MB)
                  </a>
                  <a
                    href={`${BASE_URL}video/transcript.md`}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-flex items-center px-3.5 py-2 rounded-lg bg-slate-800 text-slate-300 border border-slate-700 hover:text-white text-xs transition"
                  >
                    <FileText className="w-4 h-4 mr-1.5" />
                    Transcript
                  </a>
                </div>
              </div>

              {/* Chapter Timestamps */}
              <div className="mt-6 pt-4 border-t border-slate-800">
                <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2">Video Chapters</span>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">00:00</strong> Intro & Context</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">00:43</strong> Data Engineering</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">01:25</strong> Tableau Overview</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">02:10</strong> Clinical Gap</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">02:43</strong> Risk Tiers</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">03:19</strong> Gender Breakdown</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">04:29</strong> CGPA Paradox</span>
                  <span className="text-slate-300 font-mono"><strong className="text-teal-400">06:07</strong> Recommendations</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Documentation & Source Code Links */}
      <section id="docs" className="py-16 px-4 sm:px-6 lg:px-8 bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="text-teal-600 font-semibold text-sm uppercase tracking-wider">Repository Artifacts</span>
            <h2 className="text-3xl font-bold text-slate-900 mt-2">Comprehensive Project Documentation</h2>
            <p className="mt-3 text-slate-600">
              Verified documentation reports, reproducible pipeline scripts, and data dictionaries.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <a
              href="https://github.com/Avish-beep/Skill-wallet-project/blob/main/README.md"
              target="_blank"
              rel="noreferrer"
              className="p-4 rounded-xl border border-slate-200 hover:border-teal-500 hover:shadow-md transition bg-slate-50 flex flex-col justify-between"
            >
              <div>
                <FileText className="w-6 h-6 text-teal-600 mb-2" />
                <h3 className="font-bold text-slate-900 text-sm">Project README.md</h3>
                <p className="text-xs text-slate-600 mt-1">Complete overview, setup commands, live URLs, and data dictionary.</p>
              </div>
              <span className="mt-4 text-xs font-semibold text-teal-600 flex items-center">View on GitHub &rarr;</span>
            </a>

            <a
              href="https://github.com/Avish-beep/Skill-wallet-project/blob/main/documentation/visualization_report.md"
              target="_blank"
              rel="noreferrer"
              className="p-4 rounded-xl border border-slate-200 hover:border-teal-500 hover:shadow-md transition bg-slate-50 flex flex-col justify-between"
            >
              <div>
                <BarChart3 className="w-6 h-6 text-indigo-600 mb-2" />
                <h3 className="font-bold text-slate-900 text-sm">Visualization Report</h3>
                <p className="text-xs text-slate-600 mt-1">Detailed statistical synthesis for all 10 worksheets and 2 dashboards.</p>
              </div>
              <span className="mt-4 text-xs font-semibold text-indigo-600 flex items-center">View on GitHub &rarr;</span>
            </a>

            <a
              href="https://github.com/Avish-beep/Skill-wallet-project/blob/main/documentation/data_preparation_report.md"
              target="_blank"
              rel="noreferrer"
              className="p-4 rounded-xl border border-slate-200 hover:border-teal-500 hover:shadow-md transition bg-slate-50 flex flex-col justify-between"
            >
              <div>
                <Database className="w-6 h-6 text-blue-600 mb-2" />
                <h3 className="font-bold text-slate-900 text-sm">Data Preparation Report</h3>
                <p className="text-xs text-slate-600 mt-1">Epic 2 transformations, median age imputation, and derived formulas.</p>
              </div>
              <span className="mt-4 text-xs font-semibold text-blue-600 flex items-center">View on GitHub &rarr;</span>
            </a>

            <a
              href="https://github.com/Avish-beep/Skill-wallet-project/blob/main/documentation/project_progress.md"
              target="_blank"
              rel="noreferrer"
              className="p-4 rounded-xl border border-slate-200 hover:border-teal-500 hover:shadow-md transition bg-slate-50 flex flex-col justify-between"
            >
              <div>
                <CheckCircle className="w-6 h-6 text-emerald-600 mb-2" />
                <h3 className="font-bold text-slate-900 text-sm">Milestone Progress Tracker</h3>
                <p className="text-xs text-slate-600 mt-1">Tracking all 8 Epics and deliverables across the SkillWallet curriculum.</p>
              </div>
              <span className="mt-4 text-xs font-semibold text-emerald-600 flex items-center">View on GitHub &rarr;</span>
            </a>
          </div>
        </div>
      </section>

      {/* Project Author & Institutional Information */}
      <footer className="bg-slate-950 text-slate-400 py-12 px-4 sm:px-6 lg:px-8 border-t border-slate-800">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
          <div>
            <div className="flex items-center space-x-2">
              <Activity className="w-5 h-5 text-teal-400" />
              <span className="text-white font-bold text-base">Analysing Mental Health in Student Ecosystem</span>
            </div>
            <p className="text-xs text-slate-500 mt-1">
              Developed by <strong>Avishkar Padavi</strong> &bull; Indira College of Engineering and Management
            </p>
            <p className="text-xs text-slate-500 mt-0.5">
              Domain: Healthcare Analytics / Student Mental Health &bull; Module: Data Analytics with Tableau
            </p>
          </div>

          <div className="flex items-center space-x-4 text-sm">
            <a
              href="https://github.com/Avish-beep/Skill-wallet-project"
              target="_blank"
              rel="noreferrer"
              className="text-slate-400 hover:text-white transition flex items-center"
            >
              <GithubIcon className="w-4 h-4 mr-1.5" />
              GitHub Repository
            </a>
            <a
              href={TABLEAU_VIEW_URL}
              target="_blank"
              rel="noreferrer"
              className="text-slate-400 hover:text-white transition flex items-center"
            >
              <ExternalLink className="w-4 h-4 mr-1.5" />
              Tableau Public
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
