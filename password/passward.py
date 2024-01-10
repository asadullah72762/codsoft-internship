import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length < 1:
        messagebox.showwarning("Warning", "Password length should be at least 1.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(tk.END, password)

def copy_to_clipboard():
    password = entry_password.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
frame_password = tk.Frame(root)
frame_password.pack(pady=10)

label_length = tk.Label(frame_password, text="Password Length:")
label_length.grid(row=0, column=0, padx=5)

entry_length = tk.Entry(frame_password, width=5)
entry_length.grid(row=0, column=1, padx=5)

button_generate = tk.Button(frame_password, text="Generate Password", command=generate_password)
button_generate.grid(row=0, column=2, padx=5)

entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=10)

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack()

# Start the main loop
root.mainloop()
