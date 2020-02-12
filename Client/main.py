import move
import ultrasonic
import time

if True:
    step = 1
    move.init_all()
    try:
        if(ultrasonic.measure <= 15):
            
            for i in range(18):
                move.move(step, 35, 'left')
                time.sleep(0.2)
                step += 1
                if step == 5:
                    step = 1
        else:
            for x in range(24):
                move.move(step, 35, 'no')
                step += 1
                if step > 4:
                    step = 1
                time.sleep(0.2)    
    except:
        move.clean_all()
