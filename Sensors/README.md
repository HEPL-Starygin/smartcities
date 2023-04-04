# Sensors                                                             

Dans cette partie on va voir comment utiliser les différents capteurs. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code. 

## Capteur température et humidité  

On se sert du "Grove - Temperature & Humidity Sensor" comme capteur et c'est un DHT11.

Avec le programme : [Kit_Temperature_and_Humidity_LCD](Kit_Temperature_and_Humidity_LCD.py), on affiche toute les 0.8 secondes sur un LCD la température et le taux d'humidité ambiant à l'aide du capteur DHT11 qui nous envoie les données.                                                 
Pour la partie [LCD](https://github.com/HEPL-Starygin/smartcities/tree/main/LCD), c'est le même fonctionnement qui ont été fait dans la section LCD. Pour la partie avec les capteurs il faut importer sa bibliothèque "dht11", puis on assigne le capteur à la pin qu'on veut (ici 18) et dans le while on lit toute les 0.8 secondes la valeur de la température et de l'humidité à l'aide de "dht.readTempHumid()". il suffit plus que de transformer les valeurs en string pour les afficher sur le LCD.                                                                               
 

https://user-images.githubusercontent.com/124890653/229843489-3b398601-8484-4e74-9d94-464bdbb14b51.mp4


## ALarme                                                                                  

Avec le programme : [Alarm_temp_or_hum](Alarm_temp_or_hum.py), on fait exactement la même chose que le programme précèdent sauf qu'ici on rajoute le buzzer sur la pin 16 et on demande de faire fonctionner le [buzzer](https://github.com/HEPL-Starygin/smartcities/tree/main/AD-PWM) si il fait plus de 30°C ou il y a moins de 30% d'humidité lu par le capteur. On fait cela à l'aide de if dans le while pour pouvoir lire la valeur toute les 0.8 secondes. (Pour la vidéo la température max à été mis à 21.9°C)


https://user-images.githubusercontent.com/124890653/229843503-73bc6ada-d563-4b9b-aa18-86a17cb54f5d.mp4

## Ventilateur automatique en fonction de la température                           
Avec le programme : [temparature_sensing_intelligent_Fan](temparature_sensing_intelligent_Fan.py), on fait exactement la même chose que le 1er programme  sauf qu'ici on rajoute un mini ventilateur qui s'active si il fait plus de 22.8°C.

Pour cela, on lit cette fois ci juste la valeur de la température vu qu'on n'a pas besoin de l'humidité grâce à "dht.readTemperature()". Puis, on regarde toute les 0.8sec si la valeur de la température dépasse les 22.8°C avec un if et si c'est le cas il va rentrer dans le if et allumer le mini ventilateur en mettant un 1 comme valeur à la pin du ventilateur.



https://user-images.githubusercontent.com/124890653/229849684-c24c37fb-729f-49ba-8a65-e5fb9495f161.mp4


## Sound detector
Avec le programme : [Kit_sound](Kit_sound.py), on afficher dans l'IDE la valeur du son obtenue après avoir fais une moyenne car si on affiche juste le son sans moyenne on verra qu'il ne sera pas stable.
Pour pouvoir l'afficher on assigne le capteur à la pin ADC(1) et on lira ces valeurs sous 16 bits non signés à l'aide de Sound_SENSOR.read_u16 qu'on va diviser par 256 pour les prochains code. Toute les 0.2sec on va faire la moyenne de 1000 son obtenu à l'aide d'un for qui va de i à 1000. Puis il ne reste plus qu'à diviser par 1000 la valeur obtenue à la fin et de la print pour l'afficher.




https://user-images.githubusercontent.com/124890653/229855739-93094a1f-fb61-45c5-9551-48639ab733eb.mp4


