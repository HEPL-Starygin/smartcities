from machine import ADC #on importe ADC de la librairie machine pour pouvoir utiliser ADC
from utime import sleep #on importe sleep de la librairie utime

Sound_SENSOR = ADC(1)   #ADC(1) signifie qu'on utilise la Pin A0

while True:
    average = 0         #initialise la variable
    sleep(0.2)          #On stop le programme pendant 0.2 sec
    for i in range (1000):                  #Permet d'additionner 1000 valeurs du son 
                                            #Sound_SENSOR.read_u16() permet d'obtenir la valeur du son sous 16 bits non signé
        sound = Sound_SENSOR.read_u16()/256 #on divise par 256 pour plus tard
        average += sound                    #On addtione avec average chaque valeur obtenue
        
    sound = average/1000                    #on fait la moyenne du son obtenu 
    print(sound)                            #on affiche la valeur de la moyenne