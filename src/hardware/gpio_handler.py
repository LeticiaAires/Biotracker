import RPi.GPIO as GPIO

def setup_pin(pin, mode):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, mode)

def read_pin(pin):
    return GPIO.input(pin)
