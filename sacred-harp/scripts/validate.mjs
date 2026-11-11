import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const read=p=>JSON.parse(readFileSync(resolve(root,p),'utf8'));
const manifest=read('openclaw.plugin.json');
const lum=h=>{const c=h.slice(1).match(/../g).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return c[0]*.2126+c[1]*.7152+c[2]*.0722;};
const contrast=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);};
let palettes=0,checks=0;
for(const entry of manifest.themes){
 const d=read(entry.source);
 assert.equal(d.name,entry.name);assert.equal(d.description,entry.description);
 assert(Buffer.byteLength(JSON.stringify(d))<=4096);
 for(const mode of ['light','dark']){
  const p=d[mode];
  assert(p["font-sans"].endsWith(", serif"), "Serif UI default required");
  assert(p["font-mono"].includes("monospace"), "Code must remain monospace");
  for(const key of ['background','foreground','card','card-foreground','popover','popover-foreground','primary','primary-foreground','secondary','secondary-foreground','muted','muted-foreground','accent','accent-foreground','destructive','destructive-foreground','border','input','ring'])assert.match(p[key],/^#[0-9a-f]{6}$/i);
  let min=Infinity;
  for(const [bg,fg] of [['background','foreground'],['card','card-foreground'],['popover','popover-foreground'],['primary','primary-foreground'],['secondary','secondary-foreground'],['muted','muted-foreground'],['accent','accent-foreground'],['destructive','destructive-foreground'],['background','muted-foreground'],['card','muted-foreground']]){
   const ratio=contrast(p[bg],p[fg]);assert(ratio>=4.5,`${entry.id}/${mode} ${bg}/${fg}: ${ratio.toFixed(2)}`);min=Math.min(min,ratio);checks++;
  }
  assert(contrast(p.background,p.ring)>=3);
  console.log(`${entry.id}/${mode}: minimum checked text contrast ${min.toFixed(2)}:1`);palettes++;
 }
 for(const path of Object.values(entry.icons)){
  const svg=readFileSync(resolve(root,path),'utf8');assert(Buffer.byteLength(svg)<=32768);assert(!/script|href=|<style|<image/.test(svg));
 }
}
console.log(`PASS: ${manifest.themes.length} themes, ${palettes} palettes, ${checks} text contrast checks.`);
