import sounddevice as sd
import numpy as np
import keyboard
from time import time



def generate_tone(duration: float, frequency: float, sample_rate: float):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    tone = np.sin(2 * np.pi * frequency * t) * 0.3
    return np.vstack((tone, tone)).T


def play_sound(tone, sample_rate):
    sd.stop()
    sd.play(tone, sample_rate)
