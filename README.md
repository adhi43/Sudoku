# Sudoku Solver with Python and Tkinter
This project is a Sudoku Solver built with Python and Tkinter, featuring a graphical user interface (GUI) that allows users to input a Sudoku puzzle, validate entries, and solve it using a backtracking algorithm.
## Features
- Backtracking Solver: Uses a backtracking algorithm to fill empty cells and find solutions for the puzzle.
- Real-Time Validation: Checks for duplicate numbers in rows, columns, and 3x3 sub-grids, preventing invalid puzzles from being solved.
- User-Friendly GUI: Built with Tkinter, featuring an intuitive interface for puzzle input and solving.
- Input Restrictions: Accepts only numbers from 1-9 in each cell to ensure valid input.
## Usage
1. Run the sudoku_solver.py script to start the application.
2. Enter your Sudoku puzzle into the grid (leave empty cells blank or enter 0).
3. Click "Solve" to automatically solve the puzzle.
4. If there are any duplicates in rows, columns, or 3x3 boxes, an error message will appear, allowing you to correct the puzzle.
## How It Works
1. Input Validation:
- Ensures each cell contains only digits 1-9 or is left blank.
- Checks for duplicates in each row, column, and 3x3 sub-grid.
2. Backtracking Algorithm:
- Solves the puzzle by placing numbers 1-9 in empty cells.
- Uses recursion and backtracking to test each possibility, ensuring a valid solution is found.
3. Tkinter GUI:
- Displays a 9x9 grid of entry fields for easy input.
- Provides a "Solve" button to trigger the solution algorithm.
