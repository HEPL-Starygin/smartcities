from ws2812 import WS2812 #on importe la libraire qui permet d'utiliser la led RGB
from utime import sleep   #on stop le programme pendant 0.5sec

#Variable pour chaque couleur
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,150,0)
GREEN = (0,255,0)
CYAN = (0,255,255)
BLUE = (0,0,255)
PURPLE = (180,0,255)
WHITE = (255,255,255)
MINE = (7,26,149) #Couleur faite par moi

#On stock toutes les couleurs dans un 9-tuples
COLORS = (BLACK,RED,YELLOW,GREEN,CYAN,BLUE,PURPLE,WHITE,MINE)

led = WS2812(18,1) #18 pour la pin et 1 pour le nombre de led
led.brightness=1 #Permet de choisir la luminosité

#Montre toute les couleurs
while True:
    for color in COLORS:     
        led.pixels_fill(color)#Met la couleur de la led sélectionné
        led.pixels_show()     #affiche la couleur
        sleep(0.2)            #On stop le programme pendant 0.2 sec
        
