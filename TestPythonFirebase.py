import time
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

#Creation de la data
data = {'Temperature': 19, 'Humidite': 42, 'Presence': "oui", 'Volet': "ouvert",'Exterieur' : "jour", 'Heure': time.strftime("%H:%M")}
#Envoie de la donnee et recuperation des donnees formater JSON
result = firebase.patch('/data/salle', data)
#Affichage de la donnee Value

data = {'Temperature': 15, 'Humidite': 34, 'Presence': "non", 'Volet': "ferme", 'Exterieur' : "nuit", 'Heure': time.strftime("%H:%M")}

result = firebase.patch('/data/cuisine', data)

data = {'Temperature': 11, 'Humidite': 69, 'Presence': "oui", 'Volet': "ouvert", 'Exterieur' : "jour", 'Heure' : time.strftime("%H:%M")}

result = firebase.patch('/data/chambre', data)
