import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import random
import string
import pyperclip
from PIL import Image, ImageTk

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

#GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.resizable(False, False)

#Options Frame 
frame = ttk.LabelFrame(root, text="Password Options")
frame.pack(padx=20, pady=10, fill="x")

length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_spinbox = ttk.Spinbox(frame, from_=4, to=32, textvariable=length_var, width=5)
length_spinbox.grid(row=0, column=1, pady=5)

ttk.Checkbutton(frame, text="Include Uppercase", variable=upper_var).grid(row=1, column=0, sticky="w", padx=10)
ttk.Checkbutton(frame, text="Include Lowercase", variable=lower_var).grid(row=1, column=1, sticky="w", padx=10)
ttk.Checkbutton(frame, text="Include Numbers", variable=digit_var).grid(row=2, column=0, sticky="w", padx=10)
ttk.Checkbutton(frame, text="Include Symbols", variable=symbol_var).grid(row=2, column=1, sticky="w", padx=10)

#Generate Button 
ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

#Password Display
ttk.Entry(root, textvariable=password_var, font=("Courier", 12), justify="center", width=40).pack(pady=5)
ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

#App
root.mainloop()
