import time
import board
import digitalio
import neopixel
import analogio
import simpleio

led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP3)
led3.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.GP21)
button2.direction = digitalio.Direction.INPUT

pixels = neopixel.NeoPixel(board.GP28, 1, brightness=0.3, auto_write=False)

potentiometer = analogio.AnalogIn(board.GP27)

while True:
    adc = potentiometer.value
    bright = simpleio.map_range(adc, 0, 65535, 0, 255)
    print(bright)
    pixels.fill((bright, 0, 0))
    pixels.show()
    time.sleep(0.1)