const int pinPotenciometro = 4;
const int pinLed = 2;
float umbralVoltaje = 2.0;

void setup() {
  pinMode(pinLed, OUTPUT);
}

void loop() {
  int lectura = analogRead(pinPotenciometro);
  float voltajeActual = lectura * (3.3 / 4095.0); 
  
  if (voltajeActual > umbralVoltaje) {
    digitalWrite(pinLed, HIGH); 
  } else {
    digitalWrite(pinLed, LOW);  
  }
  
  delay(100);
}
