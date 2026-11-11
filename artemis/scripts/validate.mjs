import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
const read = p => JSON.parse(readFileSync(new URL(`../${p}`, import.meta.url), 'utf8'));
const manifest=read('openclaw.plugin.json'), data=read(manifest.themes[0].source);
assert.equal(data.name,manifest.themes[0].name);
assert.equal(data.description,manifest.themes[0].description);
assert.equal(data.description,read('package.json').description);
assert(!data.light,'Artemis remains dark-only');
assert(Buffer.byteLength(JSON.stringify(data))<=4096);
const p=data.dark;
const lum=h=>{const c=h.slice(1).match(/../g).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return c[0]*.2126+c[1]*.7152+c[2]*.0722;};
const contrast=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);};
for(const [key,value] of Object.entries(p)) if(!key.startsWith('font-')) assert.match(value,/^#[0-9a-f]{6}$/i);
let minimum=Infinity;
for(const [bg,fg] of [['background','foreground'],['card','card-foreground'],['popover','popover-foreground'],['primary','primary-foreground'],['secondary','secondary-foreground'],['muted','muted-foreground'],['accent','accent-foreground'],['destructive','destructive-foreground'],['background','muted-foreground'],['card','muted-foreground'],['background','primary'],['card','primary']]) {
 const ratio=contrast(p[bg],p[fg]);assert(ratio>=4.5,`${bg}/${fg}: ${ratio.toFixed(2)}`);minimum=Math.min(minimum,ratio);
}
for(const bg of ['background','card']) for(const fg of ['ring','border','input']) assert(contrast(p[bg],p[fg])>=3,`${bg}/${fg} requires 3:1`);
assert(p['font-sans'].includes('JetBrains Mono') && p['font-mono'].includes('monospace'));
const entry=await import(new URL('../index.js',import.meta.url));
assert.equal(entry.default.id,manifest.id);assert.equal(entry.default.register(),undefined);
console.log(`PASS: 12 text contrast pairs (minimum ${minimum.toFixed(2)}:1), 6 focus/border pairs, manifest agreement, dark-only scope, fonts, and no-op entrypoint.`);
