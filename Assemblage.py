import time
import grovepi
from grovepi import *
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

dht_sensor_port_salle = 5 # Connect the DHt sensor to port D5
dht_sensor_type_salle = 0

dht_sensor_port_cuisine = 6 # Connect the DHt sensor to port D6
dht_sensor_type_cuisine = 0

dht_sensor_port_chambre = 8 # Connect the DHt sensor to port D8
dht_sensor_type_chambre = 0

light_sensor = 0 # Connect the light sensor to port A0
ultrasonic_ranger = 7 # Connect to D7
presence = "non"

led_salle = 4 # Connect the LED to port D4
led_salle_value = 0
led_cuisine = 2 # Connect the LED to port D2
led_cuisine_value = 0
led_chambre = 3 # Connect the LED to port D3
led_chambre_value = 0
 
while True:
        try:
                print("---- GENERAL BLOCK ----")
                # Get sensor value
                sensor_value = grovepi.analogRead(light_sensor)

                if sensor_value > 100:
                        sensor_value = "Jour"
                else:
                        sensor_value = "Nuit"
                print("sensor_value = %s" %(sensor_value))# Get sensor value

                #Get Ultrasonic
		ultrasonic_value = grovepi.ultrasonicRead(ultrasonic_ranger)
		#Presence detection
		if ultrasonic_value > 10:
			presence = "non"
		else:
			presence = "oui"
		print("ultrasonic_value =", ultrasonic_value)
                #Light on auto
		if sensor_value == "Nuit" and presence == "oui":
			digitalWrite(led_salle,1)
			digitalWrite(led_cuisine,1)
			digitalWrite(led_chambre,1)

			led_salle_vallue = "Allumee"
			led_cuisine_vallue = "Allumee"
			led_chambre_vallue = "Allumee"
		else:
                        digitalWrite(led_salle,0)
			digitalWrite(led_cuisine,0)
			digitalWrite(led_chambre,0)

			led_salle_vallue = "Eteinte"
			led_cuisine_vallue = "Eteinte"
			led_chambre_vallue = "Eteinte"

		time.sleep(1)

                # -------- BLOCK SALLE --------
                print("---- BLOCK SALLE ----")
                
                #Get temp and hum salle
                [ temp_salle,hum_salle ] = dht(dht_sensor_port_salle,dht_sensor_type_salle)
                print("temperature =", temp_salle, "humidity =", hum_salle,"%")

                print("lumiere salle =", led_salle_vallue)
                
                #Creation de la data salle
                data = {'Temperature': temp_salle, 'Humidite': hum_salle, 'Presence': presence, 'Lumiere' : led_salle_vallue , 'Exterieur' : sensor_value, 'Heure': time.strftime("%H:%M")}
                #Envoie de la donnee
                result = firebase.patch('/data/salle', data)

                time.sleep(1)	

                # -------- BLOCK CUISINE --------
                print("---- BLOCK CUISINE ----")
                
                #Get temp and hum cuisine
                [ temp_cuisine,hum_cuisine ] = dht(dht_sensor_port_cuisine,dht_sensor_type_cuisine)
                print("temperature =", temp_cuisine, "humidity =", hum_cuisine,"%")

                print("lumiere cuisine =", led_cuisine_vallue)
			
		#Creation de la data cuisine
                data = {'Temperature': temp_cuisine, 'Humidite': hum_cuisine, 'Presence': presence, 'Lumiere' : led_cuisine_vallue, 'Exterieur' : sensor_value, 'Heure': time.strftime("%H:%M")}
                #Envoie de la donnee
                result = firebase.patch('/data/cuisine', data)

                time.sleep(1)
                
                # -------- BLOCK CHAMBRE --------
                print("---- BLOCK CHAMBRE ----")
                
                #Get temp and hum chambre
                [ temp_chambre,hum_chambre ] = dht(dht_sensor_port_chambre,dht_sensor_type_chambre)
                print("temperature =", temp_chambre, "humidity =", hum_chambre,"%")

                print("lumiere chambre =", led_chambre_vallue)
			
		#Creation de la data chambre
                data = {'Temperature': temp_chambre, 'Humidite': hum_chambre, 'Presence': presence, 'Lumiere' : led_chambre_vallue, 'Exterieur' : sensor_value, 'Heure': time.strftime("%H:%M")}
                #Envoie de la donnee
                result = firebase.patch('/data/chambre', data)

                time.sleep(1)
		
        except (IOError,TypeError) as e:
                print("Error")

