import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_presentation_video():
    output_dir = r"C:\Skillwallet\docs"
    os.makedirs(output_dir, exist_ok=True)
    output_video_path = os.path.join(output_dir, "project_explanation_video.mp4")
    
    # Target 1920x1080 @ 30 FPS
    width = 1920
    height = 1080
    fps = 30
    
    # Slides definition
    slides = [
        {
            "type": "title",
            "title": "Analysing Mental Health in Student Ecosystem",
            "subtitle": "Data Analytics with Tableau | SkillWallet Project Walkthrough",
            "student": "Student: Avishkar Padavi",
            "details": "Indira College of Engineering and Management | Domain: Healthcare Analytics",
            "duration": 10
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\dashboard_overview.png",
            "title": "Interactive Executive Dashboard Overview (Tableau Public)",
            "subtitle": "Cohort Size: 101 Students | High Risk: 28 | Moderate: 36 | Untreated: 58",
            "duration": 18
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\dashboard_treatment.png",
            "title": "Clinical Mental Health Risk & Specialist Treatment Gap",
            "subtitle": "Alarming Insight: 90.6% of symptomatic students have never sought specialist care",
            "duration": 18
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\mental_health_risk.png",
            "title": "Mental Health Risk Stratification Across Cohort",
            "subtitle": "Low Risk: 36.6% | Moderate Risk: 35.6% | High Comorbidity Risk: 27.7%",
            "duration": 14
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\conditions_by_gender.png",
            "title": "Self-Reported Conditions Stratified by Gender",
            "subtitle": "Female Cohort (N=75) & Male Cohort (N=26) Condition Burden Comparison",
            "duration": 15
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\treatment_gap.png",
            "title": "Campus Care Gap: Symptomatic vs. Treatment Seeking",
            "subtitle": "58 Symptomatic Students Untreated (90.6% care gap in higher education)",
            "duration": 15
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\cgpa_risk.png",
            "title": "Academic Performance (CGPA Midpoint) Across Risk Tiers",
            "subtitle": "Mean CGPA Midpoint: 3.45 in High Risk Group (Distress spans high academic achievers)",
            "duration": 15
        },
        {
            "type": "image",
            "path": r"C:\Skillwallet\evidence\epic_03\faculty_risk.png",
            "title": "Risk Prevalence Across Academic Faculties & Disciplines",
            "subtitle": "Engineering, Computer Science, and Humanities Comorbidity Distribution",
            "duration": 15
        },
        {
            "type": "title",
            "title": "Conclusion & Verified Project Links",
            "subtitle": "Tableau Public Live Dashboard & Reproducible Python Pipeline",
            "student": "Presenter: Avishkar Padavi",
            "details": "GitHub: https://github.com/Avish-beep/Skill-wallet-project\nTableau Public: Verified Live Deployment",
            "duration": 12
        }
    ]
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    # Try system fonts
    font_large = None
    font_med = None
    font_small = None
    try:
        font_large = ImageFont.truetype("arial.ttf", 52)
        font_med = ImageFont.truetype("arial.ttf", 34)
        font_small = ImageFont.truetype("arial.ttf", 26)
    except:
        font_large = ImageFont.load_default()
        font_med = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    print(f"Rendering video to {output_video_path}...")
    
    for idx, slide in enumerate(slides):
        total_frames = slide["duration"] * fps
        
        # Prepare background
        if slide["type"] == "title":
            pil_img = Image.new("RGB", (width, height), color=(15, 23, 42)) # Deep navy
            draw = ImageDraw.Draw(pil_img)
            
            # Decorative banner
            draw.rectangle([(0, 0), (width, 16)], fill=(59, 130, 246)) # Blue accent
            draw.rectangle([(0, height-24), (width, height)], fill=(30, 41, 59))
            
            # Title text
            draw.text((width // 2, 340), slide["title"], fill=(255, 255, 255), font=font_large, anchor="mm")
            draw.text((width // 2, 440), slide["subtitle"], fill=(147, 197, 253), font=font_med, anchor="mm")
            draw.text((width // 2, 580), slide["student"], fill=(52, 211, 153), font=font_med, anchor="mm")
            
            # Multiline details
            details = slide["details"].split("\n")
            for i, line in enumerate(details):
                draw.text((width // 2, 660 + (i * 45)), line, fill=(203, 213, 225), font=font_small, anchor="mm")
                
            frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            for _ in range(total_frames):
                out.write(frame)
                
        elif slide["type"] == "image":
            # Header banner with metadata
            banner_height = 110
            base_img = Image.new("RGB", (width, height), color=(241, 245, 249))
            draw = ImageDraw.Draw(base_img)
            
            # Header bar
            draw.rectangle([(0, 0), (width, banner_height)], fill=(15, 23, 42))
            draw.rectangle([(0, 0), (width, 8)], fill=(37, 99, 235))
            draw.text((40, 26), slide["title"], fill=(255, 255, 255), font=font_med)
            draw.text((40, 68), slide["subtitle"], fill=(147, 197, 253), font=font_small)
            
            # Footer bar
            draw.rectangle([(0, height - 45), (width, height)], fill=(30, 41, 59))
            draw.text((40, height - 32), "Student: Avishkar Padavi | Analysing Mental Health in Student Ecosystem | SkillWallet Demo", fill=(203, 213, 225), font=font_small)
            
            # Place screenshot
            img_path = slide["path"]
            if os.path.exists(img_path):
                raw_img = Image.open(img_path)
                avail_w = width - 40
                avail_h = height - banner_height - 65
                
                # Resize with aspect ratio
                raw_img.thumbnail((avail_w, avail_h), Image.Resampling.LANCZOS)
                paste_x = (width - raw_img.width) // 2
                paste_y = banner_height + (avail_h - raw_img.height) // 2 + 10
                base_img.paste(raw_img, (paste_x, paste_y))
                
            frame = cv2.cvtColor(np.array(base_img), cv2.COLOR_RGB2BGR)
            for _ in range(total_frames):
                out.write(frame)
                
        print(f"Slide {idx + 1}/{len(slides)} rendered ({slide['duration']}s).")
        
    out.release()
    print("Video generation successfully completed!")
    print(f"File size: {os.path.getsize(output_video_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_presentation_video()
