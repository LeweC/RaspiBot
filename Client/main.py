import move
import ultrasonic
import time

if True:
    step = 1
    move.init_all()
    try:
        while 1:
            distance = ultrasonic.measure()
            print(distance)
            while(distance >= 15):
                print("fowart")
                distance = ultrasonic.measure()
                print(distance)    
                move.move(step, 35, 'no')
                time.sleep(0.2)
                step += 1
                if step == 5:
                    step = 1
            else:
                print("turn")
                distance = ultrasonic.measure()
                print(distance)    
                move.move(step, 35, 'left')
                step += 1
                if step > 4:
                    step = 1
                time.sleep(0.2)    
    except:
        move.clean_all()
