# Toggling led with push button and interrupt
from machine import Pin   #on importe Pin de la librairie machine pour pouvoir utiliser les Pin
from utime import sleep   #on importe sleep de la librairie utime pour stopper notre programme pendant x secondes

Button = Pin(18, Pin.IN)  #on configure la pin 18 comme entrée (la où est connecté le bouton)
led = Pin(16, Pin.OUT)    #on configure la pin 16 comme sortie (la où est connecté la led)
val = 0

while True:
    val = Button.value()  #Si le bouton est pressé il sera à un niveau haut et entrera dans le if
    if val == 1:
        led.toggle()      #change l'état de la led
        sleep(0.2)        #Permet de stopper le programme pendant 0.2
                          #pour qu'il ne lise pas la valeur du bouton une 2eme fois

