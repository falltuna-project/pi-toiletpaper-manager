import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_C = 17
GPIO_LU = 18
GPIO_RU = 22
GPIO_TU = 23
GPIO_LD = 24
GPIO_RD = 27
GPIO_BD = 25
GPIO.setup(GPIO_C, GPIO.OUT)
GPIO.setup(GPIO_LU, GPIO.OUT)
GPIO.setup(GPIO_LD, GPIO.OUT)
GPIO.setup(GPIO_RU, GPIO.OUT)
GPIO.setup(GPIO_RD, GPIO.OUT)
GPIO.setup(GPIO_BD, GPIO.OUT)
GPIO.setup(GPIO_TU, GPIO.OUT)


def one(t):
    GPIO.output(GPIO_RU, True)
    GPIO.output(GPIO_RD, True)
    time.sleep(t)
    GPIO.output(GPIO_RU, False)
    GPIO.output(GPIO_RD, False)
    
def two(t):
    GPIO.output(GPIO_RU, True)
    GPIO.output(GPIO_TU, True)
    GPIO.output(GPIO_C, True)
    GPIO.output(GPIO_LD, True)
    GPIO.output(GPIO_BD, True)
    time.sleep(t)
    GPIO.output(GPIO_RU, False)
    GPIO.output(GPIO_TU, False)
    GPIO.output(GPIO_C, False)
    GPIO.output(GPIO_LD, False)
    GPIO.output(GPIO_BD, False)
    
def three(t):
    GPIO.output(GPIO_RU, True)
    GPIO.output(GPIO_TU, True)
    GPIO.output(GPIO_C, True)
    GPIO.output(GPIO_RD, True)
    GPIO.output(GPIO_BD, True)
    time.sleep(t)
    GPIO.output(GPIO_RU, False)
    GPIO.output(GPIO_TU, False)
    GPIO.output(GPIO_C, False)
    GPIO.output(GPIO_RD, False)
    GPIO.output(GPIO_BD, False)
    
def four(t):
    GPIO.output(GPIO_RU, True)
    GPIO.output(GPIO_C, True)
    GPIO.output(GPIO_RD, True)
    GPIO.output(GPIO_LU, True)
    time.sleep(t)
    GPIO.output(GPIO_RU, False)
    GPIO.output(GPIO_C, False)
    GPIO.output(GPIO_RD, False)
    GPIO.output(GPIO_LU, False)
    
def five(t):
    GPIO.output(GPIO_LU, True)
    GPIO.output(GPIO_TU, True)
    GPIO.output(GPIO_C, True)
    GPIO.output(GPIO_RD, True)
    GPIO.output(GPIO_BD, True)
    time.sleep(t)
    GPIO.output(GPIO_LU, False)
    GPIO.output(GPIO_TU, False)
    GPIO.output(GPIO_C, False)
    GPIO.output(GPIO_RD, False)
    GPIO.output(GPIO_BD, False)
    
def ssd(num,t):
    if num == "1":
        one(t)
    elif num == "2":
        two(t)
    elif num == "3":
        three(t)
    elif num =="4":
        four(t)
    elif num == "5":
        five(t)
    else:
        print("???")
        