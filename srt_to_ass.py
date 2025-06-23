from pysubs2 import SSAFile, SSAEvent, SSAStyle
import pysubs2

subs = pysubs2.load("zhuang_en.srt", encoding="utf-8")

# Optional: Define your own style
style = SSAStyle()
style.fontname = "Arial"
style.fontsize = 32
style.primarycolor = pysubs2.Color(255, 255, 255, 0)  # white
style.backcolor = pysubs2.Color(0, 0, 0, 128)         # semi-transparent black
style.bold = True
style.alignment = pysubs2.Alignment.BOTTOM_CENTER
style.marginl = 20
style.marginr = 20
style.marginv = 30
subs.styles["MyStyle"] = style

# Apply style to all lines
for line in subs:
    line.style = "MyStyle"

subs.save("zhuang_en_fixed.ass")
