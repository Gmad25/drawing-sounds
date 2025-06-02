from pygame import mixer
mixer.init(frequency=44100, size=-16, channels=2, buffer=512)  # Buffer pequeño para menor latencia

# Cargar tu sonido (reemplaza con tu archivo de sonido)

def play_sound_in_folder(audio_name: str):
    sound = mixer.Sound(audio_name)
    sound.stop()  # Detener cualquier reproducción previa
    sound.play()