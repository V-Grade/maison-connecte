import time
from firebase import firebase
from grovepi import *

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

dht_sensor_port = 7
dht_sensor_type = 0
light_sensor = 0

while True:
        try:
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                print("temp =", temp, "C\thumidity =", hum,"%")

        except (IOError,TypeError) as e:
                print("Error")


        try:
        	# Get sensor value
        	sensor_value = grovepi.analogRead(light_sensor)

        	print("sensor_value = %d" %(sensor_value))
        	time.sleep(.5)

    	except IOError:
        	print ("Error")

	#Creation de la data
	data = {'Temperature': temp, 'Humidite': hum, 'Presence': "oui", 'Volet': "ouvert",'Heure': time.strftime("%H:%M:%S")}
	#Envoie de la donnee et recuperation des donnees formater JSON
	result = firebase.patch('/data/salle', data)
	#Affichage de la donnee Value

		data = {'Temperature': 15, 'Humidite': 34, 'Presence': "non", 'Volet': "fermé", 'Heure': time.strftime("%H:%M:%S")}

		result = firebase.patch('/data/cuisine', data)

		data = {'Temperature': 11, 'Humidite': 69, 'Presence': "yes", 'Volet': "ouvert",'Heure' : time.strftime("%H:%M:%S")}

		result = firebase.patch('/data/chambre', data)
