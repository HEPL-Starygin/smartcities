from machine import I2C,Pin,ADC,PWM    #on importe PWM, I2C, ADC et Pin de la librairie machine pour pouvoir utiliser les PWM, I2C, ADC et Pin
from lcd1602 import LCD1602            #on importe la librairie qui permet d'utiliser le LCD
from utime import sleep                #on importe sleep de la librairie utime

pot = ADC(0)                           #ADC(0) signifie qu'on utilise la Pin A0
LED_PWM = PWM(Pin(16))                 #On met la Pin 16 en mode PWM
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)    #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)                #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne
d.display()                            #active l'affichage du LCD

while True:
    LED_PWM.duty_u16(pot.read_u16())   #Permet de sortir la valeur analogique dans la Led
    sleep(0.8)                         #stop le programme pendant 0.8s
    d.clear()                          #efface l'affichage du LCD
    d.setCursor(0, 0)                  #Met la postion de l'affichage au caractère 0 et ligne 0
    d.print('Angle = ')                #Affiche Angle = à partir de la ligne 0 et caractère 0
    d.setCursor(8, 0)                  #Met la postion de l'affichage au 8ème caractère et 1ère ligne
    angle = int((pot.read_u16()/65355)*300) #Vu qu'on lit la valeur sous 16 bits non signés on divise par 65355 puis on multiplie par 300 pour avoir l'angle
    d.print(str(angle))                #Affiche la valeur du potentiomètre à la position de la précédente ligne de code
    d.write(0b11011111)                #Affiche "°" sur le LCD