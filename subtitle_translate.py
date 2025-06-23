from faster_whisper import WhisperModel

# === Settings ===
video_file = "zhuang.mp4"
model_size = "base"
language = "zh"  # For Chinese

# === Load Model ===
model = WhisperModel(model_size)

# === Transcribe Video ===
segments, _ = model.transcribe(video_file, language=language)

# === Save as SRT ===
def format_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

srt_file = "zhuang_cn.srt"
with open(srt_file, "w", encoding="utf-8") as f:
    for i, segment in enumerate(segments):
        f.write(f"{i+1}\n")
        f.write(f"{format_time(segment.start)} --> {format_time(segment.end)}\n")
        f.write(f"{segment.text.strip()}\n\n")

print(f"✅ Chinese subtitles saved to {srt_file}")
