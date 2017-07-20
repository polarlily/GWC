//Starter Code for Escape Bot
#include <Servo.h>
Servo servoLeft;
Servo servoRight;

int rightWhiskerPin = 7;
int leftWhiskerPin = 5;
int rightWhiskerState = 0;
int leftWhiskerState = 0;

//Declare Right servo
//Declare Left servo
void setup() {
delay(1000); 
pinMode(rightWhiskerPin, INPUT);
pinMode(leftWhiskerPin, INPUT);
Serial.begin(9600);
//Attach Left Servo
//Attach Right Servo
  servoLeft.attach(13);
  servoRight.attach(12);
}
void loop() {
// put your main code here, to run repeatedly:
rightWhiskerState = digitalRead(rightWhiskerPin);
leftWhiskerState = digitalRead(leftWhiskerPin);
// whisker state is 1 if unpressed and 0 if pressed.
if(rightWhiskerState == 0 && leftWhiskerState == 0){
//Make it move away from the Obstacle
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(2000);
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(2000);
  
  
}
else if(leftWhiskerState == 0){
//Make it move away from the Obstacle
  servoLeft.writeMicroseconds(1300);
  delay(1000);
  servoRight.writeMicroseconds(1700);
  delay(1000);
  servoLeft.writeMicroseconds(1700);
  delay(1000);
  servoRight.writeMicroseconds(1700);
  delay(1000);
}
else if(rightWhiskerState == 0){
//Make it move away from the Obstacle
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  delay(1000);
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  delay(1000);
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  delay(1000);
}
else{
  servoLeft.writeMicroseconds(1300); // 1.7 ms -> counterclockwise
  delay(1000);
  servoRight.writeMicroseconds(1700); // 1.3 ms -> clockwise
  delay(1000);
//Just move
}
}
void stopnow(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
  delay(500);
}
void forward(int time) // Forward function
{
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(500);
// Left wheel counterclockwise
// Right wheel clockwise
// Maneuver for time ms
}
void turnLeft(int time) // Left turn function
{
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  delay(500);
}
void turnRight(int time) // Right turn function
{
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(500);
}
void backward(int time) // Backward function
{ servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}
