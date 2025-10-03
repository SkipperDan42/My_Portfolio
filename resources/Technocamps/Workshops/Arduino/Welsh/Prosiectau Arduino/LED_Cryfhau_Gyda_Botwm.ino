// Esiampl: Troi'r LED ymlaen wrth gwasgu botwm a chadw ymlaen ar ol rhyddhau

const int LED = 13;    // LED wedi cysylltu i bin digidol 13
const int BOTWM = 7;  // Botwm wedi cysylltu i bin digidol 7

int val = 0;           // defnyddio val i storio werth y pin mewnbwn
int hen_val = 0;       // storio gwerth cynharach y pin mewnbwn

int disgleirdeb = 128;  //storio werth y disgleirdeb
unsigned long amser = 0; //pryd dechreuodd ni wasgu y botwm

void setup() {
  pinMode(LED, OUTPUT);   // Gosod yr LED (pin 13) i allbwn
  pinMode(BOTWM, INPUT); // Gosod yr Botwm (pin 7) i fewnbwn
}


void loop() {
  
  val = digitalRead(BOTWM); // Darllen gwerth y botwm a storio

  //Edrych am newid mewn y botwm
  if ((val==HIGH) && (old_val==LOW)) {  
    
    cyflwr = 1 - cyflwr;   //Newid y cyflwr

    amser = millis();      //millis yw cloc Arduino, cyfri yr amser ers y reset diwethaf

    delay(10);
  }
  
  //Os mae'r botwm wedi dal lawr
  if ((val==HIGH) && (old_val==HIGH)) {

    //Os mae'r botwm wedi dal am fwy na hanner eiliad
    if (cyflwr == 1 && (millis() - amser) > 500) {
      
      disgleirdeb++;     //cynyddu y disgleirdeb gan 1
      delay(25);

      if (disgleirdeb > 255) {
        disgleirdeb = 0;      //255 yw'r disgleirdeb uchaf, mynd nol i 0
      }
    }
  }

  hen_val = val;    //Nawr mae'r gwerth yn hen gadewch i ni storio

  if (cyflwr == 1) {
    analogWrite(LED, disgleirdeb);  // gosod gwerth y LED i'r disgleirdeb
  }

  else {
    analogWrite(LED, 0);   //trowch yr LED i ffwrdd
  }
}
