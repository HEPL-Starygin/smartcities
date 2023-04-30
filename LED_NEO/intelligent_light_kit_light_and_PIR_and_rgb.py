from machine import ADC,Pin  #on importe ADC et Pin de la librairie machine pour pouvoir utiliser ADC et Pin
from ws2812 import WS2812    #on import WS2812 pour utiliser la led rgb
from utime import sleep      #on importe sleep de la librairie utime

led = WS2812(18,1)           #on met 18 pour la pin et 1 pour le nombre de led
Light_SENSOR = ADC(0)        #ADC(0) signifie qu'on utilise la Pin A0
Pir = Pin(20, Pin.IN)        #on configure la pin 18 comme entrée
WHITE = (255,255,255)        #configuration de la couleur pour avoir du blanc 
led.pixels_fill(WHITE)       #met la led blanche
led.brightness=0             #met a 0 la luminosité
nombre = 4                   #c'est égal à 4 car on veut faire une moyenne de 5 valeur
previous_light = 0           #initialisation des variables               
mesure_lumiere = []
moyenne = 0

while True:
    
    #on divise par 16 bits en décimal pour qu'on puisse faire varier la luminosité entre 0 et 1, on rajoute +0.1 pour que la led soit au moins allumé et la valeur max que le detecteur a est 0.7
    light = round((Light_SENSOR.read_u16()/65535) + 0.1, 2)  
                                  
    mesure_lumiere.append(light)                 #ajoute la valeur de light à la liste
    if len(mesure_lumiere) > nombre:             #rentre dans le if lorsque light aura 5 valeur pour faire une moyenne
        moyenne = round(sum(mesure_lumiere)/len(mesure_lumiere),2) 
        mesure_lumiere.pop(0)                    #on enleve le 1er élement de la liste pour ne pas au lieu de refaire de 0 la liste
        
    
    if Pir.value() == 1:                         #si on detecte un mouvement la led devient blanche et adapte la luminosité en fonction de la lumiere ambiante
        if moyenne - previous_light > 0.01:      #si la valeur change plus que de 0.01, on augmente la luminosité par pas de 0.01 au lieu de changer directement de valeur
            difference = (moyenne - previous_light)*100
            for i in range(1, difference):
                led.brightness = previous_light + (i/100)  #Change la luminosité en fonction de la luminosité ambiante progressivement
                led.pixels_show()                          #affiche la couleur
                sleep(0.01)
        elif previous_light - moyenne > 0.01:
            difference = (previous_light - moyenne)*100
            for i in range(1, difference):
                led.brightness = previous_light - (i/100)  #Change la luminosité en fonction de la luminosité ambiante progressivement
                led.pixels_show()                          #affiche la couleur
                sleep(0.01)
        else:
            led.brightness= moyenne                        #Change la luminosité en fonction de la luminosité ambiante
            led.pixels_show()                              #affiche la couleur
        sleep(0.1)
        
    else:                                                  #on met la luminsité à 0 si on detecte pas de mouvement
        led.brightness=0
        led.pixels_show()
        sleep(0.1)
    print(moyenne)
    previous_light = moyenne
