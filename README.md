## 🧙‍♂️ Harry Potter Desktop Assistant ##

A lightweight Python desktop assistant using Whisper (tiny model) for real-time voice recognition.
It executes predefined JSON commands and supports basic conversation responses.

## ✨ Features ##
🎙️ Real-time voice input
⚡ Fast transcription using Whisper (tiny)
📜 JSON-based command execution
💬 Basic conversation replies
🧵 Multithreaded processing

## ⚙️ How It Works ##
Audio is captured continuously from the microphone
Processed in small chunks (~3 seconds)
Whisper converts speech → text
If text matches a command → execute action
Otherwise → return a basic conversation response

## 💬 Supported Conversation ##
Greetings → "Hi", "Hello"
Status → "How are you"
Identity → "Who are you"
Thanks → "Thank you"
🪄 Usage

Speak simple commands like:

"Open Chrome"

"Open Camera"

## ⚠️ Only predefined commands in commands.json will execute.

## ⚠️ Limitations
No advanced AI understanding
Requires exact or close command match
Limited conversation capability

## 👨‍💻 Author

Devyani G
