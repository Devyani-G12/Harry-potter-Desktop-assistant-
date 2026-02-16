import context

from todo_agent import create_todo, add_todo, show_todo, clear_todo
from reminder_agent import add_reminder, show_reminders
from app_agent import open_app
from folder_agent import open_folder
from search_agent import web_search
from j_time import handle_datetime


def execute_command(text):
    text = text.lower()

    # ---------- TIME / DATE ----------
    result = handle_datetime(text)
    if result:
        return result

    # ---------- APP OPEN / CLOSE ----------
    result = open_app(text)
    if result:
        return result

    # ---------- TODO ----------
    if "make to do" in text:
        context.last_intent = "todo"
        return create_todo()

    if text.startswith("add ") and context.last_intent == "todo":
        return add_todo(text.replace("add", "", 1).strip())

    if "show todo" in text:
        return show_todo()

    if "clear todo" in text or "clear" in text:
        return clear_todo()

    # ---------- REMINDER ----------
    if "remind me" in text:
        context.last_intent = "reminder"
        return "What should I remind you about?"

    if text.startswith("add ") and context.last_intent == "reminder":
        return add_reminder(text.replace("add", "", 1).strip())

    if "show reminders" in text:
        return show_reminders()

    # ---------- FOLDER ----------
    if text.startswith("open "):
        return open_folder(text.replace("open", "", 1).strip())

    # ---------- SEARCH ----------
    if text.startswith("search "):
        return web_search(text.replace("search", "", 1).strip())

    return None
