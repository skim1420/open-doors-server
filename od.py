#!/usr/bin/python
import time
import RPi.GPIO as GPIO

# Place me in cgi-bin dir (typically /usr/lib/cgi-bin)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
time.sleep(5)
GPIO.output(2, GPIO.HIGH)

