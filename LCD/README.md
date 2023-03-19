# LCD
Dans cette partie on va voir comment utiliser l'écran LCD. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code.                                   

## Description afficheur LCD                                                     

Les afficheurs LCD (Liquid Crystal Display) utilisent des cristaux liquides pour pouvoir afficher des images, du texte (pour nous). Lorsque ces cristaux liquides sont affectés par un champ électrique les molécules vont changer de direction, ainsi ça va changer l'indice de réfraction du cristal liquide et va changer la direction par où passe la lumière. L'affichage final sur l'afficheur peut être déterminé tant qu'il y a un polariseur pour filtrer la lumière indésirable. Dans un écran LCD, on a aussi besoin d'un rétro-éclairage qui servira comme source de lumière pour pouvoir afficher.                                                      
On se sert du "The Grove - 16 x 2 LCD" comme écran LCD, il permet dafficher 16 caractères par ligne et il y a 2 lignes. Chaque caractère est composée de 5 colonnes et 8 lignes de carré, ce sont ces carrées qu'on allume ou pas pour pouvoir afficher ce que l'on veut sur le caractère.

## Description des méthodes du modules lcd1602.py                                             
Dans le module [lcd1602](lcd1602.py), on retrouve plusieurs méthodes dans les classes LCD1602 et LCD1602_RGB :
- init() : Il prend les paramètre de l'I2C, du nombre de ligne et le nombre de caractères.
- clear(): Il efface l'affichage et postitionne le curseur à 0.
- home(): Il remet la postion du curseur à 0.
- setCursor(): Il permet de choisir la position du curseur avec la ligne et la colonne.
- no_display()/display(): Il permet de désactiver/activer l'affichage.
- no_cursor()/cursor(): Il permet de désactiver/activer le curseur.
- no_blink()/blink() : Il permet de désactiver/activer le clignotement du curseur.
- autoscroll()/no_autoscroll() : Il permet de désactiver/activer le défilement automatique.     
- createChar(): Il permet de créer un caractère spécial.
- command() : Il permet d'envoyer une commande à l'afficheur LCD.
- write():  Il permet d'écrire un caractère grâce à la valeur qu'on met.
- print(): Il permet d'afficher du texte sur l'afficheur LCD.
- set_reg(): Il permet d'écrire une valeur dans un registre spécifique.
- set_rgb(): Il permet de régler la couleur du rétro-éclairage en choisissant les valeurs RGB.
- setColor(): Il permet de choisir la couleur du rétr-éclairage parmi 4 couleur.

## Affichage sur un LCD                                                         

Avec le programme : [Kit_LCD](Kit_LCD.py), on affiche sur l'écran LCD d'abord Smart au début de la 1ère ligne et cities au 4ème caractère de la 2ème ligne.                     
Pour cela, on utilise un I2C pour la communication entre la Raspberry et le LCD. On configure l'I2C en choisissant la Pin où on connecte le LCD (ici  Pin 1), puis le SCL (ici Pin 7), le SDA (ici Pin 6) et la fréquence qui permet de choisir la fréquence de SCL. Après, il faut définir le type de données du LCD (I2C), le nombre de lignet et de colonne. Ainsi avec tout cela, il suffit de faire d.print pour afficher ce que l'on veut et d.setCursor pour choisir à partir de quel caractère et quelle ligne on veut afficher.

![20230318_215801](https://user-images.githubusercontent.com/124890653/226139713-da42ba8d-a2d8-498e-97ae-ca3fb5e51217.jpg)

## Affichage de la position angulaire d'un potentiomètre sur un LCD                       

Avec le programme : [Kit_LCD_and_Potentiometre](Kit_LCD_and_Potentiometre.py), on affiche sur l'écran LCD d'abord "Angle = " puis la valeur angulaire du potentiomètre à l'aide d'un calcul dans le code et à la fin on affiche "°" pour dire que c'est des degrés.                                      
Pour cela, on fait comme dans le programme précédent pour pouvoir afficher ce que l'on veut sur le LCD. Puis, pour lire les valeurs du potentiomètre et comment ça fonctionne on peut re-utiliser les codes qui sont [ici](https://github.com/HEPL-Starygin/smartcities/tree/main/AD-PWM), pour l'afficher sur le LCD on convertir la valeur lu du potentiomètre en string. Et pour faire un "°" on utilise d.write au lieu de d.print car si on utilise le d.print il convertit le code binaire en décimal mais d.write permet d'envoyer ce code binaire qui correspond au caractère "°". Pour savoir quelle code binaire il faut utiliser, il suffit d'aller voir à la page 14 de ce [pdf](https://www.waveshare.com/datasheet/LCD_en_PDF/LCD1602.pdf) où l'on voit que "°" correspond à "11011111".


https://user-images.githubusercontent.com/124890653/226186901-2806e572-0c65-4941-9b47-3f5c338da656.mp4



