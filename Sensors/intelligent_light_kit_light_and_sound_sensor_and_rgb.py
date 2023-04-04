from machine import ADC     #on importe ADC de la librairie machine pour pouvoir utiliser AD
from ws2812 import WS2812   #on import WS2812 pour utiliser la led rgb
from utime import sleep     #on importe sleep de la librairie utime

led = WS2812(18,1)          #on met 18 pour la pin et 1 pour le nombre de led
Light_SENSOR = ADC(0)       #ADC(0) signifie qu'on utilise la Pin A0
Sound_SENSOR = ADC(1)       #ADC(1) signifie qu'on utilise la Pin A0

while True:
    average = 0             #initialise la variable
    light = Light_SENSOR.read_u16()/256     #on divise par 256 pour faciliter et car la range value de la led rgb est de 0-255
    
    for i in range (1000): 
        sound = Sound_SENSOR.read_u16()/256 #on divise par 256 car la range value de la led rgb est de 0-255
        average += sound    #On addtione avec average chaque valeur obtenue
        
    sound = average/1000    #on fait la moyenne du son obtenu
    print (light,sound)     #on affiche les valeur du son et de la lumière
    
    if light < 50:          #si light<50 la led devient blanche
        led.pixels_fill((255,255,255))  #met la led blanche
        led.pixels_show()   #affiche la couleur
        sleep(0.1)          #On stop le programme pendant 0.1 sec          
    else:                   #on change la couleur en fonction du son obtenu
        if sound >= 50:     
            led.pixels_fill((255,0,0))  #met la led rouge
            led.pixels_show()
            sleep(1)        #On stop le programme pendant 1 sec
        if sound >= 25 and sound < 50:
            led.pixels_fill((255,255,0))#met la led jaune
            led.pixels_show()  #affiche la couleur
            sleep(1)        #On stop le programme pendant 1 sec
        if sound < 25:   
            led.pixels_fill((0,255,0))  #met la led verte
            led.pixels_show()  #affiche la couleur
            sleep(1)        #On stop le programme pendant 1 sec
