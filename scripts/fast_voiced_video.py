import os
import sys
import subprocess
import pyttsx3
import imageio_ffmpeg
import wave

def generate_voiceover():
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    output_audio = r"C:\Skillwallet\docs\voiceover.wav"
    
    script = (
        "Hello everyone. My name is Avishkar Padavi. "
        "Today I am presenting my Data Analytics with Tableau project titled: Analysing Mental Health in Student Ecosystem. "
        "This project investigates psychological distress, comorbidity, and treatment-seeking patterns across university students. "
        "Here on our live Tableau Public dashboard, our surveyed cohort consists of one hundred and one students. "
        "Twenty-eight students are classified in the high comorbidity risk group, thirty-six in moderate risk, and fifty-eight symptomatic students remain untreated. "
        "Looking at our clinical treatment gap dashboard, the most critical finding in our investigation is that ninety point six percent of symptomatic students "
        "have never accessed clinical mental health consultation, exposing an urgent campus healthcare deficit. "
        "Analyzing the risk distribution, thirty-six point six percent of students are low risk, thirty-five point six percent are moderate risk, "
        "and twenty-seven point seven percent suffer from concurrent high risk conditions. "
        "Examining conditions across gender cohorts, depression, anxiety, and panic attacks are widely present across both female and male students. "
        "Looking at academic performance, high risk students maintain an average CGPA midpoint of three point four five, "
        "proving that high academic achievers also struggle with significant psychological distress. "
        "This risk distribution spans across all academic disciplines, including Engineering, Computer Science, and Arts. "
        "All data pipelines, clean datasets, and Tableau workbooks are documented and published. Thank you."
    )
    
    print("Generating speech audio...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 155)
    engine.save_to_file(script, output_audio)
    engine.runAndWait()
    print("Speech audio generated!")

    input_video = r"C:\Skillwallet\docs\project_explanation_video.mp4"
    final_output = r"C:\Skillwallet\docs\Analysing_Mental_Health_Avishkar_Padavi_Voiced.mp4"
    desktop_output = r"C:\Users\Avishkar\Desktop\Analysing_Mental_Health_Avishkar_Padavi.mp4"

    print("Merging speech with video...")
    cmd = [
        ffmpeg_exe, "-y",
        "-i", input_video,
        "-i", output_audio,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        final_output
    ]
    subprocess.run(cmd, check=True)

    import shutil
    shutil.copy2(final_output, desktop_output)
    print("Voiced video successfully created on Desktop!")

if __name__ == "__main__":
    generate_voiceover()
