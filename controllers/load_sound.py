from pygame import mixer
mixer.init(frequency=44100, size=-16, channels=2, buffer=512)  # Buffer pequeño para menor latencia

# Cargar tu sonido (reemplaza con tu archivo de sonido)
sound = mixer.Sound('tu_sonido.wav')

def play_sound(sound):
    sound.stop()  # Detener cualquier reproducción previa
    sound.play()