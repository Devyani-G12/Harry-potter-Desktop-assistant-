import subprocess
import ctypes
import ctypes

def close_active_window():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    if hwnd:
        user32.PostMessageW(hwnd, 0x0010, 0, 0)  # WM_CLOSE
        return "Closing current application"
    return "No active window to close"

def open_app(text):
    text = text.lower()

    if "google" in text:
        subprocess.Popen("start https://www.google.com", shell=True)
        return "Opening Google"

    if "youtube" in text:
        subprocess.Popen("start https://www.youtube.com", shell=True)
        return "Opening YouTube"

    if "chrome" in text:
        subprocess.Popen("start chrome", shell=True)
        return "Opening Chrome"

    if "calculator" in text:
        subprocess.Popen("start microsoft.windows.calculator:", shell=True)
        return "Opening Calculator"

    # 🔹 ONE GENERIC CLOSE
    if "close" in text or "closed" in text:
        return close_active_window()

    return None
