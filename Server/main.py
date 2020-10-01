import move
import ultrasonic
import time
import random

def handler(instructions):
    directions(instructions)
    moveUSS(instructions)
       
def moveUSS(instructions):
    move.sensor_free(instructions)

def directions(instructions): 
    if instructions[0] == "Forward":
        move.forward()
        print("LOOOOOOS1")
    elif instructions[0] == "Left":
        move.left()
        print("LOOOOOOS2")    
    elif instructions[0] == "Right":
        move.right()
    elif instructions[0] == "Standing":
        move.stand()
    elif instructions[0] == "Auto":
        move.autonom()
