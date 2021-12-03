#Importerer alle bibliotekene jeg skal bruke 
from machine import TouchPad, Pin, ADC
import time

#Setter innstillingen til ADC(bredden), potensiometeret bruker ADC
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)
#Lager en variabel som sier hvilken pin som brukes til touch
tp = TouchPad(Pin(15, Pin.IN, Pin.PULL_UP))
#En variabel som sier hvilken pin lysdioden er
led = Pin(2, Pin.OUT)

while True:
    #lager en variabel som henter ADC verdien fra potensiometeret, hvor 0 er minst motstand og 1023 er merst motstand
    sensetivity = adc.read()
    #Printer verdien på touch pinen og sensetivitet innstillingen fra potensiometeret
    print('Touch value: ', tp.read(), 'sensetivity: ', sensetivity)
    #En pause slik at man ikke leser verdier hele tiden
    time.sleep_ms(100)
    
    #Om senstiviteten er lav, krever det lite for at lysdioden skal lyse, er sensitiviteten høy krever det mer for at den skal lyse
    #Under er en if hvor man ser de 5 forskjellige nivåene
    if sensetivity <= 200 and tp.read() < 200:
        led.value(1)
    elif sensetivity <= 400 and tp.read() < 150:
        led.value(1)
    elif sensetivity <= 600 and tp.read() < 140:
        led.value(1)
    elif sensetivity <= 800 and tp.read() < 130:
        led.value(1)
    elif sensetivity <= 1023 and tp.read() < 125:
        led.value(1)
    #Om man ikke trykker ned på sensoren vil lysdioden være av
    else:
        led.value(0)