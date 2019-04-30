import time
import picamera
import RPi.GPIO as GPIO
import datetime


now = datetime.datetime.now()
day=now.strftime('%Y-%m-%d,%HH%MM%S')

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,GPIO.PUD_UP)

with picamera.PiCamera() as camera:
    camera.start_preview()
    
    while true:
        GPIO.wait_for_edge(17,GPIO.FALLING)
        time.sleep(10)
        camera.capture('/home/pi/',nowDatetime,'.jpg')
    camera.stop_preview()
