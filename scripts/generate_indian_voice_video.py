import os
import sys
import asyncio
import subprocess
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import edge_tts
import imageio_ffmpeg

VOICE = "en-IN-PrabhatNeural" # Ultra-realistic Indian Male Neural Voice

slides = [
    {
        "id": "s01",
        "type": "title",
        "title": "Analysing Mental Health in Student Ecosystem",
        "subtitle": "Data Analytics with Tableau | SkillWallet Capstone Project Walkthrough",
        "student": "Student: Avishkar Padavi",
        "details": "Indira College of Engineering and Management | Domain: Healthcare Analytics\nPlatform: SkillWallet | Guided Evaluation Walkthrough",
        "script": (
            "Hello everyone, respected evaluators and faculty members. My name is Avishkar Padavi, and today I am very excited to present "
            "my capstone data analytics project titled: Analysing Mental Health in Student Ecosystem. "
            "Across universities today, mental wellness among students has become one of the most pressing concerns. "
            "Heavy academic pressure, exam stress, social adjustment, and career uncertainties lead to significant psychological strain. "
            "Unfortunately, most college administrations do not have an empirical, data-driven system to track student distress, identify comorbidity risks, "
            "or evaluate how effectively campus counseling services are functioning. "
            "In this project, our primary goal was to take real survey data, build a clean and reproducible Python ETL pipeline, and create "
            "an interactive, responsive visual intelligence dashboard using Tableau Desktop."
        )
    },
    {
        "id": "s02",
        "type": "title",
        "title": "Data Engineering, Architecture & Integrity Standards",
        "subtitle": "Epic 1 Data Collection & Epic 2 Data Preparation Pipeline",
        "student": "Empirical Student Cohort: N = 101 Survey Records",
        "details": "Immutable Raw Data: SHA-256 Verified | Zero Fabricated Columns\nAnalytical Dataset: 101 Rows x 23 Engineered Columns",
        "script": (
            "Before diving into our charts, let me explain the data engineering behind this project. "
            "In Epic 1, Data Collection and Extraction, we ingested the raw survey dataset capturing one hundred and one university students. "
            "We audited the dataset and locked it with an SHA-256 checksum to guarantee provenance. "
            "Then in Epic 2, Data Preparation, we created an automated pipeline in Python using pandas. "
            "We handled missing age values through median imputation, standardized diverse student majors into structured academic faculties, "
            "and engineered twelve critical features—such as comorbidity count, risk classification, and clinical treatment gaps. "
            "I want to emphasize that we strictly avoided any synthetic metrics or fake fields, ensuring that our final analytical dataset of twenty-three columns is one hundred percent accurate and complete."
        )
    },
    {
        "id": "s03",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\dashboard_overview.png",
        "title": "Executive Overview Dashboard (Live Tableau Public)",
        "subtitle": "High-Density Analytical Grid: Interactive Filters, 4 Key KPIs & Multi-dimensional Panels",
        "script": (
            "Now let us look at our first interactive dashboard on Tableau Public: the Student Mental Health Overview Dashboard. "
            "This dashboard is designed with a responsive layout container and high-density cards, structured like modern executive healthcare intelligence reports. "
            "At the top, we have our four primary KPI cards: "
            "First, our total cohort comprises one hundred and one students. "
            "Second, twenty-eight students, representing twenty-seven point seven percent, are categorized in the high comorbidity risk tier. "
            "Third, thirty-six students, or thirty-five point six percent, fall under moderate risk. "
            "And fourth, an alarming fifty-eight students self-report symptomatic distress but have never received any professional medical or psychological treatment. "
            "Faculty deans and counselors can use the top interactive filters to slice the data seamlessly across gender, age groups, faculties, and risk levels."
        )
    },
    {
        "id": "s04",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\dashboard_treatment.png",
        "title": "Clinical Mental Health Risk & Specialist Treatment Gap",
        "subtitle": "Quantifying the Institutional Deficit in University Counseling Access",
        "script": (
            "Next, we move to our second specialized dashboard: Mental Health Risk and Clinical Treatment Gap. "
            "This visualization brings forward the single most shocking insight of our entire investigation. "
            "When we analyze students showing active psychological distress, a massive ninety point six percent have never consulted a clinical specialist, psychiatrist, or college counselor. "
            "In other words, only six symptomatic students out of sixty-four have ever accessed professional mental health care. "
            "This proves that the challenge in student mental health is not just about awareness, but about breaking down social stigma, confidentiality concerns, and institutional barriers to care."
        )
    },
    {
        "id": "s05",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\mental_health_risk.png",
        "title": "Cohort Risk Stratification: Low, Moderate, and High Risk",
        "subtitle": "Comorbidity Tiers Derived from Concurrent Self-Reported Conditions",
        "script": (
            "Now let us break down individual worksheets. Here is the Distribution of Mental Health Risk Levels. "
            "We systematically grouped students into three distinct risk tiers based on symptom co-occurrence: "
            "Students reporting zero conditions are classified as Low Risk, making up thirty-six point six percent of the cohort. "
            "Students reporting a single condition are categorized as Moderate Risk, comprising thirty-five point six percent. "
            "And students suffering from multiple concurrent conditions—such as co-occurring depression, anxiety, or panic attacks—are placed in the High Risk tier, representing twenty-seven point seven percent. "
            "This means that nearly two out of every three students in the campus ecosystem experience some form of mental health distress."
        )
    },
    {
        "id": "s06",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\conditions_by_gender.png",
        "title": "Within-Gender Self-Reported Conditions Analysis",
        "subtitle": "Comparative Burden across Female (N=75) and Male (N=26) Cohorts",
        "script": (
            "Here we analyze condition prevalence stratified by gender. "
            "Our surveyed cohort includes seventy-five female students and twenty-six male students. "
            "To ensure a fair analysis without sample bias, we calculated proportions within each gender group. "
            "Among female students, depression is self-reported at thirty-eight point seven percent, anxiety at thirty-two percent, and panic attacks at thirty-three point three percent. "
            "Among male students, anxiety is highest at thirty-eight point five percent, with depression and panic attacks both standing at thirty point eight percent. "
            "This shows that psychological distress affects both male and female students profoundly across all academic years."
        )
    },
    {
        "id": "s07",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\treatment_gap.png",
        "title": "In-Depth Campus Treatment Deficit: Symptomatic vs. Clinical Consultation",
        "subtitle": "90.6% Care Deficit: 58 Untreated Students vs. 6 Treated Students",
        "script": (
            "This bar chart illustrates the severity of the Student Treatment Gap. "
            "Out of sixty-four students experiencing self-reported psychological symptoms, fifty-eight students remain completely untreated, compared to only six students who sought medical help. "
            "From an administration standpoint, this data offers concrete actionable feedback: "
            "Simply having a campus counseling office is not enough. Universities must actively conduct anonymous health surveys, promote peer counseling groups, and simplify appointment scheduling so students feel safe reaching out."
        )
    },
    {
        "id": "s08",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\cgpa_risk.png",
        "title": "Academic Standing (CGPA Midpoint) Across Mental Health Risk Levels",
        "subtitle": "Challenging the Stereotype: High Academic Achievers Experience Severe Distress",
        "script": (
            "One of the most eye-opening findings of our analysis is the relationship between academic scores and mental health risk. "
            "People often assume that students who suffer from depression or anxiety are those who are failing academically. "
            "However, our data completely dispels that myth. "
            "As we see in this boxplot and stripplot visualization, students in the High Risk comorbidity group maintain an impressive average CGPA midpoint of three point four five. "
            "Similarly, moderate risk students average three point four eight. "
            "This clearly proves that high academic performers and honors students frequently experience intense anxiety and burnout, concealing their distress behind top grades."
        )
    },
    {
        "id": "s09",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\faculty_risk.png",
        "title": "Mental Health Risk Across Academic Disciplines & Faculties",
        "subtitle": "Departmental Breakdown: Engineering, IT, Sciences, and Humanities",
        "script": (
            "Looking at the breakdown across academic faculties: we mapped all student majors into seven primary disciplines: "
            "Computing and IT, Engineering, Human Sciences, Biomedical Sciences, Islamic Studies, Economics, and Languages. "
            "The data reveals that moderate and high comorbidity risks are widely spread across technical STEM fields as well as humanities programs. "
            "This proves that campus wellness programs cannot be limited to just one department; they must be integrated campus-wide."
        )
    },
    {
        "id": "s10",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\condition_count.png",
        "title": "Comorbidity Burden: Distribution of Concurrent Conditions",
        "subtitle": "Histogram Quantifying Single vs. Multiple Symptom Co-Occurrence",
        "script": (
            "This histogram represents the comorbidity distribution among students. "
            "Thirty-seven students reported zero conditions, thirty-six reported exactly one condition, "
            "seventeen students reported two concurrent conditions, and eleven students reported suffering from all three conditions simultaneously: depression, anxiety, and panic attacks. "
            "Tracking comorbidity is critical because overlapping conditions multiply emotional distress and significantly increase the risk of semester dropouts."
        )
    },
    {
        "id": "s11",
        "type": "image",
        "path": r"C:\Skillwallet\evidence\epic_03\risk_by_age_group.png",
        "title": "Risk Trajectory Across Age Groups and Undergraduate Seniority",
        "subtitle": "Underclassmen (Ages 18–20) vs. Upperclassmen (Ages 21–24)",
        "script": (
            "Examining age groups across undergraduate seniority: we compared younger underclassmen aged eighteen to twenty with senior upperclassmen aged twenty-one to twenty-four. "
            "Both groups demonstrate considerable vulnerability. "
            "Junior students face the adjustment shock of campus life and independent living, while final-year students face the stress of placement drives, competitive exams, and career uncertainty. "
            "Interventions must therefore support students at every stage of their academic journey."
        )
    },
    {
        "id": "s12",
        "type": "title",
        "title": "Conclusion, Actionable Recommendations & Project Verification",
        "subtitle": "Full Source Code, Automated Pipelines, and Tableau Public Live Deployment",
        "student": "Presenter: Avishkar Padavi | SkillWallet Project Delivery",
        "details": "Tableau Public: Verified Live Link (101 Records, 23 Columns)\nGitHub: https://github.com/Avish-beep/Skill-wallet-project\nDeliverables: Video Walkthrough + Tableau Public + Cloud Drive Evidence",
        "script": (
            "To conclude, our project Analysing Mental Health in Student Ecosystem provides a rigorous, transparent, and visually actionable framework for university administrators. "
            "Our key recommendations include: implementing anonymous screening tests, launching campus campaigns to dismantle mental health stigma, and providing structured counseling for high-performing students. "
            "All project assets—including our reproducible Python ETL pipeline, clean dataset, Tableau workbook, and the live interactive Tableau Public dashboard—are verified, documented, and published. "
            "Thank you so much for your time and kind attention."
        )
    }
]

async def generate_speech_for_slide(slide, temp_dir):
    audio_path = os.path.join(temp_dir, f"{slide['id']}.mp3")
    communicate = edge_tts.Communicate(slide["script"], VOICE, rate="-4%", pitch="+1Hz")
    await communicate.save(audio_path)
    return audio_path

async def main():
    temp_dir = r"C:\Skillwallet\docs\indian_7min"
    os.makedirs(temp_dir, exist_ok=True)
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    print("Step 1: Generating realistic Indian English voiceover with PrabhatNeural...")
    audio_files = []
    durations = []
    for idx, slide in enumerate(slides):
        print(f"Generating voice for slide {idx+1}/{len(slides)}...")
        a_path = await generate_speech_for_slide(slide, temp_dir)
        audio_files.append(a_path)
        
        # probe duration using ffprobe/ffmpeg
        probe_cmd = [
            ffmpeg_exe, "-i", a_path
        ]
        p = subprocess.run(probe_cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        # Parse duration from stderr "Duration: 00:00:32.45"
        dur = 35.0
        for line in p.stderr.splitlines():
            if "Duration:" in line:
                time_str = line.split("Duration:")[1].split(",")[0].strip()
                h, m, s = time_str.split(":")
                dur = float(h)*3600 + float(m)*60 + float(s) + 1.2
                break
        durations.append(dur)
        slide["duration"] = dur
        print(f"Slide {idx+1} duration: {dur:.1f}s")

    total_time = sum(durations)
    print(f"Total video duration: {total_time:.1f}s ({total_time/60:.2f} minutes)")

    # Step 2: Render slide graphics
    print("Step 2: Rendering slide graphics...")
    try:
        font_large = ImageFont.truetype("arial.ttf", 50)
        font_med = ImageFont.truetype("arial.ttf", 32)
        font_small = ImageFont.truetype("arial.ttf", 25)
    except:
        font_large = ImageFont.load_default()
        font_med = ImageFont.load_default()
        font_small = ImageFont.load_default()

    width, height = 1920, 1080
    for idx, slide in enumerate(slides):
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
            
        pil_img.save(os.path.join(temp_dir, f"{slide['id']}.png"))

    # Step 3: Fast encode individual segments
    print("Step 3: Rendering video segments...")
    segment_files = []
    for idx, slide in enumerate(slides):
        img_p = os.path.join(temp_dir, f"{slide['id']}.png")
        aud_p = audio_files[idx]
        seg_mp4 = os.path.join(temp_dir, f"{slide['id']}_seg.mp4")
        dur = slide["duration"]
        
        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", img_p,
            "-i", aud_p,
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "ultrafast",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", str(dur),
            seg_mp4
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        segment_files.append(seg_mp4)
        print(f"Segment {idx+1}/{len(slides)} complete.")

    # Step 4: Concat all segments
    print("Step 4: Merging all segments into final video...")
    concat_txt = os.path.join(temp_dir, "concat.txt")
    with open(concat_txt, "w") as f:
        for seg in segment_files:
            f.write(f"file '{seg.replace(chr(92), '/')}'\n")

    final_mp4 = r"C:\Skillwallet\docs\project_explanation_video.mp4"
    desktop_mp4 = r"C:\Users\Avishkar\Desktop\Analysing_Mental_Health_Avishkar_Padavi.mp4"

    cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-c", "copy",
        final_mp4
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    import shutil
    shutil.copy2(final_mp4, desktop_mp4)
    print("SUCCESS! Final 6.5+ min Indian English presentation saved to Desktop!")

if __name__ == "__main__":
    asyncio.run(main())
