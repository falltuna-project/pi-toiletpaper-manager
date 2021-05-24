from picamera import PiCamera
from time import sleep

def cam_capture(pic_id):
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('./img/img%s.jpg' % pic_id)
    print("Image Saved!")
    camera.stop_preview()
    camera.close()