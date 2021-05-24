import RPi.GPIO as GPIO
import time
sspeed = 343

print("Test Ultrasonic")

GPIO.setmode(GPIO.BCM)
TRIG = 2
ECHO = 3

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
    start_time = time.time()
print("Start Time Recorded")

while GPIO.input(ECHO) == 1:
    stop_time = time.time()
print("Stop Time Recorded")
dis = (stop_time - start_time) * sspeed / 2

print("dis=", dis, "m")