from machine import Pin, PWM    #on importe PWM et Pin de la librairie machine pour pouvoir utiliser les PWM et Pin
import utime                    #on importe sleep de la librairie utime

buzzer = PWM(Pin(27))           #On met la Pin 16 en mode PWM
while True:                     #boucle infinie
                                #on fait jouer chaque note pendant 500 ms et au volume de 100
    buzzer.freq(1046) #DO       #avec la frequence on peut choisir la note poour faire Do, c'est une fréquence de 1046
    buzzer.duty_u16(100)        #Permet de choisir le volume
    utime.sleep_ms(500)         #Permet de stopper le programme pendant 500 ms
    
    buzzer.freq(1175) #RE
    buzzer.duty_u16(100)
    utime.sleep_ms(500)
    
    buzzer.freq(1318) #MI
    buzzer.duty_u16(100)
    utime.sleep_ms(500)
    
    buzzer.freq(1397) #FA
    buzzer.duty_u16(100)
    utime.sleep_ms(500)
    
    buzzer.freq(1568) #SOL
    buzzer.duty_u16(100)
    utime.sleep_ms(500)
    
    buzzer.freq(1760) #LA
    buzzer.duty_u16(100)
    utime.sleep_ms(500)
    
    buzzer.freq(1967) #SI
    buzzer.duty_u16(100)
    utime.sleep_ms(500)