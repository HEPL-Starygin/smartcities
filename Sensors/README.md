# Sensors                                                             

Dans cette partie on va voir comment utiliser les différents capteurs. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code. 

## Capteur température et humidité  

On se sert du "Grove - Temperature & Humidity Sensor" comme capteur et c'est un DHT11.

Avec le programme : [Kit_Temperature_and_Humidity_LCD](Kit_Temperature_and_Humidity_LCD.py), on affiche toute les 0.8 secondes sur un LCD la température et le taux d'humidité ambiant à l'aide du capteur DHT11 qui nous envoie les données.                                                 
Pour la partie [LCD](https://github.com/HEPL-Starygin/smartcities/tree/main/LCD), c'est le même fonctionnement qui ont été fait dans la section LCD. Pour la partie avec les capteurs il faut importer sa bibliothèque "dht11", puis on assigne le capteur à la pin qu'on veut (ici 18) et dans le while on lit toute les 0.8 secondes la valeur de la température et de l'humidité à l'aide de "dht.readTempHumid()". il suffit plus que de transformer les valeurs en string pour les afficher sur le LCD.                                                                               
 

https://user-images.githubusercontent.com/124890653/229843489-3b398601-8484-4e74-9d94-464bdbb14b51.mp4


## ALarme                                                                                  

Avec le programme : [Alarm_temp_or_hum](Alarm_temp_or_hum.py), on fait exactement la même chose que le programme précèdent sauf qu'ici on rajoute le buzzer sur la pin 16 et on demande de faire fonctionner le buzzer si il fait plus de 30°C ou il y a moins de 30% d'humidité lu par le capteur. On fait cela à l'aide de if dans le while pour pouvoir lire la valeur toute les 0.8 secondes. (Pour la vidéo la température max à été mis à 21.9°C)


https://user-images.githubusercontent.com/124890653/229843503-73bc6ada-d563-4b9b-aa18-86a17cb54f5d.mp4

