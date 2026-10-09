import os
import sys

sys.path.insert(0, r"C:\Skillwallet")
from scripts.build_natural_walkthrough_video import slides

# Final adjusted timing multiplier (tempo=1.136 -> multiplier = 0.8804)
scale = 0.8804
cur_time = 0.0

srt_entries = []
vtt_entries = ['WEBVTT\n']
transcript_lines = [
    '# Project Presentation Transcript\n\n',
    '**Project:** Analysing Mental Health in Student Ecosystem  \n',
    '**Presenter:** Avishkar Padavi  \n',
    '**Duration:** 06:24 (6 minutes 24 seconds)  \n',
    '**Cadence & Accent:** Natural Indian English (`en-IN-PrabhatNeural` at ~130 WPM)\n\n---\n\n'
]
scene_plan_lines = [
    '# Video Scene Plan\n\n',
    '| Scene | Time Range | Title | Content / Visual | Key Points Spoken |\n',
    '| :---: | :---: | :--- | :--- | :--- |\n'
]
script_lines = [
    '# Full Narration Presentation Script\n\n',
    '**Project Title:** Analysing Mental Health in Student Ecosystem  \n',
    '**Presenter:** Avishkar Padavi  \n',
    '**Institution:** Indira College of Engineering and Management  \n',
    '**Domain:** Healthcare Analytics & Data Analytics with Tableau  \n',
    '**Pacing:** Natural Conversational (~130 WPM) &bull; Indian English Neural Voice  \n',
    '**Total Duration:** 06:24 (6 minutes 24 seconds)\n\n---\n\n'
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

# Scene raw durations from edge-tts
raw_durs = [65.0, 52.9, 60.9, 54.8, 64.6, 59.8, 33.9, 45.0]

for idx, slide in enumerate(slides):
    dur_raw = raw_durs[idx]
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
    scene_plan_lines.append(f"| {idx+1} | {fmt_vtt(start_t)[:8]} - {fmt_vtt(end_t)[:8]} | {slide['title']} | Real Website Walkthrough ({slide['frame_file']}) | {slide['script'][:85]}... |\n")
    
    # Script
    script_lines.append(f"## Scene {idx+1}: {slide['title']}\n- **Timestamp:** {fmt_vtt(start_t)[:8]} – {fmt_vtt(end_t)[:8]}\n- **Visual:** Real Website Screen Capture ({slide['frame_file']})\n- **Spoken Text:**\n  \"{slide['script']}\"\n\n---\n\n")

for d in [r"C:\Skillwallet\video", r"C:\Skillwallet\website\public\video"]:
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "captions.srt"), "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))
    with open(os.path.join(d, "captions.vtt"), "w", encoding="utf-8") as f:
        f.write("\n".join(vtt_entries))
    with open(os.path.join(d, "transcript.md"), "w", encoding="utf-8") as f:
        f.write("".join(transcript_lines))
    with open(os.path.join(d, "scene_plan.md"), "w", encoding="utf-8") as f:
        f.write("".join(scene_plan_lines))
    with open(os.path.join(d, "script.md"), "w", encoding="utf-8") as f:
        f.write("".join(script_lines))

print("All synchronized video documentation files updated successfully!")
