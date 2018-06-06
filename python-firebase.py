import json
from sense_hat import SenseHat
import time
import random
from firebase import firebase

sense = SenseHat()

'''def temp():
	temp = round(sense.get_temperature(), 1)

def hum():
	hum = round(sense.get_humidity(), 1)

def press():
	pres = round(sense.get_pressure(), 1)'''

firebase = firebase.FirebaseApplication("https://estacionmeteorologicaverano.firebaseio.com", None)
data='00'
i = 0
j = 0
while True:
	i+=30
	j+=1
	temp = round(sense.get_temperature(), 1)
	hum = round(sense.get_humidity(), 1)
	pres = round(sense.get_pressure(), 1)
	ori = sense.get_orientation()
	mag = sense.get_compass_raw()
	acc = sense.get_accelerometer_raw()
	gyro = sense.get_gyroscope_raw()
	data = {"Temp":temp,
			'Hum':hum,
			'Pres':pres,
			'Orient':ori,
			'Mag':mag,
			'Acc':acc,
			'Gyro':gyro}
	print(data)
	salida = firebase.post('/registros2Test', data)
	sense.show_message("Medición {}".format(j), scroll_speed=0.08)
	
	time.sleep(30)
	if i > 600 :
		break
#dataInJson = json.loads(data)
#firebase.post("/registros", data)

salida = firebase.get('/registros', None)
'''for key in salida.keys():
	registro = salida[key]
	print(registro['calificacion'])
	print(registro['edad'])'''
#print(salida)
