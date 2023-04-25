class Board:

    def __init__(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def get_val(self, x: int, y: int) -> int:
        return self.state[x][y]

    def print(self) -> None:
        print('0 1 2 3 4 5 6 7')
        print('---------------')
        for i, row in enumerate(self.state):
            for val in row:
                print(val, end=' ')
            print(f'| {i}')
