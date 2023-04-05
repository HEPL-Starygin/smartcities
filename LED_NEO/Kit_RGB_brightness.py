from ws2812 import WS2812 #on importe la libraire qui permet d'utiliser la led RGB
from utime import sleep   #on stop le programme pendant 0.5sec

MINE = (7,26,149) #Couleur faite par moi

#On stock toutes les couleurs dans un 9-tuples

led = WS2812(18,1) #18 pour la pin et 1 pour le nombre de led
led.pixels_fill(MINE)
#augmente la luminosité
while True:
    for br in range(20):              
        led.brightness=0.01 * br      #permet d'augmenter la luminosité
        led.pixels_show()             #affiche la couleur
        sleep(0.1)                    #On stop le programme pendant 0.1sec
    sleep(0.4)                        #On stop le programme pendant 0.1sec
        #diminue la luminosité
    for br in range(20):
        led.brightness= 0.2 - 0.01*br #permet de diminuer la luminosité
        led.pixels_show()             #affiche la couleur
        sleep(0.1)                    #On stop le programme pendant 0
