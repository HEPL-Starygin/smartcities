# Potentiometer reading    
from machine import ADC  #on importe ADC de la librairie machine pour pouvoir utiliser les ADC
import utime             #on importe sleep de la librairie utime

pot = ADC(0)             #ADC(0) signifie qu'on utilise la Pin A0

while True:             #boucle infinie
    val= pot.read_u16() #u16 => u = unsigned et 16 = 16 bits, vu que c'est 16 bits la valeurs max du potentiometre est de 65535
    print(val)          #on print dans la console la valeur du protentiomètre
    utime.sleep_ms(500) #on utilise sleep_ms de la librairie utime pour stopper le programme pendant 500 ms