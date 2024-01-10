import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_index = listbox_tasks.curselection()
        listbox_tasks.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, selectmode=tk.SINGLE, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add.pack()

button_remove = tk.Button(root, text="Remove Task", width=48, command=remove_task)
button_remove.pack()

button_quit = tk.Button(root, text="Quit", width=48, command=root.destroy)
button_quit.pack()

# Start the main loop
root.mainloop()
