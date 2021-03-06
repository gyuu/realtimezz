#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)


def rotate(angle):
  servopin = 21
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servopin, GPIO.OUT, initial=False)
  p = GPIO.PWM(servopin, 50) #50HZ
  p.start(0)
  p.ChangeDutyCycle(2.5+10*angle/180)
  time.sleep(0.02)
  p.ChangeDutyCycle(0)
  time.sleep(0.2)
