#include <SPI.h>

int chipSel = 10;
int clockPin = 13;
int dataPin = 11;
int miso = 12;

void setup() {
  Serial.begin(9600);
  pinMode(chipSel, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(miso, INPUT);

  SPI.beginTransaction(SPISettings(1000, MSBFIRST, SPI_MODE0));
  
  
  digitalWrite(chipSel, LOW); 
  Serial.println("Handshake iniciado: ");
   for (int j = 0; j < 11; j++) {

      if (send(j) == j) {
        Serial.println("Equal");
      }

      else if (send(j) == 0 && j != 0){
        Serial.println("Error"); // Error handshake
        delay(3000); // Espera 3 segundos
        send(j); // Reintenta
      }

      else {
        Serial.println("Different");
      }

      delay(1000);
   }

  digitalWrite(chipSel, HIGH);
  Serial.println("Handshake terminado");
}

int send(int n) {
    byte b = SPI.transfer(n) << 1; 
    delayMicroseconds(200);
    Serial.println("LEIDO: ");
    Serial.println(b, BIN);
    return b;
}

void loop() {
}
