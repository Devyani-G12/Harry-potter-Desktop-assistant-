"""Reminder Management Agent

Handles creating and displaying reminders with timestamps.
"""

import os
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

REMINDER_FILE = "assistant_reminders.txt"


class ReminderManager:
    """Manages reminder operations."""
    
    def __init__(self, file_path: str = REMINDER_FILE):
        """Initialize reminder manager.
        
        Args:
            file_path: Path to reminders file
        """
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Ensure reminder file exists."""
        if not Path(self.file_path).exists():
            try:
                Path(self.file_path).touch()
                logger.info(f"Created reminder file: {self.file_path}")
            except Exception as e:
                logger.error(f"Error creating reminder file: {e}")
    
    def add_reminder(self, text: str) -> str:
        """Add a new reminder.
        
        Args:
            text: Reminder text
        
        Returns:
            Status message
        """
        if not text or not isinstance(text, str):
            return "Invalid reminder text."
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {text}\n")
            
            logger.info(f"Added reminder: {text}")
            return f"Reminder saved: {text}"
        
        except Exception as e:
            logger.error(f"Error adding reminder: {e}")
            return "Could not save reminder."
    
    def get_reminders(self) -> str:
        """Get all reminders.
        
        Returns:
            Formatted reminder list
        """
        try:
            if not Path(self.file_path).exists():
                return "No reminders set."
            
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
            
            if not content:
                return "No reminders set."
            
            return content
        
        except Exception as e:
            logger.error(f"Error reading reminders: {e}")
            return "Could not read reminders."
    
    def clear_reminders(self) -> str:
        """Clear all reminders.
        
        Returns:
            Status message
        """
        try:
            Path(self.file_path).write_text("", encoding="utf-8")
            logger.info("Cleared all reminders")
            return "All reminders cleared."
        
        except Exception as e:
            logger.error(f"Error clearing reminders: {e}")
            return "Could not clear reminders."


# Global reminder manager instance
_reminder_manager = ReminderManager()


def add_reminder(text: str) -> str:
    """Add a new reminder.
    
    Args:
        text: Reminder text
    
    Returns:
        Status message
    """
    return _reminder_manager.add_reminder(text)


def show_reminders() -> str:
    """Show all reminders.
    
    Returns:
        Formatted reminder list
    """
    return _reminder_manager.get_reminders()


def clear_reminders() -> str:
    """Clear all reminders.
    
    Returns:
        Status message
    """
    return _reminder_manager.clear_reminders()
