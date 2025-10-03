//Esiampl: Troi yr LED ymlaen ac aros ymlaen

const int LED = 13;    //LED wedi cysylltu i bin digidol 13
const int BOTWM = 7;   //BOTWM wedi cysylltu i bin digidol 7

int val = 0;           //Defnyddio val i storio werth y botwm
int cyflwr = 0;        //Defnyddio val i storio'r cyflwr

void setup() {
  pinMode(LED,OUTPUT);        //Gosod yr LED i allbwn
  pinMode(BOTWM,INPUT);       //Gosod yr BOTWM i mewnbwn
}

void loop() {
  val = digitalRead(BOTWM);     //Darllen werth y BOTWM a storio

  if (val == HIGH) {            //Os mae'r gwerth yn uchel
    cyflwr = 1 - cyflwr;        //Newid y cyflwr
  }

  if (cyflwr == 1) {            //Os mae'r cyflwr yn uchel
    digitalWrite(LED, HIGH);    //Trowch yr LED ymlaen
  }
  else {                        //Os mae'r cyflwr yn isel
    digitalWrite(LED, LOW);     //Trowch yr LED i ffwrdd
  }
}
