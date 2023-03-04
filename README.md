# Projet Smartcities
Le projet Smartcities est 

Lien vers les sous-répertoires pour le projet :                                                                                                                                 
- [GPIO](GPIO) : LED simple, bouton-poussoir, interruption.                                                                                        
- [AD-PWM](AD-PWM) : lecture du potentiomètre, PWM (LED, musique, servo).                                                                           
- [LCD](LCD) : utilisation d'un écran LCD et affichage de certaines valeurs.                                              
- [LED_neo](LED_neo) : utilisation des LEDs néopixel.                                     
- [Sensors](sensors) : température et humidité, luminosité, PIR.                                              
- [Network](network) : Accès réseau avec le RPi Pico.   

## Raspberry Pi Pico W                                                                                                                                                                                                                                        
Le Raspberry Pi Pico W a été conçu pour être une plate-forme de développement à faible coût. C'est un microcontrôleur facile utiliser avec la programmation en utilisant MicroPython. On peut aussi s'en servir avec une connexion sans fil.
![215263828-670ae9c1-3d4e-4bfa-a0dd-d2cfe9a20086](https://user-images.githubusercontent.com/124890653/222923816-5105b172-7b77-4d11-bca6-92ee978b5715.png)                                                                                               
L'image ci-dessus nous montre le shcéma du brochage du Raspberry Pi Pico W, on peut y voir:
- Il y a 40 pins au total.                                                
- Il y a 26 pin GPIO multifonctionnelles de disponibles. Parmi ces pins, il y en 23 qui sont pour le digital et 3 pour l'ADC.                                              
- Il y a 3 pin ARM SWD (debug) port.                                     
- Il y a un micro-USB.    
- Il y a 2 × UART, 2 × I2C, 2 × SPI, 16 × PWM canaux.
- Alimentation 3.3V.                                              

Information complémentaires :           
- 264 Ko SRAM, et 2 Mo de mémoire Flash embarquée.                   
- Utilise une interface sans fil de 2.4GHz (802.11n).

