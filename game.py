from board import Board
from players import Player
from typing import Callable, Set, Tuple, List


class Game:

    def __init__(self, first_player: int = 1, second_player: int = 2):
        self.board = Board()
        self.players = [Player(1), Player(2)]
        self.current_player = Player(first_player)
        self.next_player = Player(second_player)

    def play(self, heuristic_fn: Callable[[List[List]], dict]) -> None:
        last_player_moved = True
        while True:
            print("\n")
            for k, v in heuristic_fn(self.board.state).items():
                print(f"Player {k}'s score: {v}")

            self.board.print()
            print(f"Player {self.current_player.number}'s turn")
            valid_moves = self._get_possible_moves()

            if not valid_moves:
                # Both players have no valid move to make
                if not last_player_moved:
                    self.end_game()
                    break

                self.current_player, self.next_player = self.next_player, self.current_player
                last_player_moved = False
                continue

            print(f'Possible moves: {valid_moves}')
            player_move = self.current_player.get_move()

            if player_move in valid_moves:
                self.board.make_move(self.current_player, player_move)
                self.current_player, self.next_player = self.next_player, self.current_player
                last_player_moved = True
            else:
                print("Invalid move!\n")

    def end_game(self) -> None:
        player1_score = player2_score = 0
        for x in range(8):
            for y in range(8):
                if self.board.get_val(x, y) == self.players[0].number:
                    player1_score += 1
                else:
                    player2_score += 1

        if player1_score > player2_score:
            print(f"Player {self.players[0].number} WON!")
        elif player2_score > player1_score:
            print(f"Player {self.players[1].number} WON!")
        else:
            print("It's a DRAW!")

    def _get_possible_moves(self) -> Set[Tuple[int, int]]:
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if self.board.get_val(i, j) == self.current_player.number:
                    possible_moves += self._get_moves_for_element(i, j)
        return set(possible_moves)

    def _get_moves_for_element(self, i: int, j: int) -> List[Tuple[int, int]]:
        possible_moves = []

        # left, right, up, down and bevels
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            count = 0

            while 0 <= x <= 7 and 0 <= y <= 7 and self.board.get_val(x, y) not in (self.current_player.number, 0):
                x += dx
                y += dy
                count += 1

            if 0 <= x <= 7 and 0 <= y <= 7 and count > 0 and self.board.get_val(x, y) == 0:
                possible_moves.append((x, y))

        return possible_moves
