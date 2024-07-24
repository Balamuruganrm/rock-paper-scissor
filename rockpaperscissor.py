import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.choices = ["Rock", "Paper", "Scissors"]

        self.user_choice = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose Rock, Paper, or Scissors:").pack()

        self.choice_menu = tk.OptionMenu(self.root, self.user_choice, *self.choices)
        self.choice_menu.pack()

        tk.Button(self.root, text="Play", command=self.play).pack()

        tk.Label(self.root, text="Result:").pack()
        self.result_label = tk.Label(self.root, textvariable=self.result)
        self.result_label.pack()

    def play(self):
        user_choice = self.user_choice.get()
        if user_choice not in self.choices:
            messagebox.showwarning("Invalid Choice", "Please select Rock, Paper, or Scissors.")
            return

        computer_choice = random.choice(self.choices)
        self.result.set(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            self.result.set(f"Computer chose: {computer_choice}\nIt's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.result.set(f"Computer chose: {computer_choice}\nYou win!")
        else:
            self.result.set(f"Computer chose: {computer_choice}\nYou lose!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
