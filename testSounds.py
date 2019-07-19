import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.mixer.pre_init(48000, -16, 1, 4096)
pygame.mixer.init()

def pauseSound():
  pygame.mixer.pause()

button_sounds = {
    Button(14): Sound("/home/pi/sounds/1.wav").play,
    Button(15): Sound("/home/pi/sounds/2.wav").play,
    Button(18): Sound("/home/pi/sounds/3.wav").play,
    Button(23): Sound("/home/pi/sounds/4.wav").play,
    Button(24): Sound("/home/pi/sounds/5.wav").play,
    Button(3): pauseSound,
}

for button, sound in button_sounds.items():
    button.when_pressed = sound

pause()
