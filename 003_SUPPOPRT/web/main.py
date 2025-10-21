# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Tiến thiện")

# ⚠️ Bắt buộc: Cho phép Godot (chạy ở http://localhost:...) gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong production, thay bằng ["http://localhost:6000"] hoặc domain thật
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dữ liệu tạm (trong thực tế dùng database)
players: Dict[str, dict] = {}

class LoginRequest(BaseModel):
    player_id: str

class ScoreUpdate(BaseModel):
    player_id: str
    score: int

@app.post("/login")
def login(req: LoginRequest):
    if req.player_id not in players:
        players[req.player_id] = {"score": 0, "online": True}
    return {"status": "ok", "player": players[req.player_id]}

@app.post("/update_score")
def update_score(req: ScoreUpdate):
    if req.player_id in players:
        players[req.player_id]["score"] = req.score
        return {"status": "ok", "new_score": req.score}
    return {"status": "error", "message": "Player not found"}

@app.get("/leaderboard")
def leaderboard():
    return sorted(
        [{"id": pid, **data} for pid, data in players.items()],
        key=lambda x: x["score"],
        reverse=True
    )