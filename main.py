from game import Game
from heuristics import count_points


def main():
    game = Game()
    game.play(count_points)


if __name__ == '__main__':
    main()
