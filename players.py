from typing import List, Callable, Tuple
from functions import make_move, get_possible_moves, is_game_over


class Player:
    def __init__(self, number: int):
        self.number = number

    def get_move(self, board: List[List]) -> (int, int):
        try:
            x, y = input("Your move: ").split(", ")
            return int(x), int(y)
        except ValueError:
            return -1, -1


class Bot:
    def __init__(self, number: int, depth: int, heuristic_fn: Callable[[List[List], int], int], pruning: bool):
        self.pruning = pruning
        self.number = number
        self.depth = depth
        self.heuristic_fn = heuristic_fn

    def get_move(self, board: List[List]) -> (int, int):
        if self.pruning:
            move = self.minimax_pruning(board, self.number, 0)[1]
        else:
            move = self.minimax(board, self.number, 0)[1]
        print(f"Bot's move: {move}")
        return move

    def minimax(self, board: List[List[int]], player: int, depth: int) -> Tuple:
        if depth == self.depth or is_game_over(board):
            return self.heuristic_fn(board, player), None

        best_score = float('-inf') if player == self.number else float('inf')
        best_move = None

        for move in get_possible_moves(board, player):
            new_board = [row[:] for row in board]
            new_board = make_move(new_board, player, move)
            score, _ = self.minimax(new_board, 1 if player == 2 else 2, depth + 1)
            if player == self.number and score > best_score or player != self.number and score < best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    def minimax_pruning(self, board: List[List[int]], player: int, depth: int, alpha=float('-inf'),
                        beta=float('inf')) -> Tuple:
        if depth == self.depth or is_game_over(board):
            return self.heuristic_fn(board, player), None

        best_score = float('-inf') if player == self.number else float('inf')
        best_move = None

        for move in get_possible_moves(board, player):
            new_board = [row[:] for row in board]
            new_board = make_move(new_board, player, move)
            score, _ = self.minimax_pruning(new_board, 1 if player == 2 else 2, depth + 1, alpha, beta)

            if player == self.number and score > best_score:
                best_score = score
                best_move = move
                alpha = max(alpha, score)
                if alpha >= beta:
                    break

            elif player != self.number and score < best_score:
                best_score = score
                best_move = move
                beta = min(beta, score)
                if alpha >= beta:
                    break

        return best_score, best_move
