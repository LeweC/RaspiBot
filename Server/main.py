import move
import ultrasonic
import time
import random

def moving(direction):
    while direction == "Forward":
        move.forward()

    while direction == "Left":
        move.left()    

    while direction == "Right":
        move.right()

    while direction == "Standing":
        move.stand()    
