import move
import ultrasonic
import time

if True:
    step = 1
    move.init_all()
    try:
        while 1:
            while ultrasonic.measure() >= 15:
                print("forward")
                print(step)
                print("------")        
                move.move(step, 35, 'no')
                step += 1
                if step == 5:
                  step = 1
                time.sleep(0.6)
            else:
                print("turn")
                print(step)
                print("------")
                move.move(step, 35, 'left')
                step += 1
                if step == 5:
                    step = 1
                time.sleep(0.6)
    except KeyboardInterrupt:
        print("Ending Scipt")
        ultrasonic.closing()
        time.sleep(1)