import os

FILE = "todo.txt"

def create_todo():
    open(FILE, "a").close()
    return "To-do ready. Say: add <task>"

def add_todo(item):
    with open(FILE, "a") as f:
        f.write(f"- {item}\n")
    return f"Added: {item}"

def show_todo():
    if not os.path.exists(FILE):
        return "No tasks."
    return open(FILE).read()

def clear_todo():
    open(FILE, "w").close()
    return "To-do cleared."
