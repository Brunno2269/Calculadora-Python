# -*- coding: utf-8 -*-

# @autor: Bruno Davila
# @github: github.com/brunno2269

import tkinter as tk
from app.themes import themes

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("400x600")
        self.master.resizable(False, False)

        # Configuração do tema
        self.theme = themes["Dark"]
        self.master.configure(bg=self.theme["master_bg"])

        # Variável para exibir a entrada e o resultado
        self.input_var = tk.StringVar()

        # Layout principal
        self.create_widgets()

    def create_widgets(self):
        # Campo de entrada
        self.input_field = tk.Entry(
            self.master,
            textvariable=self.input_var,
            bg=self.theme["input"]["bg"],
            fg=self.theme["input"]["fg"],
            font=self.theme["input"]["font"],
            justify="right",
            bd=0,
        )
        self.input_field.pack(fill=tk.BOTH, padx=10, pady=10, ipady=20)

        # Frame para os botões
        self.button_frame = tk.Frame(self.master, bg=self.theme["frame_bg"])
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        # Botões
        buttons = [
            ("C", 1, 0, self.clear, "clear"),
            ("←", 1, 1, self.backspace, "operator"),
            ("%", 1, 2, lambda: self.add_input("%"), "operator"),
            ("/", 1, 3, lambda: self.add_input("/"), "operator"),
            ("7", 2, 0, lambda: self.add_input("7"), "numeric"),
            ("8", 2, 1, lambda: self.add_input("8"), "numeric"),
            ("9", 2, 2, lambda: self.add_input("9"), "numeric"),
            ("*", 2, 3, lambda: self.add_input("*"), "operator"),
            ("4", 3, 0, lambda: self.add_input("4"), "numeric"),
            ("5", 3, 1, lambda: self.add_input("5"), "numeric"),
            ("6", 3, 2, lambda: self.add_input("6"), "numeric"),
            ("-", 3, 3, lambda: self.add_input("-"), "operator"),
            ("1", 4, 0, lambda: self.add_input("1"), "numeric"),
            ("2", 4, 1, lambda: self.add_input("2"), "numeric"),
            ("3", 4, 2, lambda: self.add_input("3"), "numeric"),
            ("+", 4, 3, lambda: self.add_input("+"), "operator"),
            ("0", 5, 0, lambda: self.add_input("0"), "numeric"),
            (".", 5, 1, lambda: self.add_input("."), "numeric"),
            ("=", 5, 2, self.calculate, "operator"),
        ]

        for text, row, col, command, style in buttons:
            button_style = self.theme["buttons"][style]
            button = tk.Button(
                self.button_frame,
                text=text,
                bg=button_style["bg"],
                fg=button_style["fg"],
                activebackground=button_style["activebackground"],
                font="Arial 20 bold",
                command=command,
                bd=0,
            )
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

    def add_input(self, value):
        self.input_var.set(self.input_var.get() + value)

    def clear(self):
        self.input_var.set("")

    def backspace(self):
        current_input = self.input_var.get()
        self.input_var.set(current_input[:-1])

    def calculate(self):
        try:
            result = eval(self.input_var.get())
            self.input_var.set(result)
        except Exception:
            self.input_var.set("Erro")
