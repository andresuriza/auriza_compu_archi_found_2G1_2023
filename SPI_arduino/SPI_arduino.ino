#include <SPI.h>

int chipSel = 10;
int clockPin = 13;
int dataPin = 11;
int miso = 12;
int reset = 9;
int ready = 8;
int done = 7;
int start = 6;

void setup() {
  pinMode(chipSel, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(miso, INPUT);
  pinMode(reset, OUTPUT);
  pinMode(ready, OUTPUT);
  pinMode(done, OUTPUT);
  pinMode(start, INPUT);
  SPI.begin();
  Serial.begin(9600);
  
  digitalWrite(chipSel, LOW);
  handshake();
  digitalWrite(chipSel, HIGH);
}

void handshake() {
  digitalWrite(reset, HIGH);
  digitalWrite(ready, LOW);
  digitalWrite(done, LOW);
  delay(100);

  digitalWrite(reset, LOW);
  digitalWrite(ready, HIGH);
  digitalWrite(done, LOW); 
  delay(100);

  if (digitalRead(start) == 1) {
    Serial.println("Handshake recibido");
    byte b = SPI.transfer(4);  //TODO if == mensaje enviado, recibido
    delayMicroseconds(200);
    Serial.println("LEIDO: ");
    Serial.println(b, BIN);
    
    digitalWrite(chipSel, HIGH);
    delay(100); 
  
    digitalWrite(reset, HIGH);
    delay(100);
    digitalWrite(reset, LOW);
    digitalWrite(ready, LOW);
    digitalWrite(done, HIGH);
    delay(100);

    digitalWrite(reset, HIGH);
    delay(100);
    digitalWrite(reset, LOW);
    digitalWrite(ready, LOW);
    digitalWrite(done, LOW);
    delay(100);
  } else {
    Serial.println("Fallido");
    delay(3000);
    handshake();
  }
}
    
  void loop() {
  }


/* Para incrementar el register
for (int j = 0; j < 16; j++) {

}
*/