from machine import Pin #on importe Pin de la librairie machine pour pouvoir utiliser les Pin
from utime import sleep #on importe sleep de la librairie utime

Pir = Pin(18, Pin.IN)   #on configure la pin 18 comme entrée

while True:
    sleep(10)           #on stop le programme pendant 10sec
    print(Pir.value())  #on affiche la valeur de du Pir