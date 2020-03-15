import move
import ultrasonic
import time

if True:
    step = 1
    move.init_all()
    try:
        while 1:
            result = ultrasonic.measure()
            while result[0] >= 15:
                print("forward")
                print(step)
                print(result[0])
                print(result[1])
                print("------")        
                move.move(step, 35, 'no')
                step += 1
                if step == 5:
                  step = 1
                result = ultrasonic.measure()
                time.sleep(0.6)
            else:
                print("turn")
                print(step)
                print(result[0])
                print(result[1])
                print("------")

                move.stand()
                time.sleep(1)
                move.sensor_right()
                move.sensor_left()
                move.sensor_middle()
                time.sleep(1)
                move.move(step, 35, 'left')
                step += 1
                if step == 5:
                    step = 1
                result = ultrasonic.measure()
                time.sleep(0.6)
    except KeyboardInterrupt:
        print("Ending Scipt")
        ultrasonic.closing()
        time.sleep(1)