import time
import board
import microcontroller
import adafruit_dotstar
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

led.brightness = 0.4
tprev = microcontroller.cpu.temperature 

while True:
    t = microcontroller.cpu.temperature
    d = t - tprev
    print(d, t)
    led.brightness = abs(d)
    led[0] = (0, 0, 255) if d < 0 else (255, 0, 0)
    tprev = t
    time.sleep(1.0)
