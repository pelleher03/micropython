from time import sleep_ms
from machine import Pin

led_red = Pin(2,Pin.OUT)
led_blue = Pin(15, Pin.OUT)
button_one = Pin(13, Pin.IN,Pin.PULL_UP)
try:
    while True:
        if not button_one.value():
            led_red.value(1)
            led_blue.value(0)
        else:
            led_red.value(0)
            led_blue.value(1)           
except:
    pass