"""
================================================================================
LESSON 2: Speech to Text - Transforming Waves into Strings
================================================================================
"""

import speech_recognition as sr
import json
import time
import os
import config
from openai import OpenAI



GROQ_URL = "https://api.groq.com/openai/v1"
MODELS = getattr(config, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])


def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:

    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: GROQ_API_KEY missing in config.py"
    c = OpenAI(api_key=key, base_url=GROQ_URL)

    last_err = None

    for m in MODELS:

        try:

            r = c.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,

            )

            return r.choices[0].message.content

        except Exception as e:

            last_err = e


    return (

        "Groq model failed.\n"
        f"Tried models: {MODELS}\n"
        "Fix:\n"
        "1) Switch to hf by importing hf.py in main.py OR\n"
        "2) Replace Groq model in groq.py (GROQ_MODELS).\n"
        f"Details: {type(last_err).__name__}: {last_err}"

    )
# ------------------------------------------------------------------------------
# ACTIVITY 1: Static Audio File Transcription Utility
# ------------------------------------------------------------------------------
def execute_static_transcription():
    print("\n=== RUNNING AUDIO FILE TRANSCRIPTION UTILITY ===")
    target_audio_path = "student_voice_test.wav"
    if not os.path.exists(target_audio_path):
        print("[WARN] Source wav file missing. Run Lesson 1 first.")
        return
    recognizer_instance = sr.Recognizer()
    with sr.AudioFile(target_audio_path) as src:
        extracted_audio_data = recognizer_instance.record(src)
    try:
        text = recognizer_instance.recognize_google(extracted_audio_data)
        print(f"TRANSCRIBED TEXT OUTPUT: \"{text}\"")
    except Exception as e: print(f"[CRITICAL] Recognition Error: {e}")

# ------------------------------------------------------------------------------
# ACTIVITY 2: Live Stream Voice to String Matrix Engine
# ------------------------------------------------------------------------------
def execute_live_stt_stream():
    print("\n=== LIVE VOICE TO STRING CONVERTER MODULE ===")
    recognizer = sr.Recognizer()
    with sr.Microphone() as src:
        print("[CALIBRATING] Please maintain environmental silence...")
        recognizer.adjust_for_ambient_noise(src, duration=1)
        print("[LISTENING] State active. Say something...")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=4)
            print(f"[SUCCESS] Extracted String Result: \"{recognizer.recognize_google(audio)}\"")
        except Exception as e: print(f"[INFO] Capture cycle dropped: {e}")

# ------------------------------------------------------------------------------
# ACTIVITY 3: Secure Speech Token Validation Logic Router
# ------------------------------------------------------------------------------
def execute_secure_voice_router():
    print("\n=== VOCAL COMMAND PARSING SECURITY LINK RUNNING ===")
    recognizer = sr.Recognizer()
    with sr.Microphone() as src:
        print("[AUTHENTICATOR] Speak critical command clearance tokens...")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=4)
            token = recognizer.recognize_google(audio).lower()
            if "activate" in token:
                print("[ACCESS GRANTED] Executing System Core Activation Grid...")
            else:
                print("[ACCESS DENIED] Signature unverified.")
        except Exception as e: print(f"Authorization Exception: {e}")

if __name__ == "__main__":
    execute_static_transcription()
    execute_live_stt_stream()
    execute_secure_voice_router()
