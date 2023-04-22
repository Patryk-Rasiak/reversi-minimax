from typing import List


def count_points(board: List[List]) -> dict:
    counts = {}

    for row in board:
        for val in row:
            if val != 0:
                counts[val] = counts.get(val, 0) + 1

    return counts
