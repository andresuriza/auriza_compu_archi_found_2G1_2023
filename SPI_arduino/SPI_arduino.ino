int chipSel = 10;
int clockPin = 13;
int dataPin = 11;
int miso = 12;

void setup() {
  pinMode(chipSel, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(miso, INPUT);
  Serial.begin(9600);

}

void loop() {
  digitalWrite(chipSel, LOW);

  shiftOut(dataPin, clockPin, MSBFIRST, 4);

  //byte incoming = shiftIn(miso, clockPin, MSBFIRST);
  

  //Serial.println(incoming, BIN);

  digitalWrite(chipSel, HIGH);

  delay(1000);
}


/* Para incrementar el register
for (int j = 0; j < 16; j++) {

}
*/