# Scenario 13 — Minesweeper

A Python-based terminal Minesweeper game enhanced through AI-assisted debugging and feature development.

## Objective

To inspect and debug the supplied Minesweeper starter code, fix the identified defect, implement the required features, and test the updated application.

## Project Structure

```text
Lab 4/
├── README.md
├── main.py
├── game.py
├── board.py
├── requirements.txt
├── test_board.py
├── test_flags_win.py
├── PES2UG24CS015_LAB_4.pdf
└── Video/
    ├── Minesweeper_Original_Before_Fix.mp4
    └── Minesweeper_Fixed_After_Improvements.mp4
```

## Requirements

- Python 3.9 or newer
- No additional package installation is required for the game.

## How to Run

Open a terminal in the project directory and execute:

```bash
python main.py
```

Select a difficulty when prompted:

- **Easy:** 6 × 6 board with 6 mines
- **Medium:** 8 × 8 board with 12 mines
- **Hard:** 10 × 10 board with 20 mines

## Game Controls

| Command | Description |
|---|---|
| `r row col` | Reveal a cell |
| `f row col` | Toggle a flag on a cell |
| `q` | Quit the game |

Rows and columns are numbered starting from 1 in the terminal interface.

## Implemented Tasks

### Task 1 — Boundary-Safe Board Traversal

Corrected the neighbour traversal condition to ensure that row and column coordinates remain within valid board boundaries.

### Task 2 — Win Detection and Flag Behaviour

Updated the win condition to ensure that all safe cells are revealed and no mine has been revealed. Flag toggling and protection against revealing flagged cells are preserved.

### Task 3 — Difficulty Modes

Added Easy, Medium, and Hard difficulty selection, with different board dimensions and mine counts.

### Task 4 — Action-Level Feedback

Added concise feedback for player reveal actions, including the adjacent-mine count for safe reveals. Feedback is displayed once per player action rather than for each internal flood-fill iteration.

## Testing

The project includes the following test files:

- `test_board.py` — checks neighbour traversal at board corners, edges, and interior cells.
- `test_flags_win.py` — checks flag toggling, revealing flagged cells, and win detection.

Run the tests using:

```bash
python test_board.py
python test_flags_win.py
```

Additional manual testing covers difficulty selection, invalid coordinates, safe reveals, mine hits, and game completion.

## Before-and-After Demonstration

The `Video/` folder contains two gameplay recordings:

1. **Original version:** Demonstrates the game before the fixes and feature additions.
2. **Fixed version:** Demonstrates the updated game, including difficulty selection and reveal feedback.

## AI-Assisted Development

An AI coding assistant was used to help identify defects, propose targeted code changes, and develop the required features. The generated changes were reviewed and tested during implementation.

The accompanying lab report contains the prompts, screenshots, and evidence of the development process.

## Submission Contents

- Updated Python source code
- Test files
- Lab report with screenshots and prompts
- Original gameplay video
- Fixed gameplay video
- Complete AI conversation history, as required by the assignment

## Conclusion

The Minesweeper project was updated to address boundary-safe traversal, win detection and flag handling, difficulty selection, and action-level feedback while retaining the existing modular Python structure.
