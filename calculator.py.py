import tkinter as tk

# Function to update the expression in the text entry box
def press(num):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Function to evaluate the final expression
def equalpress():
    try:
        total = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, total)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="black")

# Entry widget for display
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right", bg="#fafafa")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button layout (like a real calculator)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for (text, row, col, *colspan) in buttons:
    colspan = colspan[0] if colspan else 1
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 20), bg="#ffb84d", fg="black",
                        height=2, width=16, command=equalpress)
        btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Arial", 20), bg="#ff6666", fg="white",
                        height=2, width=4, command=clear)
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    else:
        btn = tk.Button(root, text=text, font=("Arial", 20), bg="#333", fg="white",
                        height=2, width=4, command=lambda t=text: press(t))
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

# Make the grid cells expand equally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()