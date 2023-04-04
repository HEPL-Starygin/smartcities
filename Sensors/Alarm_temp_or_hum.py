from machine import I2C,Pin,ADC,PWM #on importe I2C, ADC, PWM et Pin de la librairie machine pour pouvoir utiliser les I2C, ADC, PWM et Pin
from lcd1602 import LCD1602         #on importe la librairie qui permet d'utiliser le LCD
from dht11 import *                 #on importe * de la librairie dht11
from utime import sleep             #on importe sleep de la librairie utime

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)             #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne
d.display()                         #active l'affichage du LCD
  
dht = DHT(18)                       #Attribution de la pin pour le capteur de température et humidité
buzzer = PWM(Pin(16))               #On met la Pin 16 en mode PWM


while True:
    temp,humid = dht.readTempHumid()#stock la valeur des capteurs dans temp et humid
    sleep(0.8)                      #stop le programme pendant 0.8s
    d.clear()                       #efface l'affichage du LCD
    d.setCursor(0, 0)               #Met la postion de l'affichage au 1ère caractère et 1ère ligne
    d.print('Temp: '+str(temp))     #Affiche le mot "Temp" et est suivi de la valeur de la température
    d.setCursor(0, 1)               #Met la postion de l'affichage au 1ère caractère et 2ème ligne
    d.print('Humid: '+str(humid))   #Affiche le mot "Humid" et est suivi de la valeur de la humidité
    
    if temp>30 or humid<30:         #rentre dans le if si temp>30 ou que humid<30
        buzzer.freq(1000)           #Il fera un son d'une fréquence de 1000
        buzzer.duty_u16(1000)       #Permet de choisir le volume
    else:
        buzzer.duty_u16(0)          #Éteint le son du buzzer