import os
import time
import sys
import paho.mqtt.client as mqtt
import json

SERVEUR = 'localhost'
# ACCESS_TOKEN = 'DHT22_DEMO_TOKEN'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=5

sensor_data = {'temperature': 0, 'humidity': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
# client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(SERVEUR, 1883, 60)

client.loop_start()

temperature = 0.0
humidity = 0.0

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
        sensor_data['humidity'] = humidity

        temperature = round(temperature, 2)
        sensor_data['temperature'] = temperature

        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))

        # Sending humidity and temperature data to ThingsBoard
        client.publish('test_channel', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
