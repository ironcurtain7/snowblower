
// подключение библиотек
#include <driver.h>
#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <Servo.h>

// создание переменных

const char *ssid = "snow2";
const char *password = "12345678";
int pA = 16000;
int pB = 16000;
int pH = 17488;
int pT = 16000;
int pS = 16090;

// инициализация модулей

WiFiServer server(80);
Servo myservo = Servo();
IPAddress staticIP(10, 42, 0, 69);  // ESP32 static IP
IPAddress gateway(10, 42, 0, 1);    // IP Address of your network gateway (router)
IPAddress subnet(255, 255, 255, 0); // Subnet mask
driver mot;

// функция управления моторами

void setup()
{
  Serial.begin(115200);
  mot.motors_attach();
  pinMode(25, ANALOG);
  // нулевые положения для всех двигателей
  myservo.write(13, 90);
  myservo.writeMicroseconds(26, 1488);
  dacWrite(25, 0);
  delay(10000);      // задержка для инициализации бк регулятора
  dacWrite(25, 100); // звук мотором о готовности
  delay(200);
  dacWrite(25, 0);

  // Подключаемся к Wi-Fi
  if (WiFi.config(staticIP, gateway, subnet) == false)
  {
    Serial.println("Configuration failed.");
  }
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  // Запускаем сервер
  server.begin();
}

void loop()
{
  // Проверяем, есть ли подключенные клиенты
  WiFiClient client = server.available();

  if (client)
  {
    Serial.println("New Client connected.");

    while (client.connected())
    {
      if (client.available())
      {

        // Читаем данные
        pA = client.readStringUntil('\r').toInt();
        pB = client.readStringUntil('\r').toInt();
        pH = client.readStringUntil('\r').toInt();
        pT = client.readStringUntil('\r').toInt();
        pS = client.readStringUntil('\r').toInt();

        Serial.println(pA);
      }
      mot.set_motors(pA - 16000, pB - 16000);           // установка мощности на ходовые моторы
      dacWrite(25, pT - 16000);                  // установка мощности на ротор
      myservo.write(13, pS - 16000);             // установка угла сервопривода
      myservo.writeMicroseconds(26, pH - 16000); // установка мощности на шнек
    }
  }
}
