import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry # type: ignore
from tkinter import filedialog

def add_task():
    task = entry.get()
    priority = priority_var.get()
    due_date = date_entry.get()
    if task:
        # Define color based on priority
        if priority == "High":
            color = "red"
        elif priority == "Medium":
            color = "orange"
        else:
            color = "blue"
            
        # Insert task with priority and color
        listbox.insert(tk.END, f"{task} ({priority}) - Due: {due_date}")
        listbox.itemconfig(tk.END, {'fg': color})  # Apply color to the task text
        entry.delete(0, tk.END)

def complete_task():
    selection = listbox.curselection()
    if selection:
        listbox.itemconfig(selection, bg="green", fg="white")  # Change background and foreground colors
        listbox.selection_clear(selection)

def delete_task():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection)

def download_list():
    tasks = listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")

root = tk.Tk()
root.title("To-Do List Application")
root.configure(background="#F0F0F0")  # Set background color to light grey

style = ttk.Style()
style.theme_use("clam")

# Change background color for all widgets to light grey
style.configure(".", background="#F0F0F0", foreground="black", font=("Helvetica", 12))

# Highlight important widgets
style.configure("TLabel", font=("Helvetica", 12, "bold"), foreground="#333333")  # Dark grey text color for labels
style.configure("TButton", font=("Helvetica", 12, "bold"), background="light blue", foreground="white")  # Blue button with white text
style.map("TButton", background=[("active", "#0056b3")])  # Darker blue when hovered over

entry_label = ttk.Label(root, text="Task:")
entry_label.pack(pady=(10, 5))

entry = tk.Entry(root, width=50)
entry.pack()

priority_label = ttk.Label(root, text="Priority:")
priority_label.pack(pady=(10, 5))

priority_var = tk.StringVar()
priority_dropdown = ttk.Combobox(root, width=20, textvariable=priority_var)
priority_dropdown['values'] = ("High", "Medium", "Low")
priority_dropdown.current(0)
priority_dropdown.pack()

date_label = ttk.Label(root, text="Due Date:")
date_label.pack(pady=(10, 5))

date_entry = DateEntry(root, width=12, background='#007BFF', foreground='white', borderwidth=2)  # Blue background for date entry
date_entry.pack()

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

complete_button = ttk.Button(root, text="Mark Completed", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.RIGHT, padx=5)

download_button = ttk.Button(root, text="Download List", command=download_list)
download_button.pack(pady=10)

root.mainloop()
