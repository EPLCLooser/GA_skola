// import libraries
#include "Wire.h"
#include <MPU6050_light.h>
#include <Adafruit_BMP085.h>
#define seaLevelPressure_hPa 1013.25
#include <SD.h>

File myFile;
Adafruit_BMP085 bmp;
MPU6050 mpu(Wire);

// initialize variables
float angleX;
float angleY;
const int chipSelect = 9;

void setup() {
  Serial.begin(9600); 
  Wire.begin();
  byte status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);

  // Inititalizing SD-card
  if (!SD.begin(chipSelect)) {
    while (1);
  }

  // Removes data.txt if it exists on SD-card
  if (SD.exists("data.txt")) {
    SD.remove("data.txt");
  } 

  while (status != 0) {}  // stop everything if could not connect to MPU6050
  mpu.calcOffsets();  // gyro and accelero
   Serial.println(F("Calculating offsets, do not move MPU6050"));
   delay(1000);
   // mpu.upsideDownMounting = true; // uncomment this line if the MPU6050 is mounted upside-down
   mpu.calcOffsets();  // gyro and accelerometer
   Serial.println("Done!\n");
  Serial.begin(9600);
    if (!bmp.begin()){
      Serial.println("bmp not found!");
      while (1);
    }
}

void loop() {

  myFile = SD.open("data.txt", FILE_WRITE);
  mpu.update();
  float angleX = mpu.getAngleX();
  float angleY = mpu.getAngleY();
  float angleZ = mpu.getAngleZ();  

  float pressure = bmp.readPressure();

  int altitude = bmp.readAltitude();


  float temp = bmp.readTemperature();
  myFile.print(angleX);
  myFile.print(",");
  myFile.print(angleY);
  myFile.print(",");
  myFile.print(angleZ);
  myFile.print(",");
  myFile.print(pressure);
  myFile.print(",");
  myFile.print(altitude);
  myFile.print(",");
  myFile.println(temp);
  myFile.close();
  myFile = SD.open("data.txt", FILE_READ);
  while(myFile.available()) {
    Serial.print((char)myFile.read());
  }
  delay(100);
}
