# File: ntp_access.py
# Get time from NTP server
# See https://docs.micropython.org/en/latest/library/network.WLAN.html for WiFi connection
# See https://docs.micropython.org/en/latest/library/socket.html for socket usage
# See https://docs.python.org/3/library/struct.html for structure management
# info@pcamus.be
# 26/3/2023
from machine import I2C,Pin  #on importe I2C et Pin de la librairie machine pour pouvoir utiliser les I2C et Pin
import network, socket       #on importe les librairie network et socket
import struct                #on importe la librairie struct
from secrets import *        #on importe la librairie secrets 
import utime                 #on importe la librairie utime

# Offset = permet de choisir la différence de temps entre UTC et notre région en seconde, il faut un offset = 7200 car on est UTC+2
# DTS = 0 ou 1 en fonction du changement d'horaire, pour ce programme on est à 1, si on est à 0 on aurati été à UTC+1

# delta est la differnece entre 1.1.1970 et 1.1.1900, cela permet de bien synchroniser avec le temps UTC de notre ordi
# c'est reliré à comment le datetime à été codé dans NTP et
# la façon de comment le UNIX date utilisé dans python est codé
def get_time(offset=7200, delta=2208988800, host="pool.ntp.org"): #se connecte au serveur NTP avec "pool.ntp.org"
    NTP_QUERY = bytearray(48)                                     #crée un tableau de bytes et définit le 1er octet avec 0x1B
    NTP_QUERY[0] = 0x1B # c'est la version :3 et le mode :3 du protocole NTP
    
    # Resolution du nom du serveur
    addr = socket.getaddrinfo(host, 123)[0][-1] # 123 est le numéro de port pour le NTP
    # getaddrinfo() retourne l'adresse IP de l'hôte et d'autres informations
    # sous la forme d'une liste de 5-tuples, le dernier tuple [-1] contient
    # un tuple avec l'adresse IP en un string et numéro de port en entier
    
    # Créer un socket (= connexion à un service) sur le seveur NTP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP/IP
    
    try:
        s.settimeout(1)                 # Met une limite d'attente de 1 sec pour les opération sur le socket
        res = s.sendto(NTP_QUERY, addr) # Envoie une requete vide au serveur NTP avec "addr" où se trouve l'IP du serveur
                                        # et avec les champ LI, VN & MODE vide qui sont dans "NTP_QUERY"
        msg = s.recv(48)                # Recois la réponse jusqu'à 48 bytes max
    finally:
        s.close()                       # Ferme la connexion du socket 
    
    val = struct.unpack("!I", msg[40:44])[0] # extrer la donnée de l'entier, encodé en big endian
    # msg[40:44] contient la partie de l'entier du temps de transfer.
    t = val - delta # convertit depuis le format de temps NTP en type Python (Unix)    
    tm = utime.gmtime(t+offset) # ajoute un offset selon la timezone où on se trouve
    return tm  # année mois, jour, heure, minute, seconde, jour de la semaine (0-6), jour de l'année)


#connexion au WiFi 
wlan = network.WLAN(network.STA_IF) #Creer un objet WLAN et l'initialise 
wlan.active(True)                   #Permet d'activer la connexion
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"])  #se connecte à un wifi en utilisant ssid et WiFi_pass
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

t_now=get_time() # Utilise le protocole NTP pour obtenir la date et l'heure.
print("Time is: {:2d}:{:02d}:{:02d}".format(t_now[3],t_now[4],t_now[5]))

#Partie affichage sur LCD

from lcd1602 import LCD1602  #on importe la librairie qui permet d'utiliser le LCD

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) #on définit la pin (voir github)
d = LCD1602(i2c, 2, 16)      #i2c définit le type de données, 2 = le nombre de ligne = 16 le nombre de caratère par ligne;
d.display()                  #active l'affichage du LCD
i = 0

for i in range (5):
    t_now=get_time()
    d.clear()                    #efface l'affichage du LCD
    d.print('Date: ')
    d.print(str(t_now[2]) +"/" + str(t_now[1]) +"/" + str(t_now[0]))     #Affiche la date à partir de la ligne 0 et caractère 0
    d.setCursor(0, 1)            #Met la postion de l'affichage au 1er caractère et 2ème ligne
    d.print('Temps: ')            
    d.print(str(t_now[3]) +"h" + str(t_now[4]) +"m" + str(t_now[5])+"s") #Affiche l'heure, les minutes et les secondes à la position de la précèdente ligne
    utime.sleep(1)              #stop le programme pendant 60s
# ferme la connexion
wlan.disconnect()