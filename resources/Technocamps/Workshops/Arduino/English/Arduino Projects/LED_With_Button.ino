int sensorPin = A0;  //Sensor is connected to pin 0
int lightPin = 3;   //LED is connected to pin 3

int threshold = 400; //Analogue measure of when to				 	 switch the LED value

void setup() {
  Serial.begin(9600);  	  //Reset the Arduino to 						    receive USB commands
  pinMode(lightPin,OUTPUT);  //Set the LED to 					   		    output
}

void loop() {
	int sensorValue = analogRead(sensorPin);
	//Read the value of the light sensor

	Serial.println(sensorValue,DEC);
	//Send the value to the computer

if (sensorValue < threshold)  {
		digitalWrite(lightPin, HIGH); 
	}
//If the sensor value is less than the threshold set the LED to HIGH
  
	if (sensorValue > threshold) {
		digitalWrite(lightPin, LOW);  
	} 
//If the sensor value is more than the threshold set the LED to LOW

} 			 

