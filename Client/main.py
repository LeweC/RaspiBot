import move
import ultrasonic
import time

if True:
    step = 1
    move.init_all()
    try:
        while 1:   
            if(ultrasonic.measure <= 15):
                print("fowart")
                print(ultrasonic.measure)
                for i in range(18):
                    move.move(step, 35, 'left')
                    time.sleep(0.2)
                    step += 1
                    if step == 5:
                        step = 1
            else:
                print("turn")
                print(ultrasonic.measure)
                for x in range(24):
                    move.move(step, 35, 'no')
                    step += 1
                    if step > 4:
                        step = 1
                    time.sleep(0.2)    
    except:
        move.clean_all()
