#!/usr/bin/env python3
import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.init()
pygame.mixer.init()

def play(x):
    return lambda: do_play(x)

def do_play(x):
    print("sound " + str(x))
    pygame.mixer.music.load("/home/pi/newSounds/" + str(x) + ".wav")
    pygame.mixer.music.play(0)

def stop():
    return lambda: do_stop()

def do_stop():
    print("stopping")
    pygame.mixer.music.stop()



button_sounds = {
    Button(14): play(1),
    Button(15): play(2),
    Button(18): play(3),
    Button(23): play(4),
    Button(24): play(5),
    Button(3): stop(),
}
for button, callback in button_sounds.items():
    button.when_pressed = callback

pause()
