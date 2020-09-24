import move
import ultrasonic
import time
import random

def handler(instructions):
    directions(instructions)
       


def directions(instructions): 
    if instructions[0] == "Forward":
        move.forward()
    elif instructions[0] == "Left":
        move.left()    
    elif instructions[0] == "Right":
        move.right()
    elif instructions[0] == "Standing":
        move.stand()
    elif instructions[0] == "Auto":
        move.autonom()
