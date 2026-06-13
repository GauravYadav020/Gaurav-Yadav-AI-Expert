"""
================================================================================
MODULE: Speech Symphony - Talk & Listen with AI
LESSON 1: Hello AI, Can You Hear Me? - Audio Ingestion Basics
================================================================================
INTRODUCTION:
In this lesson, we explore the mechanics of how computer systems capture, analyze,
and store audio signals from the real world. Sound waves are translated into arrays
of numbers via Analog-to-Digital Conversion (ADC) using parameters like sampling rate,
bit depth, and channel configurations. Students will write Python scripts to query
audio recording hardware, capture live voice clips, and save them as WAV files.
"""

import pyaudio
import wave
import os
import time
import struct

# ------------------------------------------------------------------------------
# ACTIVITY 1: Hardware Inventory Tool (Difficulty: Beginner | Duration: 15 Mins)
# Objective: Query and list available audio input and output devices.
# ------------------------------------------------------------------------------
def execute_hardware_inventory():
    print("\n=== RUNNING CORE AUDIO HARDWARE INVENTORY ===")
    audio_manager = pyaudio.PyAudio()
    try:
        total_devices = audio_manager.get_device_count()
        print(f"[INFO] Total hardware audio profiles detected: {total_devices}\n")
        for device_index in range(total_devices):
            device_info = audio_manager.get_device_info_by_index(device_index)
            if device_info.get("maxInputChannels") > 0:
                print(f"Device Index [{device_index}]: {device_info.get('name')}")
                print(f"  -> Max Input Channels: {device_info.get('maxInputChannels')}")
                print(f"  -> Default Sampling Frequency: {device_info.get('defaultSampleRate')} Hz")
                print("-" * 40)
    except Exception as e:
        print(f"[ERROR] Failed to extract system device maps: {e}")
    finally:
        audio_manager.terminate()
        print("[INFO] Audio hardware scan complete. Resources released.")

# ------------------------------------------------------------------------------
# ACTIVITY 2: Live Buffer Capture Engine (Difficulty: Intermediate | Duration: 20 Mins)
# Objective: Capture live audio stream for 5 seconds into RAM buffers.
# ------------------------------------------------------------------------------
def execute_buffer_capture():
    print("\n=== LIVE MICROPHONE BUFFER CAPTURE ENGINE ===")
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK_SIZE = 1024
    RECORD_SECONDS = 5
    
    audio_manager = pyaudio.PyAudio()
    print("[STREAM] Opening active microphone recording stream lane...")
    input_stream = audio_manager.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)
    
    audio_frame_store = []
    total_iterations = int((RATE / CHUNK_SIZE) * RECORD_SECONDS)
    print(f"[RECORDING] Live: Speak into microphone for {RECORD_SECONDS} seconds...")
    
    for step in range(total_iterations):
        raw_data_bytes = input_stream.read(CHUNK_SIZE)
        audio_frame_store.append(raw_data_bytes)
        
    print("[RECORDING] Timeout hit. Closing stream lines.")
    input_stream.stop_stream()
    input_stream.close()
    audio_manager.terminate()
    total_bytes = len(b"".join(audio_frame_store))
    print(f"[SUCCESS] Extracted Footprint Size: {total_bytes} bytes in RAM.")

# ------------------------------------------------------------------------------
# ACTIVITY 3: Microphone to WAV Exporter (Difficulty: Advanced | Duration: 20 Mins)
# Objective: Export captured raw audio streams to standard playable WAV disk containers.
# ------------------------------------------------------------------------------
def execute_wav_exporter_stream():
    print("\n=== EXPORTING MICROPHONE INPUT TO WAV FILE ===")
    SAMPLE_FORMAT = pyaudio.paInt16
    CHANNELS_COUNT = 1
    SAMPLING_RATE_HZ = 44100
    BUFFER_CHUNK = 1024
    DURATION_TIMEFRAME = 4
    OUTPUT_FILE_PATH = "student_voice_test.wav"
    
    pyaudio_context = pyaudio.PyAudio()
    capture_stream = pyaudio_context.open(format=SAMPLE_FORMAT, channels=CHANNELS_COUNT, rate=SAMPLING_RATE_HZ, input=True, frames_per_buffer=BUFFER_CHUNK)
    binary_frames_collector = []
    loop_limit = int((SAMPLING_RATE_HZ / BUFFER_CHUNK) * DURATION_TIMEFRAME)
    
    print(">>> START SPEAKING NOW (Recording 4 seconds)...")
    for _ in range(loop_limit):
        binary_frames_collector.append(capture_stream.read(BUFFER_CHUNK))
        
    capture_stream.stop_stream()
    capture_stream.close()
    
    wf = wave.open(OUTPUT_FILE_PATH, "wb")
    wf.setnchannels(CHANNELS_COUNT)
    wf.setsampwidth(pyaudio_context.get_sample_size(SAMPLE_FORMAT))
    wf.setframerate(SAMPLING_RATE_HZ)
    wf.writeframes(b"".join(binary_frames_collector))
    wf.close()
    pyaudio_context.terminate()
    print(f"[SUCCESS] File exported successfully: {OUTPUT_FILE_PATH}")

# ------------------------------------------------------------------------------
# AFTER-CLASS PROJECT: Industrial Audio Sentinel Quality Assurance Ledger Suite
# ------------------------------------------------------------------------------
class AudioSentinelSuite:
    def __init__(self): 
        self.path = "sentinel_audio_logs"
        if not os.path.exists(self.path): os.makedirs(self.path)
    def audit_environment_telemetry(self):
        print("\n[SENTINEL] Running environmental telemetry spike check...")
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        raw_data = stream.read(1024)
        shorts = struct.unpack(f"{int(len(raw_data)/2)}h", raw_data)
        peak = max(abs(s) for s in shorts)
        print(f"[ANALYSIS] Peak Signal Amplitude Observed: {peak}")
        stream.stop_stream(); stream.close(); audio.terminate()

if __name__ == "__main__":
    execute_hardware_inventory()
    execute_buffer_capture()
    execute_wav_exporter_stream()
    sentinel = AudioSentinelSuite()
    sentinel.audit_environment_telemetry()
