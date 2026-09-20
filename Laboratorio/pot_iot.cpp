// Codigo modificado para funcionar en esp-idf

#include <Arduino.h>

// Codigo arduino normal

#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "";
const char* password = "";
String aio_user = "";
String aio_key = "";
String feed_name = "potenciometro";
const int potPin = 4;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12); 
  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado a WiFi!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    int lectura = analogRead(potPin);
    float voltaje = (lectura / 4095.0) * 3.3;
    Serial.printf("Voltaje leído: %.2f V\n", voltaje);

    HTTPClient http;
    String url = "https://io.adafruit.com/api/v2/" + aio_user + "/feeds/" + feed_name + "/data";
    http.begin(url);
    http.addHeader("X-AIO-Key", aio_key);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"value\": " + String(voltaje, 2) + "}";
    int httpResponseCode = http.POST(payload);

    if (httpResponseCode > 0) {
      Serial.printf("Dato enviado. Código HTTP: %d\n", httpResponseCode);
    } else {
      Serial.printf("Error HTTP: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();
  }
  delay(5000);
}

// Modificacion para que funcione en esp-idf

extern "C" void app_main() {
    initArduino();
    setup();
    while (true) {
        loop();
        vTaskDelay(10 / portTICK_PERIOD_MS); // Previene que el Watchdog Timer reinicie el ESP32
    }
}
