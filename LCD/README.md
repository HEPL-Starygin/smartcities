# LCD

## Affichage sur un LCD                                                         

Avec le programme : [Kit_LCD](Kit_LCD.py), on affiche sur l'écran LCD d'abord Smart au début de la 1ère ligne et cities au 4ème caractère de la 2ème ligne.                     
Pour cela, on utilise un I2C pour la communication entre la Raspberry et le LCD. On configure l'I2C en choisissant la Pin où on connecte le LCD (ici  Pin 1), puis le SCL (ici Pin 7), le SDA (ici Pin 6) et la fréquence qui permet de choisir la fréquence de SCL. Après, il faut définir le type de données du LCD (I2C), le nombre de lignet et de colonne. Ainsi avec tout cela, il suffit de faire d.print pour afficher ce que l'on veut et d.setCursor pour choisir à partir de quel caractère et quelle ligne on veut afficher.

![20230318_215801](https://user-images.githubusercontent.com/124890653/226139713-da42ba8d-a2d8-498e-97ae-ca3fb5e51217.jpg)

## Affichage de la position angulaire d'un potentiomètre sur un LCD                       

Avec le programme : [Kit_LCD_and_Potentiometre](Kit_LCD_and_Potentiometre.py), on affiche sur l'écran LCD d'abord "Angle = " puis la valeur angulaire du potentiomètre en 16 bits non signés et à la fin on affiche "°" pour dire que c'est des degrés.                                      
Pour cela, on fait comme dans le programme précédent pour pouvoir afficher ce que l'on veut sur le LCD. Puis, pour lire les valeurs du potentiomètre et comment ça fonctionne on peut re-utiliser les codes qui sont [ici](https://github.com/HEPL-Starygin/smartcities/tree/main/AD-PWM), pour l'afficher sur le LCD on convertir la valeur lu du potentiomètre en string. Et pour faire un "°" on utilise d.write au lieu de d.print car si on utilise le d.print il convertit le code binaire en décimal mais d.write permet d'envoyer ce code binaire qui correspond au caractère "°". Pour savoir quelle code binaire il faut utiliser, il suffit d'aller voir à la page 14 de ce [pdf](https://www.waveshare.com/datasheet/LCD_en_PDF/LCD1602.pdf) où l'on voit que "°" correspond à "11011111".

https://user-images.githubusercontent.com/124890653/226140641-15cf17a6-687b-4f2c-9b6e-ebd3e379a86c.mp4

