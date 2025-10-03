
// Example: Smart Light with two LEDs

int sensorPin = 0;      // Sensor connected to pin 0

int redLightPin = 3;    // Red LED connected to pin 3
int greenLightPin = 5;  // Green LED connected to pin 5

int threshold = 500;    // An analog value to turn the LED on/off


void setup() {
  Serial.begin(9600);             // Reset the Arduine to communitcate via USB
  
  pinMode(redLightPin,OUTPUT);    // Set the Red LED (pin 3) to Output
  pinMode(greenLightPin,OUTPUT);  // Set the Green LED (pin 5) to Output
}

void loop() {
  int sensorValue = analogRead(sensorPin); // Read the value of the Light Sensor
  
  Serial.println(sensorValue,DEC);         // Send the light sensor value back to the computer
  

if (sensorValue < threshold){              // If the sensor value is below the threshold
  digitalWrite(greenLightPin, HIGH);       // set the Green LED to HIGH
  digitalWrite(redLightPin,LOW);           // set the Red LED to LOW
}


if (sensorValue > threshold){              // If the sensor value is above the threshold
  digitalWrite(greenLightPin, LOW);        // set the Green LED to LOW
  digitalWrite(redLightPin, HIGH);         // set the Red LED to HIGH
}
}
