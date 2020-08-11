import move
import ultrasonic
import time
import random

def handler(instructions):
    print(instructions[0])
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
       


'''def directions(instructions): 
    if instructions == "Forward":
        move.forward()
    elif instructions[0] == "Left":
        move.left()    
    elif instructions[0] == "Right":
        move.right()
    elif instructions[0] == "Standing":
        move.stand()
    elif instructions[0] == "Auto":
        move.autonom()'''
