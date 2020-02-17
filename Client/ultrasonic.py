import RPi.GPIO as GPIO
import time

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 11
pinEcho = 8

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


def measure():
    # set Trigger to HIGH
    GPIO.output(pinTrigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    start_time = time.time()
    stop_time = time.time()

    # save start time
    while GPIO.input(pinEcho) == 0:
        start_time = time.time()

    # save time of arrival
    while GPIO.input(pinEcho) == 1:
        stop_time = time.time()

    # time difference between start and arrival
    time_elapsed = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2

    print("Distance: %.1f cm" % distance)
    time.sleep(0.001)
    return distance

def closing():
    GPIO.output(pinTrigger, False)
    GPIO.cleanup()
