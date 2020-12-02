
import sys
import psutil
import RPi.GPIO as GPIO
import os
import time
import datetime

def main():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    pwm = GPIO.PWM(12,500)

    while True:
            
        
        cpu = psutil.cpu_percent()
        pwm.start(cpu)

        time.sleep(2)
    

if __name__ == "__main__":
    main()
