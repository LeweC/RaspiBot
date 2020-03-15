#! /usr/bin/python
# File name   : move.py
# Description : Controlling all servos
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
    leftSide_direction = 1
    rightSide_direction = 0
else:
    leftSide_direction = 0
    rightSide_direction = 1

'''
change these two variables to reverse the height of the legs.
'''
if set_direction:
    leftSide_height = 0
    rightSide_height = 1
else:
    leftSide_height = 1
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
range_Mid = (steady_range_Min + steady_range_Max) / 2
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
for i in range(0, 16):
    exec('pwm%d=300' % i)


def init_all():
    pwm.set_all_pwm(0, 300)
    pwm.set_pwm(12,0,300)


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


def left_I(pos, wiggle, heightAdjust=0):
    if pos == 0:
        # pwm.set_pwm(0,0,pwm0)
        if leftSide_height:
            pwm.set_pwm(1, 0, pwm1 + heightAdjust)
        else:
            pwm.set_pwm(1, 0, pwm1 - heightAdjust)
    else:
        if leftSide_direction:
            if pos == 1:
                pwm.set_pwm(0, 0, pwm0)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 + 3 * height_change)
                else:
                    pwm.set_pwm(1, 0, pwm1 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(0, 0, pwm0 + wiggle)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 - height_change)
                else:
                    pwm.set_pwm(1, 0, pwm1 + height_change)
            elif pos == 3:
                pwm.set_pwm(0, 0, pwm0)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 - height_change)
                else:
                    pwm.set_pwm(1, 0, pwm1 + height_change)
            elif pos == 4:
                pwm.set_pwm(0, 0, pwm0 - wiggle)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 - height_change)
                else:
                    pwm.set_pwm(1, 0, pwm1 + height_change)
        else:
            if pos == 1:
                pwm.set_pwm(0, 0, pwm0)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 + 3 * wiggle)
                else:
                    pwm.set_pwm(1, 0, pwm1 - 3 * wiggle)
            elif pos == 2:
                pwm.set_pwm(0, 0, pwm0 - wiggle)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 - wiggle)
                else:
                    pwm.set_pwm(1, 0, pwm1 + wiggle)
            elif pos == 3:
                pwm.set_pwm(0, 0, pwm0)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 - wiggle)
                else:
                    pwm.set_pwm(1, 0, pwm1 + wiggle)
            elif pos == 4:
                pwm.set_pwm(0, 0, pwm0 + wiggle)
                if leftSide_height:
                    pwm.set_pwm(1, 0, pwm1 - wiggle)
                else:
                    pwm.set_pwm(1, 0, pwm1 + wiggle)


def left_II(pos, wiggle, heightAdjust=0):
    if pos == 0:
        # pwm.set_pwm(2,0,pwm2)
        if leftSide_height:
            pwm.set_pwm(3, 0, pwm3 + heightAdjust)
        else:
            pwm.set_pwm(3, 0, pwm3 - heightAdjust)
    else:
        if leftSide_direction:
            if pos == 1:
                pwm.set_pwm(2, 0, pwm2)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 + 3 * height_change)
                else:
                    pwm.set_pwm(3, 0, pwm3 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(2, 0, pwm2 + wiggle)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 - height_change)
                else:
                    pwm.set_pwm(3, 0, pwm3 + height_change)
            elif pos == 3:
                pwm.set_pwm(2, 0, pwm2)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 - height_change)
                else:
                    pwm.set_pwm(3, 0, pwm3 + height_change)
            elif pos == 4:
                pwm.set_pwm(2, 0, pwm2 - wiggle)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 - height_change)
                else:
                    pwm.set_pwm(3, 0, pwm3 + height_change)
        else:
            if pos == 1:
                pwm.set_pwm(2, 0, pwm2)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 + 3 * wiggle)
                else:
                    pwm.set_pwm(3, 0, pwm3 - 3 * wiggle)
            elif pos == 2:
                pwm.set_pwm(2, 0, pwm2 - wiggle)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 - wiggle)
                else:
                    pwm.set_pwm(3, 0, pwm3 + wiggle)
            elif pos == 3:
                pwm.set_pwm(2, 0, pwm2)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 - wiggle)
                else:
                    pwm.set_pwm(3, 0, pwm3 + wiggle)
            elif pos == 4:
                pwm.set_pwm(2, 0, pwm2 + wiggle)
                if leftSide_height:
                    pwm.set_pwm(3, 0, pwm3 - wiggle)
                else:
                    pwm.set_pwm(3, 0, pwm3 + wiggle)


def left_III(pos, wiggle, heightAdjust=0):
    if pos == 0:
        # pwm.set_pwm(4,0,pwm4)
        if leftSide_height:
            pwm.set_pwm(5, 0, pwm5 + heightAdjust)
        else:
            pwm.set_pwm(5, 0, pwm5 - heightAdjust)
    else:
        if leftSide_direction:
            if pos == 1:
                pwm.set_pwm(4, 0, pwm4)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 + 3 * height_change)
                else:
                    pwm.set_pwm(5, 0, pwm5 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(4, 0, pwm4 + wiggle)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 - height_change)
                else:
                    pwm.set_pwm(5, 0, pwm5 + height_change)
            elif pos == 3:
                pwm.set_pwm(4, 0, pwm4)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 - height_change)
                else:
                    pwm.set_pwm(5, 0, pwm5 + height_change)
            elif pos == 4:
                pwm.set_pwm(4, 0, pwm4 - wiggle)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 - height_change)
                else:
                    pwm.set_pwm(5, 0, pwm5 + height_change)
        else:
            if pos == 1:
                pwm.set_pwm(4, 0, pwm4)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 + 3 * wiggle)
                else:
                    pwm.set_pwm(5, 0, pwm5 - 3 * wiggle)
            elif pos == 2:
                pwm.set_pwm(4, 0, pwm4 - wiggle)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 - wiggle)
                else:
                    pwm.set_pwm(5, 0, pwm5 + wiggle)
            elif pos == 3:
                pwm.set_pwm(4, 0, pwm4)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 - wiggle)
                else:
                    pwm.set_pwm(5, 0, pwm5 + wiggle)
            elif pos == 4:
                pwm.set_pwm(4, 0, pwm4 + wiggle)
                if leftSide_height:
                    pwm.set_pwm(5, 0, pwm5 - wiggle)
                else:
                    pwm.set_pwm(5, 0, pwm5 + wiggle)


def right_I(pos, wiggle, heightAdjust=0):
    # wiggle = -wiggle
    if pos == 0:
        # pwm.set_pwm(6,0,pwm6)
        if rightSide_height:
            pwm.set_pwm(7, 0, pwm7 + heightAdjust)
        else:
            pwm.set_pwm(7, 0, pwm7 - heightAdjust)
    else:
        if rightSide_direction:
            if pos == 1:
                pwm.set_pwm(6, 0, pwm6)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 + 3 * height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(6, 0, pwm6 + wiggle)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 - height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 + height_change)
            elif pos == 3:
                pwm.set_pwm(6, 0, pwm6)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 - height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 + height_change)
            elif pos == 4:
                pwm.set_pwm(6, 0, pwm6 - wiggle)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 - height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 + height_change)
        else:
            if pos == 1:
                pwm.set_pwm(6, 0, pwm6)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 + 3 * height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(6, 0, pwm6 - wiggle)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 - height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 + height_change)
            elif pos == 3:
                pwm.set_pwm(6, 0, pwm6)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 - height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 + height_change)
            elif pos == 4:
                pwm.set_pwm(6, 0, pwm6 + wiggle)
                if rightSide_height:
                    pwm.set_pwm(7, 0, pwm7 - height_change)
                else:
                    pwm.set_pwm(7, 0, pwm7 + height_change)


def right_II(pos, wiggle, heightAdjust=0):
    # wiggle = -wiggle
    if pos == 0:
        # pwm.set_pwm(8,0,pwm8)
        if rightSide_height:
            pwm.set_pwm(9, 0, pwm9 + heightAdjust)
        else:
            pwm.set_pwm(9, 0, pwm9 - heightAdjust)
    else:
        if rightSide_direction:
            if pos == 1:
                pwm.set_pwm(8, 0, pwm8)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 + 3 * height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(8, 0, pwm8 + wiggle)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 - height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 + height_change)
            elif pos == 3:
                pwm.set_pwm(8, 0, pwm8)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 - height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 + height_change)
            elif pos == 4:
                pwm.set_pwm(8, 0, pwm8 - wiggle)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 - height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 + height_change)
        else:
            if pos == 1:
                pwm.set_pwm(8, 0, pwm8)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 + 3 * height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(8, 0, pwm8 - wiggle)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 - height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 + height_change)
            elif pos == 3:
                pwm.set_pwm(8, 0, pwm8)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 - height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 + height_change)
            elif pos == 4:
                pwm.set_pwm(8, 0, pwm8 + wiggle)
                if rightSide_height:
                    pwm.set_pwm(9, 0, pwm9 - height_change)
                else:
                    pwm.set_pwm(9, 0, pwm9 + height_change)


def right_III(pos, wiggle, heightAdjust=0):
    # wiggle = -wiggle
    if pos == 0:
        # pwm.set_pwm(10,0,pwm10)
        if rightSide_height:
            pwm.set_pwm(11, 0, pwm11 + heightAdjust)
        else:
            pwm.set_pwm(11, 0, pwm11 - heightAdjust)
    else:
        if rightSide_direction:
            if pos == 1:
                pwm.set_pwm(10, 0, pwm10)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 + 3 * height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(10, 0, pwm10 + wiggle)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 - height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 + height_change)
            elif pos == 3:
                pwm.set_pwm(10, 0, pwm10)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 - height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 + height_change)
            elif pos == 4:
                pwm.set_pwm(10, 0, pwm10 - wiggle)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 - height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 + height_change)
        else:
            if pos == 1:
                pwm.set_pwm(10, 0, pwm10)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 + 3 * height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 - 3 * height_change)
            elif pos == 2:
                pwm.set_pwm(10, 0, pwm10 - wiggle)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 - height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 + height_change)
            elif pos == 3:
                pwm.set_pwm(10, 0, pwm10)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 - height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 + height_change)
            elif pos == 4:
                pwm.set_pwm(10, 0, pwm10 + wiggle)
                if rightSide_height:
                    pwm.set_pwm(11, 0, pwm11 - height_change)
                else:
                    pwm.set_pwm(11, 0, pwm11 + height_change)


def move(step_input, speed, command):
    step_I = step_input
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
    pwm.set_pwm(0, 0, 300)
    pwm.set_pwm(1, 0, 300)
    pwm.set_pwm(2, 0, 300)
    pwm.set_pwm(3, 0, 300)
    pwm.set_pwm(4, 0, 300)
    pwm.set_pwm(5, 0, 300)
    pwm.set_pwm(6, 0, 300)
    pwm.set_pwm(7, 0, 300)
    pwm.set_pwm(8, 0, 300)
    pwm.set_pwm(9, 0, 300)
    pwm.set_pwm(10, 0, 300)
    pwm.set_pwm(11, 0, 300)


def sensor_right():
    pwm.set_pwm(12,0,100)

def sensor_left():
    pwm.set_pwm(12,0,500)

def sensor_middle():
    pwm.set_pwm(12,0,300)

def release():
    pwm.set_all_pwm(0, 0)



def clean_all():
    pwm.set_all_pwm(0, 0)


def destroy():
    clean_all()