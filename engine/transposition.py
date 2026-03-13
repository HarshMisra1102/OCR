class TranspositionTable:
    def __init__(self):
        self.table = {}

    def lookup(self, board_hash, depth):
        entry = self.table.get(board_hash)
        if entry and entry["depth"] >= depth:
            return entry["score"]
        return None

    def store(self, board_hash, depth, score):
        self.table[board_hash] = {
            "depth": depth,
            "score": score
        }