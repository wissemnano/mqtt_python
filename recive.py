import os

try:
    os.system("mosquitto_sub -h 192.168.1.25 -t test_channel")
except KeyboardInterrupt:
    pass