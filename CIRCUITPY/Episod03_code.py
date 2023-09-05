import time
import board
import digitalio

led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP3)
led3.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.GP21)
button2.direction = digitalio.Direction.INPUT

while True:
    if button1.value == False:
        print("Butang GP20 ditekan")
        led2.value = True
        while button1.value == False:
            continue
    else:
        led2.value = False
    
    if button2.value == False:
        print("Butang GP21 ditekan")
        led3.value = True
        while button2.value == False:
            continue
    else:
        led3.value = False
