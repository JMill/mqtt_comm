import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+str(rc))

	#Subscribing in on_connect() means that if we lose the connection and
	#reconnect then subscriptions will be renewed
	client.subscribe("device/#")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("162.243.219.88", 1883, 60)

client.publish("device/hi", 'hi')

#Blocking call that processes network traffic, dispatches callbacks and
#handles reconnecting.
#Other loop*() functions are available that give a threaded interface and a 
#manual interface.
client.loop_forever()



