#include <Arduino.h>
#include <Servo.h>

#define PIR_PIN 21
#define SERVO_PIN 22

unsigned long stableTime = 1000;
bool motionDetected = false;

Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
  myServo.attach(SERVO_PIN);
  myServo.write(0);
}

void loop() {
  int reading = digitalRead(PIR_PIN);

  // If PIR goes HIGH, double-check it after a delay
  if (reading == HIGH) {
    delay(stableTime);
    if (digitalRead(PIR_PIN) == HIGH && !motionDetected) {
      motionDetected = true;
      Serial.println("Motion CONFIRMED");
      myServo.write(90);
      delay(500);
      myServo.write(0);
    }
  }

  // If PIR goes LOW, reset state
  if (reading == LOW && motionDetected) {
    motionDetected = false;
    Serial.println("Motion ended");
  }
  delay(200);
}

