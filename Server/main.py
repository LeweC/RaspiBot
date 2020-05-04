import move
import ultrasonic
import time
import random

def moving(direction):
    print("moving wurde ausgeführt")
    if direction == "Forward":
        move.forward()
    elif direction == "Left":
        move.left()    
    elif direction == "Right":
        move.right()
    elif direction == "Standing":
        move.stand()    
