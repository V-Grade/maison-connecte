import time
import grovepi
from grovepi import *
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

dht_sensor_port = 7
dht_sensor_type = 0
light_sensor = 0

while True:
        try:
                # Get sensor value
                sensor_value = grovepi.analogRead(light_sensor)

                if sensor_value > 100:
                        sensor_value = "Jour"
                else:
                        sensor_value = "Nuit"
                print("sensor_value = %s" %(sensor_value))# Get sensor value

        #Get temp and hum
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
                print("temperature =", temp, "humidity =", hum,"%") 
                time.sleep(.5)

		
        except (IOError,TypeError) as e:
                print("Error")

	#Creation de la data
	data = {'Temperature': temp, 'Humidite': hum, 'Presence': "oui", 'Volet': "ouvert", 'Exterieur' : sensor_value, 'Heure': time.strftime("%H:%M")}
	#Envoie de la donnee et recuperation des donnees formater JSON
	result = firebase.patch('/data/salle', data)
	#Affichage de la donnee Value
