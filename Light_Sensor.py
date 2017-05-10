import time
import grovepi

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        print("sensor_value = %d" %(sensor_value))
        time.sleep(.5)

    except IOError:
        print ("Error")
