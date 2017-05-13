import paho.mqtt.client as mqtt
import json
import random
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print ("Connected with result code "+str(rc))

    #Subscribing in on_connect() means that if we lose the connection and
    #reconnect then subscriptions will be renewed
    client.subscribe("device/#")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("162.243.219.88", 1883, 60)

while 1 > 0: 
    payload = json.dumps({"position_x": str(random.random()), "position_y": str(random.random())})
    print(payload)
    # payload = json.loads(payload) # you can use json.loads to convert string to json
    # print(payload)
    client.publish("ae/turret", payload)
    time.sleep(3) # in seconds


#Blocking call that processes network traffic, dispatches callbacks and
#handles reconnecting.
#Other loop*() functions are available that give a threaded interface and a 
#manual interface.
client.loop_forever()



