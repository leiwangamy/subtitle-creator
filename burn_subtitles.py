import subprocess

video_file = "zhuang.mp4"
subtitle_file = "zhuang_en.srt"
output_file = "zhuang_with_en_subs.mp4"

# FFmpeg command
cmd = [
    "ffmpeg",
    "-i", video_file,
    "-vf", f"subtitles={subtitle_file}",
    "-c:a", "copy",
    output_file
]

subprocess.run(cmd)
print(f"✅ Output saved as {output_file}")
