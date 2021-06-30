from sensors.ultrasonicsensor import distance
from sensors.camera import cam_capture
from LED.led import led_on, led_off
import time
init_dist = 40


if __name__ == '__main__':
    i = 0
    try:
        while True:
            dist = distance()
            print ("Distance = %.1f cm" % dist)
            if dist < init_dist - 5 and dist > 4:
                i +=1
                led_on()
                cam_capture(i)
                led_off()
            time.sleep(0.7)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()