import chess
import sys
from engine.search import ChessEngine
from engine.book import get_book_move


def uci_loop():
    board = chess.Board()
    engine = ChessEngine()

    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command == "uci":
            print("id name SmartChessAI")
            print("id author Ayush Mishra")
            print("uciok")

        elif command == "isready":
            print("readyok")

        elif command == "ucinewgame":
            board.reset()
            engine = ChessEngine()

        elif command.startswith("position"):
            parts = command.split()

            if "startpos" in parts:
                board.reset()
                move_index = parts.index("moves") if "moves" in parts else -1
            else:
                fen_index = parts.index("fen") + 1
                fen = " ".join(parts[fen_index:fen_index + 6])
                board.set_fen(fen)
                move_index = parts.index("moves") if "moves" in parts else -1

            if move_index != -1:
                for move in parts[move_index + 1:]:
                    board.push_uci(move)

        elif command.startswith("go"):
            time_limit = 3  # default seconds

            parts = command.split()

            # Support movetime
            if "movetime" in parts:
                idx = parts.index("movetime") + 1
                time_limit = int(parts[idx]) / 1000.0

            # Try opening book first
            book_move = get_book_move(board)
            if book_move:
                print(f"bestmove {book_move}")
                sys.stdout.flush()
                continue

            best_move = engine.search(board, time_limit=time_limit)

            if best_move is None:
                print("bestmove 0000")
            else:
                print(f"bestmove {best_move}")

        elif command == "quit":
            break

        sys.stdout.flush()