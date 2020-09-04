import sys
import urllib.request
from time import sleep
import random


myapi = '5NKLBPLHTEJC42RI'
myurl = "https://api.thingspeak.com/update?api_key=5NKLBPLHTEJC42RI"

while True:
    floor = random.randint(0, 20)
    pressure = random.uniform(10, 20) #max is 18
    speed = random.uniform(0, 3) #max is 2m/s
    governor = 0
    level = random.uniform(-1,1) 
    Voltage = random.uniform(100, 260) #range is 120 to 240
    power = random.uniform(200, 400) 
    temperature = random.randrange(25, 90) #max is 82
    emer_no = 0

    if speed > 1.8:
        governor += 1
    if pressure > 18 & temperature > 82:
            emer_no += 1
    if floor == 0:
        send_pressure = urllib.request.urlopen(myurl + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s&field8=%s' % (pressure, speed, governor, level, Voltage, power, temperature, emer_no))
        print('Uploaded Successfully')
   





    



        



