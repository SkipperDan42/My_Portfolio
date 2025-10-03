
// Example: Blinking LED

const int LED = 13; // LED connected to digital pin 13


void setup() {
  pinMode(LED, OUTPUT); // Set the LED (pin 13) to Output
}


void loop() {
  digitalWrite(LED, HIGH); // set the LED to HIGH
  delay (1000);            // wait for 1 second
  
  digitalWrite(LED, LOW);  // set the LED to Low
  delay(1000);             // wait for 1 second
}
