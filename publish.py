import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+str(rc))

	#Subscribing in on_connect() means that if we lose the connection and
	#reconnect then subscriptions will be renewed
	client.subscribe("$SYS/#")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("iot.eclipse.org", 1883, 60)

client.publish("$SYS/hi", 'hi')

#Blocking call that processes network traffic, dispatches callbacks and
#handles reconnecting.
#Other loop*() functions are available that give a threaded interface and a 
#manual interface.
client.loop_forever()



