from machine import Pin
import neopixel
import time

#Setter hvilke pin som neopixelen skal bruke til data
#Setter den til utgang fordi pinnen skal gi data til neopixelen
neo_pin = Pin(2, Pin.OUT)
np = neopixel.NeoPixel(neo_pin, 8)

speed_b_two = 1
speed_b_one = 1
speed_index_one = 0
speed_index_two = 0

#Setter at jeg bruker 2 piner som inngang, siden jeg skal lese data fra knappene
#Sier også at disse er koblet med pull up motstand
button_one = Pin(12, Pin.IN, Pin.PULL_UP)
button_two = Pin(13, Pin.IN, Pin.PULL_UP)
button_reset = Pin(14, Pin.IN, Pin.PULL_UP)
    
#Fuksjon for hva som skal skje når man trykker knapp 1
def med_klokka(speed):
    brightness = 80
    color = [[brightness, 0, 0],
            [0, brightness, 0],
            [0, 0, brightness],
            [0, brightness, brightness],
            [brightness, brightness, brightness]]
    while button_one.value() == 1 and button_two.value() == 1:
        for i in range (0, 8):
            if i == 0:
                for x in range (0, 8):
                    np[x] = [0,0,0]
                    np.write()
                np[i] = color[speed_index_one]
                np.write()
                time.sleep(0.5)
                np[i] = [0,0,0]
                np.write()
            else:
                np[i] = color[speed_index_one]
                np.write()
                for y in range (0, i):
                    np[y] = color[speed_index_one]
                    np.write()
                    brightness = brightness - 10
                time.sleep(speed)
                np[i] = [0,0,0]
                np.write()
                np[y] = [0,0,0]
                np.write()
        
#Funksjon for hva som skal skjer når man trykker knapp 2
def mot_klokka(speed):
    while button_one.value() == 1 and button_two.value() == 1:
        for i in range (7, -1, -1):
            if i == 7:
                for x in range (0, 8):
                    np[x] = [0,0,0]
                    np.write()
                np[i] = color[speed_index_two]
                np.write()
                time.sleep(0.5)
                np[i] = [0,0,0]
                np.write()
            else:
                np[i] = color[speed_index_two]
                np.write()
                for y in range (7, i, -1):
                    np[y] = color[2]
                    np.write()
                time.sleep(speed)
                np[i] = [0,0,0]
                np.write()
                np[y] = [0,0,0]
                np.write()

#En evig loop som kjører helt til den blir avbrutt
while True:
    if not button_one.value():
        time.sleep_ms(20)
        if not button_one.value():
            print('lyset går med klokka')
            time.sleep(0.5)
            med_klokka(speed_b_one)
            if speed_index_one < 4:
                speed_index_one += 1
            speed_b_one = speed_b_one / 2
            time.sleep(0.5)
            
    if not button_two.value():
        time.sleep_ms(20)
        if not button_two.value():
            print('lyset går mot klokka')
            time.sleep(0.5)
            mot_klokka(speed_b_two)
            if speed_index_two < 4:
                speed_index_two += 1
            speed_b_two = speed_b_two / 2
            time.sleep(0.5)
            
    if not button_reset.value():
        time.sleep_ms(20)
        if not button_reset.value():
            print('reseter hastighet')
            speed_b_two = 1
            speed_b_one = 1
            speed_index_one = 0
            speed_index_two = 0
            time.sleep(0.5)
            
    
    
