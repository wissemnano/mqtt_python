import os
import time
import sys
import json


# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=5


temperature = 0.0
humidity = 0.0

next_reading = time.time()

def readData(fileName):
    global temperature, humidity
    with open(fileName) as json_data:
        data_sensors = json.load(json_data)
    temperature = data_sensors['temperature']
    humidity = data_sensors['humidity']

try:
    while True:
        readData('data.json')
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        
        # Sending humidity and temperature data to ThingsBoard

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
