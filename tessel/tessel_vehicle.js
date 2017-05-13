//To run on Tessel: listen for vehicle emergency brake command
var mqtt = require('mqtt');

client = mqtt.connect('mqtt://162.243.219.88', 1883);

client.on('connect',function(){
	console.log('connected');
	client.subscribe('ae/car');
});

client.on('message', function(topic, message){
	// message is Buffer
	console.log(message.toString())
	client.end()
})