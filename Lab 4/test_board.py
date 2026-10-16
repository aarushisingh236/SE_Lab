from board import Board

board = Board(rows=6, cols=6, mines=6)

test_cells = [
    (0, 0), (0, 5),
    (5, 0), (5, 5),
    (0, 3), (5, 3),
    (3, 0), (3, 5),
    (2, 2)
]

for r, c in test_cells:
    neighbours = list(board.neighbors(r, c))

    assert all(
        board.in_bounds(nr, nc)
        for nr, nc in neighbours
    ), f"Out-of-bounds neighbour for {(r, c)}"

    assert (r, c) not in neighbours

print("All boundary tests passed!")