const fs=require('fs'),vm=require('vm'),assert=require('assert');
const js=fs.readFileSync('output/.qa/runtime.js','utf8');
const handler=js.match(/window.addEventListener\('message',e=>\{[\s\S]*?\}\);/)[0];
function context(presenter){const c={sessionKey:'session-a',presenter,popup:null,window:{opener:{},addEventListener:(type,fn)=>c.receive=fn},linked:!presenter,localMode:presenter,audienceBoot:null,index:2,revealed:3,showAll:false,running:false,elapsedMs:0,slideMs:0,targetMin:55,lastSync:0,Date,render:()=>c.renders++,drawTime:()=>{},sync:()=>c.syncs++,command:()=>{},location:{reload:()=>c.reloads++},renders:0,syncs:0,reloads:0};vm.createContext(c);vm.runInContext(handler,c);return c}
const owner=context(true),child={closed:false};
owner.receive({source:child,data:{type:'deck-ready',sessionKey:'wrong'}});assert.equal(owner.popup,null);
owner.receive({source:child,data:{type:'deck-ready',sessionKey:'session-a'}});assert.equal(owner.popup,child);assert.equal(owner.syncs,1);
const a=context(false);const data={type:'deck-state',sessionKey:'session-a',bootId:'boot-1',index:2,revealed:3,showAll:false,running:false,elapsedMs:0,slideMs:0,targetMin:55};
a.receive({source:a.window.opener,data});assert.equal(a.reloads,0);
a.receive({source:a.window.opener,data});assert.equal(a.reloads,0);
a.receive({source:a.window.opener,data:{...data,bootId:'boot-2'}});assert.equal(a.reloads,1);assert.equal(a.renders,1);assert.equal(a.index,2);assert.equal(a.revealed,3);
const b=context(false);b.receive({source:b.window.opener,data:{...data,bootId:'boot-2'}});assert.equal(b.reloads,0);
console.log('PASS: session validation, reconnection after presenter reload, audience refresh, slide/reveal preservation and no refresh loop.');
