import time
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

#Creation de la data
data = {'Temperature': 20, 'Humidite': 20, 'Presence': 1, 'Porte': 1, 'Value': '1', 'Type': 'Salle de bain',
        'Heure': time.strftime("%H:%M:%S")}
#Envoie de la donnee et recuperation des donnees formater JSON
result = firebase.patch('/data/chambre1', data)
#Affichage de la donnee Value
print(result['Value'])

data = {'Temperature': 16, 'Humidite': 15, 'Presence': 1, 'Porte': 1, 'Value': '1', 'Type': 'Chambre',
        'Heure': time.strftime("%H:%M:%S")}

result = firebase.patch('/data/chambre2', data)

print(result['Value'])

data = {'Temperature': 10, 'Humidite': 10, 'Presence': 1, 'Porte': 1, 'Value': '1', 'Type': 'Cuisine',
        'Heure' : time.strftime("%H:%M:%S")}

result = firebase.patch('/data/chambre3', data)

print(result['Value'])