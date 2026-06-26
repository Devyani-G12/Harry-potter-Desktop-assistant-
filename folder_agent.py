"""Folder Management Agent

Handles opening folders via voice commands.
"""

import os
import subprocess
import logging
import sys
from typing import Optional, Dict
from pathlib import Path

logger = logging.getLogger(__name__)

# Common folder shortcuts
FOLDER_SHORTCUTS: Dict[str, str] = {
    "documents": os.path.join(os.environ.get("USERPROFILE", Path.home()), "Documents"),
    "downloads": os.path.join(os.environ.get("USERPROFILE", Path.home()), "Downloads"),
    "desktop": os.path.join(os.environ.get("USERPROFILE", Path.home()), "Desktop"),
    "music": os.path.join(os.environ.get("USERPROFILE", Path.home()), "Music"),
    "pictures": os.path.join(os.environ.get("USERPROFILE", Path.home()), "Pictures"),
    "videos": os.path.join(os.environ.get("USERPROFILE", Path.home()), "Videos"),
    "home": os.path.expanduser("~"),
}


def open_folder(name: str) -> Optional[str]:
    """Open a folder by name or path.
    
    Args:
        name: Folder name or path
    
    Returns:
        Status message or None if not found
    """
    if not name or not isinstance(name, str):
        logger.warning("Invalid folder name provided")
        return None
    
    name_lower = name.lower().strip()
    folder_path = None
    folder_display_name = name
    
    # Check shortcuts first
    if name_lower in FOLDER_SHORTCUTS:
        folder_path = FOLDER_SHORTCUTS[name_lower]
        folder_display_name = name_lower
    else:
        # Try direct path
        expanded_path = os.path.expanduser(name)
        if os.path.isdir(expanded_path):
            folder_path = expanded_path
            folder_display_name = name
    
    if not folder_path:
        logger.warning(f"Folder not found: {name}")
        return None
    
    try:
        if sys.platform.startswith('win'):
            subprocess.Popen(f'explorer "{folder_path}"')
        elif sys.platform == 'darwin':  # macOS
            subprocess.Popen(['open', folder_path])
        else:  # Linux
            subprocess.Popen(['xdg-open', folder_path])
        
        logger.info(f"Opened folder: {folder_path}")
        return f"Opening {folder_display_name}."
    
    except Exception as e:
        logger.error(f"Error opening folder '{name}': {e}")
        return f"Could not open {folder_display_name}."


def add_custom_folder(name: str, path: str) -> bool:
    """Add a custom folder shortcut.
    
    Args:
        name: Shortcut name
        path: Folder path
    
    Returns:
        True if added successfully, False otherwise
    """
    if not os.path.isdir(path):
        logger.error(f"Path does not exist: {path}")
        return False
    
    FOLDER_SHORTCUTS[name.lower()] = path
    logger.info(f"Added custom folder shortcut: {name} -> {path}")
    return True
