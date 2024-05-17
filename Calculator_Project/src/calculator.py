import tkinter as tk
import math

def click_button(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power():
    try:
        expression = entry.get()
        result = eval(expression) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def trig_function(func):
    try:
        value = float(entry.get())
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def logarithm():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry field
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons
button_list = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("C", 1, 3), ("AC", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3), ("-", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3), ("/", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("^", 4, 2), ("√", 4, 3), ("=", 4, 4),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), ("(", 5, 4),
    (")", 6, 0), (math.pi, 6, 1), (math.e, 6, 2), ("^", 6, 3), (" ", 6, 4)
]

for (text, row, column) in button_list:
    if text in ["C", "AC", "=", "^", "√", "sin", "cos", "tan", "log", "(", ")", math.pi, math.e]:
        command = lambda t=text: click_button(t)
    else:
        command = lambda t=text: click_button(str(t))
    button = tk.Button(root, text=str(text), padx=20, pady=10, command=command)
    button.grid(row=row, column=column)

# Function buttons
button_square = tk.Button(root, text="x^2", padx=20, pady=10, command=power)
button_square.grid(row=7, column=0)
button_log = tk.Button(root, text="log", padx=20, pady=10, command=logarithm)
button_log.grid(row=7, column=1)
button_sin = tk.Button(root, text="sin", padx=20, pady=10, command=lambda: trig_function("sin"))
button_sin.grid(row=7, column=2)
button_cos = tk.Button(root, text="cos", padx=20, pady=10, command=lambda: trig_function("cos"))
button_cos.grid(row=7, column=3)
button_tan = tk.Button(root, text="tan", padx=20, pady=10, command=lambda: trig_function("tan"))
button_tan.grid(row=7, column=4)

# Equal button
equal_button = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
equal_button.grid(row=4, column=4)

root.mainloop()