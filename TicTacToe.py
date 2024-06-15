import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="lightblue")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font='Helvetica 24 bold', bg="lightblue", fg="darkblue")
        title.grid(row=0, column=0, columnspan=3, pady=20)
        
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font='Helvetica 20 bold', height=2, width=5, 
                                   bg="white", fg="black", command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row+1, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                self.buttons[row][col].config(text="X", bg="lightgreen", fg="black")
            else:
                self.buttons[row][col].config(text="O", bg="lightpink", fg="black")

            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "The game is a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        win_conditions = (
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        )
        return [player, player, player] in win_conditions

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", bg="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
