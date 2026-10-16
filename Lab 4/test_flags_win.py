from board import Board

board = Board(rows=3, cols=3, mines=1)

# Use a known mine location for predictable tests
board.mines = {(2, 2)}
safe_cell = (0, 0)

# Flag and unflag
assert board.toggle_flag(safe_cell)
assert safe_cell in board.flags

assert board.toggle_flag(safe_cell)
assert safe_cell not in board.flags

# A flagged cell must not be revealed
board.toggle_flag(safe_cell)
board.reveal(safe_cell)
assert safe_cell not in board.revealed
assert safe_cell in board.flags

# Clear the flag and test win detection
board.toggle_flag(safe_cell)
board.revealed = {
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1)
}
assert board.won()

# Revealing a mine must never count as a win
board.revealed.add((2, 2))
assert not board.won()

print("All flag and win tests passed!")