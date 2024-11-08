import tkinter as tk
from tkinter import messagebox

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved      
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Reset if not valid

    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True

def check_for_duplicates(board):
    for i in range(9):
        row = [num for num in board[i] if num != 0]
        if len(row) != len(set(row)):
            return False, f"Duplicate entries in row {i+1}"

        col = [board[j][i] for j in range(9) if board[j][i] != 0]
        if len(col) != len(set(col)):
            return False, f"Duplicate entries in column {i+1}"

    # Check 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for i in range(3):
                for j in range(3):
                    num = board[box_row * 3 + i][box_col * 3 + j]
                    if num != 0:
                        box.append(num)
            if len(box) != len(set(box)):
                return False, f"Duplicate entries in 3x3 box starting at ({box_row * 3 + 1}, {box_col * 3 + 1})"

    return True, ""

def display_board(board):
    for i in range(9):
        for j in range(9):
                entries[i][j].insert(0,board[i][j])

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            enter = entries[i][j].get()
            row.append(int(enter) if enter.isdigit() and enter != "" else 0)
        board.append(row)
    return board

def solve():
    board = get_board()
    val, message = check_for_duplicates(board)
    if not val:
        messagebox.showerror("Error", message)
        return
    
    solve_sudoku(board)
    display_board(board)

def validate_input(M):
    if M == "" or M in "123456789" and len(M)==1 :  # Allow empty input or digits 1-9
        return True
    return False

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None for k in range(9)] for k in range(9)]
for i in range(9):
    for j in range(9):
        entry = tk.Entry(root,width=3, font=('Arial', 30), justify='center')
        entry.grid(row=i, column=j, padx=5, pady=5)
        entries[i][j] = entry
        entry.config(validate="key",validatecommand = (root.register(validate_input), '%P'))

solve_button = tk.Button(root, text="Solve", command=solve, font=('Arial', 16))
solve_button.grid(row=9, columnspan=10, pady=10)
root.mainloop()
