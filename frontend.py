import tkinter as tk
import customtkinter as ctk
import requests

# Initialize the root window
root = ctk.CTk()
root.geometry("400x400")
root.title("To-Do List")

# Function to fetch and display tasks
def refresh_tasks():
    response = requests.get("http://127.0.0.1:5000/todos")
    tasks = response.json()

    # Clear current list
    for widget in frame.winfo_children():
        widget.destroy()

    # Display tasks
    for i, task in enumerate(tasks):
        task_text = task['task']
        task_label = ctk.CTkLabel(frame, text=task_text, width=200)
        task_label.grid(row=i, column=0, padx=10, pady=5)

        # Button to toggle task completion
        toggle_button = ctk.CTkButton(frame, text="Toggle Complete", command=lambda i=i: toggle_task(i))
        toggle_button.grid(row=i, column=1, padx=10, pady=5)

        # Button to delete task
        delete_button = ctk.CTkButton(frame, text="Delete", command=lambda i=i: delete_task(i))
        delete_button.grid(row=i, column=2, padx=10, pady=5)

# Function to toggle task completion
def toggle_task(index):
    response = requests.put(f"http://127.0.0.1:5000/todos/{index}")
    if response.status_code == 200:
        refresh_tasks()
    else:
        print(f"Error: {response.json()}")


# Function to delete a task
def delete_task(index):
    requests.delete(f"http://127.0.0.1:5000/todos/{index}")
    refresh_tasks()

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        requests.post("http://127.0.0.1:5000/todos", json={"task": task})
        task_entry.delete(0, tk.END)
        refresh_tasks()

# Frame for the task list
frame = ctk.CTkFrame(root)
frame.pack(pady=20)

# Input field for new tasks
task_entry = ctk.CTkEntry(root, placeholder_text="New Task", width=300)
task_entry.pack(pady=10)

# Button to add new tasks
add_button = ctk.CTkButton(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

# Load initial tasks
refresh_tasks()

# Start the main loop
root.mainloop()
