//Esiampl: LED sy'n gwanhau a chryfhau

const int LED = 9;       //LED wedi cysylltu i bin digidol 
int i = 0;               //Creu newidyn i gyda gwerth 0

void setup() {
 pinMode(LED, OUTPUT);   //Gosod yr LED (pin 9) i allbwn
}

void loop() {
  
  for (i=0; i<255; i++) {   //Creu dolen o 0 i 255 (cryfhau)
    analogWrite(LED, i);    //Gosod cryfder yr LED i 'i'
    delay(10);              //Aros 10 milieiliad
  }

  for (i=255; i>0; i--) {   //Creu dolen o 255 i 0 (gwanhau)
    analogWrite(LED, i);    //Gosod cryfder yr LED i 'i'
    delay(10);              //Aros 10 milieiliad
  }
}
