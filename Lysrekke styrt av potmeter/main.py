import time
from machine import Pin, ADC

potentiometer = ADC(Pin(36))
potentiometer.atten(ADC.ATTN_11DB)
pins = [15, 2, 0, 4, 5, 18, 19, 21, 22, 23]

def show_leds(pot_val):
    if pot_val >= 0 and pot_val <= 410:
        led = Pin(pins[0], Pin.OUT)
        led.value(1)
    elif pot_val > 410 and pot_val <= 820:
        led = Pin(pins[1], Pin.OUT)
        led.value(1)
    elif pot_val > 820 and pot_val <= 1230:
        led = Pin(pins[2], Pin.OUT)
        led.value(1)
    elif pot_val > 1230 and pot_val <= 1640:
        led = Pin(pins[3], Pin.OUT)
        led.value(1)
    elif pot_val > 1640 and pot_val <= 2050:
        led = Pin(pins[4], Pin.OUT)
        led.value(1)
    elif pot_val > 2050 and pot_val <= 2460:
        led = Pin(pins[5], Pin.OUT)
        led.value(1)
    elif pot_val > 2460 and pot_val <= 2870:
        led = Pin(pins[6], Pin.OUT)
        led.value(1)
    elif pot_val > 2870 and pot_val <= 3280:
        led = Pin(pins[7], Pin.OUT)
        led.value(1)
    elif pot_val > 3280 and pot_val <= 3690:
        led = Pin(pins[8], Pin.OUT)
        led.value(1)
    elif pot_val > 3690 and pot_val <= 4095:
        led = Pin(pins[9], Pin.OUT)
        led.value(1)
        
def reset_pins():
    for pin in pins:
        led = Pin(pin, Pin.OUT)
        led.value(0)
        
        
while True:
    reset_pins()
    potentiometer_value = potentiometer.read()
    print(potentiometer_value)
    show_leds(potentiometer_value)
        
