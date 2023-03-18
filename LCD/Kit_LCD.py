from machine import I2C,Pin  #on importe I2C et Pin de la librairie machine pour pouvoir utiliser les I2C et Pin
from lcd1602 import LCD1602  #on importe la librairie qui permet d'utiliser le LCD
from utime import sleep      #on importe sleep de la librairie utime

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)      #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne;
d.display()                  #active l'affichage du LCD
sleep(1)                     #stop le programme pendant 1s
d.clear()                    #efface l'affichage du LCD

d.print('Smart')             #Affiche Smart à partir de la ligne 0 et caractère 0
sleep(1)                     #stop le programme pendant 1s
d.setCursor(4, 1)            #Met la postion de l'affichage au 4ème caractère et 2ème ligne
d.print('cities')            #Affiche cities à la position de la précédente ligne de code