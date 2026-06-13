"""
================================================================================
LESSON 5: Voice-Activated Assistant - Wake Word Infrastructure
================================================================================
"""

import speech_recognition as sr
import pyttsx3

# ------------------------------------------------------------------------------
# ACTIVITY 1: Simulated Substring Token Trigger Identification Engine
# ------------------------------------------------------------------------------
def execute_simulated_wake_trigger():
    print("\n=== EVALUATING DATA STREAMS FOR WAKE TOKENS ===")
    WAKE_WORD = "symphony"
    mock_stream = ["hello system status logs", "hey symphony initialize deployment configurations"]
    for track in mock_stream:
        if WAKE_WORD in track.lower():
            print(f"[MATCH DETECTED] Wake token found inside sequence: {track}")

# ------------------------------------------------------------------------------
# ACTIVITY 2: Live Background Standby Monitor Wake Phrase Interfacing
# ------------------------------------------------------------------------------
def execute_live_wake_word_listener():
    print("\n=== VOICE TRIGGER LISTENER ACTIVE ===")
    WAKE_PHRASE = "hello orchestra"
    recognizer = sr.Recognizer()
    with sr.Microphone() as src:
        print(f"[STANDBY] Say explicit token: '{WAKE_PHRASE}'")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=3)
            transcription = recognizer.recognize_google(audio).lower()
            if WAKE_PHRASE in transcription:
                print("[WAKE SUCCESS] Background pipeline transition verified.")
        except Exception as e: print(f"Standby Loop Exception: {e}")

# ------------------------------------------------------------------------------
# ACTIVITY 3: Two-Stage Hierarchical Wake and Command Routing Engine
# ------------------------------------------------------------------------------
def execute_two_stage_assistant():
    print("\n=== TWO-STAGE SYSTEM ENGINE ACTIVE ===")
    WAKE_TOKEN = "attention core"
    engine = pyttsx3.init(); recognizer = sr.Recognizer()
    with sr.Microphone() as src:
        print(f"Stage 1: Monitor for wake string token '{WAKE_TOKEN}'")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=3)
            if WAKE_TOKEN in recognizer.recognize_google(audio).lower():
                engine.say("Core active. State operational instructions."); engine.runAndWait()
                print("Stage 2: Processing dependent query commands configurations...")
                cmd_audio = recognizer.listen(src, timeout=4, phrase_time_limit=4)
                print(f"Captured intent: {recognizer.recognize_google(cmd_audio)}")
        except Exception as e: print(f"Stage Abort Logic: {e}")

if __name__ == "__main__":
    execute_simulated_wake_trigger()
    execute_live_wake_word_listener()
    execute_two_stage_assistant()
