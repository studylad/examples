from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture(f'/home/pi/Desktop/image{i}.jpg')
camera.stop_preview()