from grovepi import *

dht_sensor_port = 7             # Connect the DHt sensor to port 7
dht_sensor_type = 0             # change this depending on your sensor type - s$

while True:
        try:
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)            $
                print("temp =", temp, "C\thumidity =", hum,"%")

        except (IOError,TypeError) as e:
                print("Error")

