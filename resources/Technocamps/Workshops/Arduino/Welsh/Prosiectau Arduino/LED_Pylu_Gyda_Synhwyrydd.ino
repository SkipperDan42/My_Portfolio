
// Esiampl: LED Pylu Gyda Synhwyrydd

int sensorPin = 0;   // Synhwyrydd wedi cysylltu i bin 0
int lightPin = 3;    // LED wedi cysylltu i bin 3

int darkest = 460;   // Mesur analog tywyllwch i newid werth yr LED
int lightest = 620;  // Mesur analog disgleirdeb i newid werth yr LED


void setup() {
  Serial.begin(9600);         // Ailosod yr Arduino i derbyn cyfarwyddiadau trwy USB
  
  pinMode(lightPin, OUTPUT);  // Gosod yr LED (pin 3) i allbwn
}

void loop() {
  int sensorValue = analogRead(sensorPin);      // Darllen gwerth y synhwyrydd golau
  Serial.println(sensorValue);                  // Anfon gwerth y synhwyrydd nol i'r cyfrifiadur
  
  int brightness = setBrightness(sensorValue);  // Gosod y disgleirdeb o werth y synhwyrydd
  analogWrite(lightPin, brightness);            // Ysgrifennu gwerth y disgleirdeb i'r LED
}

int setBrightness(int value) {                    // Creu ffwythiant setBrightness sy'n derbyn 
                                                  // gwerth y synhwyrydd a newid i allbwn digidol
  
  value = max(value, darkest);                    // Gosod gwerth value i'r gwerth 
                                                  // mwyaf tu fewn y cromfachau
  value = min(value, lightest);                   // Gosod gwerth value i'r gwerth 
                                                  // lleiaf tu fewn y cromfachau
  
  value = map(value, darkest, lightest, 0, 255);  // Creu map sy'n cyfateb werth y 
                                                  // synhwyrydd i amrediad yr LED
                                                  
  value = 255 - value;                            // Newid gwerth yr LED i wrthwyneb 
                                                  // gwerth y synhwyrydd
  
  return value;                                   // Anfon y gwerth nol allan o'r ffwythiant
}
