from typing import List
from functions import get_possible_moves


def piece_score(board: List[List[int]], player: int) -> int:
    """
    The points count is the difference in the number of players tiles and opponents.
    """
    score = 0

    for row in board:
        for val in row:
            if val == player:
                score += 1

    return score


def piece_difference_score(board: List[List[int]], player: int) -> int:
    """
    The piece difference score is the difference in the number of players tiles and opponents.
    """
    score = 0
    for row in board:
        for val in row:
            if val == player:
                score += 1
            elif val != 0:
                score -= 1

    return score


def mobility_score(board: List[List], player: int) -> int:
    """
    The mobility score is the number of legal moves available to the player.
    """
    return len(get_possible_moves(board, player)) - len(get_possible_moves(board, 2 if player == 1 else 1))


def corner_occupancy_score(board: List[List], player: int) -> int:
    """
    The corner occupancy score is the number of corner tiles that the player has occupied.
    """
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

    score = 0
    for x, y in corners:
        if board[x][y] == player:
            score += 1

        elif board[x][y] != 0:
            score -= 1

    return score


def super_heuristic(board: List[List], player: int) -> int:
    """
    The super heuristic is a combination of piece difference, weighted tiles, corner occupancy,
    corner closeness and mobility.
    """

    # Piece difference, frontier disks and disk squares
    weights = [[20, -3, 11, 8, 8, 11, -3, 20],
               [-3, -7, -4, 1, 1, -4, -7, -3],
               [11, -4, 2, 2, 2, 2, -4, 11],
               [8, 1, 2, -3, -3, 2, 1, 8],
               [8, 1, 2, -3, -3, 2, 1, 8],
               [11, -4, 2, 2, 2, 2, -4, 11],
               [-3, -7, -4, 1, 1, -4, -7, -3],
               [20, -3, 11, 8, 8, 11, -3, 20]]

    x1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    y1 = [0, 1, 1, 1, 0, -1, -1, -1]

    weighted_score = 0
    player_tiles = opponent_tiles = 0
    player_front_tiles = opponent_front_tiles = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                weighted_score += weights[i][j]
                player_tiles += 1
            elif board[i][j] != 0:
                weighted_score -= weights[i][j]
                opponent_tiles += 1

        if board[i][j] != 0:
            for k in range(8):
                x = i + x1[k]
                y = j + y1[k]
                if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 0:
                    if board[i][j] == player:
                        player_front_tiles += 1
                    else:
                        opponent_front_tiles += 1
                    break

    if player_tiles > opponent_tiles:
        score_tiles = (100 * player_tiles) / (opponent_tiles + player_tiles)
    elif player_tiles < opponent_tiles:
        score_tiles = -(100 * player_tiles) / (opponent_tiles + player_tiles)
    else:
        score_tiles = 0

    if player_front_tiles > opponent_front_tiles:
        score_front_tiles = (100 * player_front_tiles) / (opponent_front_tiles + player_front_tiles)
    elif player_tiles < opponent_front_tiles:
        score_front_tiles = -(100 * player_front_tiles) / (opponent_front_tiles + player_front_tiles)
    else:
        score_front_tiles = 0

    # Corner occupancy score
    player_tiles = opponent_tiles = 0
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

    for x, y in corners:
        if board[x][y] == player:
            player_tiles += 1
        elif board[x][y] != 0:
            opponent_tiles += 1

    score_corners = 25 * (player_tiles - opponent_tiles)

    # Corner closeness score
    player_tiles = opponent_tiles = 0
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

    for i, j in corners:
        if board[i][j] == 0:
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                         (i - 1, j + 1), (i - 1, j - 1)]:
                if 0 <= a <= 7 and 0 <= b <= 7:
                    if board[a][b] == player:
                        player_tiles += 1
                    elif board[a][b] != 0:
                        opponent_tiles += 1

    score_corners_closeness = -12.5 * (player_tiles - opponent_tiles)

    # Mobility score
    player_tiles = len(get_possible_moves(board, player))
    opponent_tiles = len(get_possible_moves(board, 1 if player == 2 else 2))
    if player_tiles > opponent_tiles:
        score_mobility = (100 * player_tiles) / (player_tiles + opponent_tiles)
    elif player_tiles < opponent_tiles:
        score_mobility = -(100 * player_tiles) / (player_tiles + opponent_tiles)
    else:
        score_mobility = 0

    # Summing up scores with the appropriate weights to get the final score
    final_score = (10 * weighted_score) + (10 * score_tiles) + (74.396 * score_front_tiles) + (801.724 * score_corners) + (
                382.026 * score_corners_closeness) + (78.922 * score_mobility)

    return round(final_score)
