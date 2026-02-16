from datetime import datetime

FILE = "reminders.txt"

def add_reminder(text):
    with open(FILE, "a") as f:
        f.write(f"[{datetime.now()}] {text}\n")
    return "Reminder saved."

def show_reminders():
    try:
        return open(FILE).read()
    except:
        return "No reminders."
