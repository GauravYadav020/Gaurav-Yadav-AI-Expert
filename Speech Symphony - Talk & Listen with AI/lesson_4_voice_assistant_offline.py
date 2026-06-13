"""
================================================================================
LESSON 4: Voice Assistant (Offline) - Local Feedback Architectures
================================================================================
"""

import speech_recognition as sr
import pyttsx3
import platform

# ------------------------------------------------------------------------------
# ACTIVITY 1: Static Keyword Logic Router Framework
# ------------------------------------------------------------------------------
def execute_static_assistant_loop():
    print("\n=== OFFLINE COMMAND PROCESSING SYSTEM OPERATIONAL ===")
    engine = pyttsx3.init()
    queries = ["identify yourself", "check system status"]
    for q in queries:
        if "identify" in q:
            reply = "I am the Speech Symphony local assistant loop configuration."
        else: reply = "Unknown runtime command variant."
        engine.say(reply); engine.runAndWait()

# ------------------------------------------------------------------------------
# ACTIVITY 2: Integrated Offline Voice Interaction Loop Engine
# ------------------------------------------------------------------------------
def execute_integrated_offline_loop():
    print("\n=== OFFLINE INTEGRATED VOICE ASSISTANT ON-LINE ===")
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    with sr.Microphone() as src:
        recognizer.adjust_for_ambient_noise(src, duration=1)
        print("[READY] Ask a question aloud (e.g. status)...")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=4)
            query = recognizer.recognize_google(audio).lower()
            if "status" in query:
                reply = "Internal architecture telemetry looks stable and fully secure."
            else: reply = "Intent pattern unmapped."
            engine.say(reply); engine.runAndWait()
        except Exception as e: print(f"Processing Info: {e}")

# ------------------------------------------------------------------------------
# ACTIVITY 3: Continuous Workstation Interaction Escape Loop Engine
# ------------------------------------------------------------------------------
def execute_continuous_escape_loop():
    print("\n=== CONTINUOUS SYSTEM INTERACTION LIFE-CYCLE ===")
    engine = pyttsx3.init(); recognizer = sr.Recognizer()
    for cycle in range(1, 3):
        print(f"--- Iteration Spin Loop Index #{cycle} ---")
        with sr.Microphone() as src:
            try:
                audio = recognizer.listen(src, timeout=3, phrase_time_limit=3)
                text = recognizer.recognize_google(audio).lower()
                if "terminate" in text or "exit" in text:
                    engine.say("Deactivating core assistant matrix."); engine.runAndWait()
                    break
                else:
                    engine.say("Command logged securely."); engine.runAndWait()
            except Exception: print("Timeout bypass grid safely.")

if __name__ == "__main__":
    execute_static_assistant_loop()
    execute_integrated_offline_loop()
    execute_continuous_escape_loop()
