from typing import List, Set, Tuple


def make_move(board: List[List[int]], player: int, move: Tuple[int, int]) -> List[List]:
    resulting_board = [row[:] for row in board]
    resulting_board[move[0]][move[1]] = player

    # Left, right, up, down and bevels
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        x, y = move[0] + dx, move[1] + dy
        fields_to_update = []
        while 0 <= x <= 7 and 0 <= y <= 7 and resulting_board[x][y] not in (player, 0):
            fields_to_update.append((x, y))
            x += dx
            y += dy

        if 0 <= x <= 7 and 0 <= y <= 7 and resulting_board[x][y] != 0:
            for i, j in fields_to_update:
                resulting_board[i][j] = player

    return resulting_board


def get_possible_moves(board: List[List[int]], current_player: int) -> Set[Tuple[int, int]]:
    possible_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == current_player:
                possible_moves += _get_moves_for_element(board, current_player, i, j)

    return set(possible_moves)


def _get_moves_for_element(board: List[List[int]], current_player: int, i: int, j: int) -> List[Tuple[int, int]]:
    # Left, right, up, down and bevels
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    possible_moves = []

    for dx, dy in directions:
        x, y = i + dx, j + dy
        count = 0

        while 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] not in (current_player, 0):
            x += dx
            y += dy
            count += 1

        if 0 <= x <= 7 and 0 <= y <= 7 and count > 0 and board[x][y] == 0:
            possible_moves.append((x, y))

    return possible_moves


def is_game_over(board: List[List[int]]) -> bool:
    """
    Game ends when both players have no valid move to make
    """
    return len(get_possible_moves(board, 1)) == len(get_possible_moves(board, 2)) == 0
