# Sensors                                                             

Dans cette partie on va voir comment utiliser les différents capteurs. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code. 

## Catpeur température et humidité  

On se sert du "Grove - Temperature & Humidity Sensor" comme capteur et c'est un DHT11.

Avec le programme : [Kit_Temperature_and_Humidity_LCD](Kit_Temperature_and_Humidity_LCD.py), on affiche toute les 0.8 secondes sur un LCD la température et le taux d'humidité ambiant à l'aide du capteur DHT11 qui nous envoie les données.                                                 
Pour la partie [LCD](https://github.com/HEPL-Starygin/smartcities/tree/main/LCD), c'est le même fonctionnement qui ont été fait dans la section LCD. Pour la partie avec les capteurs il faut importer sa bibliothèque "dht11", puis on assigne le capteur à la pin qu'on veut (ici 18) et dans le while on lit toute les 0.8 secondes la valeur de la température et de l'humidité à l'aide de "dht.readTempHumid()". il suffit plus que de transformer les valeurs en string pour les afficher sur le LCD.
