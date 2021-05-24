from sensors.ultrasonicsensor import distance
from sensors.camera import cam_capture
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
                cam_capture(i)
            time.sleep(0.7)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()