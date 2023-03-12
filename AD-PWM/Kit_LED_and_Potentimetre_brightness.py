# Varying LED luminosity
from machine import Pin, PWM, ADC   #on importe Pin, ADC et PWM de la librairie machine pour pouvoir utiliser les Pin, ADC et PWM
import utime                        #on importe sleep de la librairie utime


pwm = PWM(Pin(16))                  #On met la Pin 16 en mode PWM
pwm.freq(500)                       #fréquence assez élevée pour pas percevoir les clignotement à l'oeil humain

# variation manuelle
pot = ADC(0)                        #ADC(0) signifie qu'on utilise la Pin A0
while True:                         #boucle infinie
    pwm.duty_u16(pot.read_u16())    #Permet de sortir la valeur analogique dans la Led
    
# # variation linéaire
# while True:
#     for i in range(20):
#         pwm.duty_u16(i*3276)       #on va jusque i=20 car c'est sur 16bits=65535
#         utime.sleep_ms(100)
    
# # variation quadratique
# lum=[]
# for i in range(20):
#     lum.append(i*i)
#     
# while True:
#     for i in range(20):
#         pwm.duty_u16(i*181)
#         utime.sleep_ms(100)