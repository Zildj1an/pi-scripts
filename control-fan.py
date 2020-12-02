
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
        
        get_temp = os.popen('vcgencmd measure_temp').readline()
        str_temp = get_temp[5] + get_temp[6]
        temp = int(str_temp)

        #normalize the temp from (30-80) to 0-100

        normalized_temp = (temp-30) * 2
        
        cpu = psutil.cpu_percent()
        pwm.start( (cpu + normalized_temp) / 2)

        time.sleep(2)
    

if __name__ == "__main__":
    main()
