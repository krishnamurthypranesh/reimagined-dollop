from typing import List

_input = [
            [5, 3, 4,],
            [1, 5, 8,],
            [6, 4, 2,],
        ]

def formingMagicSquare(s: List[List[int]]) -> int:
    i, j = 0, 0
    unit: List[int] = []
    threeTuples: List[List[int]] = []

    while i < 3:
        unit: List[int] = []
        while j < 3:
            unit.append(s[i][j])
            j += 1
        threeTuples.append(unit)
        i += 1

    print(threeTuples)
    return 0

formingMagicSquare(_input)
