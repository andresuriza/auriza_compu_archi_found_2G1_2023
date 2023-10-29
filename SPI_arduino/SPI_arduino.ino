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
  start_handshake();
  digitalWrite(chipSel, HIGH);
}

void send(int n) {
    Serial.println("Handshake recibido");
    byte b = SPI.transfer(n);  //TODO if == mensaje enviado, recibido
    delayMicroseconds(200);
    Serial.println("LEIDO: ");
    Serial.println(b, BIN);

    end_handshake();
}

void end_handshake() {
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
}

void start_handshake() {
  digitalWrite(reset, HIGH);
  digitalWrite(ready, LOW);
  digitalWrite(done, LOW);
  delay(100);

  digitalWrite(reset, LOW);
  digitalWrite(ready, HIGH);
  digitalWrite(done, LOW); 
  delay(100);

  if (digitalRead(start) == 1) {
    send(4);
    
  } else {
    Serial.println("Fallido");
    delay(3000);
    start_handshake();
  }
}
    
  void loop() {
  }


/* Para incrementar el register
for (int j = 0; j < 16; j++) {

}
*/