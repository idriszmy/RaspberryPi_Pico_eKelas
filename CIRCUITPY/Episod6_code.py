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

simpleio.tone(board.GP18, 523, 0.3)
simpleio.tone(board.GP18, 392, 0.15)
simpleio.tone(board.GP18, 392, 0.15)
simpleio.tone(board.GP18, 440, 0.3)
simpleio.tone(board.GP18, 392, 0.3)
time.sleep(0.3)
simpleio.tone(board.GP18, 493, 0.3)
simpleio.tone(board.GP18, 523, 0.3)