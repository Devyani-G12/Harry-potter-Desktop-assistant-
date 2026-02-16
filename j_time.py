from datetime import datetime, timedelta
import re

def handle_datetime(text):
    text = text.lower()
    now = datetime.now()

    # ---- TIME ----
    if "time" in text or "what is time" in text or "whats time":
        return now.strftime("Current time is %I:%M %p")

    # ---- DATE / TODAY ----
    if "date" in text or "today" in text or "today is ":
        return now.strftime("Today's date is %d %B %Y")

    # ---- DAY ----
    if "day" in text or "what is today " in text:
        return now.strftime("Today is %A")

    # ---- MONTH ----
    if "month" in text or"which month is this" in text or "we are in month"in text:
        return now.strftime("Current month is %B")

    # ---- YEAR ----
    if "year" in text or " we are in " in text :
        return now.strftime("Current year is %Y")

    # ---- YESTERDAY ----
    if "yesterday" in text:
        d = now - timedelta(days=1)
        return d.strftime("Yesterday was %A, %d %B %Y")

    # ---- LAST WEEK ----
    if "last week" in text:
        d = now - timedelta(days=7)
        return d.strftime("Last week was %A, %d %B %Y")

    # ---- ANY N DAYS BACK / AGO ----
    match = re.search(r'(\d+)\s+days?\s+(back|ago|before)', text)
    if match:
        days = int(match.group(1))
        d = now - timedelta(days=days)
        return d.strftime(f"{days} days back was %A, %d %B %Y")

    return None
