import time
import board
import digitalio
import neopixel

led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP3)
led3.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.GP21)
button2.direction = digitalio.Direction.INPUT

pixels = neopixel.NeoPixel(board.GP28, 1, brightness=0.3, auto_write=False)

while True:
    if button1.value == False:
        pixel.fill((255, 0, 0))
        pixels.show()
        
        while button1.value == False:
            continue
    
    if button2.value == False:
        pixel.fill((255, 0, 0))
        pixels.show()
        
        while button2.value == False:
            continue