import time
from firebase import firebase

#Serveur Firebase
URL = "https://projet-maison-co-test.firebaseio.com"
#Connexion au serveur
firebase = firebase.FirebaseApplication(URL)

liste1 = []
liste2 = []
liste3 = []
liste4 = []
liste5 = []

while True:
		try:
			if time.strftime("%H:%M:%S") == time.strftime("%H:%M:00"): #liste 1

				liste1.append(22)
				liste1.append(47)
				liste1.append(time.strftime("%H:%M:%S"))
				print(liste1)
				data = {'liste1' : liste1}
				result = firebase.patch('/data/graph', data)
				liste1 = []

			else:
				time.sleep(.1)

			if time.strftime("%H:%M:%S") == time.strftime("%H:%M:10"): #liste 2

				liste2.append(23)
				liste2.append(48)
				liste2.append(time.strftime("%H:%M:%S"))
				print(liste2)
				data = {'liste2' : liste2}
				result = firebase.patch('/data/graph', data)
				liste2 = []
			else:
				time.sleep(.1)

			if time.strftime("%H:%M:%S") == time.strftime("%H:%M:20"): #liste 3

				liste3.append(24)
				liste3.append(49)
				liste3.append(time.strftime("%H:%M:%S"))
				print(liste3)
				data = {'liste3' : liste3}
				result = firebase.patch('/data/graph', data)
				liste3 = []
			else:
				time.sleep(.1)

			if time.strftime("%H:%M:%S") == time.strftime("%H:%M:30"): #liste 4

				liste4.append(25)
				liste4.append(50)
				liste4.append(time.strftime("%H:%M:%S"))
				print(liste4)
				data = {'liste4' : liste4}
				result = firebase.patch('/data/graph', data)
				liste4 = []
			else:
				time.sleep(.1)

			if time.strftime("%H:%M:%S") == time.strftime("%H:%M:40"): #liste 5

				liste5.append(26)
				liste5.append(51)
				liste5.append(time.strftime("%H:%M:%S"))
				print(liste5)
				data = {'liste5' : liste5}
				result = firebase.patch('/data/graph', data)
				liste5 = []
			else:
				time.sleep(.1)

		except (IOError,TypeError) as e:
			print("Error")
