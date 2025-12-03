#include <Arduino.h>
#include <Servo.h>
#include <HX711.h>

#define PIR_PIN 21
#define SERVO_PIN 22
#define LOADCELL_DT_PIN 23 // data pin
#define LOADCELL_SCK_PIN 24 // clock pin
#define LED_PIN 25

unsigned long stableTime = 1000;
bool motionDetected = false;
float calibration = -500.0;

Servo myServo;
HX711 scale;

void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
  myServo.attach(SERVO_PIN);
  myServo.write(0);
  scale.begin(LOADCELL_DT_PIN, LOADCELL_SCK_PIN); // initialize scale
  scale.set_scale(calibration); // set the calibration
  scale.tare();
}

void loop() {
  int reading = digitalRead(PIR_PIN);

  // If PIR goes HIGH, double-check it after a delay
  if (reading == HIGH) {
    delay(stableTime);
    if (digitalRead(PIR_PIN) == HIGH && !motionDetected) {
      motionDetected = true;
      Serial.println("Motion CONFIRMED");
      Serial.print(scale.get_units());
    Serial.println("g");
      myServo.write(90);
      delay(500);
      myServo.write(0);
    }
  }

  // If PIR goes LOW, reset state
  if (reading == LOW && motionDetected) {
    motionDetected = false;
    Serial.println("Motion ended");
    Serial.print(scale.get_units());
    Serial.println("g");
  }

  // If food is low, light up LED
  if (scale.get_units() < 500.0) {
    digitalWrite(LED_PIN, HIGH);
  
  }

  
  delay(200);
}


