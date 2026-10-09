import os
import sys

# Import slides definition
sys.path.insert(0, r"C:\Skillwallet")
from scripts.generate_indian_voice_video import slides

scale = 0.625 # atempo=1.6 multiplier
cur_time = 0.0

srt_entries = []
vtt_entries = ['WEBVTT\n']
transcript_lines = [
    '# Project Presentation Transcript\n\n',
    '**Project:** Analysing Mental Health in Student Ecosystem  \n',
    '**Student:** Avishkar Padavi  \n',
    '**Duration:** 06:37  \n',
    '**Language:** Indian English (en-IN-PrabhatNeural)\n\n---\n\n'
]
scene_plan_lines = [
    '# Video Scene Plan\n\n',
    '| Scene | Time Range | Title | Content / Visual | Key Spoken Points |\n',
    '| :---: | :---: | :--- | :--- | :--- |\n'
]
script_lines = [
    '# Full Narration Presentation Script\n\n',
    '**Project Title:** Analysing Mental Health in Student Ecosystem  \n',
    '**Presenter:** Avishkar Padavi  \n',
    '**Institution:** Indira College of Engineering and Management  \n',
    '**Domain:** Healthcare Analytics & Data Analytics with Tableau  \n',
    '**Accent & Voice:** Indian English (`en-IN-PrabhatNeural`)  \n',
    '**Total Duration:** 06:37 (6 minutes 37 seconds)\n\n---\n\n'
]

def fmt_srt(t):
    hrs = int(t // 3600)
    mins = int((t % 3600) // 60)
    secs = int(t % 60)
    millis = int((t - int(t)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def fmt_vtt(t):
    hrs = int(t // 3600)
    mins = int((t % 3600) // 60)
    secs = int(t % 60)
    millis = int((t - int(t)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}.{millis:03d}"

for idx, slide in enumerate(slides):
    dur_raw = slide.get("duration", 40.0)
    dur_scaled = dur_raw * scale
    start_t = cur_time
    end_t = cur_time + dur_scaled
    cur_time = end_t
    
    # SRT
    srt_entries.append(f"{idx+1}\n{fmt_srt(start_t)} --> {fmt_srt(end_t)}\n{slide['script']}\n")
    
    # VTT
    vtt_entries.append(f"{idx+1}\n{fmt_vtt(start_t)} --> {fmt_vtt(end_t)}\n{slide['script']}\n")
    
    # Transcript
    transcript_lines.append(f"### Scene {idx+1}: {slide['title']} ({fmt_vtt(start_t)[:8]} - {fmt_vtt(end_t)[:8]})\n\n{slide['script']}\n\n")
    
    # Scene Plan
    vis_desc = "Title Slide Graphic" if slide['type'] == 'title' else "High-Res Dashboard Evidence"
    scene_plan_lines.append(f"| {idx+1} | {fmt_vtt(start_t)[:8]} - {fmt_vtt(end_t)[:8]} | {slide['title']} | {vis_desc} | {slide['script'][:90]}... |\n")
    
    # Script
    script_lines.append(f"## Slide {idx+1}: {slide['title']}\n- **Timestamp:** {fmt_vtt(start_t)[:8]} – {fmt_vtt(end_t)[:8]}\n- **Visual:** {vis_desc}\n- **Spoken Text:**\n  \"{slide['script']}\"\n\n---\n\n")

os.makedirs(r"C:\Skillwallet\video", exist_ok=True)

with open(r"C:\Skillwallet\video\captions.srt", "w", encoding="utf-8") as f:
    f.write("\n".join(srt_entries))

with open(r"C:\Skillwallet\video\captions.vtt", "w", encoding="utf-8") as f:
    f.write("\n".join(vtt_entries))

with open(r"C:\Skillwallet\video\transcript.md", "w", encoding="utf-8") as f:
    f.write("".join(transcript_lines))

with open(r"C:\Skillwallet\video\scene_plan.md", "w", encoding="utf-8") as f:
    f.write("".join(scene_plan_lines))

with open(r"C:\Skillwallet\video\script.md", "w", encoding="utf-8") as f:
    f.write("".join(script_lines))

print("All video artifacts written successfully to C:\\Skillwallet\\video\\")
