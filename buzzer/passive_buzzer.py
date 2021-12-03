from machine import Pin, PWM
import math
import time

Pi = 3.14
button = Pin(4, Pin.IN, Pin.PULL_UP)
passive_buzzer = PWM(Pin(13), 2000,512)

def alert():
    for x in range(0, 36):
        sinVal=math.sin(x*10*Pi/180)
        toneVal = 2000+int(sinVal*500)
        passive_buzzer.freq(toneVal)
        time.sleep_ms(10)
        
try:
    while True:
        if not button.value():
            alert()
        else:
            passive_buzzer.freq(0)
            
except:
    passive_buzzer.deint()