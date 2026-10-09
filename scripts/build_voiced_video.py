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

def build_voiced_video():
    temp_dir = r"C:\Skillwallet\docs\temp_media"
    os.makedirs(temp_dir, exist_ok=True)
    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # Initialize TTS
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) # Natural clear pacing
    
    slides = [
        {
            "id": "slide_1",
            "type": "title",
            "title": "Analysing Mental Health in Student Ecosystem",
            "subtitle": "Data Analytics with Tableau | SkillWallet Project Walkthrough",
            "student": "Student: Avishkar Padavi",
            "details": "Indira College of Engineering and Management | Domain: Healthcare Analytics",
            "script": "Hello everyone. My name is Avishkar Padavi. Today I am presenting my Data Analytics with Tableau project titled Analysing Mental Health in Student Ecosystem. In this project, we investigate psychological distress, comorbidity, and treatment-seeking patterns across university students."
        },
        {
            "id": "slide_2",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\dashboard_overview.png",
            "title": "Interactive Executive Dashboard Overview (Tableau Public)",
            "subtitle": "Cohort Size: 101 Students | High Risk: 28 | Moderate: 36 | Untreated: 58",
            "script": "Here is our primary Tableau Public dashboard. Our cohort consists of one hundred and one surveyed students. Twenty-eight students are classified in the high comorbidity risk group, thirty-six in moderate risk, and fifty-eight symptomatic students remain untreated."
        },
        {
            "id": "slide_3",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\dashboard_treatment.png",
            "title": "Clinical Mental Health Risk & Specialist Treatment Gap",
            "subtitle": "Alarming Insight: 90.6% of symptomatic students have never sought specialist care",
            "script": "This is our clinical treatment gap dashboard. The most critical finding in our investigation is that ninety point six percent of symptomatic students have never accessed clinical mental health consultation, exposing an urgent campus healthcare deficit."
        },
        {
            "id": "slide_4",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\mental_health_risk.png",
            "title": "Mental Health Risk Stratification Across Cohort",
            "subtitle": "Low Risk: 36.6% | Moderate Risk: 35.6% | High Comorbidity Risk: 27.7%",
            "script": "Analyzing the risk distribution, thirty-six point six percent of students are low risk, thirty-five point six percent are moderate risk, and twenty-seven point seven percent suffer from concurrent high risk conditions."
        },
        {
            "id": "slide_5",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\conditions_by_gender.png",
            "title": "Self-Reported Conditions Stratified by Gender",
            "subtitle": "Female Cohort (N=75) & Male Cohort (N=26) Condition Burden Comparison",
            "script": "Examining conditions across gender cohorts, we observe depression, anxiety, and panic attacks present in both female and male students, with substantial comorbidity across disciplines."
        },
        {
            "id": "slide_6",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\treatment_gap.png",
            "title": "Campus Care Gap: Symptomatic vs. Treatment Seeking",
            "subtitle": "58 Symptomatic Students Untreated (90.6% care gap in higher education)",
            "script": "Fifty-eight symptomatic students have not sought treatment, while only six students have sought specialist help. This highlights the vital need for institutional counseling access."
        },
        {
            "id": "slide_7",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\cgpa_risk.png",
            "title": "Academic Performance (CGPA Midpoint) Across Risk Tiers",
            "subtitle": "Mean CGPA Midpoint: 3.45 in High Risk Group (Distress spans high academic achievers)",
            "script": "Looking at academic performance, high risk students maintain an average CGPA midpoint of three point four five. This proves that high academic performers also struggle with significant mental health distress."
        },
        {
            "id": "slide_8",
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\faculty_risk.png",
            "title": "Risk Prevalence Across Academic Faculties & Disciplines",
            "subtitle": "Engineering, Computer Science, and Humanities Comorbidity Distribution",
            "script": "The risk distribution spans across all departments, including Engineering, Computer Science, and Arts, demonstrating that mental health is a campus wide priority."
        },
        {
            "id": "slide_9",
            "type": "title",
            "title": "Conclusion & Verified Project Links",
            "subtitle": "Tableau Public Live Dashboard & Reproducible Python Pipeline",
            "student": "Presenter: Avishkar Padavi",
            "details": "GitHub: https://github.com/Avish-beep/Skill-wallet-project\nTableau Public: Verified Live Deployment",
            "script": "In conclusion, our project provides reproducible data pipelines and verified Tableau dashboards for campus wellness administrators. Thank you for your time."
        }
    ]
    
    # Fonts
    try:
        font_large = ImageFont.truetype("arial.ttf", 52)
        font_med = ImageFont.truetype("arial.ttf", 34)
        font_small = ImageFont.truetype("arial.ttf", 26)
    except:
        font_large = ImageFont.load_default()
        font_med = ImageFont.load_default()
        font_small = ImageFont.load_default()

    width, height, fps = 1920, 1080, 30
    slide_video_files = []

    print("Step 1: Generating audio and video segments for each slide...")

    for idx, slide in enumerate(slides):
        audio_file = os.path.join(temp_dir, f"{slide['id']}.wav")
        engine.save_to_file(slide["script"], audio_file)
        engine.runAndWait()
        
        duration = get_audio_duration(audio_file) + 1.2 # extra pause
        total_frames = int(duration * fps)
        
        # Build slide image
        if slide["type"] == "title":
            pil_img = Image.new("RGB", (width, height), color=(15, 23, 42))
            draw = ImageDraw.Draw(pil_img)
            draw.rectangle([(0, 0), (width, 16)], fill=(59, 130, 246))
            draw.rectangle([(0, height-24), (width, height)], fill=(30, 41, 59))
            draw.text((width // 2, 340), slide["title"], fill=(255, 255, 255), font=font_large, anchor="mm")
            draw.text((width // 2, 440), slide["subtitle"], fill=(147, 197, 253), font=font_med, anchor="mm")
            draw.text((width // 2, 580), slide["student"], fill=(52, 211, 153), font=font_med, anchor="mm")
            for i, line in enumerate(slide["details"].split("\n")):
                draw.text((width // 2, 660 + (i * 45)), line, fill=(203, 213, 225), font=font_small, anchor="mm")
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
        
        # Combine image + audio into slide mp4 using ffmpeg
        segment_mp4 = os.path.join(temp_dir, f"{slide['id']}.mp4")
        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", slide_img_path,
            "-i", audio_file,
            "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            segment_mp4
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        slide_video_files.append(segment_mp4)
        print(f"Slide {idx + 1}/{len(slides)} generated with audio ({duration:.1f}s)")

    # Step 2: Concatenate segments
    print("Step 2: Merging all narrated video segments...")
    concat_list_file = os.path.join(temp_dir, "concat_list.txt")
    with open(concat_list_file, "w") as f:
        for seg in slide_video_files:
            f.write(f"file '{seg.replace(chr(92), '/')}'\n")

    final_doc_path = r"C:\Skillwallet\docs\project_explanation_video.mp4"
    desktop_path = r"C:\Users\Avishkar\Desktop\Analysing_Mental_Health_Avishkar_Padavi.mp4"

    concat_cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        final_doc_path
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Copy to Desktop
    import shutil
    shutil.copy2(final_doc_path, desktop_path)
    
    print(f"Voiced Video successfully completed!")
    print(f"Saved to: {desktop_path}")
    print(f"File size: {os.path.getsize(desktop_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    build_voiced_video()
