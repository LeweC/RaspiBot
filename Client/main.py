import move
import time

if True:
    step = 1
    move.init_all()
    try:
        while 1:
            for x in range(24):
                move.move(step, 35, 'no')
                step += 1
                if step > 4:
                    step = 1
                time.sleep(0.2)

            for i in range(18):
                move.move(step, 35, 'left')
                time.sleep(0.2)
                step += 1
                if step == 5:
                    step = 1
            """ 
            for i in range(18):
                move.move(step, 35, 'left')
                time.sleep(0.2)
                step += 1
                if step == 5:
                    step = 1
            """
    except:
        move.clean_all()
