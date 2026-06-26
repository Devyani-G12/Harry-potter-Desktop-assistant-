"""Context and State Management Module

Manages the global state and context of the assistant throughout its lifecycle.
"""

from typing import Optional, Dict, Any
import json
from pathlib import Path


class AssistantContext:
    """Manages the assistant's state and context."""
    
    _STATE_FILE = "assistant_state.json"
    
    def __init__(self):
        """Initialize context with default values."""
        self.last_intent: Optional[str] = None
        self.conversation_history: Dict[str, Any] = {}
        self.load_state()
    
    def set_intent(self, intent: str) -> None:
        """Set the current intent.
        
        Args:
            intent: The current user intent (e.g., 'todo', 'reminder')
        """
        self.last_intent = intent
        self.save_state()
    
    def clear_intent(self) -> None:
        """Clear the current intent."""
        self.last_intent = None
        self.save_state()
    
    def save_state(self) -> None:
        """Save context state to file."""
        try:
            state = {
                "last_intent": self.last_intent,
                "conversation_history": self.conversation_history
            }
            with open(self._STATE_FILE, 'w') as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save state: {e}")
    
    def load_state(self) -> None:
        """Load context state from file."""
        try:
            if Path(self._STATE_FILE).exists():
                with open(self._STATE_FILE, 'r') as f:
                    state = json.load(f)
                    self.last_intent = state.get("last_intent")
                    self.conversation_history = state.get("conversation_history", {})
        except Exception as e:
            print(f"Warning: Could not load state: {e}")


# Global context instance
last_intent: Optional[str] = None  # For backward compatibility
_context = AssistantContext()


def get_context() -> AssistantContext:
    """Get the global assistant context.
    
    Returns:
        AssistantContext: The global context instance
    """
    return _context
