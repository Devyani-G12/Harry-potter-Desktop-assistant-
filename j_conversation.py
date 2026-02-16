import random

def basic_conversation(text):
    if any(w in text for w in ("hi", "hello", "hey")):
        return random.choice([
            "Hello. How can I help?",
            "Hi. I’m listening."
        ])

    if "how are you" in text or "harry how are you" in text:
        return "I’m running smoothly."

    if "who are you" in text or "harry who are you" in text:
        return "I’m your desktop assistant." or "I'am The boy who lived !!"

    if " harry thank" in text:
        return "You’re welcome."

    return None
