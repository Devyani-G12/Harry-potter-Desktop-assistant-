"""Conversation Handler Module

Manages basic conversation responses and natural interactions with the user.
"""

import random
import logging
from typing import Optional, List, Tuple

logger = logging.getLogger(__name__)

# Conversation patterns - tuple of (keywords, responses)
CONVERSATION_PATTERNS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "greetings"],
        "responses": [
            "Hello! How can I help?",
            "Hi there! What do you need?",
            "Hey! I'm listening.",
            "Greetings! Ready to assist."
        ]
    },
    "status": {
        "keywords": ["how are you", "how you doing", "how are you doing"],
        "responses": [
            "I'm running smoothly, thank you!",
            "Operating at full capacity!",
            "All systems optimal!",
            "Functioning perfectly!"
        ]
    },
    "identity": {
        "keywords": ["who are you", "what are you", "introduce yourself"],
        "responses": [
            "I'm your desktop assistant!",
            "I'm Harry Potter, the boy who lived! Well, his digital counterpart anyway.",
            "I'm your voice-controlled desktop companion.",
            "I'm a magical desktop assistant here to help!"
        ]
    },
    "thanks": {
        "keywords": ["thank you", "thanks", "appreciate", "much appreciated"],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "My pleasure!",
            "Anytime! That's what I'm here for."
        ]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "responses": [
            "Goodbye! See you later!",
            "Take care!",
            "Until next time!",
            "Farewell, my friend!"
        ]
    }
}


def basic_conversation(text: str) -> Optional[str]:
    """Generate a basic conversation response.
    
    Args:
        text: User input text
    
    Returns:
        Response string or None if no match found
    """
    if not text or not isinstance(text, str):
        return None
    
    text_lower = text.lower().strip()
    
    # Check each conversation pattern
    for pattern_name, pattern_data in CONVERSATION_PATTERNS.items():
        keywords = pattern_data["keywords"]
        responses = pattern_data["responses"]
        
        # Check if any keyword matches
        if any(keyword in text_lower for keyword in keywords):
            response = random.choice(responses)
            logger.debug(f"Matched conversation pattern '{pattern_name}': {response}")
            return response
    
    return None


def is_farewell(text: str) -> bool:
    """Check if text is a farewell expression.
    
    Args:
        text: User input text
    
    Returns:
        True if farewell detected, False otherwise
    """
    if not text:
        return False
    
    text_lower = text.lower().strip()
    farewell_keywords = CONVERSATION_PATTERNS["farewell"]["keywords"]
    return any(keyword in text_lower for keyword in farewell_keywords)
