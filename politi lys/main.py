from time import sleep_ms
from machine import Pin

led_red = Pin(2,Pin.OUT)
led_blue = Pin(15, Pin.OUT)
try:
    while True:
        led_red.value(1)
        led_blue.value(0)
        sleep_ms(1000)
        led_red.value(0)
        led_blue.value(1)
        sleep_ms(1000)
except:
    pass