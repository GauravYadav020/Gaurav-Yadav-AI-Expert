"""
================================================================================
LESSON 6: Real-Time Speech Translation - Cross-Cultural Bridges
================================================================================
"""

from googletrans import Translator
import speech_recognition as sr
import pyttsx3

# ------------------------------------------------------------------------------
# ACTIVITY 1: Static Text Transmutation Localization Controller
# ------------------------------------------------------------------------------
def execute_text_translation_link():
    print("\n=== TRANSLATING STATIC TEXT RECORDS ===")
    translator = Translator()
    eng_text = "Welcome to the advanced software development lab session."
    try:
        res = translator.translate(eng_text, dest="es")
        print(f"[ORIGINAL]: {eng_text}")
        print(f"[SPANISH TRANSLATION]: {res.text}")
    except Exception as e: print(f"Translation Failure: {e}")

# ------------------------------------------------------------------------------
# ACTIVITY 2: Live Inbound Voice Capturer and Text Pipeline Exporter
# ------------------------------------------------------------------------------
def execute_live_speech_translator():
    print("\n=== LIVE SPEECH TO TEXT TRANSLATION RUNNING ===")
    recognizer = sr.Recognizer(); translator = Translator()
    with sr.Microphone() as src:
        print("[PROMPT] Speak clearly in English (Target Translation: French [fr])...")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=4)
            transcript = recognizer.recognize_google(audio)
            res = translator.translate(transcript, dest="fr")
            print(f"[ORIGINAL]: {transcript}")
            print(f"[TRANSLATED TARGET STRING]: {res.text}")
        except Exception as e: print(f"Pipeline fault grid trace: {e}")

# ------------------------------------------------------------------------------
# ACTIVITY 3: End-to-End Real-Time Voice Translation Sound Core Machine
# ------------------------------------------------------------------------------
def execute_full_speech_translation_pipeline():
    print("\n=== END-TO-END TRANSLATION SOUND MACHINE OPERATIONAL ===")
    recognizer = sr.Recognizer(); translator = Translator(); engine = pyttsx3.init()
    with sr.Microphone() as src:
        print("[ORCHESTRATOR] Say phrase in English -> Output will translate & speak German [de]")
        try:
            audio = recognizer.listen(src, timeout=4, phrase_time_limit=4)
            raw_text = recognizer.recognize_google(audio)
            translated_pack = translator.translate(raw_text, dest="de")
            print(f"Speaking German audio node string track: {translated_pack.text}")
            engine.say(translated_pack.text); engine.runAndWait()
        except Exception as e: print(f"Pipeline structural exception: {e}")

if __name__ == "__main__":
    execute_text_translation_link()
    execute_live_speech_translator()
    execute_full_speech_translation_pipeline()
