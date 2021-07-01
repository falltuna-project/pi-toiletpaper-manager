import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_LED = 4
GPIO.setup(GPIO_LED, GPIO.OUT) 

def led_on():
    GPIO.output(GPIO_LED, True)
    
def led_off():
    GPIO.output(GPIO_LED, False)

