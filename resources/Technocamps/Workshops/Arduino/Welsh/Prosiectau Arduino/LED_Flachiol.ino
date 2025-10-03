
// Esiampl : LED Flachiol

const int LED = 13; // LED wedi cysylltu i bin digidol 13


void setup() {
  pinMode(LED, OUTPUT); // Gosod yr LED (pin 13) i allbwn
}


void loop() {
  digitalWrite(LED, HIGH); // gosod gwerth y LED i UCHEL
  delay (1000);            // aros am 1 eiliad
  
  digitalWrite(LED, LOW);  // gosod gwerth y LED i ISEL
  delay(1000);             // aros am 1 eiliad
}
