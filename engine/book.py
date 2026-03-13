import chess
import random


class OpeningBook:
    def __init__(self):
        self.book = {
            chess.STARTING_FEN: ["e2e4", "d2d4", "g1f3", "c2c4"]
        }

    def get_book_move(self, board):
        if board.fen() in self.book:
            return chess.Move.from_uci(random.choice(self.book[board.fen()]))
        return None