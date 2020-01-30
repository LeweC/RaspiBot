#! /usr/bin/python
# File name   : move.py
# Description : Controlling all servos
# Website    : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date      : 2019/04/08
import time
import Adafruit_PCA9685
from mpu6050 import mpu6050

'''
change this variables to 0 to reverse all the servos.
'''
set_direction = 1

'''
change these two variables to reverse the direction of the legs.
'''
if set_direction:
    leftSide_direction  = 1
    rightSide_direction = 0
else:
    leftSide_direction  = 0
    rightSide_direction = 1

'''
change these two variables to reverse the height of the legs.
'''
if set_direction:
    leftSide_height  = 0
    rightSide_height = 1
else:
    leftSide_height  = 1
    rightSide_height = 0

'''
change this variable to set the range of the height range.
'''
height_change = 30

'''
change these two variables to adjuest the function for observing.
'''
if set_direction:
    Up_Down_direction = 1
    Left_Right_direction = 1
else:
    Up_Down_direction = 0
    Left_Right_direction = 0
Left_Right_input = 300
Up_Down_input = 300
Left_Right_Max = 500
Left_Right_Min = 100
Up_Down_Max = 500
Up_Down_Min = 270
look_wiggle = 30
move_stu = 1


'''
change these variable to adjuest the steady function.
'''
steady_range_Min = -40
steady_range_Max = 130
range_Mid = (steady_range_Min+steady_range_Max)/2
X_fix_output = range_Mid
Y_fix_output = range_Mid
steady_X_set = 73

'''
Set PID
'''
P = 5
I = 0.01
D = 0

'''
>>> instantiation <<<
'''

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

try:
    sensor = mpu6050(0x68)
    mpu6050_connection = 1
except:
    mpu6050_connection = 0

'''
change these two variable to adjuest the steady status.
       (X+)
       /|\
  (Y+)<-+->(Y-)
        |
       (X-)
Example: If you want the forhead of the robot to point down,
         you need to increase the value target_X.
'''
target_X = 0
target_Y = 0

pwm0 = 0
pwm1 = 0
pwm2 = 0
pwm3 = 0
pwm4 = 0
pwm5 = 0
pwm6 = 0
pwm7 = 0
pwm8 = 0
pwm9 = 0
pwm10 = 0
pwm11 = 0
pwm12 = 0
pwm13 = 0
pwm14 = 0
pwm15 = 0
pwm16 = 0



'''
Set a default pwm value for all servos.
'''
for i in range(0,16):
    exec('pwm%d=300'%i)

'''
Get raw data from mpu6050.
'''
def mpu6050Test():
    while 1:
        accelerometer_data = sensor.get_accel_data()
        print('X=%f,Y=%f,Z=%f'%(accelerometer_data['x'],accelerometer_data['y'],accelerometer_data['x']))
        time.sleep(0.3)

        
def init_all():
    pwm.set_all_pwm(0,300)
    

def ctrl_range(raw, max_genout, min_genout):
    if raw > max_genout:
        raw_output = max_genout
    elif raw < min_genout:
        raw_output = min_genout
    else:
        raw_output = raw
    return int(raw_output)

'''
left_I   -<forward>-- right_III
left_II  ---<BODY>---  right_II
left_III -<Backward>-   right_I

            pos=1
           /     \
          /       \
         /         \
    pos=2---pos=3---pos=4

Change the value of wiggle to set the range and direction that the legs moves.
'''
def left_I(pos,wiggle,heightAdjust=0):
    if pos == 0:
        #pwm.set_pwm(0,0,pwm0)
        if leftSide_height:
            pwm.set_pwm(1,0,pwm1+heightAdjust)
        else:
            pwm.set_pwm(1,0,pwm1-heightAdjust)
    else:
        if leftSide_direction:
            if pos == 1:
                pwm.set_pwm(0,0,pwm0)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1+3*height_change)
                else:
                    pwm.set_pwm(1,0,pwm1-3*height_change)
            elif pos == 2:
                pwm.set_pwm(0,0,pwm0+wiggle)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1-height_change)
                else:
                    pwm.set_pwm(1,0,pwm1+height_change)
            elif pos == 3:
                pwm.set_pwm(0,0,pwm0)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1-height_change)
                else:
                    pwm.set_pwm(1,0,pwm1+height_change)
            elif pos == 4:
                pwm.set_pwm(0,0,pwm0-wiggle)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1-height_change)
                else:
                    pwm.set_pwm(1,0,pwm1+height_change)
        else:
            if pos == 1:
                pwm.set_pwm(0,0,pwm0)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1+3*wiggle)
                else:
                    pwm.set_pwm(1,0,pwm1-3*wiggle)
            elif pos == 2:
                pwm.set_pwm(0,0,pwm0-wiggle)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1-wiggle)
                else:
                    pwm.set_pwm(1,0,pwm1+wiggle)
            elif pos == 3:
                pwm.set_pwm(0,0,pwm0)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1-wiggle)
                else:
                    pwm.set_pwm(1,0,pwm1+wiggle)
            elif pos == 4:
                pwm.set_pwm(0,0,pwm0+wiggle)
                if leftSide_height:
                    pwm.set_pwm(1,0,pwm1-wiggle)
                else:
                    pwm.set_pwm(1,0,pwm1+wiggle)


def left_II(pos,wiggle,heightAdjust=0):
    if pos == 0:
        #pwm.set_pwm(2,0,pwm2)
        if leftSide_height:
            pwm.set_pwm(3,0,pwm3+heightAdjust)
        else:
            pwm.set_pwm(3,0,pwm3-heightAdjust)
    else:
        if leftSide_direction:
            if pos == 1:
                pwm.set_pwm(2,0,pwm2)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3+3*height_change)
                else:
                    pwm.set_pwm(3,0,pwm3-3*height_change)
            elif pos == 2:
                pwm.set_pwm(2,0,pwm2+wiggle)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3-height_change)
                else:
                    pwm.set_pwm(3,0,pwm3+height_change)
            elif pos == 3:
                pwm.set_pwm(2,0,pwm2)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3-height_change)
                else:
                    pwm.set_pwm(3,0,pwm3+height_change)
            elif pos == 4:
                pwm.set_pwm(2,0,pwm2-wiggle)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3-height_change)
                else:
                    pwm.set_pwm(3,0,pwm3+height_change)
        else:
            if pos == 1:
                pwm.set_pwm(2,0,pwm2)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3+3*wiggle)
                else:
                    pwm.set_pwm(3,0,pwm3-3*wiggle)
            elif pos == 2:
                pwm.set_pwm(2,0,pwm2-wiggle)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3-wiggle)
                else:
                    pwm.set_pwm(3,0,pwm3+wiggle)
            elif pos == 3:
                pwm.set_pwm(2,0,pwm2)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3-wiggle)
                else:
                    pwm.set_pwm(3,0,pwm3+wiggle)
            elif pos == 4:
                pwm.set_pwm(2,0,pwm2+wiggle)
                if leftSide_height:
                    pwm.set_pwm(3,0,pwm3-wiggle)
                else:
                    pwm.set_pwm(3,0,pwm3+wiggle)


def left_III(pos,wiggle,heightAdjust=0):
    if pos == 0:
        #pwm.set_pwm(4,0,pwm4)
        if leftSide_height:
            pwm.set_pwm(5,0,pwm5+heightAdjust)
        else:
            pwm.set_pwm(5,0,pwm5-heightAdjust)
    else:
        if leftSide_direction:
            if pos == 1:
                pwm.set_pwm(4,0,pwm4)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5+3*height_change)
                else:
                    pwm.set_pwm(5,0,pwm5-3*height_change)
            elif pos == 2:
                pwm.set_pwm(4,0,pwm4+wiggle)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5-height_change)
                else:
                    pwm.set_pwm(5,0,pwm5+height_change)
            elif pos == 3:
                pwm.set_pwm(4,0,pwm4)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5-height_change)
                else:
                    pwm.set_pwm(5,0,pwm5+height_change)
            elif pos == 4:
                pwm.set_pwm(4,0,pwm4-wiggle)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5-height_change)
                else:
                    pwm.set_pwm(5,0,pwm5+height_change)
        else:
            if pos == 1:
                pwm.set_pwm(4,0,pwm4)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5+3*wiggle)
                else:
                    pwm.set_pwm(5,0,pwm5-3*wiggle)
            elif pos == 2:
                pwm.set_pwm(4,0,pwm4-wiggle)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5-wiggle)
                else:
                    pwm.set_pwm(5,0,pwm5+wiggle)
            elif pos == 3:
                pwm.set_pwm(4,0,pwm4)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5-wiggle)
                else:
                    pwm.set_pwm(5,0,pwm5+wiggle)
            elif pos == 4:
                pwm.set_pwm(4,0,pwm4+wiggle)
                if leftSide_height:
                    pwm.set_pwm(5,0,pwm5-wiggle)
                else:
                    pwm.set_pwm(5,0,pwm5+wiggle)


def right_I(pos,wiggle,heightAdjust=0):
    #wiggle = -wiggle
    if pos == 0:
        #pwm.set_pwm(6,0,pwm6)
        if rightSide_height:
            pwm.set_pwm(7,0,pwm7+heightAdjust)
        else:
            pwm.set_pwm(7,0,pwm7-heightAdjust)
    else:
        if rightSide_direction:
            if pos == 1:
                pwm.set_pwm(6,0,pwm6)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7+3*height_change)
                else:
                    pwm.set_pwm(7,0,pwm7-3*height_change)
            elif pos == 2:
                pwm.set_pwm(6,0,pwm6+wiggle)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7-height_change)
                else:
                    pwm.set_pwm(7,0,pwm7+height_change)
            elif pos == 3:
                pwm.set_pwm(6,0,pwm6)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7-height_change)
                else:
                    pwm.set_pwm(7,0,pwm7+height_change)
            elif pos == 4:
                pwm.set_pwm(6,0,pwm6-wiggle)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7-height_change)
                else:
                    pwm.set_pwm(7,0,pwm7+height_change)
        else:
            if pos == 1:
                pwm.set_pwm(6,0,pwm6)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7+3*height_change)
                else:
                    pwm.set_pwm(7,0,pwm7-3*height_change)
            elif pos == 2:
                pwm.set_pwm(6,0,pwm6-wiggle)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7-height_change)
                else:
                    pwm.set_pwm(7,0,pwm7+height_change)
            elif pos == 3:
                pwm.set_pwm(6,0,pwm6)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7-height_change)
                else:
                    pwm.set_pwm(7,0,pwm7+height_change)
            elif pos == 4:
                pwm.set_pwm(6,0,pwm6+wiggle)
                if rightSide_height:
                    pwm.set_pwm(7,0,pwm7-height_change)
                else:
                    pwm.set_pwm(7,0,pwm7+height_change)


def right_II(pos,wiggle,heightAdjust=0):
    #wiggle = -wiggle
    if pos == 0:
        #pwm.set_pwm(8,0,pwm8)
        if rightSide_height:
            pwm.set_pwm(9,0,pwm9+heightAdjust)
        else:
            pwm.set_pwm(9,0,pwm9-heightAdjust)
    else:
        if rightSide_direction:
            if pos == 1:
                pwm.set_pwm(8,0,pwm8)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9+3*height_change)
                else:
                    pwm.set_pwm(9,0,pwm9-3*height_change)
            elif pos == 2:
                pwm.set_pwm(8,0,pwm8+wiggle)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9-height_change)
                else:
                    pwm.set_pwm(9,0,pwm9+height_change)
            elif pos == 3:
                pwm.set_pwm(8,0,pwm8)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9-height_change)
                else:
                    pwm.set_pwm(9,0,pwm9+height_change)
            elif pos == 4:
                pwm.set_pwm(8,0,pwm8-wiggle)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9-height_change)
                else:
                    pwm.set_pwm(9,0,pwm9+height_change)
        else:
            if pos == 1:
                pwm.set_pwm(8,0,pwm8)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9+3*height_change)
                else:
                    pwm.set_pwm(9,0,pwm9-3*height_change)
            elif pos == 2:
                pwm.set_pwm(8,0,pwm8-wiggle)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9-height_change)
                else:
                    pwm.set_pwm(9,0,pwm9+height_change)
            elif pos == 3:
                pwm.set_pwm(8,0,pwm8)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9-height_change)
                else:
                    pwm.set_pwm(9,0,pwm9+height_change)
            elif pos == 4:
                pwm.set_pwm(8,0,pwm8+wiggle)
                if rightSide_height:
                    pwm.set_pwm(9,0,pwm9-height_change)
                else:
                    pwm.set_pwm(9,0,pwm9+height_change)


def right_III(pos,wiggle,heightAdjust=0):
    #wiggle = -wiggle
    if pos == 0:
        #pwm.set_pwm(10,0,pwm10)
        if rightSide_height:
            pwm.set_pwm(11,0,pwm11+heightAdjust)
        else:
            pwm.set_pwm(11,0,pwm11-heightAdjust)
    else:
        if rightSide_direction:
            if pos == 1:
                pwm.set_pwm(10,0,pwm10)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11+3*height_change)
                else:
                    pwm.set_pwm(11,0,pwm11-3*height_change)
            elif pos == 2:
                pwm.set_pwm(10,0,pwm10+wiggle)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11-height_change)
                else:
                    pwm.set_pwm(11,0,pwm11+height_change)
            elif pos == 3:
                pwm.set_pwm(10,0,pwm10)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11-height_change)
                else:
                    pwm.set_pwm(11,0,pwm11+height_change)
            elif pos == 4:
                pwm.set_pwm(10,0,pwm10-wiggle)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11-height_change)
                else:
                    pwm.set_pwm(11,0,pwm11+height_change)
        else:
            if pos == 1:
                pwm.set_pwm(10,0,pwm10)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11+3*height_change)
                else:
                    pwm.set_pwm(11,0,pwm11-3*height_change)
            elif pos == 2:
                pwm.set_pwm(10,0,pwm10-wiggle)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11-height_change)
                else:
                    pwm.set_pwm(11,0,pwm11+height_change)
            elif pos == 3:
                pwm.set_pwm(10,0,pwm10)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11-height_change)
                else:
                    pwm.set_pwm(11,0,pwm11+height_change)
            elif pos == 4:
                pwm.set_pwm(10,0,pwm10+wiggle)
                if rightSide_height:
                    pwm.set_pwm(11,0,pwm11-height_change)
                else:
                    pwm.set_pwm(11,0,pwm11+height_change)


def move(step_input, speed, command):
    step_I  = step_input
    step_II = step_input + 2

    if step_II > 4:
        step_II = step_II - 4
    if speed == 0:
        return

    if command == 'no':
        right_I(step_I, speed, 0)
        left_II(step_I, speed, 0)
        right_III(step_I, speed, 0)

        left_I(step_II, speed, 0)
        right_II(step_II, speed, 0)
        left_III(step_II, speed, 0)
    elif command == 'left':
        right_I(step_I, speed, 0)
        left_II(step_I, -speed, 0)
        right_III(step_I, speed, 0)

        left_I(step_II, -speed, 0)
        right_II(step_II, speed, 0)
        left_III(step_II, -speed, 0)
    elif command == 'right':
        right_I(step_I, -speed, 0)
        left_II(step_I, speed, 0)
        right_III(step_I, -speed, 0)

        left_I(step_II, speed, 0)
        right_II(step_II, -speed, 0)
        left_III(step_II, speed, 0)


def stand():
    pwm.set_pwm(0,0,300)
    pwm.set_pwm(1,0,300)
    pwm.set_pwm(2,0,300)
    pwm.set_pwm(3,0,300)
    pwm.set_pwm(4,0,300)
    pwm.set_pwm(5,0,300)
    pwm.set_pwm(6,0,300)
    pwm.set_pwm(7,0,300)
    pwm.set_pwm(8,0,300)
    pwm.set_pwm(9,0,300)
    pwm.set_pwm(10,0,300)
    pwm.set_pwm(11,0,300)


'''
---Dove---
making the servo moves smooth.
'''
def dove_Left_I(horizontal, vertical):
    if leftSide_direction:
        pwm.set_pwm(0,0,pwm0 + horizontal)
    else:
        pwm.set_pwm(0,0,pwm0 - horizontal)

    if leftSide_height:
        pwm.set_pwm(1,0,pwm1+vertical)
    else:
        pwm.set_pwm(1,0,pwm1-vertical)


def dove_Left_II(horizontal, vertical):
    if leftSide_direction:
        pwm.set_pwm(2,0,pwm2 + horizontal)
    else:
        pwm.set_pwm(2,0,pwm2 - horizontal)

    if leftSide_height:
        pwm.set_pwm(3,0,pwm3+vertical)
    else:
        pwm.set_pwm(3,0,pwm3-vertical)


def dove_Left_III(horizontal, vertical):
    if leftSide_direction:
        pwm.set_pwm(4,0,pwm4 + horizontal)
    else:
        pwm.set_pwm(4,0,pwm4 - horizontal)

    if leftSide_height:
        pwm.set_pwm(5,0,pwm5+vertical)
    else:
        pwm.set_pwm(5,0,pwm5-vertical)


def dove_Right_I(horizontal, vertical):
    if rightSide_direction:
        pwm.set_pwm(6,0,pwm6 + horizontal)
    else:
        pwm.set_pwm(6,0,pwm6 - horizontal)

    if rightSide_height:
        pwm.set_pwm(7,0,pwm7+vertical)
    else:
        pwm.set_pwm(7,0,pwm7-vertical)


def dove_Right_II(horizontal, vertical):
    if rightSide_direction:
        pwm.set_pwm(8,0,pwm8 + horizontal)
    else:
        pwm.set_pwm(8,0,pwm8 - horizontal)

    if rightSide_height:
        pwm.set_pwm(9,0,pwm9+vertical)
    else:
        pwm.set_pwm(9,0,pwm9-vertical)


def dove_Right_III(horizontal, vertical):
    if rightSide_direction:
        pwm.set_pwm(10,0,pwm10 + horizontal)
    else:
        pwm.set_pwm(10,0,pwm10 - horizontal)

    if rightSide_height:
        pwm.set_pwm(11,0,pwm11+vertical)
    else:
        pwm.set_pwm(11,0,pwm11-vertical)


def dove(step_input, speed, timeLast, dpi, command):
    #step_I  = step_input
    step_II = step_input + 2

    if step_II > 4:
        step_II = step_II - 4
    
    if speed > 0:
        if step_input == 1:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_I, 3*speed_II)
                    dove_Right_II(-speed_I, 3*speed_II)
                    dove_Left_III(-speed_I, 3*speed_II)

                    dove_Right_I(speed_I, -10)
                    dove_Left_II(speed_I, -10)
                    dove_Right_III(speed_I, -10)
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if command == 'left':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_I, 3*speed_II)
                    dove_Right_II(-speed_I, 3*speed_II)
                    dove_Left_III(speed_I, 3*speed_II)

                    dove_Right_I(speed_I, -10)
                    dove_Left_II(-speed_I, -10)
                    dove_Right_III(speed_I, -10)
                    time.sleep(timeLast/dpi)
                elif command == 'right':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_I, 3*speed_II)
                    dove_Right_II(speed_I, 3*speed_II)
                    dove_Left_III(-speed_I, 3*speed_II)

                    dove_Right_I(-speed_I, -10)
                    dove_Left_II(speed_I, -10)
                    dove_Right_III(-speed_I, -10)
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if move_stu == 0 and command == 'no':
                    break

        elif step_input == 2:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_II, 3*(speed-speed_II))
                    dove_Right_II(speed_II, 3*(speed-speed_II))
                    dove_Left_III(speed_II, 3*(speed-speed_II))

                    dove_Right_I(-speed_II, -10)
                    dove_Left_II(-speed_II, -10)
                    dove_Right_III(-speed_II, -10)
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if command == 'left':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_II, 3*(speed-speed_II))
                    dove_Right_II(speed_II, 3*(speed-speed_II))
                    dove_Left_III(-speed_II, 3*(speed-speed_II))

                    dove_Right_I(-speed_II, -10)
                    dove_Left_II(speed_II, -10)
                    dove_Right_III(-speed_II, -10)
                    time.sleep(timeLast/dpi)
                elif command == 'right':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_II, 3*(speed-speed_II))
                    dove_Right_II(-speed_II, 3*(speed-speed_II))
                    dove_Left_III(speed_II, 3*(speed-speed_II))

                    dove_Right_I(speed_II, -10)
                    dove_Left_II(-speed_II, -10)
                    dove_Right_III(speed_II, -10)
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if move_stu == 0 and command == 'no':
                    break
        elif step_input == 3:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_I, -10)
                    dove_Right_II(speed_I, -10)
                    dove_Left_III(speed_I, -10)

                    dove_Right_I(-speed_I, 3*speed_II)
                    dove_Left_II(-speed_I, 3*speed_II)
                    dove_Right_III(-speed_I, 3*speed_II)
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if command == 'left':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_I, -10)
                    dove_Right_II(speed_I, -10)
                    dove_Left_III(-speed_I, -10)

                    dove_Right_I(-speed_I, 3*speed_II)
                    dove_Left_II(speed_I, 3*speed_II)
                    dove_Right_III(-speed_I, 3*speed_II)
                    time.sleep(timeLast/dpi)
                elif command == 'right':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_I, -10)
                    dove_Right_II(-speed_I, -10)
                    dove_Left_III(speed_I, -10)

                    dove_Right_I(speed_I, 3*speed_II)
                    dove_Left_II(-speed_I, 3*speed_II)
                    dove_Right_III(speed_I, 3*speed_II)
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if move_stu == 0 and command == 'no':
                    break
        elif step_input == 4:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_II, -10)
                    dove_Right_II(-speed_II, -10)
                    dove_Left_III(-speed_II, -10)

                    dove_Right_I(speed_II, 3*(speed-speed_II))
                    dove_Left_II(speed_II, 3*(speed-speed_II))
                    dove_Right_III(speed_II, 3*(speed-speed_II))
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if command == 'left':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_II, -10)
                    dove_Right_II(-speed_II, -10)
                    dove_Left_III(speed_II, -10)

                    dove_Right_I(speed_II, 3*(speed-speed_II))
                    dove_Left_II(-speed_II, 3*(speed-speed_II))
                    dove_Right_III(speed_II, 3*(speed-speed_II))
                    time.sleep(timeLast/dpi)
                elif command == 'right':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_II, -10)
                    dove_Right_II(speed_II, -10)
                    dove_Left_III(-speed_II, -10)

                    dove_Right_I(-speed_II, 3*(speed-speed_II))
                    dove_Left_II(speed_II, 3*(speed-speed_II))
                    dove_Right_III(-speed_II, 3*(speed-speed_II))
                    time.sleep(timeLast/dpi)
                else:
                    pass

                if move_stu == 0 and command == 'no':
                    break
    else:
        speed = -speed
        if step_input == 1:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_I, 3*speed_II)
                    dove_Right_II(speed_I, 3*speed_II)
                    dove_Left_III(speed_I, 3*speed_II)

                    dove_Right_I(-speed_I, -10)
                    dove_Left_II(-speed_I, -10)
                    dove_Right_III(-speed_I, -10)
                    time.sleep(timeLast/dpi)
                else:
                    pass
        elif step_input == 2:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_II, 3*(speed-speed_II))
                    dove_Right_II(-speed_II, 3*(speed-speed_II))
                    dove_Left_III(-speed_II, 3*(speed-speed_II))

                    dove_Right_I(speed_II, -10)
                    dove_Left_II(speed_II, -10)
                    dove_Right_III(speed_II, -10)
                    time.sleep(timeLast/dpi)
                else:
                    pass
        elif step_input == 3:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(-speed_I, -10)
                    dove_Right_II(-speed_I, -10)
                    dove_Left_III(-speed_I, -10)

                    dove_Right_I(speed_I, 3*speed_II)
                    dove_Left_II(speed_I, 3*speed_II)
                    dove_Right_III(speed_I, 3*speed_II)
                    time.sleep(timeLast/dpi)
                else:
                    pass
        elif step_input == 4:
            for speed_I in range(0, (speed+int(speed/dpi)), int(speed/dpi)):
                if move_stu and command == 'no':
                    speed_II = speed_I
                    speed_I = speed - speed_I
                    dove_Left_I(speed_II, -10)
                    dove_Right_II(speed_II, -10)
                    dove_Left_III(speed_II, -10)

                    dove_Right_I(-speed_II, 3*(speed-speed_II))
                    dove_Left_II(-speed_II, 3*(speed-speed_II))
                    dove_Right_III(-speed_II, 3*(speed-speed_II))
                    time.sleep(timeLast/dpi)
                else:
                    pass


def steady_X():
    if leftSide_direction:
        pwm.set_pwm(0,0,pwm0+steady_X_set)
        pwm.set_pwm(2,0,pwm2)
        pwm.set_pwm(4,0,pwm4-steady_X_set)
    else:
        pwm.set_pwm(0,0,pwm0+steady_X_set)
        pwm.set_pwm(2,0,pwm2)
        pwm.set_pwm(4,0,pwm4-steady_X_set)

    if rightSide_direction:
        pwm.set_pwm(10,0,pwm10+steady_X_set)
        pwm.set_pwm(8,0,pwm8)
        pwm.set_pwm(6,0,pwm6-steady_X_set)
    else:
        pwm.set_pwm(10,0,pwm10-steady_X_set)
        pwm.set_pwm(8,0,pwm8)
        pwm.set_pwm(6,0,pwm6+steady_X_set)



def steadyTest():
    if leftSide_direction:
        pwm.set_pwm(0,0,pwm0+steady_X)
        pwm.set_pwm(2,0,pwm2)
        pwm.set_pwm(4,0,pwm4-steady_X)
    else:
        pwm.set_pwm(0,0,pwm0+steady_X)
        pwm.set_pwm(2,0,pwm2)
        pwm.set_pwm(4,0,pwm4-steady_X)

    if rightSide_direction:
        pwm.set_pwm(10,0,pwm10+steady_X)
        pwm.set_pwm(8,0,pwm8)
        pwm.set_pwm(6,0,pwm6-steady_X)
    else:
        pwm.set_pwm(10,0,pwm10-steady_X)
        pwm.set_pwm(8,0,pwm8)
        pwm.set_pwm(6,0,pwm6+steady_X)

    while 1:
        left_H = steady_range_Min
        right_H = steady_range_Max
        left_I(0, 35, left_H)
        left_II(0, 35, left_H)
        left_III(0, 35, left_H)
        
        right_I(0, 35, right_H)
        right_II(0, 35, right_H)
        right_III(0, 35, right_H)

        time.sleep(1)
        
        left_H = 130
        right_H = -40
        left_I(0, 35, left_H)
        left_II(0, 35, left_H)
        left_III(0, 35, left_H)
        
        right_I(0, 35, right_H)
        right_II(0, 35, right_H)
        right_III(0, 35, right_H)

        time.sleep(1)
        

def look_up(wiggle=look_wiggle):
    global Up_Down_input
    if Up_Down_direction:
        Up_Down_input += wiggle
        Up_Down_input = ctrl_range(Up_Down_input, Up_Down_Max, Up_Down_Min)
    else:
        Up_Down_input -= wiggle
        Up_Down_input = ctrl_range(Up_Down_input, Up_Down_Max, Up_Down_Min)
    pwm.set_pwm(13, 0, Up_Down_input)


def look_down(wiggle=look_wiggle):
    global Up_Down_input
    if Up_Down_direction:
        Up_Down_input -= wiggle
        Up_Down_input = ctrl_range(Up_Down_input, Up_Down_Max, Up_Down_Min)
    else:
        Up_Down_input += wiggle
        Up_Down_input = ctrl_range(Up_Down_input, Up_Down_Max, Up_Down_Min)
    pwm.set_pwm(13, 0, Up_Down_input)


def look_left(wiggle=look_wiggle):
    global Left_Right_input
    if Left_Right_direction:
        Left_Right_input += wiggle
        Left_Right_input = ctrl_range(Left_Right_input, Left_Right_Max, Left_Right_Min)
    else:
        Left_Right_input -= wiggle
        Left_Right_input = ctrl_range(Left_Right_input, Left_Right_Max, Left_Right_Min)
    pwm.set_pwm(12, 0, Left_Right_input)


def look_right(wiggle=look_wiggle):
    global Left_Right_input
    if Left_Right_direction:
        Left_Right_input -= wiggle
        Left_Right_input = ctrl_range(Left_Right_input, Left_Right_Max, Left_Right_Min)
    else:
        Left_Right_input += wiggle
        Left_Right_input = ctrl_range(Left_Right_input, Left_Right_Max, Left_Right_Min)
    pwm.set_pwm(12, 0, Left_Right_input)


def look_home():
    global Left_Right_input, Up_Down_input
    pwm.set_pwm(13, 0, 300)
    pwm.set_pwm(12, 0, 300)
    Left_Right_input = 300
    Up_Down_input = 300


def relesae():
    pwm.set_all_pwm(0,0)


def clean_all():
    pwm.set_all_pwm(0, 0)


def destroy():
    clean_all()


if __name__ == '__main__':
    step = 1
    move_stu = 1
    try:
        # '''
        while 1:
            move(step, 35, 'no')
            step += 1
            if step > 4:
                step = 1
            time.sleep(0.08)
        # '''
        
    except KeyboardInterrupt:
        pwm.set_all_pwm(0, 300)
        time.sleep(1)
        
    

