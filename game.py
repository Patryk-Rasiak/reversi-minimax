from board import Board
from players import Player, Bot
from typing import Callable, List

from functions import make_move, get_possible_moves
from heuristics import piece_score


class Game:
    def __init__(self, player1, player2, heuristic_fn: Callable[[List[List]], int]):
        self.board = Board()
        self.current_player = player1
        self.next_player = player2
        self.heuristic_fn = piece_score

    def play(self) -> None:
        """
        Each iteration we print scoreboard
        """
        last_player_moved = True
        while True:

            # Printing scores, board and current player
            self.print_current_scores()
            self.board.print()
            print(f"Player {self.current_player.number}'s turn")

            # Retrieving player's available moves
            valid_moves = get_possible_moves(self.board.state, self.current_player.number)
            if not valid_moves:
                # Both players have no valid move to make - game ends
                if not last_player_moved:
                    self.end_game()
                    break

                print('No valid moves - skipping..')
                self.current_player, self.next_player = self.next_player, self.current_player
                last_player_moved = False
                continue

            # Retrieving and validating player's move
            print(f'Possible moves: {valid_moves}')
            player_move = self.current_player.get_move(self.board.state)

            if player_move in valid_moves:
                self.board.state = make_move(self.board.state, self.current_player.number, player_move)
                self.current_player, self.next_player = self.next_player, self.current_player
                last_player_moved = True
            else:
                print("Invalid move!\n")

    def print_current_scores(self) -> None:
        score1 = self.heuristic_fn(self.board.state, 1)
        score2 = self.heuristic_fn(self.board.state, 2)

        print("\n")
        print(f"Player 1's score: {score1}")
        print(f"Player 2's score: {score2}")

    def end_game(self) -> None:
        player1_score = piece_score(self.board.state, 1)
        player2_score = piece_score(self.board.state, 2)

        if player1_score > player2_score:
            print(f"Player 1 WON!")
        elif player2_score > player1_score:
            print(f"Player 2 WON!")
        else:
            print("It's a DRAW!")
