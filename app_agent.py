"""Application Management Agent

Handles opening and closing applications via voice commands.
"""

import subprocess
import ctypes
import logging
import sys
from typing import Optional
from pathlib import Path

logger = logging.getLogger(__name__)

# Application shortcuts
APP_SHORTCUTS = {
    "chrome": "chrome",
    "google chrome": "chrome",
    "firefox": "firefox",
    "edge": "msedge",
    "calculator": "microsoft.windows.calculator:",
    "notepad": "notepad",
    "paint": "paint",
    "camera": "microsoft.windows.camera:",
    "settings": "ms-settings:"
}

# Website shortcuts
WEBSITE_SHORTCUTS = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://stackoverflow.com",
    "linkedin": "https://www.linkedin.com"
}


def is_windows() -> bool:
    """Check if running on Windows.
    
    Returns:
        True if on Windows, False otherwise
    """
    return sys.platform.startswith('win')


def close_active_window() -> str:
    """Close the currently active window.
    
    Returns:
        Status message
    """
    try:
        if not is_windows():
            logger.warning("Close window only supported on Windows")
            return "Close window is only supported on Windows."
        
        user32 = ctypes.windll.user32
        hwnd = user32.GetForegroundWindow()
        
        if hwnd:
            user32.PostMessageW(hwnd, 0x0010, 0, 0)  # WM_CLOSE
            logger.info("Closed active window")
            return "Closing current application."
        else:
            logger.warning("No active window found")
            return "No active window to close."
    
    except Exception as e:
        logger.error(f"Error closing window: {e}")
        return "Could not close window."


def open_app(name: str) -> Optional[str]:
    """Open an application by name.
    
    Args:
        name: Application name
    
    Returns:
        Status message or None if not found
    """
    if not name or not isinstance(name, str):
        return None
    
    text = name.lower().strip()
    
    # Check for close command
    if any(word in text for word in ["close", "closed"]):
        return close_active_window()
    
    # Check application shortcuts
    for app_key, app_value in APP_SHORTCUTS.items():
        if app_key in text:
            try:
                if is_windows():
                    subprocess.Popen(f"start {app_value}", shell=True)
                else:
                    # Fallback for non-Windows systems
                    subprocess.Popen([app_value])
                
                logger.info(f"Opened application: {app_value}")
                return f"Opening {app_key}."
            except Exception as e:
                logger.error(f"Error opening {app_key}: {e}")
                return f"Could not open {app_key}."
    
    # Check website shortcuts
    for site_key, site_url in WEBSITE_SHORTCUTS.items():
        if site_key in text:
            try:
                if is_windows():
                    subprocess.Popen(f"start {site_url}", shell=True)
                else:
                    subprocess.Popen(["open", site_url])
                
                logger.info(f"Opened website: {site_url}")
                return f"Opening {site_key}."
            except Exception as e:
                logger.error(f"Error opening {site_key}: {e}")
                return f"Could not open {site_key}."
    
    return None
