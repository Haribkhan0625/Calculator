import tkinter as tk
from tkinter import ttk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_pi():
    entry.insert(tk.END, math.pi)

def button_cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("720x560")
root.configure(bg="#222222")

# Create an entry widget
entry = tk.Entry(root, width=44, borderwidth=5, font=('Arial', 20), bg="#333333", fg="#FFFFFF")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('π', 5, 0), ('√', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
    ('tan', 6, 0)
]

# Create buttons
for (text, row, col) in buttons:
    button = ttk.Button(root, text=text, width=8, padding="20", command=lambda text=text: button_click(text), style='TButton')
    button.grid(row=row, column=col, padx=5, pady=5)
    if text == '=':
        button.config(command=button_equal)
    elif text == 'C':
        button.config(command=button_clear)
    elif text == '√':
        button.config(command=button_sqrt)
    elif text == 'π':
        button.config(command=button_pi)
    elif text == 'sin':
        button.config(command=button_sin)
    elif text == 'cos':
        button.config(command=button_cos)
    elif text == 'tan':
        button.config(command=button_tan)

# Style customization for buttons
style = ttk.Style()
style.configure('TButton', background='#77DDFF', foreground='#000000', font=('Arial', 14))

root.mainloop()
