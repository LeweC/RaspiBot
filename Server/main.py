import move
import ultrasonic
import time
import random

def moving(direction):
    if direction == "Forward":
        move.forward()
    elif direction == "Left":
        move.left()    
    elif direction == "Right":
        move.right()
    elif direction == "Standing":
        move.stand()
    elif direction == "Auto":
        move.autonom()    
