from machine import I2C,Pin,RTC  #on importe I2C, RTC et Pin de la librairie machine pour pouvoir utiliser les I2C, RTC et Pin
from lcd1602 import LCD1602  #on importe la librairie qui permet d'utiliser le LCD
from utime import sleep      #on importe sleep de la librairie utime
     
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)      #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne;
d.display()                  #active l'affichage du LCD
while True:
    sleep(1)                     #stop le programme pendant 1s
    d.clear()                    #efface l'affichage du LCD
    d.print('Date: ')
    d.print(str(RTC().datetime()[1]) +"/" + str(RTC().datetime()[2]) +"/" + str(RTC().datetime()[0]))     #Affiche la date à partir de la ligne 0 et caractère 0
    d.setCursor(0, 1)            #Met la postion de l'affichage au 1er caractère et 2ème ligne
    d.print('Temps: ')            
    d.print(str(RTC().datetime()[4]) +"h" + str(RTC().datetime()[5]) +"m" + str(RTC().datetime()[6])+"s") #Affiche l'heure, les minutes et les secondes à la position de la précèdente ligne
