# AD-PWM                                                                                                                                
Dans cette partie on va voir comment utiliser le poteniomètre, les PWM et le buzzer pour faire une musique. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code.

## PWM                                                                     
Une PWM est un signal d'impulsion qui est un signal numérique. Ce signal n'a que 2 états, il passe uniquement entre l'état bas et l'état haut (comme on peut le voir sur l'image).                      
Le signal PWM est défini par 3 composants : cyle, duty cycle et fréquence. Le cycle est la période pour que le signal d'impulsion passe par l'état haut à l'état bas. Le duty cycle montre le pourcentage de temps où il reste à l'état haut (sur l'image, on voit en haut qu'il est de 50% et en bas de 10%). Et la fréquence montre le nombre de cycle par seconde.              
À partir du signal PWM on peut en faire un signal analogique en changeant le duty cycle de la PWM. Par exemple sur l'image on peut voir qu'on arrive à faire varier la luminosité de la Led en fonction du duty cycle, lorsque le duty cycle est faible la luminsoité de la Led est faible et plus on augmente le duty cycle plus la led sera brillante (voir sous-titre "Changement de luminosité de la Led" pour le fonctionnement).




## Potentiomètre
Avec le programme : [Kit_Potentiomètre](Kit_Potentiomètre.py), on lit les valeur de la pin A0 (où est connecté le potentiomètre) indéfinement à l'aide de la boucle while. Pour lire ces valeurs on utilise "read_u16" qui permet de lire la valeur analogue entre 0 et 65535 car c'est en 16 bits non signé. Puis, avec "print" on affiche dans la console la valeur lue. On fait ca en boucle toute les 500ms avec sleep_ms qui stoppe le programme.




https://user-images.githubusercontent.com/124890653/224558597-f9624105-a7fe-4ea2-a95c-a9e4ae9802e3.mp4




## Allumer une Led à l'aide d'un potentiomètre                                     
Avec le programme : [Kit_LED_and_Potentimetre](Kit_LED_and_Potentimetre.py), à l'aide d'un if et d'un else, on demande d'allumer la led si la valeur du potentiomètre dépasse 30000. Sinon le fonctionnement est le même que le programme précédent pour le potentiomètre et aussi pour la Led avec le programme de la rubrique [GPIO](https://github.com/HEPL-Starygin/smartcities/tree/main/GPIO).


https://user-images.githubusercontent.com/124890653/224558394-50eab2a3-edfe-48d4-9143-6b5faa070b4b.mp4


## Changement de luminosité de la Led
Avec le programme : [Kit_LED_and_Potentimetre_brightness](Kit_LED_and_Potentimetre_brightness.py), on met la Pin 16 (où est connecté la Led) en mode PWM pour pouvoir modifier la luminosité en fonction de la tension envoyé et on connecte le potentiomètre à la pin analogue A0. On met aussi une fréquence de 500 à la PWM pour que les clignottement de la Led ne soit pas perçu par l'oeil.                                                                                                                                        

Avec une boucle infinie, on lit constamment la valeur du potentiomètre sous 16 bits et c'est la valeur de ce potentiomètre qui va définir le duty cycle de la PWM qui est aussi sous 16 bits. Donc lorsque la valeur du potentiomètre sera minimum la Led sera éteinte et lorsqu'il sera maximum la Led sera très brillante. Dans le programme, il y a aussi une partie en commentaire pour changer la luminosité automatiquement de façon lineaire ou quadratique.


https://user-images.githubusercontent.com/124890653/224558408-b4294ae8-46c0-4176-84ac-da414d31051e.mp4


## Buzzer                                                                        
Avec le programme : [Kit_Buzzer](Kit_Buzzer.py), on met la pin 27 en mode PWM (où est connecté le buzzer). Dans la boucle infinie, on fait constamment jouer les 7 notes de musiques dans l'ordre. Pour pouvoir jouer la note qu'on veut il faut mettre le signal sous une certaine fréquence (on peut retrouver les fréquences de chaque note facilement sur internet). Par exemple si on veut faire un DO, on met la fréquence de la PWM à 1046 et on met un sleep_ms de 500 pour qu'on entende le son pendant 500ms. Le duty cycle ici il permet de changer le volume.


https://user-images.githubusercontent.com/124890653/224558427-42e416e3-7219-4c28-9a4c-5e762658651e.mp4


## Musique  
Avec le programme : [Frere_Jaques](Frere_Jaques.py), on met la pin 27 en mode PWM (où est connecté le buzzer) et on met le volume à 100 pour chaque note. Dans ce programme, au lieu de d'écrire la fréquence, le duty cycle et le sleep pour chaque note d'une musique il y a une fonction pour chaque note. Grâce a ces fonction il suffit d'écrire par exemple DO(0.25) pour entendre le son DO pendant 250ms. Ce qui se passe est quand on écrit DO(0.25) il va exécuter ce qu'il y a dans la fonction DO(utime) et on écrit 0.25 entre parenthèse pour changer la valeur de utime par 0.25 pour le sleep.                                                             
Ainsi, il suffit jsute d'écrire le nom de la note accompagné du temps qu'elle dure entre parenthèse. Et c'est ce qui se passe pour pouvoir jouer la musique Frère Jaque.


https://user-images.githubusercontent.com/124890653/224558433-b3657113-2e4d-40ef-b0ac-ce85886a4e10.mp4


