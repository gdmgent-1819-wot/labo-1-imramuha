"""
Labo 1 - Mario Jumps
Create a mario that springs when the joystick on SenseHat is held up
"""
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

sense = SenseHat()
sense.clear()

# pixels colour
X = [255, 0, 0]
O = [0, 0, 0]
B = [100, 100, 100]
Y = [255, 255, 0]
S = [255, 255, 150]
Z = [0, 0, 255]
L = [133, 97, 35]

# mario on ground
mario_low = [
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, X, O, O,
    O, O, X, X, X, X, X, O,
    O, O, L, S, L, S, O, O,
    O, O, O, S, L, L, O, O,
    O, O, X, Z, Y, Z, X, O,
    O, O, Z, Y, Z, Y, Z, O,
    O, O, O, Z, Z, Z, O, O
    ]

#mario jumping
mario_high = [
    O, O, O, X, X, X, O, O,
    O, O, X, X, X, X, X, O,
    O, O, L, S, L, S, O, O,
    O, O, O, S, L, L, O, O,
    O, O, X, Z, Y, Z, X, O,
    O, O, Z, Y, Z, Y, Z, O,
    O, O, O, Z, Z, Z, O, O,
    O, O, O, O, O, O, O, O
    ]

# 
def pushed_up(event):
    sense.clear()
    sense.set_pixels(mario_high)
    if event.action == ACTION_RELEASED:
        sense.clear()
        sense.set_pixels(mario_low)
    
# brings mario back to ground   
def refresh():
    sense.clear()
    sense.set_pixels(mario_low)


sense.stick.direction_up = pushed_up
refresh()



