# 🎬 Subtitle Creator

This project converts `.srt` subtitle files into styled `.ass` format and burns them into videos using `ffmpeg`.

## ✅ Features

- Converts standard `.srt` subtitles to `.ass` with custom fonts, sizes, and positions
- Burns subtitles into `.mp4` video with style
- Supports Chinese and English subtitles
- Editable font size, margin, and subtitle position
- Created using Python + FFmpeg

## 📁 File Structure
Subtitle Creator/

srt_to_ass.py # Converts .srt to .ass with custom style

zhuang.mp4 # Input video file

zhuang_en.srt # English subtitle file

zhuang_en.ass # Styled ASS subtitle (output)

zhuang_with_styled_subs.mp4 # Final output with subtitles

requirements.txt # Dependencies

README.md # This file


## 💡 How to Use

1. Place your `.srt` and `.mp4` files in the same directory.
2. Run the conversion script:

   ```bash
   python srt_to_ass.py
3. Burn subtitles into video using ffmpeg:
ffmpeg -i zhuang.mp4 -vf "ass=zhuang_en.ass" -c:a copy zhuang_with_styled_subs.mp4

📦 Requirements
Install dependencies:
pip install -r requirements.txt

📌 Notes
To adjust font size, style, and position, modify the [V4+ Styles] section in the .ass file.

This script does not require a virtual environment but can run in one.

🧠 Inspiration
Includes translated quotes from Wang Xiangzhai on Zhan Zhuang (站桩) – a standing meditation and internal martial art practice.

📷 Preview
<img src="https://user-images.githubusercontent.com/..." alt="Subtitle Preview" width="600" />

👨‍💻 Author
Lei Wang – built using Python, FFmpeg, and pysubs2.