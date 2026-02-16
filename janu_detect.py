import sounddevice as sd
import numpy as np
import time
import threading
import queue
from whisper import load_model

from j_commands import execute_command
from j_conversation import basic_conversation

model = load_model("tiny")   # 🔥 MUST be tiny for realtime

SAMPLE_RATE = 16000
BUFFER_SECONDS = 3
BUFFER_SIZE = SAMPLE_RATE * BUFFER_SECONDS

audio_q = queue.Queue()
buffer = []

icon_ref = None

def audio_callback(indata, frames, time_info, status):
    global buffer
    buffer.extend(indata.flatten())

    if len(buffer) >= BUFFER_SIZE:
        chunk = np.array(buffer[:BUFFER_SIZE], dtype=np.float32)
        buffer = buffer[BUFFER_SIZE:]
        audio_q.put(chunk)

def audio_worker():
    while True:
        audio = audio_q.get()
        print("🧠 Transcribing...")
        result = model.transcribe(audio, language="en", fp16=False)
        text = result["text"].strip().lower()

        if not text:
            continue

        print("VOICE:", text)

        cmd = execute_command(text)
        if cmd:
            icon_ref.after(0, icon_ref.show_panel, cmd)
            continue

        reply = basic_conversation(text)
        if reply:
            icon_ref.after(0, icon_ref.show_panel, reply)

def start_listening(icon):
    global icon_ref
    icon_ref = icon

    threading.Thread(target=audio_worker, daemon=True).start()

    sd.default.samplerate = 16000
    sd.default.channels = 1

    with sd.InputStream(callback=audio_callback):
        while True:
            time.sleep(1)

