from game import Game
from heuristics import super_heuristic, piece_score
from players import Player, Bot


def main():
    """
        Representation of the board:
        0 - Empty field
        1 - Player 1's field
        2 - Player 2's field

       Y 0 1 2 3 4 5 6 7
         ---------------   X
       | 0 0 0 0 0 0 0 0 | 0
       | 0 0 0 0 0 0 0 0 | 1
       | 0 0 0 0 0 0 0 0 | 2
       | 0 0 0 2 1 0 0 0 | 3
       | 0 0 0 1 2 0 0 0 | 4
       | 0 0 0 0 0 0 0 0 | 5
       | 0 0 0 0 0 0 0 0 | 6
       | 0 0 0 0 0 0 0 0 | 7
         ---------------

         Each move in the game needs to be put in format X, Y
         For example:
         Your move: 2, 4

    """

    # Player vs Player game
    game1 = Game(Player(1), Player(2), piece_score)

    # Player vs Bot game
    game2 = Game(Player(1), Bot(2, 4, super_heuristic, False), piece_score)

    # Bot vs Bot game
    game3 = Game(Bot(1, 2, super_heuristic, False), Bot(2, 4, super_heuristic, False), piece_score)

    game3.play()


if __name__ == '__main__':
    main()
