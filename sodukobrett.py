import tkinter as tk
import random
import tkinter.messagebox

def generate_full_board():
    # Backtracking Sudoku generator
    board = [[0 for _ in range(9)] for _ in range(9)]

    def is_valid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def fill_board(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if fill_board(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    fill_board(board)
    return board

# Legg til knapp for "Meduim" i GUI
def fill_medium_board(gui):
    board = generate_medium_board()
    for i in range(9):
        for j in range(9):
            gui.entries[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                gui.entries[i][j].insert(0, str(board[i][j]))

# Legg til knapp for "Meduim" i GUI
def fill_expert_board(gui):
    board = generate_expert_board()
    for i in range(9):
        for j in range(9):
            gui.entries[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                gui.entries[i][j].insert(0, str(board[i][j]))

# Legg til knapp for "Lett" i GUI
def fill_easy_board(gui):
    board = generate_easy_board()
    for i in range(9):
        for j in range(9):
            gui.entries[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                gui.entries[i][j].insert(0, str(board[i][j]))

def generate_easy_board():
    # Generate a random full board, then remove numbers to leave 6 per row
    board = generate_full_board()
    for i in range(9):
        filled = random.sample(range(9), 7)
        for j in range(9):
            if j not in filled:
                board[i][j] = 0
    return board

def generate_medium_board():
    # Generate a random full board, then remove numbers to leave 6 per row
    board = generate_full_board()
    for i in range(9):
        filled = random.sample(range(9), 5)
        for j in range(9):
            if j not in filled:
                board[i][j] = 0
    return board

def generate_expert_board():
    # Generate a random full board, then remove numbers to leave 6 per row
    board = generate_full_board()
    for i in range(9):
        filled = random.sample(range(9), 3)
        for j in range(9):
            if j not in filled:
                board[i][j] = 0
    return board

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku")

        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                padx = 2
                pady = 2
                # Ekstra space kun under rad 3 og rad 6
                if i == 2 or i == 5:
                    pady = (2, 10)  # (top, bottom) ekstra under rad 3 og 6
                # Ekstra space kun på høyresiden av kolonne 3 og 6
                if j == 2 or j == 5:
                    padx = (2, 10)  # (left, right) ekstra på høyre av kolonne 3 og 6
                e = tk.Entry(master, width=2, font=('Arial', 18), justify='center')
                e.grid(row=i, column=j, padx=padx, pady=pady)
                # Koble til sjekk-funksjon når feltet mister fokus
                e.bind("<FocusOut>", lambda event: self.check_board())
                row.append(e)
            self.entries.append(row)

        self.solve_button = tk.Button(master, text="Løs", command=self.solve)
        self.solve_button.grid(row=1, column=11)

        self.easy_button = tk.Button(master, text="Lett", command=lambda: fill_easy_board(self))
        self.easy_button.grid(row=2, column=11)

        self.medium_button = tk.Button(master, text="Medium", command=lambda: fill_medium_board(self))
        self.medium_button.grid(row=3, column=11)

        self.expert_button = tk.Button(master, text="Expert", command=lambda: fill_expert_board(self))
        self.expert_button.grid(row=4, column=11)

    def solve(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    row.append(int(val))
                else:
                    row.append(0)
            board.append(row)

        def is_valid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num or board[x][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        def solve_sudoku(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for num in range(1, 10):
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve_sudoku(board):
                                    return True
                                board[i][j] = 0
                        return False
            return True

        if solve_sudoku(board):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(board[i][j]))
        else:
            tk.messagebox.showinfo("Sudoku", "Ingen løsning funnet!")

    def check_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    row.append(int(val))
                else:
                    row.append(0)
            board.append(row)

        # Sjekk om brettet er fullt
        if all(all(cell != 0 for cell in row) for row in board):
            # Sjekk om løsningen er gyldig
            if self.is_solution_valid(board):
                tkinter.messagebox.showinfo("Sudoku", "Gratulerer! Løsningen er riktig.")
            else:
                tkinter.messagebox.showinfo("Sudoku", "Beklager, løsningen er feil.")

    def is_solution_valid(self, board):
        # Sjekk rader, kolonner og bokser
        for i in range(9):
            if len(set(board[i])) != 9:
                return False
            col = [board[j][i] for j in range(9)]
            if len(set(col)) != 9:
                return False
        for box_row in range(3):
            for box_col in range(3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        nums.append(board[box_row*3 + i][box_col*3 + j])
                if len(set(nums)) != 9:
                    return False
        return True

root = tk.Tk()
gui = SudokuGUI(root)
root.mainloop()