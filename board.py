from typing import Tuple
from players import Player


class Board:

    def __init__(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0, 0, 0, 0, 0, 0, 0, 0],  # 1
            [0, 0, 0, 0, 0, 0, 0, 0],  # 2
            [0, 0, 0, 2, 1, 0, 0, 0],  # 3
            [0, 0, 0, 1, 2, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [0, 0, 0, 0, 0, 0, 0, 0]   # 7
            # 0 1  2  3  4  5  6  7
        ]

    def make_move(self, player: Player, move: Tuple[int, int]) -> None:
        self.state[move[0]][move[1]] = player.number
        # left, right, up, down and bevels
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            x, y = move[0] + dx, move[1] + dy
            places_to_change = []
            while 0 <= x <= 7 and 0 <= y <= 7 and self.get_val(x, y) not in (player.number, 0):
                places_to_change.append((x, y))
                x += dx
                y += dy

            if 0 <= x <= 7 and 0 <= y <= 7 and self.get_val(x, y) != 0:
                for i, j in places_to_change:
                    self.state[i][j] = player.number

    def get_val(self, x: int, y: int) -> int:
        return self.state[x][y]

    def print(self) -> None:
        print('0 1 2 3 4 5 6 7')
        print('---------------')
        for i, row in enumerate(self.state):
            for val in row:
                print(val, end=' ')
            print(f'| {i}')
