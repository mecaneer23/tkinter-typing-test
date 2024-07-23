#!/usr/bin/env python3
import tkinter as tk
import time
import random


class TypingSpeedTest:
    def _get_random_word(self) -> str:
        with open("words.txt", encoding="utf-8") as file:
            return random.choice(file.read().split("\n"))

    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.word_label = tk.Label(root, font=("Verdana", 30))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Verdana", 30), width=20)
        self.entry.pack()

        self.start_button = tk.Button(
            root, text="Start", command=self.start_test, font=("Verdana", 20)
        )
        self.start_button.pack(pady=20)

        self.speed_label = tk.Label(root, font=("Verdana", 20))
        self.speed_label.pack()

        self.current_word = ""
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.start_elapsed_time = 0
        self.word_count = 0

    def generate_word(self):
        self.current_word = self._get_random_word()
        self.word_label.config(
            text=self.current_word,
            background="black",
            foreground="white",
        )

    def start_test(self):
        self.generate_word()
        self.start_button.pack_forget()

        self.entry.delete(0, tk.END)
        self.entry.focus()

        self.start_time = time.time()

    def restart_test(self):
        self.total_time = 0
        self.speed_label.config(text="")
        self.entry.config(state="normal")
        self.start_test()

    def calculate_speed(self):
        self.end_time = time.time()
        self.total_time += self.end_time - self.start_time

        wpm = round(self.word_count / (self.total_time / 60))
        self.speed_label.config(text=f"Your typing speed is {wpm} WPM.")
        self.start_button.pack(pady=20)
        self.entry.config(state="disabled")
        self.start_button.config(text="Restart", command=self.restart_test)

    def check_word(self, _):
        typed_word = self.entry.get()
        if typed_word == self.current_word:
            self.entry.delete(0, tk.END)
            self.word_count += 1
            self.generate_word()
        else:
            self.switch_label_bg_fg(self.word_label)

    def switch_label_bg_fg(self, label):
        bg = label.cget("background")
        fg = label.cget("foreground")
        label.configure(background=fg, foreground=bg)

    def run(self):
        self.root.bind("<Return>", self.check_word)
        self.root.after(60000, self.calculate_speed)
        self.root.mainloop()


root = tk.Tk()
app = TypingSpeedTest(root)

app.run()
