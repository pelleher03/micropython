#Importerer de modulene som skal brukes 
from machine import Pin, ADC
import time
#Setter at lysdioen er på pin 2, og at den er en output
led = Pin(2, Pin.OUT)

#Sier hvilken pin som buzzeren er tilkoblet, og setter buzzeren til å starte avslått
active_buzzer = Pin(13, Pin.OUT)
active_buzzer.value(0)

#Sette innstillingen for hvordan verdiene fra potensiometeret blir skriv ut, 10bit(0-1023)
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)

while True:
    #adc_val er en variabel som leser verdien fra potmetert og lagrer det i en variabel
    adc_val = adc.read()
    print(adc_val)
    #Skruer på buzzeren og lysdioden
    active_buzzer.value(1)
    led.value(1)
    #Har en pause i ms, som tilsvarer verdien til potensiometert 
    time.sleep_ms(adc_val)
    #Etter pausen skrues buzzeren og lysdioen av, før det igjen kommer en ny pause
    active_buzzer.value(0)
    led.value(0)
    time.sleep_ms(adc_val)
    #På denne måten bruker man et potmeter til å styre hastigheten mellom hver gang lysdioen og buzzeren er av og på