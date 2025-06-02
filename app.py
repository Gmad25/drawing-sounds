from controllers.sound_controller import *
from controllers.load_sound import *

# Configuracion del sonido (un simple beep)
sample_rate = 44100
duration = 0.1
frequency = 440

tone = generate_tone(duration, frequency, sample_rate)

print("""
      Presiona la tecla asignada 'a' para reproducir un beep
      Presiona la tecla asignada 's' para reproducir un sonido
    """)

# Sound a beep
keyboard.on_press_key('a', lambda _: play_sound(tone, sample_rate))
# Sound a audio
keyboard.on_press_key('s', lambda _: play_sound_in_folder('some.wav'))


# Solo sale del programa si tocas Escape
keyboard.wait('esc')
