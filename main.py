import move

if True:
    step = 1
    move.init_all()
    try:
        while 1:
            move.move(step, 35, 'no')
            step += 1
            if step > 4:
                step = 1
            time.sleep(0.5)
    
    except:
        move.clean_all()
