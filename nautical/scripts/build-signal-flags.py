"""Generate editable signal-flag bunting backgrounds; rasterize separately."""
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parents[1]
B,R,Y,W,K='#164b91','#c52e37','#f7ce43','#fffdf1','#14202b'
def rect(x,y,w,h,c): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
def path(d,c):return f'<path d="{d}" fill="{c}"/>'
def stripes(cols,vertical=False):
 return ''.join(rect(i*112/len(cols),0,112/len(cols),84,c) if vertical else rect(0,i*84/len(cols),112,84/len(cols),c) for i,c in enumerate(cols))
def cross(bg,fg,diagonal=False):
 return rect(0,0,112,84,bg)+(f'<path d="M0 0L112 84M112 0L0 84" stroke="{fg}" stroke-width="13"/>' if diagonal else rect(47,0,18,84,fg)+rect(0,33,112,18,fg))
def flag(c):
 if c=='A':return path('M0 0H112L88 42 112 84H0Z',B)+rect(0,0,56,84,W)
 if c=='B':return path('M0 0H112L88 42 112 84H0Z',R)
 if c=='C':return stripes([B,W,R,W,B])
 if c=='D':return stripes([Y,B,Y])
 if c=='E':return stripes([B,R])
 if c=='F':return rect(0,0,112,84,W)+path('M56 0L112 42 56 84 0 42Z',R)
 if c=='G':return stripes([Y,B]*3,True)
 if c=='H':return stripes([W,R],True)
 if c=='I':return rect(0,0,112,84,Y)+f'<circle cx="56" cy="42" r="23" fill="{K}"/>'
 if c=='J':return stripes([B,W,B])
 if c=='K':return stripes([Y,B],True)
 if c=='L':return ''.join(rect(x*56,y*42,56,42,Y if x==y else K) for y in range(2) for x in range(2))
 if c=='M':return cross(B,W,True)
 if c=='N':return ''.join(rect(x*28,y*21,28,21,B if (x+y)%2==0 else W) for y in range(4) for x in range(4))
 if c=='O':return rect(0,0,112,84,Y)+path('M0 0H112V84Z',R)
 if c=='P':return rect(0,0,112,84,B)+rect(34,24,44,36,W)
 if c=='Q':return rect(0,0,112,84,Y)
 if c=='R':return cross(R,Y)
 if c=='S':return rect(0,0,112,84,W)+rect(34,24,44,36,B)
 if c=='T':return stripes([R,W,B],True)
 if c=='U':return ''.join(rect(x*56,y*42,56,42,R if x==y else W) for y in range(2) for x in range(2))
 if c=='V':return cross(W,R,True)
 if c=='W':return rect(0,0,112,84,B)+rect(22,16,68,52,W)+rect(40,29,32,26,R)
 if c=='X':return cross(W,B)
 if c=='Y':
  return '<svg width="112" height="84" viewBox="0 0 112 84" overflow="hidden">'+rect(0,0,112,84,Y)+''.join(path(f'M{x} 0h14L{x-84} 84h-14Z',R) for x in range(0,210,28))+'</svg>'
 if c=='Z':return path('M0 0H112L56 42Z',Y)+path('M112 0V84L56 42Z',B)+path('M112 84H0L56 42Z',R)+path('M0 84V0L56 42Z',K)
 raise ValueError(c)
for mode in ['light','dark']:
 bg,sea,rope=('#edf3f6','#bdd3df','#a48b57') if mode=='light' else ('#0b182b','#142d48','#bc9954')
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000"><defs><linearGradient id="cloth"><stop stop-color="#fff" stop-opacity=".12"/><stop offset=".35" stop-color="#000" stop-opacity=".12"/><stop offset=".7" stop-color="#fff" stop-opacity=".09"/><stop offset="1" stop-color="#000" stop-opacity=".16"/></linearGradient></defs><rect width="1600" height="1000" fill="{bg}"/>'
 s+=f'<path d="M0 865Q400 820 800 870T1600 865V1000H0Z" fill="{sea}" opacity=".25"/>'
 # Three top swags, 27 flags total; all 26 letters represented.
 spans=[(-35,560,25,105,9),(520,1090,25,100,9),(1050,1635,25,105,9)]
 letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ';n=0
 for left,right,y,sag,count in spans:
  width=right-left
  s+=f'<path d="M{left} {y}Q{(left+right)/2} {y+2*sag} {right} {y}" fill="none" stroke="{rope}" stroke-width="3"/>'
  for i in range(count):
   t=(i+.5)/count;x=left+t*width;fy=y+4*sag*t*(1-t)
   angle=math.degrees(math.atan(4*sag*(1-2*t)/width));scale=min(.58,width/count/125)
   letter=letters[n%26];n+=1
   s+=f'<g transform="translate({x:.2f} {fy:.2f}) rotate({angle:.2f}) scale({scale})"><g transform="translate(-56 4)"><title>Signal flag {letter}</title>{flag(letter)}<path d="M0 -8V88" stroke="{rope}" stroke-width="2"/>'
   if letter not in 'AB':s+='<rect width="112" height="84" fill="url(#cloth)"/>'
   s+='</g></g>'
 s+='</svg>'
 (ROOT/f'artwork/signal-flags-{mode}.svg').write_text(s)
