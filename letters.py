"""
Labo 1 - All letters of a string in a loop
Show "NMD" letters with random colors in a loop
Extra: possible to change the speed and string through CLI
"""
from sense_hat import SenseHat
import time
import random

# generating a random color

# loop NMD on SenseHat 1 seconds - clear after every succesful loop and wait 2 seconds
sense = SenseHat()
while True:
    for letter in 'NMD':
        sense.show_letter(letter, text_colour=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        time.sleep(1)
    
    sense.clear()
    time.sleep(2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    