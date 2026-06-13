"""
================================================================================
LESSON 3: Building an Interactive AI Voice Application: Text-to-Speech (TTS)
================================================================================
"""

import pyttsx3
import time

# ------------------------------------------------------------------------------
# ACTIVITY 1: Baseline Offline Vocalization Engine
# ------------------------------------------------------------------------------
def execute_basic_speech():
    print("\n=== INITIALIZING NATIVE TEXT TO SPEECH ENGINE ===")
    speech_engine = pyttsx3.init()
    speech_engine.say("Hello student, welcome to the Speech Symphony development track.")
    speech_engine.runAndWait()

# ------------------------------------------------------------------------------
# ACTIVITY 2: Configurable Custom Voice Property Tuning Engine
# ------------------------------------------------------------------------------
def execute_property_tuning():
    print("\n=== ADJUSTING VOCAL ENGINE ATTRIBUTED PROPERTIES ===")
    engine = pyttsx3.init()
    engine.setProperty("rate", 145)
    voices = engine.getProperty("voices")
    if len(voices) > 1: engine.setProperty("voice", voices[1].id)
    engine.say("Adjusting speech metrics modifies the processing properties of synthetic outputs.")
    engine.runAndWait()

# ------------------------------------------------------------------------------
# ACTIVITY 3: Industrial Multi-Tiered Alert Notification Processing Matrix
# ------------------------------------------------------------------------------
def execute_alert_notifier_matrix():
    print("\n=== EMITTING LEVEL CONTROL NOTIFICATION LOGS ===")
    engine = pyttsx3.init()
    incidents = [
        {"level": "INFO", "msg": "System backup complete.", "rate": 150, "vol": 0.4},
        {"level": "CRITICAL", "msg": "Cooling system failure mapped!", "rate": 220, "vol": 1.0}
    ]
    for alert in incidents:
        engine.setProperty("rate", alert["rate"])
        engine.setProperty("volume", alert["vol"])
        engine.say(f"Attention status {alert['level']}. {alert['msg']}")
        engine.runAndWait()

if __name__ == "__main__":
    execute_basic_speech()
    execute_property_tuning()
    execute_alert_notifier_matrix()
