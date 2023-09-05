import time
import board
import digitalio

led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP3)
led3.direction = digitalio.Direction.OUTPUT

while True:
    led2.value = True
    led3.value = False
    time.sleep(1)
    led2.value = False
    led3.value = True
    time.sleep(1)
