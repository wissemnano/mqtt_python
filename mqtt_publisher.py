import paho.mqtt.publish as publish
 
MQTT_SERVER = "192.168.1.69"
MQTT_PATH = "test_channel"
 
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)