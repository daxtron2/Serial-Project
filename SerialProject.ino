#include "Adafruit_Si7021.h"
Adafruit_Si7021 sensor = Adafruit_Si7021();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2, INPUT);

  if(!sensor.begin()){
    Serial.println("Humidity Sensor not found");
    while(true);
  }

  Serial.print("Starting Humidity: ");
  Serial.println(sensor.readHumidity(), 0);
}
void loop() {
  float humidity = sensor.readHumidity();
  bool state = false;

  if(humidity < 40.0f || humidity > 50.0f){
    state = true;
  }

  if(state){
    Serial.print("SEND|");    
  }
  else{
    Serial.print("SAFE|");
  }
  Serial.println(humidity,6);
}
