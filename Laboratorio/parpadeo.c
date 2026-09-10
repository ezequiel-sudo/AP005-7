const int ledContinuo = 2;
const int ledTresVeces = 4;
int contador = 0;

void setup() {
  pinMode(ledContinuo, OUTPUT);
  pinMode(ledTresVeces, OUTPUT);
}

void loop() {
  digitalWrite(ledContinuo, HIGH);
  
  if (contador < 3) {
    digitalWrite(ledTresVeces, HIGH);
  }
  
  delay(500);
  
  digitalWrite(ledContinuo, LOW);
  
  if (contador < 3) {
    digitalWrite(ledTresVeces, LOW);
  }
  
  delay(500);
  
  if (contador < 3) {
    contador++;
  }
}
