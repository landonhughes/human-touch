// The timeline is the only clock. All poses are pure functions of its time.
const directed = document.body.dataset.variant === 'with-skill';
const clamp = v => Math.max(0, Math.min(1, v));
const smooth = v => { v=clamp(v);return v*v*(3-2*v); };
const mix = (a,b,v) => a+(b-a)*v;
const pulse = (t,start,end) => t<start||t>end?0:Math.sin(Math.PI*(t-start)/(end-start))**2;
function bunnyState(time){
 const t=Math.max(0,Math.min(8,time));
 let x=215,y=575,rotation=0,sx=1,sy=1,ear=0,chew=0;
 const launch=directed?2.05:2,peak=directed?2.72:2.7,drop=directed?3.25:3.3;
 // A smooth jump parabola, followed by a vertical drop through the hat opening.
 if(t>=launch&&t<peak){const u=(t-launch)/(peak-launch);x=mix(215,520,smooth(u));y=mix(575,385,u)-125*Math.sin(Math.PI*u);rotation=directed?12*Math.sin(Math.PI*u):0;}
 else if(t>=peak&&t<drop){const u=(t-peak)/(drop-peak);x=520;y=mix(385,735,u*u);rotation=directed?-6*Math.sin(Math.PI*u):0;}
 else if(t>=drop&&t<4.1){x=520;y=735;}
 else if(t>=4.1&&t<4.58){const u=(t-4.1)/.48;x=520;y=mix(735,335,1-(1-u)**2);rotation=directed?-8*Math.sin(Math.PI*u):0;}
 else if(t>=4.58&&t<5.5){const u=(t-4.58)/.92;x=mix(520,215,smooth(u));y=mix(335,575,u*u)-45*Math.sin(Math.PI*u);rotation=directed?-10*Math.sin(Math.PI*u):0;}
 if(directed){
  const crouch=pulse(t,1.68,2.05),land=pulse(t,5.5,5.86);
  const stretch=pulse(t,2.05,2.52)+pulse(t,4.1,4.48);
  sx=1+.14*crouch+.13*land-.055*stretch;sy=1-.16*crouch-.15*land+.1*stretch;
  ear=9*pulse(t,2.13,2.95)-12*pulse(t,4.2,4.94)+7*pulse(t,5.54,6.12);
 }
 // Bites don't progressively erase the prop: its silhouette is loop-invariant.
 const bites=directed?[.3,.72,1.22,4.58,5.08,5.96,6.38,6.96,7.38]:[.3,.75,1.2,4.55,5.05,5.95,6.4,6.85,7.3];
 for(const start of bites)chew+=pulse(t,start,start+.24);
 return {x,y,rotation,sx,sy,ear,chew};
}
const el=id=>document.getElementById(id);
function drawBunny(time){
 const s=bunnyState(time);
 el('bunny-position').setAttribute('transform',`translate(${s.x} ${s.y})`);
 el('bunny-pose').setAttribute('transform',`rotate(${s.rotation}) scale(${.82*s.sx} ${.82*s.sy})`);
 el('ear-back').setAttribute('transform',`rotate(${-s.ear*.75} -17 -210)`);
 el('ear-front').setAttribute('transform',`rotate(${s.ear} 10 -208)`);
 el('bunny-head').setAttribute('transform',`translate(0 ${s.chew*1.8})`);
 el('snack').setAttribute('transform',`translate(${-s.chew*2.5} ${-s.chew*1.2})`);
 el('mouth').setAttribute('transform',`translate(53 -145) scale(1 ${1+s.chew*.8}) translate(-53 145)`);
 const height=Math.max(0,575-s.y),shadowScale=1-Math.min(height/600,.5);
 el('bunny-shadow').setAttribute('transform',`translate(${s.x-215} 0) translate(215 581) scale(${shadowScale} 1) translate(-215 -581)`);
 el('bunny-shadow').setAttribute('opacity',s.x>412&&s.y>500?0:.28*(1-height/500));
}
const driver={time:0};
const tl=gsap.timeline({paused:true});
tl.fromTo(driver,{time:0},{time:8,duration:8,ease:'none',onUpdate:()=>drawBunny(driver.time)},0);
drawBunny(0);
window.__timelines = window.__timelines || {};
window.__timelines['main']=tl;
window.bunnyState=bunnyState;
window.drawBunny=drawBunny;
