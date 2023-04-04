# Projet Smartcities
Dans ce github on va voir comment utiliser les différents composants qui sont présents dans le Grove Starter Kit of Raspberry Pi Pico. Afin d'utiliser ces composants on se servira d'un Raspberry Pi Pico W qui sera connecté au shield Grove où on fera du microPython à l'aide de l'IDE Thonny.

Lien vers les sous-répertoires pour le projet :                                                                                                                                 
- [GPIO](GPIO) : LED simple, bouton-poussoir, interruption.                                                                                        
- [AD-PWM](AD-PWM) : lecture du potentiomètre, PWM (LED, musique, servo).                                                                           
- [LCD](LCD) : utilisation d'un écran LCD et affichage de certaines valeurs.                                              
- [LED_neo](LED_neo) : utilisation des LEDs néopixel.                                     
- [Sensors](sensors) : DHT11(température et humidité), microphone, luminosité et PIR.                                              
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

## MicroPython                                                                 
MicroPython est un langage de programmation qui provient du langage de programmation Python 3  mais en version plus légère et efficace et elle inclut un petit sous-ensemble de la bibliothèque standard Python et est optimisée pour fonctionner sur des microcontrôleurs.   

Pour l'utiliser sur le Raspberry Pico W, il faut connecter le Raspbeery sur le PC tout en restant appuyé sur le bouton boot du Raspberry et le dossier du périphérique va s'ouvrir sur votre PC (si ce n'est pas le cas vous pouvez y accéder depuis vos dossiers). Puis, il faut ouvrir le fichier "INDEX.HTM" qui va ouvrir un site et sur ce il faut télécharger le Micropyhton et de le glisser dans le fichier du Raspberry.

## Thonny
Thonny un IDE (environnement de travail) qui est facile à utiliser pour programmer sous le langage Python ou Micropython dans notre cas. Il est aussi facile à télécharger et à mettre en place pour un usage rapide.         

Pour utiliser MicroPython sur cette IDE, il suffit d'aller dans Tools->Options->Interpreter et choisir MicroPython (Raspberry Pi Pico).

## Grove 
Pour chaque composants qu'on utilise dans les différents programme viennent  du [Grove Starter Kit of Raspberry Pi Pico](https://www.seeedstudio.com/Grove-Starter-Kit-for-Raspberry-Pi-Pico-p-4851.html). Dans le kit on retrouve aussi le Grove shield où on peut connecter le raspberry via les pins, ce shield sert à faciliter le branchement entre les composants et le Raspberry Pi Pico W.
