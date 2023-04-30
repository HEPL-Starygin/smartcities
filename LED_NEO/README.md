#LED_NEO                                                
Dans cette partie on va voir comment utiliser les différents capteurs. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code. 

Si on veut faire la couleur noir, il faut mettre (0,0,0) car les 0 qui sont entre parenthèse permette de choisir la couleur. Le 1er 0 correspond à combien on veut de rouge, le 2ème 0 est pour le vert et le 3ème est pour le bleu, se sont ces 3 couleurs car c'est les 3 couleurs primaires. Et la valeur max qu'on peut mettre pour une couleur est de 255. Donc on peut faire une multitude de couleur en choisissant différentes valeurs de R,G et B.

## Couleurs                                           

Avec le programme : [Kit_RGB](Kit_RGB.py), on change la couleur de la led toutes les 0.2 avec la luminosité au maximum.
Pour cela, il faut importer la librairie "WS2812" pour pouvoir utilsier les fonctions. Ensuite, on met dans une variable pour chaque couleur et on les stock dans une variable "COLORS" comme tuples. Puis, avec "WS2812(18,1)" on configure quelle pin on utilise et le nombre de led qu'on a et avec "led.brightness" on peut choisir la luminosité de 0 à 1. Pour changer de couleurs, on est dans une boucle for qui va mettre chaque couleur de la led qu'on a mis grâce à "led.pixels_fill" puis l'afficher avec "led.pixels_show()" toute les 0.2 sec.


https://user-images.githubusercontent.com/124890653/230111179-7dede5d7-64e8-478e-b325-df01f70dcda3.mp4

#Luminosité 

Avec le programme : [Kit_RGB_brightness](Kit_RGB_brightness.py), on augmente petit à petit la luminosité puis on la diminue petit à petit et ca en boucle.
Pour cela, le fonctionnement est le même que le programme précèdent sauf qu'ici on utilise qu'une seul couleur. On va faire tourner en boucle 2 boucle for avec une boucle while, dans la 1ère boucle for, on commence la luminosité par 0 puis on augmente par 0.01xbr (br qui va de 0 à 19) puis dans la 2ème boucle for, on commence la luminosité par 0.2 et on diminue par 0.01xbr (br qui va de 0 à 19).

https://user-images.githubusercontent.com/124890653/230112802-05ce552a-6533-4b07-a7f9-595b9fcdfcd9.mp4

## Intelligent light 1                                
Cette partie à déjà été écrite [ici](https://github.com/HEPL-Starygin/smartcities/tree/main/Sensors)

## Intelligent light 2

Avec le programme : [intelligent_light_kit_light_and_PIR_and_rgb](intelligent_light_kit_light_and_PIR_and_rgb.py), on allume la lumière de la led lorsqu'il y a detection de mouvement avec le PIR puis fais une moyenne de 5 valeur capté par le detecteur de lumière enregistré dans une liste car la valeur varie trop. Après, on augmente/diminue la valeur de luminosité par pas de 0.01 pour qu'elle s'allume/s'éteint petit à petit au lieu de passer à par exemple de 10% de luminosité à 100% d'un coup ou l'inverse.                                                                                                

Dans la vidéo on se rend pas trop compte de la  différence de luminosité (j'ai éteint la lumière et utilisé la lumière de la led pour augmenter la valeur lue par le capteur de lumière car ca se voyait mieux en vidéo)


https://user-images.githubusercontent.com/124890653/235371460-a009dedf-0b03-402f-b500-05016e9388a9.mp4

