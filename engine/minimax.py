import chess
from engine.evaluation import evaluate_board


def quiescence(board: chess.Board, alpha: float, beta: float):

    stand_pat = evaluate_board(board)

    if stand_pat >= beta:
        return beta

    if alpha < stand_pat:
        alpha = stand_pat

    # Only explore captures
    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiescence(board, -beta, -alpha)
            board.pop()

            if score >= beta:
                return beta

            if score > alpha:
                alpha = score

    return alpha


def minimax(board: chess.Board, depth: int, alpha: float, beta: float, maximizing: bool):

    if depth == 0:
        return quiescence(board, alpha, beta)

    if board.is_game_over():
        return evaluate_board(board)

    if maximizing:
        max_eval = float('-inf')

        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float('inf')

        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()

            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            if beta <= alpha:
                break

        return min_eval