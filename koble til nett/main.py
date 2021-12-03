from machine import Pin
import neopixel
import time

#Setter hvilke pin som neopixelen skal bruke til data
#Setter den til utgang fordi pinnen skal gi data til neopixelen
neo_pin = Pin(2, Pin.OUT)
np = neopixel.NeoPixel(Pin, 8)

#Setter at jeg bruker 2 piner som inngang, siden jeg skal lese data fra knappene
#Sier også at disse er koblet med pull up motstand
button_one = Pin(12, Pin.IN, Pin.PULL_UP)
button_two = Pin(13, Pin.IN, Pin.PULL_UP)

#Fuksjon for hva som skal skje når man trykker knapp 1
def med_klokka:
    pass
#Funksjon for hva som skal skjer når man trykker knapp 2
def mot_klokka:
    pass

#En evig loop som kjører helt til den blir avbrutt
while True:
    if button_one.value():
        time.sleep_ms(20)
        if button_one.value():
            print(button_one.value(), 'kanppen er trykket')
    
    