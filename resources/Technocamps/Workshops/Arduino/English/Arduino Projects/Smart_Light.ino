
// Example: Smart Light

int sensorPin = 0;   // Sensor connected to pin 0
int lightPin = 3;    // LED connected to pin 3

int threshold = 400; // An analog value to turn the LED on/off


void setup() {
  Serial.begin(9600);        // Reset the Arduine to communitcate via USB
  
  pinMode(lightPin,OUTPUT);  // Set the LED (pin 3) to Output
}


void loop() {
  int sensorValue = analogRead(sensorPin); // Read the value of the Light Sensor
  Serial.println(sensorValue,DEC);         // Send the light sensor value back to the computer


  if (sensorValue < threshold){            // If the sensor value is below the threshold
    digitalWrite(lightPin, HIGH);          // set the LED to HIGH
  }

  if (sensorValue > threshold){            // If the sensor value is above the threshold
    digitalWrite(lightPin, LOW);           // set the LED to LOW
  }
}
