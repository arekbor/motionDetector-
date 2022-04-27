import RPi.GPIO as GPIO
import time

time.sleep(10)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.OUT)
GPIO.output(25,False)
def motionSensor(channel):
    if GPIO.input(4):
        GPIO.output(25,True)

GPIO.add_event_detect(4,GPIO.BOTH,callback=motionSensor,bouncetime=50)

try: 
    while True:
        time.sleep(1)
finally:
    GPIO.cleanup()
