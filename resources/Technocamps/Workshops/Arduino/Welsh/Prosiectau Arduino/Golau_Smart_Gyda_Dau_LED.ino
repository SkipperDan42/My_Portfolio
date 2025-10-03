
// Esiampl : Golau Smart gyda Dau LED

int sensorPin = 0;      // Synhwyrydd wedi cysylltu i bin 0

int redLightPin = 3;    // LED coch wedi cysylltu i bin 3
int greenLightPin = 5;  // LED gwyrdd wedi cysylltu i bin 5

int threshold = 500;    // Mesur analog o bryd i newid werth yr LED


void setup() {
  Serial.begin(9600);             // Ailosod yr Arduino i derbyn cyfarwyddiadau trwy USB
  
  pinMode(redLightPin,OUTPUT);    // Gosod yr LED coch (pin 3) i allbwn
  pinMode(greenLightPin,OUTPUT);  // Gosod yr LED gwyrdd (pin 5) i allbwn
}

void loop() {
  int sensorValue = analogRead(sensorPin); // Darllen gwerth y synhwyrydd golau
  
  Serial.println(sensorValue,DEC);         // Anfon gwerth y synhwyrydd nol i'r cyfrifiadur


if (sensorValue < threshold){              // Os mae gwerth y synhwyrydd yn llai na'r threshold
  digitalWrite(greenLightPin, HIGH);       // gosod gwerth y LED wyrdd i UCHEL
  digitalWrite(redLightPin,LOW);           // a gosod gwerth y LED goch i ISEL
}


if (sensorValue > threshold){              // Os mae gwerth y synhwyrydd yn llai na'r threshold
  digitalWrite(greenLightPin, LOW);        // gosod gwerth y LED wyrdd i ISEL
  digitalWrite(redLightPin, HIGH);         // a gosod gwerth y LED goch i UCHEL
}
}
