#include <SPI.h>

void setup(void)
{
  Serial.begin (115200);
  Serial.println ();
  
  digitalWrite(SS, HIGH);  

  SPI.begin ();

  SPI.setClockDivider(SPI_CLOCK_DIV8); // Clock del master
}

byte transferAndWait(const byte what)
{
  byte a = SPI.transfer (what);
  delayMicroseconds (20);
  return a;
} 

void loop(void)
{
  byte a, b, c, d;
  
  digitalWrite(SS, LOW); // Se activa el chip select   

  transferAndWait('a');
  transferAndWait(10);
  a = transferAndWait(17);
  b = transferAndWait(33);
  c = transferAndWait(42);
  d = transferAndWait(0);

  digitalWrite(SS, HIGH); // Se desactiva el chip select

  Serial.println ("Sumando resultados:");
  Serial.println (a, DEC);
  Serial.println (b, DEC);
  Serial.println (c, DEC);
  Serial.println (d, DEC);
  
  delay (1000); 
}