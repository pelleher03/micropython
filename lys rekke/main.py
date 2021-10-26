import time
from machine import Pin

pins = [15, 2, 0, 4, 5, 18, 19, 21, 22, 23]

def show_leds():
    for current_pin in pins:
        led = Pin(current_pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
while True:
    show_leds()
        
