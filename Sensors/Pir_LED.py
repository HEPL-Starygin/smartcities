from machine import Pin #on importe Pin de la librairie machine pour pouvoir utiliser les Pin
from utime import sleep #on importe sleep de la librairie utime

Pir = Pin(18, Pin.IN)   #on configure la pin 18 comme entrée
led = Pin(16,Pin.OUT)   #on configure la pin 16 comme sortie
while True:
    if Pir.value() == 1:    #rentre dans le if lorsqu'on détecte un mouvement
        led.value(1)        #on éteint la led
        sleep(10)           #on stop le programme pendant 10sec
    else:
        led.value(0)        #on éteint la led