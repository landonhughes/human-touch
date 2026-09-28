// NODE_PATH=/path/to/playwright/node_modules node examples/bunny/verify.cjs
// Checks the actual shared art and seeked compositions before rendering.
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{const browser=await chromium.launch({headless:true});try{
for(const variant of ['without-skill','with-skill']){
 const page=await browser.newPage({viewport:{width:720,height:720}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(path.join(__dirname,variant,'index.html')).href);
 const seek=async t=>page.evaluate(t=>{window.__timelines.main.seek(t,false);return true;},t);
 const state=await page.evaluate(()=>({first:bunnyState(0),last:bunnyState(8)}));assert.deepEqual(state.first,state.last);
 await seek(0);const first=await page.screenshot();await seek(8);const last=await page.screenshot();assert(first.equals(last),'Loop endpoints must be pixel identical');
 await seek(7.96);assert(first.equals(await page.screenshot()),'Last 25 fps frame must match first');
 await seek(3.6);const belowHat={x:0,y:590,width:720,height:130};const hidden=await page.screenshot({clip:belowHat});await page.evaluate(()=>document.querySelector('#bunny-position').style.opacity='0');assert(hidden.equals(await page.screenshot({clip:belowHat})),'No bunny or carrot pixels may leak below the hat');await page.evaluate(()=>document.querySelector('#bunny-position').style.opacity='');
 await seek(.42);const chew=await page.locator('#snack').getAttribute('transform');await seek(0);assert.notEqual(chew,await page.locator('#snack').getAttribute('transform'));
 await seek(4.9);const jump=await page.screenshot();assert(!first.equals(jump),'Bunny must visibly leave its starting position');
 // Seek order must not change the image.
 await seek(2.4);const forward=await page.screenshot();await seek(7);await seek(2.4);assert(forward.equals(await page.screenshot()),'Seeking backwards must be deterministic');
 assert.deepEqual(errors,[]);await page.close();console.log(variant+': pixel-identical seam, hidden-state occlusion, chew motion, hop, reverse seek and runtime passed.');
}
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
