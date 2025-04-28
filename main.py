import tkinter as tk
from tkinter import messagebox

# A basic starting Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.root, width=50, height=50)
                frame.grid(row=i, column=j, padx=1, pady=1)
                entry = tk.Entry(frame, width=2, font=('Arial', 24), justify="center")
                entry.pack(expand=True, fill="both")
                if board[i][j] != 0:
                    entry.insert(0, str(board[i][j]))
                    entry.config(state='disabled', disabledforeground="black")
                self.entries[i][j] = entry

        submit_button = tk.Button(self.root, text="Check", command=self.check_solution, font=('Arial', 14))
        submit_button.grid(row=9, column=0, columnspan=9, sticky="nsew")

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val == "":
                    messagebox.showerror("Error", "Incomplete board!")
                    return
                if not val.isdigit() or not (1 <= int(val) <= 9):
                    messagebox.showerror("Error", "Invalid entry at ({}, {})".format(i+1, j+1))
                    return

        if self.is_valid_solution():
            messagebox.showinfo("Success", "Congratulations! You solved the Sudoku!")
        else:
            messagebox.showerror("Error", "Wrong solution. Try again!")

    def is_valid_solution(self):
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                # Row
                num1 = int(self.entries[i][j].get())
                if num1 in row:
                    return False
                row.add(num1)

                # Column
                num2 = int(self.entries[j][i].get())
                if num2 in col:
                    return False
                col.add(num2)

                # Box
                box_row = 3 * (i // 3) + j // 3
                box_col = 3 * (i % 3) + j % 3
                num3 = int(self.entries[box_row][box_col].get())
                if num3 in box:
                    return False
                box.add(num3)

        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
