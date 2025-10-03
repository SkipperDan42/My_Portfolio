
// Example: Dimmer LED with Sensor

int sensorPin = 0;   // Sensor connected to pin 0
int lightPin = 3;    // LED connected to pin 3

int darkest = 460;   // An analog value of darkness to change the LED value
int lightest = 620;  // An analog value of brightness to change the LED value


void setup() {
  Serial.begin(9600);         // Reset the Arduine to communitcate via USB
  
  pinMode(lightPin, OUTPUT);  // Set the LED (pin 3) to Output
}

void loop() {
  int sensorValue = analogRead(sensorPin);      // Read the value of the Light Sensor
  Serial.println(sensorValue);                  // Send the light sensor value back to the computer
  
  int brightness = setBrightness(sensorValue);  // Set the brightness from the sensor value
  analogWrite(lightPin, brightness);            // Write the brightness value to the LED
}

int setBrightness(int value) {                    // Create the function setBrightness from the 
                                                  // sensor value and convert to digital output
  
  value = max(value, darkest);                    // Set the worth of value to the
                                                  // highest value within the brakets
                                                  
  value = min(value, lightest);                   // Set the worth of value to the 
                                                  // lowest value within the brakets
  
  value = map(value, darkest, lightest, 0, 255);  // Create a map to equate the sensor value 
                                                  // to the range of values the LED can have
                                                  
  value = 255 - value;                            // Change the LED value to the 
                                                  // reverse of the sensor value
  
  return value;                                   // Send the value back out of this function
}
