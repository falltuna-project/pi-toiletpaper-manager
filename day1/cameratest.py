from picamera import PiCamera
from time import sleep

camera = PiCamera()
sleep(6)
print("Start Capturing")
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Documents/Project5781/imgae.jpg')
print("Image Saved!")
camera.stop_preview()           