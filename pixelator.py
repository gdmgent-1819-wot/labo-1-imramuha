"""
Labo 1 - Pixelator
Run through all the LED's with random colour and repeat
Use "easing function" to manipulate the speed
"""
from sense_hat import SenseHat
import time
import random

# run pixel through the senseHat with random colours - CLI for speed input
sense = SenseHat()
manipulateSpeed = input('Enter time span in seconds ')
while True:
    for yCounter in range(0,8):
        for xCounter in range (0,8):
            sense.clear()
            sense.set_pixel(xCounter, yCounter, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            time.sleep(int(manipulateSpeed))


