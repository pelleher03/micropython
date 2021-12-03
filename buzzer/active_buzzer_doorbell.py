from machine import Pin

button = Pin(4, Pin.IN, Pin.PULL_UP)
active_buzzer = Pin(13, Pin.OUT)

active_buzzer.value(0)

while True:
    if not button.value():
        active_buzzer.value(1)
    else:
        active_buzzer.value(0)