# GPIO                                                                                    
Dans cette partie on va voir comment utiliser la led et le bouton poussoir. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code.

## LED                                                                 
Avec le programme : [Kit_LED](Kit_LED.py), on fait clignoter une led toutes les 0.5 secondes indéfiniment. Pour cela, on configure la pin utilisé par la led (ici 16) comme sortie et on fait clignoter la led en boucle toutes les 0.5 sec à l'aide du while et du sleep.

Pour que la led soit allumée ou éteinte il faut que l'état de la led soit à 1 ou 0 et pour changer cette état on utilise led.toggle() qui permet de changer l'état (donc si la led est à 1, elle passera à 0 et inversément).


## Bouton                                                           
Avec le programme : [Kit_LED_and_Button](Kit_LED_and_Button.py), on utilise un bouton pour allumer une led ou l'éteindre. Il suffit d'appuyer une fois pour changer l'état de la led. Pour cela, on met dans une boucle while pour regarder constament la valeur du bouton à l'aide de la méthode ".value" et quand on appuyera sur le bouton, sa valeur va passer de 0 à 1 et le programme pourra executer ce qu'il y a dans le if pour changer l'état de la led.                   

