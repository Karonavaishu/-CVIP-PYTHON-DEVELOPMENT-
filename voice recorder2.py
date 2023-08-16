import sounddevice as sd
import numpy as np
import wavio

def record_audio(filename, duration, sample_rate):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    print("Recording finished.")
    
    wavio.write(filename, audio, sample_rate, sampwidth=2)  # Save as WAV file

if __name__ == "__main__":
    filename = "recorded_audio.wav"
    duration = 5  # Recording duration in seconds
    sample_rate = 44100  # Sampling rate (samples per second)
    
    record_audio(filename, duration, sample_rate)
    print(f"Audio saved as '{filename}'")
