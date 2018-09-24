"""
Labo 1 - Randomized Arcade Character
Generate a random arcade character (8x8) on SenseHat
Extra:
"""
from sense_hat import SenseHat
import random
import time

sense = SenseHat()
sense.clear()
sense.set_pixel(random.randint(0, 7), random.randint(0, 3), 155, 155, 255)
sense.set_pixel(random.randint(0, 7), random.randint(0, 3), 155, 155, 255)
sense.set_pixel(random.randint(0, 7), random.randint(0, 3), 155, 155, 255)
sense.set_pixel(random.randint(0, 7), random.randint(0, 3), 155, 155, 255)
sense.set_pixel(random.randint(0, 7), random.randint(0, 3), 155, 155, 255)
sense.set_pixel(random.randint(0, 7), random.randint(0, 3), 155, 155, 255)

pixels = sense.get_pixels()
sense.flip_v()
pixelss = sense.get_pixels()
time.sleep(1)
sense.set_pixels(pixels)
print(pixels)
