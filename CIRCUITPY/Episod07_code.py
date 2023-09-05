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

light = analogio.AnalogIn(board.GP27)

note_frequency = [
    0,
    261, 277, 293, 311, 329,
    349, 367, 392, 415, 440,
    466, 494, 523, 554, 587,
    622, 659, 698, 739, 784,
]

while True:
    adc = light.value
    index = simpleio.map_range(adc, 1000, 45000, 20, 0)
    simpleio.tone(board.GP18, note_frequency[int(index)], 0.1)
