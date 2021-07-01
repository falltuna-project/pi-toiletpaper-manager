from sensors.ultrasonicsensor import distance
from sensors.camera import cam_capture
from LED.led import led_on, led_off
from LED.seven import ssd
import time
from gesture import img_rec
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
                result = img_rec(['./img/img%s.jpg' % i])
                ssd(result,1)
            time.sleep(0.7)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()