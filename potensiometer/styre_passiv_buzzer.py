#Imporeret de modulene jeg skal bruke i koden
from machine import Pin, PWM, ADC
import time

#Lager to PWM objekter, en for den passive buzzeren og en for lysdioden
#Buzzeren har en satt starter frekven på 2000 og en start duty på 512
passive_buzzer = PWM(Pin(13), 2000,512)
led = PWM(Pin(19, Pin.OUT))

#Setter innstillingene på hvordan verdien man skal lese fra potensiometeret
#Man vil lese et tall på 10bit (0-1023)
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)


while True:
    #Lager en variabel som leser og lagrer verdien som man får fra potensiometeret
    adc_val = adc.read()
    #En tone variabel som sier hvilken tone buzzeren skal spille
    toneVal = adc_val
    #Printer både potensiometer verdien og tone verdien
    print(adc_val, toneVal)
    #Setter duty cyclen til lysdioden til det samme som potensiometeret, slik at man kan dimme leden med potmeteret 
    led.duty(adc_val)
    #Gjør at buzzeren spiller den tonen/frekvensen som vi har satt
    passive_buzzer.freq(toneVal)
    time.sleep_ms(20)
