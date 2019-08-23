import time
import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.1.25"
MQTT_PATH = "test_channel"

#Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with Code "+str(rc))
    #Subscribe Topic
    client.subscribe("test_channel")

def on_message(client, userdata, msg):
    print(str(msg.payload))
    # more callbacks, etc


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

"""
try:
    os.system("mosquitto_sub -h 192.168.1.25 -t test_channel")
except KeyboardInterrupt:
    pass
"""
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.


#client.loop_forever()
client.loop_start()
try:
    while True:
        client.publish("other_topic_channel", "Get started with MQTT")
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()

    
