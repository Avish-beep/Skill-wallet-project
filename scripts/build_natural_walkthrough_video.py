import os
import sys
import asyncio
import subprocess
import edge_tts
import imageio_ffmpeg

VOICE = "en-IN-PrabhatNeural"
# Natural measured conversational speed (125-135 words per minute)
RATE = "-14%" 

slides = [
    {
        "id": "s01_intro",
        "title": "Project Introduction & Student Context",
        "visual_type": "website",
        "frame_file": "w01_hero.png",
        "script": (
            "Hello everyone, respected evaluators and faculty members. My name is Avishkar Padavi, and today I am pleased "
            "to present my capstone data analytics project titled: Analysing Mental Health in Student Ecosystem. "
            "Student mental wellness across university campuses has become one of the most pressing challenges in higher education. "
            "Academic pressures, exam competition, and career uncertainties create significant psychological strain. "
            "However, many institutions lack empirical, data-driven systems to monitor student distress or evaluate counseling intervention gaps. "
            "In this project, I developed an end-to-end analytics workflow using Python for reproducible data preparation, and Tableau Desktop for interactive visual intelligence."
        )
    },
    {
        "id": "s02_problem",
        "title": "Problem Statement & Analytical Boundaries",
        "visual_type": "website",
        "frame_file": "w02_problem.png",
        "script": (
            "Here in our project framework, we define clear investigative objectives and ethical boundaries. "
            "Our study analyzes empirical survey records from one hundred and one university students. "
            "I want to emphasize that all responses represent self-reported psychological indicators rather than formal clinical diagnoses. "
            "Furthermore, our findings are observational and correlational. "
            "In strict accordance with data integrity, we excluded generic template fields such as sleep hours, attendance rate, or stress scores, "
            "focusing entirely on authentic, verified survey dimensions."
        )
    },
    {
        "id": "s03_methodology",
        "title": "Data Engineering Pipeline (Epic 1 & Epic 2)",
        "visual_type": "website",
        "frame_file": "w03_methodology.png",
        "script": (
            "Moving to our methodology, we established a four-stage reproducible pipeline. "
            "In Epic 1, Data Collection, we ingested the immutable survey dataset and validated its SHA-256 checksum. "
            "In Epic 2, Data Preparation, we built an automated Python ETL script using pandas. "
            "We imputed a single missing age value using the cohort median of nineteen, cleaned CGPA ranges into numeric midpoints, "
            "and standardized diverse majors into seven academic faculties. "
            "We engineered twelve derived analytical features, including concurrent condition counts and clinical care gap indicators, "
            "producing a clean dataset with zero missing cells and zero duplicate rows."
        )
    },
    {
        "id": "s04_tableau_preview",
        "title": "Tableau Visual Intelligence & Publishing Status",
        "visual_type": "website",
        "frame_file": "w04_dashboard.png",
        "script": (
            "Here is the interactive Tableau visual intelligence section of our website. "
            "In our local validated workbook, we developed ten dedicated worksheets and two responsive executive dashboards. "
            "Our primary dashboard organizes four key performance indicator cards: total cohort size of one hundred and one students, "
            "twenty-eight high-risk students, thirty-six moderate-risk students, and fifty-eight untreated symptomatic students. "
            "We have provided a clear status notice: while our local Tableau Desktop workbook is fully verified against our authentic dataset, "
            "republishing over the older generic template on Tableau Public remains in progress."
        )
    },
    {
        "id": "s05_findings",
        "title": "Key Analytical Findings & The 90.6% Care Gap",
        "visual_type": "website",
        "frame_file": "w05_findings.png",
        "script": (
            "Now let us examine our key analytical findings, recalculated directly from the validated dataset. "
            "The most critical discovery is the ninety point six percent campus clinical care deficit. "
            "Out of sixty-four students reporting at least one mental health condition, fifty-eight have never sought treatment from a psychiatrist or counselor. "
            "Only six symptomatic students accessed specialist care. "
            "Furthermore, sixty-three point four percent of students experience at least one condition, with twenty-seven point seven percent in the high comorbidity tier. "
            "Condition indicators are closely distributed across the cohort: depression at thirty-four point seven percent, anxiety at thirty-three point seven percent, and panic attacks at thirty-two point seven percent."
        )
    },
    {
        "id": "s06_story",
        "title": "Project Story & The High-Achiever Paradox",
        "visual_type": "website",
        "frame_file": "w06_story.png",
        "script": (
            "In our guided Project Story section, we explore six sequential chapters of the student mental health journey. "
            "One of our most compelling insights is the high-achiever paradox. "
            "Common assumptions suggest that only academically struggling students face mental distress. "
            "However, our data demonstrates that high-risk comorbidity students maintain an impressive average CGPA midpoint of three point four five out of four point zero. "
            "Top academic performers frequently experience acute anxiety and burnout, concealing their distress behind stellar grades. "
            "In addition, comorbidity spans both male and female students across engineering, computing, and humanities departments."
        )
    },
    {
        "id": "s07_video_player",
        "title": "Presentation Video Player & Chapter Markers",
        "visual_type": "website",
        "frame_file": "w07_video.png",
        "script": (
            "This is our dedicated presentation video walkthrough section on the website. "
            "It features an accessible native video player with synchronized WebVTT subtitles, downloadable high-definition MP4 media, "
            "and interactive chapter timestamps. "
            "Viewers can navigate seamlessly between our introduction, data engineering pipeline, Tableau dashboard review, and policy recommendations."
        )
    },
    {
        "id": "s08_docs_conclusion",
        "title": "Documentation, Live Resources & Conclusion",
        "visual_type": "website",
        "frame_file": "w08_docs.png",
        "script": (
            "Finally, our website provides direct links to our GitHub repository, comprehensive data preparation reports, "
            "visualization dictionaries, and responsive testing evidence. "
            "In conclusion, this project delivers an empirical, transparent foundation for university counseling centers to conduct proactive screenings "
            "and eliminate mental health stigma. "
            "All source code, automated scripts, and portfolio assets are published under Avishkar Padavi on GitHub. "
            "Thank you very much for your time and kind consideration."
        )
    }
]

async def generate_voiced_presentation():
    temp_dir = r"C:\Skillwallet\docs\natural_walkthrough"
    os.makedirs(temp_dir, exist_ok=True)
    frames_dir = r"C:\Skillwallet\evidence\walkthrough_frames"
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    print("Step 1: Generating natural-paced Indian English voiceover (RATE: -14%)...")
    audio_files = []
    durations = []
    
    for idx, slide in enumerate(slides):
        a_path = os.path.join(temp_dir, f"{slide['id']}.mp3")
        communicate = edge_tts.Communicate(slide["script"], VOICE, rate=RATE, pitch="+0Hz")
        await communicate.save(a_path)
        audio_files.append(a_path)
        
        # probe duration
        probe_cmd = [ffmpeg_exe, "-i", a_path]
        p = subprocess.run(probe_cmd, stderr=subprocess.PIPE, text=True)
        dur = 40.0
        for l in p.stderr.splitlines():
            if "Duration:" in l:
                t_str = l.split("Duration:")[1].split(",")[0].strip()
                h, m, s = t_str.split(":")
                dur = float(h)*3600 + float(m)*60 + float(s) + 1.2
                break
        durations.append(dur)
        slide["duration"] = dur
        print(f"Slide {idx+1}/{len(slides)}: {slide['title']} -> {dur:.1f}s")
        
    total_time = sum(durations)
    print(f"\nTotal Walkthrough Video Duration: {total_time:.1f}s ({total_time/60:.2f} minutes)")
    
    # Step 2: Render individual segments using real website screenshots
    print("\nStep 2: Rendering video segments from real website frames...")
    segment_files = []
    
    for idx, slide in enumerate(slides):
        img_p = os.path.join(frames_dir, slide["frame_file"])
        aud_p = audio_files[idx]
        seg_mp4 = os.path.join(temp_dir, f"{slide['id']}.mp4")
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
        
    # Step 3: Concat all segments
    print("\nStep 3: Merging all segments into final presentation video...")
    concat_txt = os.path.join(temp_dir, "concat.txt")
    with open(concat_txt, "w") as f:
        for seg in segment_files:
            f.write(f"file '{seg.replace(chr(92), '/')}'\n")
            
    final_video_path = r"C:\Skillwallet\video\project_presentation.mp4"
    website_video_path = r"C:\Skillwallet\website\public\video\project_presentation.mp4"
    desktop_video_path = r"C:\Users\Avishkar\Desktop\Analysing_Mental_Health_Avishkar_Padavi.mp4"
    
    cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-c", "copy",
        final_video_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    import shutil
    shutil.copy2(final_video_path, website_video_path)
    shutil.copy2(final_video_path, desktop_video_path)
    
    # Generate updated thumbnail from hero frame
    thumbnail_path = r"C:\Skillwallet\video\thumbnail.png"
    website_thumb_path = r"C:\Skillwallet\website\public\video\thumbnail.png"
    shutil.copy2(os.path.join(frames_dir, "w01_hero.png"), thumbnail_path)
    shutil.copy2(os.path.join(frames_dir, "w01_hero.png"), website_thumb_path)
    
    print("\nSUCCESS! Final walkthrough video generated and copied to all locations!")
    print(f"Final Path: {final_video_path}")
    print(f"File Size: {os.path.getsize(final_video_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    asyncio.run(generate_voiced_presentation())
