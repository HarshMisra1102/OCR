from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chess

from engine.search import ChessEngine
from engine.evaluation import evaluate_board

app = FastAPI()
engine = ChessEngine()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PositionRequest(BaseModel):
    fen: str
    time_limit: float = 1.0

def format_score(score):
    if abs(score) > 90000:
        mate_in = 100000 - abs(score)
        return f"M{mate_in}" if score > 0 else f"M-{mate_in}"
    return round(score / 100, 2)

@app.post("/analyze")
def analyze_position(request: PositionRequest):

    board = chess.Board(request.fen)
    previous_eval = evaluate_board(board)

    best_move = engine.search(board, time_limit=request.time_limit)
    evaluation = evaluate_board(board)

    if board.turn == chess.BLACK:
        evaluation = -evaluation

    formatted_score = format_score(evaluation)
    swing = abs(evaluation - previous_eval)
    blunder = swing > 300

    is_book = engine.depth_reached == 0

    return {
        "best_move": str(best_move) if best_move else None,
        "evaluation": formatted_score,
        "depth": engine.depth_reached,
        "nodes": engine.nodes,
        "pv": [str(m) for m in engine.best_pv],
        "blunder": blunder,
        "tt_hits": engine.tt_hits,
        "tt_stores": engine.tt_stores,
        "tt_size": len(engine.tt),
        "book_move": is_book
    }