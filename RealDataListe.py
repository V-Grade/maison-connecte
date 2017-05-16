import time
import grovepi
from grovepi import *
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

#liste salle
liste_salle1 = []
liste_salle2 = []
liste_salle3 = []
liste_salle4 = []
liste_salle5 = []

#liste cuisine
liste_cuisine1 = []
liste_cuisine2 = []
liste_cuisine3 = []
liste_cuisine4 = []
liste_cuisine5 = []

#liste chambre
liste_chambre1 = []
liste_chambre2 = []
liste_chambre3 = []
liste_chambre4 = []
liste_chambre5 = []

dht_sensor_port_salle = 5 # Connect the DHt sensor to port D5
dht_sensor_type_salle = 0

dht_sensor_port_cuisine = 6 # Connect the DHt sensor to port D6
dht_sensor_type_cuisine = 0

dht_sensor_port_chambre = 8 # Connect the DHt sensor to port D8
dht_sensor_type_chambre = 0

while True:
    try:
        #Get temp and hum salle
        [ temp_salle,hum_salle ] = dht(dht_sensor_port_salle,dht_sensor_type_salle)
        time.sleep(.2)

        #Get temp and hum cuisine
        [ temp_cuisine,hum_cuisine ] = dht(dht_sensor_port_cuisine,dht_sensor_type_cuisine)
        time.sleep(.2)

        #Get temp and hum chambre
        [ temp_chambre,hum_chambre ] = dht(dht_sensor_port_chambre,dht_sensor_type_chambre)
        time.sleep(.2)
        #Send salle / cuisine / chambre data to graph on firebase
        if time.strftime("%H:%M:%S") == time.strftime("%H:%M:00"): #liste 1
            liste_salle1.append(temp_salle)
            liste_cuisine1.append(temp_cuisine)
            liste_chambre1.append(temp_chambre)
            liste_salle1.append(hum_salle)
            liste_cuisine1.append(hum_cuisine)
            liste_chambre1.append(hum_chambre)
            liste_salle1.append(time.strftime("%H:%M:%S"))
            liste_cuisine1.append(time.strftime("%H:%M:%S"))
            liste_chambre1.append(time.strftime("%H:%M:%S"))
            print("Data salle 1 =",liste_salle1)
            print("Data cuisine 1 =",liste_cuisine1)
            print("Data chambre 1 =",liste_chambre1)
            data_salle = {'liste_salle1' : liste_salle1}
            data_cuisine = {'liste_cuisine1' : liste_cuisine1}
            data_chambre = {'liste_chambre1' : liste_chambre1}
            result_salle = firebase.patch('/data/graph', data_salle)
            result_cuisine = firebase.patch('/data/graph', data_cuisine)
            result_chambre = firebase.patch('/data/graph', data_chambre)
            liste_salle1 = []
            liste_cuisine1 = []
            liste_chambre1 = []

        else:
            time.sleep(.1)

	if time.strftime("%H:%M:%S") == time.strftime("%H:%M:10"): #liste 2

            liste_salle2.append(temp_salle)
            liste_cuisine2.append(temp_cuisine)
            liste_chambre2.append(temp_chambre)
            liste_salle2.append(hum_salle)
            liste_cuisine2.append(hum_cuisine)
            liste_chambre2.append(hum_chambre)
            liste_salle2.append(time.strftime("%H:%M:%S"))
            liste_cuisine2.append(time.strftime("%H:%M:%S"))
            liste_chambre2.append(time.strftime("%H:%M:%S"))
            print("Data salle 2 =",liste_salle2)
            print("Data cuisine 2 =",liste_cuisine2)
            print("Data chambre 2 =",liste_chambre2)
            data_salle = {'liste_salle2' : liste_salle2}
            data_cuisine = {'liste_cuisine2' : liste_cuisine2}
            data_chambre = {'liste_chambre2' : liste_chambre2}
            result_salle = firebase.patch('/data/graph', data_salle)
            result_cuisine = firebase.patch('/data/graph', data_cuisine)
            result_chambre = firebase.patch('/data/graph', data_chambre)
            liste_salle2 = []
            liste_cuisine2 = []
            liste_chambre2 = []
        else:
            time.sleep(.1)

	if time.strftime("%H:%M:%S") == time.strftime("%H:%M:20"): #liste 3
            liste_salle3.append(temp_salle)
            liste_cuisine3.append(temp_cuisine)
            liste_chambre3.append(temp_chambre)
            liste_salle3.append(hum_salle)
            liste_cuisine3.append(hum_cuisine)
            liste_chambre3.append(hum_chambre)
            liste_salle3.append(time.strftime("%H:%M:%S"))
            liste_cuisine3.append(time.strftime("%H:%M:%S"))
            liste_chambre3.append(time.strftime("%H:%M:%S"))
            print("Data salle 3 =",liste_salle3)
            print("Data cuisine 3 =",liste_cuisine3)
            print("Data chambre 3 =",liste_chambre3)
            data_salle = {'liste_salle3' : liste_salle3}
            data_cuisine = {'liste_cuisine3' : liste_cuisine3}
            data_chambre = {'liste_chambre3' : liste_chambre3}
            result_salle = firebase.patch('/data/graph', data_salle)
            result_cuisine = firebase.patch('/data/graph', data_cuisine)
            result_chambre = firebase.patch('/data/graph', data_chambre)
            liste_salle3 = []
            liste_cuisine3 = []
            liste_chambre3 = []
	else:
            time.sleep(.1)

	if time.strftime("%H:%M:%S") == time.strftime("%H:%M:30"): #liste 4

            liste_salle4.append(temp_salle)
            liste_cuisine4.append(temp_cuisine)
            liste_chambre4.append(temp_chambre)
            liste_salle4.append(hum_salle)
            liste_cuisine4.append(hum_cuisine)
            liste_chambre4.append(hum_chambre)
            liste_salle4.append(time.strftime("%H:%M:%S"))
            liste_cuisine4.append(time.strftime("%H:%M:%S"))
            liste_chambre4.append(time.strftime("%H:%M:%S"))
            print("Data salle 4 =",liste_salle4)
            print("Data cuisine 4 =",liste_cuisine4)
            print("Data chambre 4 =",liste_chambre4)
            data_salle = {'liste_salle4' : liste_salle4}
            data_cuisine = {'liste_cuisine4' : liste_cuisine4}
            data_chambre = {'liste_chambre4' : liste_chambre4}
            result_salle = firebase.patch('/data/graph', data_salle)
            result_cuisine = firebase.patch('/data/graph', data_cuisine)
            result_chambre = firebase.patch('/data/graph', data_chambre)
            liste_salle4 = []
            liste_cuisine4 = []
            liste_chambre4 = []
        else:
            time.sleep(.1)

	if time.strftime("%H:%M:%S") == time.strftime("%H:%M:40"): #liste 5

            liste_salle5.append(temp_salle)
            liste_cuisine5.append(temp_cuisine)
            liste_chambre5.append(temp_chambre)
            liste_salle5.append(hum_salle)
            liste_cuisine5.append(hum_cuisine)
            liste_chambre5.append(hum_chambre)
            liste_salle5.append(time.strftime("%H:%M:%S"))
            liste_cuisine5.append(time.strftime("%H:%M:%S"))
            liste_chambre5.append(time.strftime("%H:%M:%S"))
            print("Data salle 5 =",liste_salle5)
            print("Data cuisine 5 =",liste_cuisine5)
            print("Data chambre 5 =",liste_chambre5)
            data_salle = {'liste_salle5' : liste_salle5}
            data_cuisine = {'liste_cuisine5' : liste_cuisine5}
            data_chambre = {'liste_chambre5' : liste_chambre5}
            result_salle = firebase.patch('/data/graph', data_salle)
            result_cuisine = firebase.patch('/data/graph', data_cuisine)
            result_chambre = firebase.patch('/data/graph', data_chambre)
            liste_salle5 = []
            liste_cuisine5 = []
            liste_chambre5 = []
        else:
            time.sleep(.1)

    except (IOError,TypeError) as e:
        print("Error")
