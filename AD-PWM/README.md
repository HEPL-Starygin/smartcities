# AD-PWM                                                                                                                                
Dans cette partie on va voir comment utiliser le poteniomètre, les PWM et le buzzer pour faire une musique. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code.

## PWM                                                                     
Une PWM est un signal d'impulsion qui est un signal numérique. Ce signal n'a que 2 états, il passe uniquement entre l'état bas et l'état haut (comme on peut le voir sur l'image).                      
Le signal PWM est défini par 3 composants : cyle, duty cycle et fréquence. Le cycle est la période pour que le signal d'impulsion passe par l'état haut à l'état bas. Le duty cycle montre le pourcentage de temps où il reste à l'état haut (sur l'image, on voit en haut qu'il est de 50% et en bas de 10%). Et la fréquence montre le nombre de cycle par seconde.              
À partir du signal PWM on peut en faire un signal analogique en changeant le duty cycle de la PWM. Par exemple sur l'image on peut voir qu'on arrive à faire varier la luminosité de la Led en fonction du duty cycle, lorsque le duty cycle est faible la luminsoité de la Led est faible et plus on augmente le duty cycle plus la led sera brillante (voir sous-titre "Changement de luminosité de la Led" pour le fonctionnement).

![pwm](https://user-images.githubusercontent.com/124890653/224550594-1cd5d8bb-d064-4920-bc4b-c0aac1371a16.png)


## Potentiomètre
Avec le programme : [Kit_Potentiomètre](Kit_LED.py), on lit les valeur de la pin A0 (où est connecté le potentiomètre) indéfinement à l'aide de la boucle while. Pour lire ces valeurs on utilise "read_u16" qui permet de lire la valeur analogue entre 0 et 65535 car c'est en 16 bits non signé. Puis, avec "print" on affiche dans la console la valeur lue. On fait ca en boucle toute les 500ms avec sleep_ms qui stoppe le programme.

## Allumer une Led à l'aide d'un potentiomètre                                     
Avec le programme : [Kit_LED_and_Potentimetre](Kit_LED_and_Potentimetre.py), à l'aide d'un if et d'un else, on demande d'allumer la led si la valeur du potentiomètre dépasse 30000. Sinon le fonctionnement est le même que le programme précédent pour le potentiomètre et aussi pour la Led avec le programme de la rubrique [GPIO](https://github.com/HEPL-Starygin/smartcities/tree/main/GPIO).

## Changement de luminosité de la Led
Avec le programme : [Kit_LED_and_Potentimetre_brightness](Kit_LED_and_Potentimetre_brightness.py), on met la Pin 16 (où est connecté la Led) en mode PWM pour pouvoir modifier la luminosité en fonction de la tension envoyé et on connecte le potentiomètre à la pin analogue A0. On met aussi une fréquence de 500 à la PWM pour que les clignottement de la Led ne soit pas perçu par l'oeil.                                                                                                                                        

Avec une boucle infinie, on lit constamment la valeur du potentiomètre sous 16 bits et c'est la valeur de ce potentiomètre qui va définir le duty cycle de la PWM qui est aussi sous 16 bits. Donc lorsque la valeur du potentiomètre sera minimum la Led sera éteinte et lorsqu'il sera maximum la Led sera très brillante.
