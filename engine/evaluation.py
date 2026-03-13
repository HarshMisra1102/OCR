import chess
from engine.nn_eval import nn_evaluate

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

USE_NN = True  # Toggle hybrid mode

def classical_eval(board):
    score = 0
    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
    return score

def evaluate_board(board):
    score = classical_eval(board)

    if USE_NN:
        score += nn_evaluate(board)

    return score