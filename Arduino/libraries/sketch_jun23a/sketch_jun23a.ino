#include <Servo.h>
int rightWhiskerPin = 7;
int leftWhiskerPin = 5;
int rightWhiskerState = 0;
int leftWhiskerState = 0;
Servo servoLeft;
Servo servoRight;
//Declare Right servo
//Declare Left servo
void setup() {
// put your setup code here, to run once:

delay(1000); 
pinMode(rightWhiskerPin, INPUT);
pinMode(leftWhiskerPin, INPUT);
Serial.begin(9600);
servoLeft.attach(13);
servoRight.attach(12);
//Attach Left Servo
//Attach Right Servo
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1300);

}
void loop() {
// put your main code here, to run repeatedly:
rightWhiskerState = digitalRead(rightWhiskerPin);
leftWhiskerState = digitalRead(leftWhiskerPin);
// whisker state is 1 if unpressed and 0 if pressed.
if(rightWhiskerState == 0 && leftWhiskerState == 0){
  servoLeft.writeMicroseconds(1300);   // 
  servoRight.writeMicroseconds(1700);  // This means it's moving backwards
  delay(5000); // for 5 seconds
  servoLeft.writeMicroseconds(1700);   //
  servoRight.writeMicroseconds(1700); //move right
  delay(5000); //for 5 seconds
//Make it move away from the Obstacle
}
else if(leftWhiskerState == 0){
  servoLeft.writeMicroseconds(1300);   // 
  servoRight.writeMicroseconds(1700);  // This means it's moving backwards
  delay(3000); // for 3 seconds
  servoLeft.writeMicroseconds(1700); //
  servoRight.writeMicroseconds(1700); //move right
  delay(1000); //for a second  
//Make it move away from the Obstacle
}
else if(rightWhiskerState == 0){
  servoLeft.writeMicroseconds(1300);   // 
  servoRight.writeMicroseconds(1700);  // This means it's moving backwards
  delay(3000); // for 3 seconds
  servoLeft.writeMicroseconds(1300);   // 
  servoRight.writeMicroseconds(1300);  // move left
  delay(3000); // for a second
//Make it move away from the Obstacle
}
else{
  servoLeft.writeMicroseconds(1700);   // Left wheel clockwise
  servoRight.writeMicroseconds(1300);  // Right wheel counterclockwise
  
//Just move
}
}
void stopnow(){
 servoLeft.writeMicroseconds(1500);
 servoRight.writeMicroseconds(1500);
}
void forward(int time) // Forward function
 {  
  servoLeft.writeMicroseconds(1700);   // Left wheel clockwise
  servoRight.writeMicroseconds(1300);  // Right wheel counterclockwise
  
// Left wheel counterclockwise
// Right wheel clockwise
// Maneuver for time ms
 }
void turnLeft(int time) // Left turn function
 {
 servoLeft.writeMicroseconds(1300);   // Left wheel clockwise
 servoRight.writeMicroseconds(1300);  // Right wheel clockwise

 }
void turnRight(int time) // Right turn function
{
  servoLeft.writeMicroseconds(1700);   // Left wheel counterclockwise
  servoRight.writeMicroseconds(1700); // Right wheel counterclockwise

}
void backward(int time) // Backward function
{ 
   servoLeft.writeMicroseconds(1300);   // Left wheel clockwise
   servoRight.writeMicroseconds(1700);  // Right wheel counterclockwise
}
