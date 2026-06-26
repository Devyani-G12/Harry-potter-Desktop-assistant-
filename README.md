## 🧙‍♂️ Harry Potter Desktop Assistant

A lightweight Python desktop assistant using Whisper (tiny model) for real-time voice recognition. It executes predefined commands and supports conversation responses with multiple automation features.

## ✨ Features

### 🎙️ **Voice Control**
- Real-time voice input from microphone
- Fast transcription using Whisper (tiny model)
- Continuous audio processing in 3-second chunks
- Multi-threaded audio processing

### 💻 **Application Management**
- Open applications (Chrome, Calculator, YouTube, Google)
- Open web browsers and websites
- Close active applications with voice command
- Support for custom application shortcuts

### 📝 **Task Management**
- **To-Do List**: Create, add, view, and clear tasks
- **Reminders**: Set and view reminders
- Persistent state tracking for different intents

### 📂 **File & Folder Navigation**
- Open folders from voice commands
- File system access capabilities
- Folder navigation support

### 🔍 **Web Capabilities**
- Web search functionality
- Browser integration
- URL handling

### ⏰ **Time & Date Features**
- Get current time
- Get today's date
- Get current day
- Get current month
- Get current year
- Calculate relative dates (yesterday, last week, N days ago)
- Regex-based date parsing for flexible queries

### 💬 **Conversation Support**
- Greetings recognition (Hi, Hello)
- Status inquiries (How are you)
- Identity responses (Who are you)
- Gratitude handling (Thank you)
- Basic AI-like responses

### ⚙️ **Technical Features**
- JSON-based command execution
- Multi-threaded processing
- GUI icon panel for responses
- Modular architecture with separate agents
- Configurable settings via config files

## 🏗️ Architecture

The assistant is built with a modular design:

- **main.py** - Entry point
- **app_agent.py** - Application control
- **folder_agent.py** - Folder management
- **todo_agent.py** - To-do list management
- **reminder_agent.py** - Reminder management
- **search_agent.py** - Web search functionality
- **j_time.py** - Date/time handling
- **j_commands.py** - Command execution orchestration
- **j_conversation.py** - Conversation responses
- **janu_detect.py** - Audio capture and transcription
- **janu_icon.py** - GUI/Icon display
- **j_config.py** - Configuration settings

## ⚙️ How It Works

1. Audio is captured continuously from the microphone
2. Processed in 3-second chunks using Whisper
3. Whisper converts speech → text
4. If text matches a command → execute action
5. Otherwise → return a conversation response
6. Response displayed via GUI panel

## 🚀 Usage

Speak simple commands like:

- **App Control**: "Open Chrome", "Open Camera", "Close"
- **Tasks**: "Make to do", "Add buy groceries", "Show todo"
- **Reminders**: "Remind me", "Add call mom", "Show reminders"
- **Search**: "Search Python tutorials"
- **Time/Date**: "What's the time?", "What's today's date?", "What day is it?"
- **Navigation**: "Open Documents"

## 📦 Dependencies

- **SpeechRecognition** - Audio processing
- **openai-whisper** - Speech-to-text (tiny model)
- **torch** - Deep learning framework
- **numpy** - Numerical computing
- **sounddevice** - Audio input/output
- **pyttsx3** - Text-to-speech
- **opencv-python** - Computer vision
- **psutil** - System utilities

## ⚠️ Limitations

- No advanced AI understanding (pattern matching based)
- Requires exact or close command match
- Limited conversation capability (predefined responses)
- Whisper tiny model may have accuracy limitations
- Windows-specific features (tested on Windows)
- Requires microphone and speakers setup

## 🔧 Configuration

Edit **j_config.py** to customize:
- Audio settings
- Response messages
- Application paths
- Supported commands

## 🎯 Future Enhancements

- [ ] Natural Language Processing (NLP) for better command understanding
- [ ] Custom command training
- [ ] Cloud-based AI responses
- [ ] Cross-platform support (Mac, Linux)
- [ ] Advanced reminder scheduling
- [ ] Email integration
- [ ] Calendar integration
- [ ] Voice output/Text-to-speech responses
- [ ] Command recording and playback
- [ ] Desktop notification system

## 👨‍💻 Author

**Devyani G**

---

*Accio Assistant!* 🪄
