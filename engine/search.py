import time
import chess
from engine.evaluation import evaluate_board
from engine.zobrist import ZobristHash
from engine.book import OpeningBook

INF = 10**9
MATE_SCORE = 100000


class ChessEngine:
    def __init__(self):
        self.zobrist = ZobristHash()
        self.book = OpeningBook()

        self.tt = {}
        self.nodes = 0
        self.depth_reached = 0
        self.best_move = None
        self.best_pv = []

    def search(self, board, time_limit=1.0):

        # --- Opening Book ---
        book_move = self.book.get_book_move(board)
        if book_move:
            self.best_move = book_move
            self.best_pv = [book_move]
            self.depth_reached = 0
            return book_move

        self.start_time = time.time()
        self.time_limit = time_limit
        self.nodes = 0
        self.depth_reached = 0
        self.best_move = None
        self.best_pv = []

        depth = 1

        while True:
            if time.time() - self.start_time > self.time_limit:
                break

            score, pv = self.alpha_beta(board, depth, -INF, INF)

            if time.time() - self.start_time > self.time_limit:
                break

            if pv:
                self.best_move = pv[0]
                self.best_pv = pv

            self.depth_reached = depth
            depth += 1

        return self.best_move

    def alpha_beta(self, board, depth, alpha, beta):

        if time.time() - self.start_time > self.time_limit:
            return 0, []

        self.nodes += 1

        # Terminal
        if board.is_checkmate():
            return -MATE_SCORE + depth, []

        if board.is_stalemate() or board.is_insufficient_material():
            return 0, []

        if depth == 0:
            return evaluate_board(board), []

        best_score = -INF
        best_line = []

        moves = list(board.legal_moves)

        # Simple capture-first ordering (stable)
        moves.sort(key=lambda m: board.is_capture(m), reverse=True)

        for move in moves:
            board.push(move)
            score, child_pv = self.alpha_beta(board, depth - 1, -beta, -alpha)
            score = -score
            board.pop()

            if score > best_score:
                best_score = score
                best_line = [move] + child_pv

            alpha = max(alpha, score)
            if alpha >= beta:
                break

        return best_score, best_line