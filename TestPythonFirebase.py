import time
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

#Creation de la data
data = {'Temperature': 19, 'Humidite': 42, 'Presence': "yes", 'Porte': "open",'Heure': time.strftime("%H:%M:%S")}
#Envoie de la donnee et recuperation des donnees formater JSON
result = firebase.patch('salle', data)
#Affichage de la donnee Value

data = {'Temperature': 15, 'Humidite': 34, 'Presence': "no", 'Porte': "close", 'Heure': time.strftime("%H:%M:%S")}

result = firebase.patch('cuisine', data)

data = {'Temperature': 11, 'Humidite': 69, 'Presence': "yes", 'Porte': "close",'Heure' : time.strftime("%H:%M:%S")}

result = firebase.patch('chambre', data)
