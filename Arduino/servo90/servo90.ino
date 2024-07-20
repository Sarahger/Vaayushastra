#include <Servo.h> 

Servo myservo;
int input;
void setup() 
{ 
  myservo.attach(9);
  Serial.begin(9600);
  //myservo.write(75);
  myservo.write(0);
} 

void loop() {
    //input = Serial.read();
    //Serial.println(input);
    delay (3000);
    myservo.write(0);
    delay (3000);
    myservo.write(90);

}