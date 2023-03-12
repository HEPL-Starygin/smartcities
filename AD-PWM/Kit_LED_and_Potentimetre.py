from machine import ADC,Pin     #on importe ADC et Pin de la librairie machine pour pouvoir utiliser les ADC et Pin
import utime                    #on importe sleep de la librairie utime

pot = ADC(0)                    #ADC(0) signifie qu'on utilise la Pin A0
led = Pin(16, Pin.OUT)          #on configure la pin 16 comme sortie (la où est connecté la led)

while True:                     #boucle infinie
    print(pot.read_u16())       #On affiche la valeur du potentiomètre dans la console
    if pot.read_u16() > 30000:  #Si la valeur du potentiomètre est plus grand que 30000 on allume la led
        led.value(1)            #Permet d'allumer la Led en mettant l'état de la Led à 1
        utime.sleep_ms(500)     #On stoppe le programme pendant 500 ms
    else:                       #Si la valeur du potentiomètre est plus petit que 30000 on éteint la led
        led.value(0)            #Permet d'éteindre la Led en mettant l'état de la Led à 0
        utime.sleep_ms(500)     #On stoppe le programme pendant 500 ms
    
    