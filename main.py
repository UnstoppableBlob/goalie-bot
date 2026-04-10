from machine import Pin
import time

DIR_PIN = 15
STEP_PIN = 14
dir_pin = Pin(DIR_PIN, Pin.OUT)
step_pin = Pin(STEP_PIN, Pin.OUT)

btn_right  = Pin(3, Pin.IN, Pin.PULL_UP)
btn_left   = Pin(2, Pin.IN, Pin.PULL_UP)
btn_home   = Pin(6, Pin.IN, Pin.PULL_UP)

position = 0  # tracks steps from start

def step(direction):
    global position
    dir_pin.value(direction)
    step_pin.value(1)
    time.sleep_us(1400)
    step_pin.value(0)
    time.sleep_us(1400)
    if direction == 1:
        position += 1
    else:
        position -= 1

time.sleep(2)

while True:
    if btn_right.value() == 0:
        step(1)

    elif btn_left.value() == 0:
        step(0)

    elif btn_home.value() == 0:
        # return to start by stepping opposite direction
        if position > 0:
            while position > 0:
                step(0)
        elif position < 0:
            while position < 0:
                step(1)