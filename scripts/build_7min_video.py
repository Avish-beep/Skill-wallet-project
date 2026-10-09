import os
import sys
import subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pyttsx3
import imageio_ffmpeg
import wave

def get_audio_duration(file_path):
    with wave.open(file_path, 'r') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        return frames / float(rate)

def build_7min_presentation():
    temp_dir = r"C:\Skillwallet\docs\temp_7min"
    os.makedirs(temp_dir, exist_ok=True)
    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # 12 slides comprehensively covering the entire project for ~7 mins
    slides = [
        {
            "id": "s01_intro",
            "type": "title",
            "title": "Analysing Mental Health in Student Ecosystem",
            "subtitle": "Data Analytics with Tableau | End-to-End SkillWallet Capstone Walkthrough",
            "student": "Student: Avishkar Padavi",
            "details": "Indira College of Engineering and Management | Domain: Healthcare Analytics\nPlatform: SkillWallet | Guided Evaluation Video",
            "script": (
                "Hello everyone, respected evaluators and faculty members. My name is Avishkar Padavi, and today I am proud to present "
                "my comprehensive data analytics project titled: Analysing Mental Health in Student Ecosystem. "
                "Mental health among higher education students has emerged as one of the most critical public health concerns globally. "
                "The pressures of academic performance, social transitions, career expectations, and emerging adulthood frequently create severe "
                "psychological stress. However, many academic institutions lack empirical, data-driven frameworks to monitor distress, evaluate risk, "
                "and optimize counseling intervention programs. This project bridges that critical gap by building a robust, reproducible "
                "data engineering pipeline and interactive visual intelligence dashboards using Python and Tableau."
            )
        },
        {
            "id": "s02_pipeline",
            "type": "title",
            "title": "Data Architecture, Methodology & Integrity Standards",
            "subtitle": "Epic 1 Data Collection & Epic 2 Data Preparation Pipeline",
            "student": "Verified Student Dataset: N = 101 Cohort Records",
            "details": "Immutable Raw Data: SHA-256 Verified | Zero Synthetic Columns\nClean Analytical Dataset: 101 Rows x 23 Engineered Columns",
            "script": (
                "Before delving into the visualizations, it is essential to highlight our data engineering rigor. "
                "Our investigation utilizes an empirical survey dataset capturing university students across various disciplines. "
                "During Epic 1, Data Collection and Extraction, we ingested the immutable baseline survey dataset and verified its integrity "
                "with an SHA-256 checksum. In Epic 2, Data Preparation, we implemented a fully automated ETL pipeline using Python and pandas. "
                "We performed median-based imputation for missing age values, mapped academic disciplines into standardized faculties, "
                "and engineered twelve derived features including comorbidity counts, risk stratifications, and clinical care gap metrics. "
                "Most importantly, our dataset maintains absolute data integrity, eliminating any synthetic or fabricated values."
            )
        },
        {
            "id": "s03_overview_dashboard",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\dashboard_overview.png",
            "title": "Executive Overview Dashboard (Live Tableau Public)",
            "subtitle": "High-Density Analytical Grid: Interactive Filters, 4 Key Metrics & Multi-dimensional Panels",
            "script": (
                "Now, let us examine our primary Tableau Public dashboard: the Student Mental Health Overview Dashboard. "
                "This dashboard is designed following modern healthcare intelligence standards, featuring responsive layout containers, "
                "intuitive filter hierarchies, and clean executive metric scorecards. "
                "Looking at the four key performance indicators at the top: first, our total surveyed student cohort consists of one hundred and one students. "
                "Second, twenty-eight students, or twenty-seven point seven percent, are classified in the high comorbidity risk tier. "
                "Third, thirty-six students, or thirty-five point six percent, fall under moderate risk. "
                "And fourth, an alarming fifty-eight students self-report symptomatic mental health distress without receiving any specialist care. "
                "This multi-panel grid allows university administrators to instantly filter by gender, age group, faculty, and risk tier."
            )
        },
        {
            "id": "s04_treatment_dashboard",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\dashboard_treatment.png",
            "title": "Mental Health Risk & Clinical Treatment Gap Dashboard",
            "subtitle": "Quantifying the Institutional Deficit in University Counseling Access",
            "script": (
                "Our second dedicated dashboard focuses directly on Clinical Risk and Treatment Gap Analysis. "
                "The most significant finding revealed by our empirical data is the massive institutional care deficit. "
                "Among all students reporting symptomatic psychological conditions, an astounding ninety point six percent have never sought "
                "professional help from a psychiatrist, psychologist, or campus counselor. "
                "Only six students out of the entire symptomatic cohort have accessed clinical care. "
                "This visualization clearly demonstrates that university mental health distress is not primarily an awareness challenge, "
                "but an accessibility and stigma barrier that requires proactive institutional outreach."
            )
        },
        {
            "id": "s05_risk_distribution",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\mental_health_risk.png",
            "title": "Population Risk Stratification: Low, Moderate, and High Risk",
            "subtitle": "Comorbidity Tiers Derived from Concurrent Self-Reported Conditions",
            "script": (
                "Let us now break down the specific analytical worksheets. First is the Distribution of Mental Health Risk Levels. "
                "In our data pipeline, risk tiers were systematically defined based on concurrent symptom counts: "
                "Students with zero self-reported conditions are classified as Low Risk, accounting for thirty-six point six percent of the cohort. "
                "Students with a single condition are categorized as Moderate Risk, comprising thirty-five point six percent. "
                "And students suffering from two or three concurrent conditions—such as co-occurring depression and panic attacks—are categorized "
                "as High Risk, representing twenty-seven point seven percent of the student body. "
                "This proves that nearly two-thirds of the student ecosystem experiences some degree of psychological vulnerability."
            )
        },
        {
            "id": "s06_gender_analysis",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\conditions_by_gender.png",
            "title": "Within-Gender Self-Reported Conditions Analysis",
            "subtitle": "Comparative Burden across Female (N=75) and Male (N=26) Cohorts",
            "script": (
                "Next, we examine the distribution of self-reported conditions stratified by gender. "
                "Our dataset contains seventy-five female respondents and twenty-six male respondents. "
                "To prevent sampling bias, we evaluated condition prevalence within each respective gender cohort. "
                "Among female students, self-reported depression, anxiety, and panic attacks are distributed across thirty-eight point seven percent, "
                "thirty-two percent, and thirty-three point three percent respectively. "
                "Among male students, anxiety is self-reported at thirty-eight point five percent, with depression and panic attacks each at thirty point eight percent. "
                "This reveals that while presentation patterns vary, anxiety and mood disorders represent significant challenges across all genders."
            )
        },
        {
            "id": "s07_treatment_gap_detail",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\treatment_gap.png",
            "title": "In-Depth Treatment Deficit: Symptomatic vs. Clinical Consultation",
            "subtitle": "90.6% Care Deficit: 58 Untreated Students vs. 6 Treated Students",
            "script": (
                "This visualization isolates the Student Mental Health Treatment Gap. "
                "Out of sixty-four students who exhibited at least one mental health symptom, fifty-eight students remain completely untreated. "
                "When asked whether they had sought treatment from a medical or mental health professional, only nine point four percent replied affirmatively. "
                "In higher education administration, this empirical evidence is vital: establishing campus wellness centers is insufficient "
                "unless colleges actively de-stigmatize mental health consultations and provide frictionless, confidential appointment systems."
            )
        },
        {
            "id": "s08_cgpa_analysis",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\cgpa_risk.png",
            "title": "Academic Standing (CGPA Midpoint) Across Mental Health Risk Levels",
            "subtitle": "Challenging the Stereotype: High Academic Achievers Experience Severe Distress",
            "script": (
                "One of the most fascinating discoveries of this research is the relationship between academic achievement and mental health risk. "
                "There is often a common stereotype that only students who are struggling academically experience psychological distress. "
                "However, our data directly challenges that assumption. As shown in this boxplot and stripplot visualization, "
                "students in the High Risk category maintain a mean CGPA midpoint of three point four five out of four point zero. "
                "Similarly, moderate risk students average three point four eight. "
                "This demonstrates that academic high achievers and honors students are under intense competitive pressure, often concealing severe "
                "anxiety and depressive symptoms behind stellar academic transcripts."
            )
        },
        {
            "id": "s09_faculty_risk",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\faculty_risk.png",
            "title": "Mental Health Risk Across Academic Disciplines & Faculties",
            "subtitle": "Macro Departmental Breakdown: Engineering, Computing, Sciences, and Arts",
            "script": (
                "Looking at the departmental breakdown across academic faculties: our mapping standardized diverse student majors into "
                "seven primary faculties: Computing and IT, Engineering, Human Sciences, Biomedical and Allied Health, Islamic Studies, Economics, and Languages. "
                "The visualization indicates that high and moderate comorbidity risks are distributed across technical STEM fields as well as the humanities. "
                "This proves that campus wellness initiatives cannot be isolated to a single department, but must be embedded across the entire university infrastructure."
            )
        },
        {
            "id": "s10_condition_count",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\condition_count.png",
            "title": "Comorbidity Burden: Distribution of Concurrent Conditions",
            "subtitle": "Histogram Quantifying Single vs. Multiple Symptom Co-Occurrence",
            "script": (
                "This histogram illustrates the comorbidity burden by tracking the exact number of concurrent conditions reported by each student. "
                "Thirty-seven students reported zero conditions, thirty-six students reported exactly one condition, "
                "seventeen students reported two concurrent conditions, and eleven students reported suffering from all three conditions simultaneously: "
                "depression, anxiety, and panic attacks. "
                "Addressing comorbidity is crucial because clinical literature indicates that students with overlapping symptoms have a significantly higher risk "
                "of academic burnout and dropout."
            )
        },
        {
            "id": "s11_age_group",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\risk_by_age_group.png",
            "title": "Risk Trajectory Across Age Groups and Undergraduate Seniority",
            "subtitle": "Underclassmen (Ages 18–20) vs. Upperclassmen (Ages 21–24)",
            "script": (
                "Examining risk trajectory across undergraduate seniority levels: we segmented students into younger underclassmen aged eighteen to twenty, "
                "and senior upperclassmen aged twenty-one to twenty-four. "
                "Both cohorts exhibit pronounced vulnerability. First and second-year students frequently encounter transitional homesickness, "
                "new social environments, and sudden academic rigor. Meanwhile, senior students face the looming pressures of graduation, "
                "career placements, and economic uncertainty. Institutional interventions must therefore be tailored to each stage of the student lifecycle."
            )
        },
        {
            "id": "s12_conclusion",
            "type": "title",
            "title": "Conclusion, Actionable Recommendations & Project Verification",
            "subtitle": "Full Source Code, Automated Scripts, and Tableau Public Live Deployment",
            "student": "Presenter: Avishkar Padavi | SkillWallet Project Delivery",
            "details": "Tableau Public: Verified Live Link (101 Records, 23 Columns)\nGitHub: https://github.com/Avish-beep/Skill-wallet-project\nDeliverables: Video Walkthrough + Tableau Public + Cloud Drive Evidence",
            "script": (
                "In conclusion, our project 'Analysing Mental Health in Student Ecosystem' successfully provides a transparent, data-driven, "
                "and visually compelling foundation for institutional wellness policy. "
                "Key policy recommendations include: establishing proactive, confidential mental health screenings, "
                "launching stigma-reduction campaigns to address the ninety point six percent care gap, and integrating wellness counseling "
                "into high-achieving academic programs. "
                "All project assets—including our reproducible Python ETL scripts, Tableau workbook files, high-resolution evidence renders, "
                "and the live Tableau Public interactive dashboard—are fully documented and published. "
                "Thank you very much for your time and evaluation."
            )
        }
    ]

    print("Step 1: Generating detailed audio voiceover for all 12 slides...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 148) # Natural, measured academic cadence

    # Fonts
    try:
        font_large = ImageFont.truetype("arial.ttf", 50)
        font_med = ImageFont.truetype("arial.ttf", 32)
        font_small = ImageFont.truetype("arial.ttf", 25)
    except:
        font_large = ImageFont.load_default()
        font_med = ImageFont.load_default()
        font_small = ImageFont.load_default()

    width, height, fps = 1920, 1080, 30
    slide_video_files = []

    for idx, slide in enumerate(slides):
        audio_file = os.path.join(temp_dir, f"{slide['id']}.wav")
        engine.save_to_file(slide["script"], audio_file)
        engine.runAndWait()
        
        raw_dur = get_audio_duration(audio_file)
        dur = raw_dur + 1.5 # Natural transition buffer
        
        # Build image
        if slide["type"] == "title":
            pil_img = Image.new("RGB", (width, height), color=(15, 23, 42))
            draw = ImageDraw.Draw(pil_img)
            draw.rectangle([(0, 0), (width, 16)], fill=(59, 130, 246))
            draw.rectangle([(0, height-24), (width, height)], fill=(30, 41, 59))
            draw.text((width // 2, 320), slide["title"], fill=(255, 255, 255), font=font_large, anchor="mm")
            draw.text((width // 2, 420), slide["subtitle"], fill=(147, 197, 253), font=font_med, anchor="mm")
            draw.text((width // 2, 560), slide["student"], fill=(52, 211, 153), font=font_med, anchor="mm")
            for i, line in enumerate(slide["details"].split("\n")):
                draw.text((width // 2, 650 + (i * 45)), line, fill=(203, 213, 225), font=font_small, anchor="mm")
        else:
            banner_height = 110
            pil_img = Image.new("RGB", (width, height), color=(241, 245, 249))
            draw = ImageDraw.Draw(pil_img)
            draw.rectangle([(0, 0), (width, banner_height)], fill=(15, 23, 42))
            draw.rectangle([(0, 0), (width, 8)], fill=(37, 99, 235))
            draw.text((40, 26), slide["title"], fill=(255, 255, 255), font=font_med)
            draw.text((40, 68), slide["subtitle"], fill=(147, 197, 253), font=font_small)
            draw.rectangle([(0, height - 45), (width, height)], fill=(30, 41, 59))
            draw.text((40, height - 32), "Student: Avishkar Padavi | Analysing Mental Health in Student Ecosystem | SkillWallet Demo", fill=(203, 213, 225), font=font_small)
            
            raw_img = Image.open(slide["path"])
            avail_w = width - 40
            avail_h = height - banner_height - 65
            raw_img.thumbnail((avail_w, avail_h), Image.Resampling.LANCZOS)
            paste_x = (width - raw_img.width) // 2
            paste_y = banner_height + (avail_h - raw_img.height) // 2 + 10
            pil_img.paste(raw_img, (paste_x, paste_y))
            
        slide_img_path = os.path.join(temp_dir, f"{slide['id']}.png")
        pil_img.save(slide_img_path)
        
        # Render segment
        segment_mp4 = os.path.join(temp_dir, f"{slide['id']}.mp4")
        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", slide_img_path,
            "-i", audio_file,
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "ultrafast",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", str(dur),
            segment_mp4
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        slide_video_files.append(segment_mp4)
        print(f"Slide {idx + 1}/{len(slides)} generated ({dur:.1f}s)")

    # Concatenate all 12 slides
    print("Step 2: Merging 12 segments into final master presentation...")
    concat_list = os.path.join(temp_dir, "concat.txt")
    with open(concat_list, "w") as f:
        for seg in slide_video_files:
            f.write(f"file '{seg.replace(chr(92), '/')}'\n")

    final_doc_path = r"C:\Skillwallet\docs\project_explanation_video.mp4"
    desktop_path = r"C:\Users\Avishkar\Desktop\Analysing_Mental_Health_Avishkar_Padavi.mp4"

    concat_cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        final_doc_path
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    import shutil
    shutil.copy2(final_doc_path, desktop_path)
    
    total_time = sum([get_audio_duration(os.path.join(temp_dir, f"{s['id']}.wav")) + 1.5 for s in slides])
    print(f"Master 7-minute presentation completed! Total Duration: {total_time/60:.2f} minutes")
    print(f"Saved to: {desktop_path}")

if __name__ == "__main__":
    build_7min_presentation()
