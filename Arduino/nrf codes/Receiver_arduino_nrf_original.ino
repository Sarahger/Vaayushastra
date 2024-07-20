//Mert Arduino and Tech YouTube Channel -- https://goo.gl/ivcZhW

//Add the necessary libraries
//You can find all the necessary library links in the video description
#include <SPI.h>      //SPI library for communicate with the nRF24L01+
#include "RF24.h"     //The main library of the nRF24L01+
#include <nRF24L01.h>
#define CE_PIN 7
#define CSN_PIN 8
//Define packet for the direction (X axis and Y axis)
float data[8];
RF24 radio(CE_PIN, CSN_PIN);

//Create a pipe addresses for the communicate 
const uint64_t pipe = 0xE8E8F0F0E1LL;     //common adress which the receiver will send to (acts like a pipe)

void setup(){
 
  Serial.begin(115200);
  radio.begin();                          //Start the nRF24 communicate            
  radio.openReadingPipe(1, pipe);         //Sets the address of the transmitter to which the program will receive data.
  radio.startListening();                 //Start listening 
  }

void loop(){
  if (radio.available()){                 //if transmitter is sending data
    radio.read(data, sizeof(data));   //read the data , size of data
    Serial.print("ID: ");
    Serial.print(data[0]);
    Serial.print("\t");
    Serial.print("ypr: ");
    Serial.print(data[1]);               //print the data (roll) so that python can pick it up y
    Serial.print("\t");                 //this comma will act out as a divider for axises  a
    Serial.print(data[2]);   
    Serial.print("\t");                  //this comma will act out as a divider for axises  a
    Serial.print(data[3]);
    Serial.print("\t");   
    Serial.print(data[4]);
    Serial.print(F("*C"));  
    Serial.print("\t");
    Serial.print(data[5]);
    Serial.print(F("hPa"));
    Serial.print("\t");
    Serial.print(data[6]);
    Serial.print(F("m")); 
    Serial.print("\t");
    Serial.print(data[7]);
    Serial.print("m/s");
    Serial.print("\t");
    Serial.print("\t");
    Serial.print("Size: ");
    Serial.println(sizeof(data));
    Serial.println("-----------------------------------------------------------------------------------------------"); 
    }
}
