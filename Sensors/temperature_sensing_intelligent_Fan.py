from lcd1602 import LCD1602     #on importe la librairie qui permet d'utiliser le LCD
from dht11 import *             #on importe * de la librairie dht11
from machine import I2C,Pin,ADC #on importe I2C, ADC et Pin de la librairie machine pour pouvoir utiliser les I2C, ADC et Pin
from utime import sleep         #on importe sleep de la librairie utime

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)         #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne
d.display()                     #active l'affichage du LCD

dht = DHT(18)                   #Attribution de la pin pour le capteur de température et humidité
miniFan = Pin(16,Pin.OUT)       #On met la Pin 16 comme sortie pour le ventilo

while True:
    temp = dht.readTemperature()#stock la valeur du capteur dans temp
    sleep(0.8)                  #stop le programme pendant 0.8s
    d.clear()                   #efface l'affichage du LCD
    d.setCursor(0, 0)           #Met la postion de l'affichage au 1ère caractère et 1ère ligne
    d.print('Temp: '+str(temp)) #Affiche le mot "Temp" et est suivi de la valeur de la température
    
    if temp>22.8:                 #Si la temp>21.5 on met en marche le ventilo
        miniFan.value(1)          #On active le ventilo en mettant un 1
    else:
        miniFan.value(0)          #On desactive le ventilo en mettant un 0

    
