"""To-Do List Management Agent

Handles creating, managing, and displaying to-do lists.
"""

import os
import logging
from pathlib import Path
from typing import List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

TODO_FILE = "assistant_todos.txt"
TODO_BACKUP = "assistant_todos.backup"


class TodoManager:
    """Manages to-do list operations."""
    
    def __init__(self, file_path: str = TODO_FILE):
        """Initialize todo manager.
        
        Args:
            file_path: Path to todo file
        """
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Ensure todo file exists."""
        if not Path(self.file_path).exists():
            try:
                Path(self.file_path).touch()
                logger.info(f"Created todo file: {self.file_path}")
            except Exception as e:
                logger.error(f"Error creating todo file: {e}")
    
    def add_todo(self, item: str) -> str:
        """Add a new to-do item.
        
        Args:
            item: To-do item text
        
        Returns:
            Status message
        """
        if not item or not isinstance(item, str):
            return "Invalid to-do item."
        
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                f.write(f"[ ] {item} ({timestamp})\n")
            
            logger.info(f"Added todo: {item}")
            return f"Added: {item}"
        
        except Exception as e:
            logger.error(f"Error adding todo: {e}")
            return "Could not add to-do item."
    
    def get_todos(self) -> str:
        """Get all to-do items.
        
        Returns:
            Formatted to-do list
        """
        try:
            if not Path(self.file_path).exists():
                return "No tasks yet."
            
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
            
            if not content:
                return "No tasks yet."
            
            return content
        
        except Exception as e:
            logger.error(f"Error reading todos: {e}")
            return "Could not read to-do list."
    
    def clear_todos(self) -> str:
        """Clear all to-do items.
        
        Returns:
            Status message
        """
        try:
            # Create backup before clearing
            if Path(self.file_path).exists():
                with open(self.file_path, "r", encoding="utf-8") as f:
                    backup_content = f.read()
                
                with open(TODO_BACKUP, "w", encoding="utf-8") as f:
                    f.write(backup_content)
            
            # Clear the file
            Path(self.file_path).write_text("", encoding="utf-8")
            logger.info("Cleared all todos")
            return "To-do list cleared."
        
        except Exception as e:
            logger.error(f"Error clearing todos: {e}")
            return "Could not clear to-do list."
    
    def remove_todo(self, item_number: int) -> str:
        """Remove a specific to-do item.
        
        Args:
            item_number: Index of item to remove (1-based)
        
        Returns:
            Status message
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            if 0 < item_number <= len(lines):
                removed_item = lines.pop(item_number - 1)
                
                with open(self.file_path, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                
                logger.info(f"Removed todo item {item_number}")
                return f"Removed: {removed_item.strip()}"
            else:
                return "Invalid item number."
        
        except Exception as e:
            logger.error(f"Error removing todo: {e}")
            return "Could not remove to-do item."


# Global todo manager instance
_todo_manager = TodoManager()


def create_todo() -> str:
    """Create a new to-do list.
    
    Returns:
        Status message
    """
    _todo_manager._ensure_file_exists()
    return "To-do list ready! Say: add <task>"


def add_todo(item: str) -> str:
    """Add an item to the to-do list.
    
    Args:
        item: To-do item text
    
    Returns:
        Status message
    """
    return _todo_manager.add_todo(item)


def show_todo() -> str:
    """Show all to-do items.
    
    Returns:
        Formatted to-do list
    """
    return _todo_manager.get_todos()


def clear_todo() -> str:
    """Clear all to-do items.
    
    Returns:
        Status message
    """
    return _todo_manager.clear_todos()
