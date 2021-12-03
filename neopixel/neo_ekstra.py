#Importerer alle biblotekene og modulene jeg skal bruke
from machine import Pin
import neopixel
import time

#Setter hvilke pin som neopixelen skal bruke til data
#Setter den til utgang(Pin.OUT) fordi pinnen skal gi data til neopixelen
neo_pin = Pin(2, Pin.OUT)
np = neopixel.NeoPixel(neo_pin, 8)

#variabler som sier hvor lang tid det skal gå før en lysdiode går til neste lysdiode
speed_b_two = 1
speed_b_one = 1
#Setter hvor mange ganger man har trykket på hver av knappene, brukes til å sette farge nå man trykker den samme knappen omigjen
speed_index_one = 0
speed_index_two = 0

#Setter at jeg bruker 3 piner som inngang, siden jeg skal lese data fra knappene
#Sier også at disse er koblet med pull up motstand(Pin.PULL_UP)
button_one = Pin(12, Pin.IN, Pin.PULL_UP)
button_two = Pin(13, Pin.IN, Pin.PULL_UP)
button_reset = Pin(14, Pin.IN, Pin.PULL_UP)

#Funskjon som lager en liste med farger, hvor man enkelt kan varierre lysstyrken
#Funkjsonen returnerer deretter denne listen
def get_color(brightness):
    color = [[brightness, 0, 0],
            [0, brightness, 0],
            [0, 0, brightness],
            [0, brightness, brightness],
            [brightness, brightness, brightness]]
    return color
    

#Fuksjon for hva som skal skje når man trykker knapp 1
#Da starter man en evig loop, hvor en lysdiode lyser en satt tid får den slukker og neste tenner, sånn foresetter det
#Trykker man knappen igjen er denne tiden mindre og i tilegg endres fargen
def med_klokka(speed):
    #Funksjonen vil gjøre så lenge ingen av knappene er tyrykket 
    while button_one.value() == 1 and button_two.value() == 1:
        #En løkke for kjører 8 ganger, hvor i begynner som 0 og slutter som 7, +1 hver gang løkken kjører 
        for i in range (0, 8):
            #Variabel som sier hva lysstyrken skal være, standaren er 16
            brightness = 16
            #Når i er lik 1, vil første for løkken gjøre at alle lysdiodene sette til av 0, 0, 0
            if i == 0:
                for x in range (0, 8):
                    np[x] = [0,0,0]
                    np.write()
                #Deretter kaller man funkjonen med øsnket lysstyrke, tilbake får man en liste med fargen som skal brukes
                #Tilslutt tenner man den første lysdioden, venter en satt tid, og skrur av lysdioden igjen
                color = get_color(brightness)
                np[i] = color[speed_index_one]
                np.write()
                time.sleep(speed)
                np[i] = [0,0,0]
                np.write()
            #Når i ikke er lik 1, tenner man lysdioden i posjonen til verdien av i
            else:
                color = get_color(brightness)
                np[i] = color[speed_index_one]
                np.write()
                brightness = 0
                #En for løkke hvor løkke får fra 0 og til verdien som er 1 mindre enn i
                #Dette brukes til å tenne lysene bak "hovedlyset", dette gjør at man får en type afterglow effekt
                #I tilegg blir lysstyrken sterkere og sterkere, slik at man får en fade effekt, hvor de lysene som er nærmest
                #hovedlyset er sterkre enn de som er lengere bak 
                for y in range (0, i):
                    brightness += 1
                    color = get_color(brightness)
                    np[y] = color[speed_index_one]
                    np.write()
                #Denne pausen gjør at man kan kontrollere hastigheten til lys rundene
                time.sleep(speed)
        
#Funksjon for hva som skal skjer når man trykker knapp 2
#Denne funskjonen fungerer på akkuratt samme måte som med klokka
#Forsjellen er at lysdiodene her starter på "slutten", altså lysdiode 7 og ender på lysdiode 0
#Dette gjøres ved at man endrer for løkken til å gå fra 7 til 0, istedenfor 0 til 7
def mot_klokka(speed):
    while button_one.value() == 1 and button_two.value() == 1:
        for i in range (7, -1, -1):
            brightness = 16
            if i == 7:
                for x in range (0, 8):
                    np[x] = [0,0,0]
                    np.write()
                color = get_color(brightness)
                np[i] = color[speed_index_two]
                np.write()
                time.sleep(speed)
                np[i] = [0,0,0]
                np.write()
            else:
                color = get_color(brightness)
                np[i] = color[speed_index_two]
                np.write()
                brightness = 0
                for y in range (7, i, -1):
                    brightness += 1
                    color = get_color(brightness) 
                    np[y] = color[speed_index_two]
                    np.write()
                time.sleep(speed)

#En evig loop som kjører helt til den blir avbrutt
while True:
    #Hvis knapp 1 trykkes brukes en pause slik at man ikke gjør noen handling før man har fått god kontakt
    if not button_one.value():
        time.sleep_ms(20)
        #Når knappen trykkes starter man funsjonen mot_klokka
        if not button_one.value():
            print('lyset går med klokka')
            time.sleep(0.5)
            med_klokka(speed_b_one)
            #Det er fire forskjellige farger til forskjellige hastigheter, så lenge man ikke har en hastighet indeks på over 4
            #Vil man få +1 indeks, som betyr en ny farge
            if speed_index_one < 4:
                speed_index_one += 1
            speed_b_one = speed_b_one / 2

            
    #Hvis knapp 2 trykkes brukes en pause slik at man ikke gjør noen handling før man har fått god kontakt       
    if not button_two.value():
        time.sleep_ms(20)
        if not button_two.value():
            print('lyset går mot klokka')
            time.sleep(0.5)
            #Når knappen trykkes starter man funsjonen mot_klokka
            mot_klokka(speed_b_two)
            #Det er fire forskjellige farger til forskjellige hastigheter, så lenge man ikke har en hastighet indeks på over 4
            #Vil man få +1 indeks, som betyr en ny farge
            if speed_index_two < 4:
                speed_index_two += 1
            speed_b_two = speed_b_two / 2
            
    #Når man trykker inn reset knappen vil alle variabler bli satt til sin orginale (start verdi)
    if not button_reset.value():
        time.sleep_ms(20)
        if not button_reset.value():
            print('reseter hastighet')
            speed_b_two = 1
            speed_b_one = 1
            speed_index_one = 0
            speed_index_two = 0
            
    
    

