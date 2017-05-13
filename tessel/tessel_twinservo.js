//To run on Twin Servo Tessel: listen for coordinates
var tessel = require('tessel');
var servolib = require('servo-pca9685');
var mqtt = require('mqtt');

var servo = servolib.use(tessel.port['A']);
var servoY = 1; //x-axis
var servoX = 16; //y-axis





client = mqtt.connect('mqtt://162.243.219.88', 1883);

client.on('connect',function(){
	console.log('connected');
	client.subscribe('ae/turret');
});


var positionX;
var positionY;

client.on('message', function(topic, message){
	// message is Buffer
	console.log(payload);
	var payload = JSON.parse(message);
	console.log(payload);
	positionX = payload.position_x;
	positionY = payload.position_y;

	//console.log(message.toString())
	//client.end()
})


//var positionX = 0.4980; // 0.000 = LEFT
//var positionY = 0.0580; // 0.0000 = DOWN


servo.on('ready', function () {
	
	//settings: 0.05, 0.12
	servo.configure(servoX, 0.025, 0.123, function (){
		setInterval(function () {
			//console.log('X:', positionX);
			servo.move(servoX, positionX);
		}, 200); //in milliseconds
	});

	servo.configure(servoY, 0.026, 0.057, function (){
		setInterval(function () {
			//console.log('Y:', positionY);
			servo.move(servoY, positionY);
		}, 200); //in milliseconds
	});

	
});
