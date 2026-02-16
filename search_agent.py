import subprocess
import urllib.parse

def web_search(query):
    q = urllib.parse.quote(query)
    subprocess.Popen(f"start https://www.google.com/search?q={q}", shell=True)
    return f"Searching: {query}"
