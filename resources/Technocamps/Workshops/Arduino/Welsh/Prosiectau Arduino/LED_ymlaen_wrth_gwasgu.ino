
// Esiampl: Troi'r LED ymlaen wrth gwasgu botwm

const int LED = 13;    // LED wedi cysylltu i bin digidol 13
const int BOTWM = 7;  // Botwm wedi cysylltu i bin digidol 7
int val = 0;           // defnyddio val i storio werth y pin mewnbwn


void setup() {
  pinMode(LED, OUTPUT);   // Gosod yr LED (pin 13) i allbwn
  
  pinMode(BOTWM, INPUT); // Gosod yr Botwm (pin 7) i fewnbwn
}


void loop() {
  
  val = digitalRead(BOTWM); // Darllen gwerth y botwm a storio

  // Gwirio os ydy'r mewnbwn yn UCHEL (botwm wedi'i wasgu)

  if (val==HIGH) {            // Os mae'r botwm wedi'i gwasgu
    digitalWrite(LED, HIGH);  // gosod gwerth y LED i UCHEL
  }

  else {                      // Os nad ydy'r botwm wedi'i gwasgu
    digitalWrite(LED, LOW);   // gosod gwerth y LED i ISEL
  }
}
