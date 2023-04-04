from machine import ADC #on importe ADC de la librairie machine pour pouvoir utiliser ADC
from utime import sleep #on importe sleep de la librairie utime

Light_SENSOR = ADC(0)   #ADC(0) signifie qu'on utilise la Pin A0

while True:

    sleep(0.2)                           #On stop le programme pendant 0.2 sec        
    light = Light_SENSOR.read_u16()/256  #on divise par 256 pour plus tard
    print(light)                         #on affiche la valeur