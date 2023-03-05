# LED Blink
from machine import Pin #on importe Pin de la librairie machine pour pouvoir utiliser les Pin
from utime import sleep #on importe sleep de la librairie utime pour stopper notre programme pendant x secondes

led = Pin(16, Pin.OUT) #on configure la pin 16 comme sortie (la où est connecté la led)

while True:            #on fait une boucle infinie
    led.toggle()       #change l'état de la led
    sleep(0.5)         #on arrête le programme pendant 0.5sec
    





