"""Build original static binary artwork. Runtime image dimming is owned by OpenClaw."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import random
random.seed(314)
w,h=1600,1000
base=Image.new('RGBA',(w,h),'#061009')
layer=Image.new('RGBA',(w,h))
d=ImageDraw.Draw(layer)
font=ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',20)
for x in range(12,w,38):
    strength=.18+.82*(abs(x-w/2)/(w/2))**1.4
    for stream in range(2):
        y=random.randrange(-450,h)
        length=random.randrange(9,31)
        for i in range(length):
            # Bright source compensates for the host's contrast-preserving scrim.
            alpha=min(255,int((120+240*i/length)*strength))
            d.text((x,y+i*27),random.choice('01'),font=font,fill=(158,255,188,alpha))
layer=layer.filter(ImageFilter.GaussianBlur(1.0))
Image.alpha_composite(base,layer).convert('RGB').save(
    Path(__file__).resolve().parents[1]/'assets/binary-canopy-dark.webp',quality=94)
