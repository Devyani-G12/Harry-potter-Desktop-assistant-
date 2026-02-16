import os
import subprocess

FOLDERS = {
    "documents": os.path.join(os.environ["USERPROFILE"], "Documents"),
    "downloads": os.path.join(os.environ["USERPROFILE"], "Downloads"),
    "desktop": os.path.join(os.environ["USERPROFILE"], "Desktop"),
}

def open_folder(name):
    if name in FOLDERS:
        subprocess.Popen(f'explorer "{FOLDERS[name]}"')
        return f"Opening {name}"
    return None
