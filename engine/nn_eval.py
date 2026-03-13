import chess
import torch
import torch.nn as nn
import torch.nn.functional as F

# Simple NN model
class EvalNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(64 * 12, 128)
        self.fc2 = nn.Linear(128, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

model = EvalNet()

def board_to_tensor(board: chess.Board):
    tensor = torch.zeros(64 * 12)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            index = (piece.piece_type - 1) + (6 if piece.color == chess.BLACK else 0)
            tensor[square * 12 + index] = 1

    return tensor

def nn_evaluate(board: chess.Board):
    with torch.no_grad():
        x = board_to_tensor(board)
        score = model(x)
        return score.item() * 100  # scale to centipawns