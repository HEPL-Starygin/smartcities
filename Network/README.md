# Network                                                               
Dans cette partie on va voir comment se connecter à un WIFI et comment récupérer les donnéees d'une API et afficher ces valeurs. Dans les fichiers .py, il y aura la description de ce que fais chaque ligne de code. 

## Librairie secrets                                                              
Dans cette partie on utilise la librairie [secrets](secrets.py) qui nous permet de rentrer les valerus de la latitude et longitude qu'on veut. Mais c'est surtout pour rentrer notre clé API de OpenWeatherMap et mettre le mot-de-passe du wifi + le wifi utilisé.        

## NTP                                                                               

Avec le programme : [NTP](NTP.py), on se connecte au wifi qu'on a sélectionné dans "secrets" et renvoie un message de confirmation si ça a marché et dans l'autre cas il renvoie un message d'erreur. Puis, il affiche l'adresse IP, le mask, le gateway et le DNS du réseau. Si la connexion est établit, on utilise la definition du début pour obtenir, via le wifi, l'heure UTC+2 avec NTP et on le print pour voir si c'est juste. À la fin, on utilise le [LCD](https://github.com/HEPL-Starygin/smartcities/tree/main/LCD) pour pouvoir afficher la date et l'heure dessustoute les minutes.

Attention au changement d'heure, il ne se fait pas automatiquement. Si on est en hiver, on est en UTC+1 et faudra mettre un offset de 1h soit 3600sec alors qu'avec l'heure d'été on est à UTC+2 et on a un offset de 2h soit 7200sec.

## OpenWeatherMap

OpenweatherMap est une API où l'on peut faire 1000 requête gratuitement par jour pour recevoir la météo d'un endroit spécifique (région,pays ou même selon la longitude et latitude).

Avec le programme : [openweathermap_wifi](openweathermap_wifi.py), le fonctionnement pour se connecter via le wifi est pareil que le code précédent. Dans ce prograramme, on se sert de l'URL de base du site pour avoir les données puis on lui rajoute des paramètres pour spécifier la météo de quelle région on veut et sélectionner quelle type de données on veut (metric) et il faut rajouter aussi sa clé pour pouvoir avoiraccès aux données. Ensuite, on envoie une requête à cette URL pour recevoir les données de la météo qu'on mettra dans un dictionnaire pour se faciliter. Et on affiche à la fin les données que l'on souhaite.
