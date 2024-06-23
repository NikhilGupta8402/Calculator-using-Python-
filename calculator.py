import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="#1e1e1e")

        self.entry = tk.Entry(root, width=15, font=('Arial', 18), borderwidth=3, relief="flat", bg="#333333", fg="white")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            ('C', 1, 0, '#ff3b30'), ('%', 1, 1, '#ff9500'), ('←', 1, 2, '#ff9500'), ('/', 1, 3, '#ff9500'),
            ('7', 2, 0, '#4a4a4a'), ('8', 2, 1, '#4a4a4a'), ('9', 2, 2, '#4a4a4a'), ('*', 2, 3, '#ff9500'),
            ('4', 3, 0, '#4a4a4a'), ('5', 3, 1, '#4a4a4a'), ('6', 3, 2, '#4a4a4a'), ('-', 3, 3, '#ff9500'),
            ('1', 4, 0, '#4a4a4a'), ('2', 4, 1, '#4a4a4a'), ('3', 4, 2, '#4a4a4a'), ('+', 4, 3, '#ff9500'),
            ('00', 5, 0, '#4a4a4a'), ('0', 5, 1, '#4a4a4a'), ('.', 5, 2, '#4a4a4a'), ('=', 5, 3, '#34c759')
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            column = button[2]
            color = button[3]
            colspan = button[4] if len(button) == 5 else 1
            self.create_circle_button(text, row, column, color, colspan)

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

        self.root.bind("<Key>", self.on_key_press)

    def create_circle_button(self, text, row, column, color, colspan=1):
        btn_canvas = tk.Canvas(self.root, width=60, height=60, bg="#1e1e1e", highlightthickness=0)
        btn_canvas.grid(row=row, column=column, columnspan=colspan, padx=2, pady=2)
        btn_canvas.create_oval(5, 5, 55, 55, fill=color, outline=color)
        btn_canvas.create_text(30, 30, text=text, fill="white", font=('Arial', 14, 'bold'))
        btn_canvas.bind("<Button-1>", lambda event, t=text: self.on_button_click(t))

    def on_button_click(self, value):
        if value == "C":
            self.entry.delete(0, tk.END)
        elif value == "←":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])
        elif value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "%":
            try:
                result = eval(self.entry.get()) / 100
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in "+-*/.":
            self.entry.insert(tk.END, key)
        elif key == '\r':
            self.on_button_click('=')
        elif key == '\b':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])
        elif key.lower() == 'c':
            self.on_button_click('C')


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
