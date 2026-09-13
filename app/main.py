from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from .models import ApprovalRequest, Episode, GenerateRequest, Status
from .generator import generate_episode
from .store import load_episodes, save_episode

app = FastAPI(title="KidsTube Autopilot", version="0.1.0")

DASHBOARD = '''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>KidsTube Autopilot</title><style>body{font-family:system-ui;max-width:1100px;margin:40px auto;padding:0 20px;background:#f7f7fb;color:#202124}h1{margin-bottom:4px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}.card{background:white;padding:18px;border-radius:16px;box-shadow:0 2px 12px #0001}button{padding:10px 14px;border:0;border-radius:10px;cursor:pointer}input{padding:10px;width:70%;border:1px solid #ddd;border-radius:10px}.muted{color:#666}.pill{display:inline-block;padding:4px 8px;border-radius:99px;background:#eee}</style></head><body><h1>🎬 KidsTube Autopilot</h1><p class="muted">Original, safety-first kids content pipeline</p><div class="card"><input id="topic" value="Sharing a toy"><button onclick="generate()">Generate episode</button></div><br><div id="episodes" class="grid"></div><script>async function load(){let r=await fetch('/api/episodes');let x=await r.json();document.querySelector('#episodes').innerHTML=x.map(e=>`<div class="card"><h2>${e.title}</h2><span class="pill">${e.status}</span><p>${e.description}</p><p><b>${e.scenes.length}</b> scenes · lesson: ${e.lesson}</p>${e.status==='ready'?`<button onclick="approve('${e.id}')">Approve</button>`:''}</div>`).join('')||'<p>No episodes yet.</p>'}async function generate(){let topic=document.querySelector('#topic').value;await fetch('/api/episodes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({topic,lesson:'kindness',scene_count:6})});load()}async function approve(id){await fetch('/api/episodes/'+id+'/approval',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({approved:true})});load()}load()</script></body></html>'''

@app.get("/", response_class=HTMLResponse)
def dashboard(): return DASHBOARD

@app.get("/health")
def health(): return {"status":"ok","service":"kidstube-autopilot"}

@app.get("/api/episodes", response_model=list[Episode])
def episodes(): return load_episodes()

@app.post("/api/episodes", response_model=Episode, status_code=201)
def create_episode(req: GenerateRequest):
    episode = generate_episode(req)
    save_episode(episode)
    return episode

@app.get("/api/episodes/{episode_id}", response_model=Episode)
def get_episode(episode_id: str):
    episode = next((e for e in load_episodes() if e.id == episode_id), None)
    if not episode: raise HTTPException(404, "Episode not found")
    return episode

@app.post("/api/episodes/{episode_id}/approval", response_model=Episode)
def approval(episode_id: str, req: ApprovalRequest):
    episode = next((e for e in load_episodes() if e.id == episode_id), None)
    if not episode: raise HTTPException(404, "Episode not found")
    episode.status = Status.APPROVED if req.approved else Status.DRAFT
    save_episode(episode)
    return episode
