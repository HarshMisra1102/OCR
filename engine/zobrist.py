import chess
import random


class ZobristHash:
    def __init__(self):
        random.seed(42)
        self.piece_keys = {}
        self.side_key = random.getrandbits(64)

        for square in chess.SQUARES:
            for piece_type in range(1, 7):
                for color in (chess.WHITE, chess.BLACK):
                    self.piece_keys[(square, piece_type, color)] = random.getrandbits(64)

    def hash(self, board):
        h = 0

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                h ^= self.piece_keys[(square, piece.piece_type, piece.color)]

        if board.turn == chess.BLACK:
            h ^= self.side_key

        return h