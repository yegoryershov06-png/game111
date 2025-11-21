import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.player = "X"                    # кто сейчас ходит
        self.board = [""] * 9                # игровое поле

        # Заголовок
        self.label = tk.Label(self.root, text="Ход: X", font=("Arial", 20))
        self.label.pack(pady=20)

        # Игровое поле 3x3
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            btn = tk.Button(self.frame, text="", font=("Arial", 36), width=4, height=2,
                            bg="#f0f0f0", activebackground="#d0d0d0",
                            command=lambda x=i: self.click(x))
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

        # Кнопка новой игры
        restart_btn = tk.Button(self.root, text="Новая игра", font=("Arial", 16),
                                command=self.restart)
        restart_btn.pack(pady=20)

        self.root.mainloop()

    def click(self, pos):
        if self.board[pos] != "":           # клетка уже занята
            return

        self.board[pos] = self.player
        self.buttons[pos].config(text=self.player)

        if self.check_win():
            messagebox.showinfo("Победа!", f"Игрок {self.player} выиграл!")
            self.disable_buttons()
            return

        if "" not in self.board:
            messagebox.showinfo("Ничья!", "Ничья!")
            return

        # смена игрока
        self.player = "O" if self.player == "X" else "X"
        self.label.config(text=f"Ход: {self.player}")

    def check_win(self):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  # строки
            [0,3,6], [1,4,7], [2,5,8],  # столбцы
            [0,4,8], [2,4,6]            # диагонали
        ]
        for combo in wins:
            if (self.board[combo[0]] == self.board[combo[1]] ==
                self.board[combo[2]] == self.player):
                return True
        return False

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def restart(self):
        self.player = "X"
        self.board = [""] * 9
        self.label.config(text="Ход: X")
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#f0f0f0")

if __name__ == "__main__":
    TicTacToe()