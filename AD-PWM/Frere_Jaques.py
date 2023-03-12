from machine import Pin, PWM        #on importe PWM et Pin de la librairie machine pour pouvoir utiliser les PWM et Pin
from time import sleep              #on importe sleep de la librairie utime

buzzer = PWM(Pin(27))               #On met la Pin 16 en mode PWM
vol = 100                           #on configue le son (ici on le met à 100)
def DO(utime):                      #On fait une fonction pour chaque note pour pouvoir jouer chaque note plus facilement
    buzzer.freq(1046)               #avec la frequence on peut choisir la note poour faire Do, c'est une fréquence de 1046
    buzzer.duty_u16(vol)            #Permet de choisir le volume
    sleep(utime)                    #Permet de stopper le programme pour choisir le temps de la note
def RE(utime):
    buzzer.freq(1175) 
    buzzer.duty_u16(vol)
    sleep(utime)
def MI(utime):
    buzzer.freq(1318) 
    buzzer.duty_u16(vol)
    sleep(utime)
def FA(utime):
    buzzer.freq(1397) 
    buzzer.duty_u16(vol)
    sleep(utime)
def SOL(utime):
    buzzer.freq(1568) 
    buzzer.duty_u16(vol)
    sleep(utime)
def LA(utime):
    buzzer.freq(1760) 
    buzzer.duty_u16(vol)
    sleep(utime)
def SI(utime):
    buzzer.freq(1967) 
    buzzer.duty_u16(vol)
    sleep(utime)
def N(utime):
    buzzer.freq(1046) #1
    buzzer.duty_u16(vol)
    sleep(utime)
    
while True:                         #Boucle infinie
    DO(0.25)                        #On appelle la fonction et on met combient de temps dure la note entre parenthèse
    RE(0.25)                        #cela va jouer la note sans devoir tout re-écrire de nouveau
    MI(0.25)
    DO(0.25)
    N(0.01)
    
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    
    MI(0.25)
    FA(0.25)
    SOL(0.5)
    
    MI(0.25)
    FA(0.25)
    SOL(0.5)
    N(0.01)
    
    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    SOL(0.125)
    LA(0.125)
    SOL(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)
    
    RE(0.25)
    SOL(0.25)
    DO(0.5)
    N(0.01)
    
    RE(0.25)
    SOL(0.25)
    DO(0.5)