from deep_translator import GoogleTranslator

input_file = "zhuang_cn.srt"
output_file = "zhuang_en.srt"

translator = GoogleTranslator(source='zh-CN', target='en')


with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    lines = fin.readlines()
    for line in lines:
        if "-->" in line or line.strip().isdigit() or line.strip() == "":
            fout.write(line)  # keep timestamp, numbering, and spacing
        else:
            translated = translator.translate(line.strip())
            fout.write(translated + "\n")

print(f"✅ English subtitles saved to {output_file}")
