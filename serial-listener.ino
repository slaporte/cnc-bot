// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.

#include <Servo.h> 
 
Servo x_servo;
Servo y_servo;

int max_angle = 140;
int min_angle = 0;
int increment = 5;
int position;
byte byteRead;
char servo = 'n';

void setup() {
  x_servo.attach(13);
  y_servo.attach(12);
  Serial.begin(9600);
} 

void loop() {
  if (Serial.available()) {
    byteRead = Serial.read();
    if (byteRead > 47 && byteRead < 58) {
      // only because I have no idea how to decode ascii...
      position = (position * 10) + byteRead - 48;
    } else {
      if (byteRead == 120) {
        // move on x-axis
        Serial.print('x');
        Serial.println(position);
        if (position > max_angle || position < min_angle) {
          Serial.println("I can't let you do that...");
        } else {
          x_servo.write(position);
        }
        position = 0;
      } else if (byteRead == 121) {
        // move on y-axis
        Serial.print('y');
        Serial.println(position);
        if (position > max_angle || position < min_angle) {
          Serial.println("I can't let you do that...");
        } else {
          y_servo.write(position);
        }
        position = 0;
      }
    }
  } 
}
