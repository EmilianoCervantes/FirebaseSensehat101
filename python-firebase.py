import json
from sense_hat import SenseHat
import time
import random
from firebase import firebase
import datetime

sense = SenseHat()

#firebase = firebase.FirebaseApplication("https://estacionmeteorologicaverano.firebaseio.com", None)
file = open('data' + str(datetime.datetime.now().isoformat()) + '.txt', 'w')
time.sleep(10)
sense.clear(0, 240, 21)
time.sleep(2)
sense.clear(0, 0, 0)
for i in range(600):
	temp = round(sense.get_temperature(), 1)
	hum = round(sense.get_humidity(), 1)
	pres = round(sense.get_pressure(), 1)
	ori = sense.get_orientation()
	mag = sense.get_compass_raw()
	acc = sense.get_accelerometer_raw()
	gyro = sense.get_gyroscope_raw()
	data = {
			'temperature':temp,
			'humidity':hum,
			'pressure':pres,
			'orientation':ori,
			'compass':mag,
			'acceleration':acc,
			'gyroscope':gyro,
			'time': datetime.datetime.now().isoformat()
			}
	file.write(str(data) + ',\n')
	time.sleep(1)
sense.clear(255, 0, 0)
file.close()
