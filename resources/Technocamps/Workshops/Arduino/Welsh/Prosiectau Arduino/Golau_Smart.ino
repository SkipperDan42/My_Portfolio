
// Esiampl : Golau Smart

int sensorPin = 0;   // Synhwyrydd wedi cysylltu i bin 0
int lightPin = 3;    // LED wedi cysylltu i bin 3

int threshold = 400; // Mesur analog o bryd i newid werth yr LED


void setup() {
  Serial.begin(9600);        // Ailosod yr Arduino i derbyn cyfarwyddiadau trwy USB
  
  pinMode(lightPin,OUTPUT);  // Gosod yr LED (pin 3) i allbwn
}


void loop() {
  int sensorValue = analogRead(sensorPin); // Darllen gwerth y synhwyrydd golau
  Serial.println(sensorValue,DEC);         // Anfon gwerth y synhwyrydd nol i'r cyfrifiadur


  if (sensorValue < threshold){            // Os mae gwerth y synhwyrydd yn llai na'r threshold
    digitalWrite(lightPin, HIGH);          // gosod gwerth y LED i UCHEL
  }

  if (sensorValue > threshold){            // Os mae gwerth y synhwyrydd yn fwy na'r threshold
    digitalWrite(lightPin, LOW);           // gosod gwerth y LED i ISEL
  }
}
