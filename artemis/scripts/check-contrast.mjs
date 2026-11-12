import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const p=JSON.parse(readFileSync(new URL('../themes/canopy-dark.json',import.meta.url))).dark;
const lum=h=>h.slice(1).match(/../g).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((s,x,i)=>s+x*[.2126,.7152,.0722][i],0);
const ratio=(a,b)=>(Math.max(lum(a),lum(b))+.05)/(Math.min(lum(a),lum(b))+.05);
for(const [bg,fg] of [['background','foreground'],['card','card-foreground'],['popover','popover-foreground'],['primary','primary-foreground'],['secondary','secondary-foreground'],['muted','muted-foreground'],['accent','accent-foreground'],['destructive','destructive-foreground'],['background','accent'],['card','accent'],['popover','accent']]){
 const r=ratio(p[bg],p[fg]);assert(r>=4.5,bg+'/'+fg+': '+r);console.log(bg+'/'+fg+': '+r.toFixed(2)+':1');
}
