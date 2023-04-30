# File: owm_picow.py
# Demo program to connect to openweathermap.org using a WiFi connection
# on Raspberry Pi Pico W and to retreive and parse data using the openweather API.
# API : https://openweathermap.org/current
# info@pcamus.be
# 23/11/2022

import urequests, network #on importe les librairie network et urequests
from secrets import *     #on importe la librairie secrets
import utime              #on importe la librairie utime

wlan = network.WLAN(network.STA_IF) #Creer un objet WLAN et l'initialise
wlan.active(True)                   #Permet d'activer la connexion
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"]) #se connecte à un wifi en utilisant ssid et WiFi_pass
                                                         #qui sont dans la librairie secrets

print("Connection to WiFi network.")
print("---------------------------")
print("Trying to connect to WiFi...")
print()

# Attend pour la connexion ou quitte avec une erreur si la connexion échoue
retry = 10                    #initialise la variable retry avec 10 comme valeur pour avoir 9 essaie dans le while 
while (retry > 0):
    wlan_stat=wlan.status()   #Permet d'avoir l'état actuel de la connexion WiFi
    if wlan_stat==3:                                #Si l'état vaut 3 on a l'IP
        print("Got IP")
        break
    if wlan_stat==-1:                               #Si l'état vaut -1, la connexion a echoué            
        raise RuntimeError('WiFi connection failed')
    if wlan_stat==-2:                               #Si l'état vaut -2, l'AP n'a pas été trouvé
        raise RuntimeError('No AP found')    
    if wlan_stat==-3:                               #Si l'état vaut -3, on s'est trompé dans le mot-de-passe
        raise RuntimeError('Wrong WiFi password')
    
    if wlan.status() < 0 or wlan.status() >= 3:
        break                                       #sort de la boucle while car la connexion ne marche pas
    retry = retry-1                                 #Décrémentre retry de 1
    utime.sleep(1)

if wlan_stat!=3:                                    #Si on sort du while et que la connexion ne marche pas, il envoue un message d'erreur
    raise RuntimeError('WiFi connection failed')


print()
print('Connected to WiFi network: ',end="")
print(wlan.config("ssid"))
print()

# On peut maintenant utiliser la connexion pour avoir accès à internet.

# URL de base pour utiliser l'API de openweathermap
root_url = "http://api.openweathermap.org/data/2.5/weather?"

# prend l'url de base et rajoute des parametre qu'on veut pour pouvoir avoir les informations
url=root_url+"lat="+my_secrets["lat"]+"&lon="+my_secrets["lon"]+"&appid="+my_secrets["OWM_API_key"]+"&units="+my_secrets["units"]
r = urequests.get(url) # Envoie une requête HTTP get à l'URL et stock les données reçus dans "r"

dict=r.json() #convertit les données reçus de la réponse de l'HTTP en JSON
              #et stock la valeur dans un dictionnaire

#Stock les valeurs qu'on veut des données reçus dans des variables
temp=float((dict["main"]["temp"]))
temp_min=float((dict["main"]["temp_min"]))
temp_max=float((dict["main"]["temp_max"]))
humidity=float((dict["main"]["humidity"]))
pressure=float((dict["main"]["pressure"]))

#Affiche les données qu'on veut
print("Weather forecast from openweathermap.org")
print("----------------------------------------")
print("Location:",dict["name"])
print("Type of weather: ",dict["weather"][0]["main"])
print("Current temperature: ",round(temp,1),"°C")
print("Minimum temperature today: ",round(temp_min),"°C")
print("Miaximum temperature today: ",round(temp_max,1),"°C")
print("Relative humidity: ",round(humidity),"%")
print("Atmospheric pressure: ",round(pressure),"hPa")