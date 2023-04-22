class Player:
    def __init__(self, number: int):
        self.number = number

    def get_move(self):
        try:
            x, y = input("Your move: ").split(", ")
            return int(x), int(y)
        except ValueError:
            return False
