import move
import ultrasonic
import time

if True:
    step = 1
    move.init_all()
    while 1:
        while(ultrasonic.measure() >= 15):
            print("fowart")
            print("------")        
            move.move(step, 35, 'no')
            time.sleep(0.2)
            step += 1
            if step > 4:
                step = 1
        else:
            print("turn")
            print("------")
            move.move(step, 35, 'left')
            step += 1
            if step == 5:
                step = 1
            time.sleep(0.2)    
    
