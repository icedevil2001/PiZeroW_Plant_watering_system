#!/usr/bin/env python
import RPi.GPIO as GPIO
import time 


channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("no water detected")
    else:
        print('water detected')

