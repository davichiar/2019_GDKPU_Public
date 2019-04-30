import time
import picamera
import datetime
import os

now = datetime.datetime.now()
day=now.strftime('%Y-%m-%d,%HH%MM%S')

path=os.getenv("HOME")+""  #adjust path for location of this program
with picamera.PiCamera() as picam:
    picam.rotation=90 #adjust as necessary
    picam.start_preview()
    while True:
        time.sleep(5)
        camera.capture('/home/pi/',nowDatetime,'.jpg')
    picam.stop_preview()
    picam.close()
