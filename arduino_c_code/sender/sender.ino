// import libraries
#include "Wire.h"
//#include <MPU6050_light.h>
#include <Adafruit_BMP085.h>
#define seaLevelPressure_hPa 1013.25

Adafruit_BMP085 bmp;
//MPU6050 mpu(Wire);

// initialize variables
float angleX;
float angleY;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Remove serial when 
  //Wire.begin();

  //byte status = mpu.begin();
  //Serial.print(F("MPU6050 status: "));
  //Serial.println(status);
  //while (status != 0) {}  // stop everything if could not connect to MPU6050
  //mpu.calcOffsets();  // gyro and accelero
  // Serial.println(F("Calculating offsets, do not move MPU6050"));
  // delay(1000);
  // // mpu.upsideDownMounting = true; // uncomment this line if the MPU6050 is mounted upside-down
  // mpu.calcOffsets();  // gyro and accelero
  // Serial.println("Done!\n");
  Serial.begin(9600);
    if (!bmp.begin()){
      Serial.println("bmp not found!");
      while (1);
    }
}

void loop() {
  //mpu.update();
  //float angleX = mpu.getAngleX();
  //float angleY = mpu.getAngleY();
  //float angleZ = mpu.getAngleZ();
  //Serial.print("X: ");
  //Serial.println(angleX);
  //serial.print("Y: ");
  //Serial.println(angleY);
  //Serial.print("Z: ")
  //Serial.println(angleZ);
  Serial.print("Pressure: ");
  Serial.print(bmp.readPressure());
  Serial.println(" Pa");

  Serial.print("Altitude = ");
  Serial.print(bmp.readAltitude());
  Serial.println(" meters");

  Serial.print("Pressure at sealevel (calculated) = ");
  Serial.print(bmp.readSealevelPressure());
  Serial.println(" Pa");

  Serial.print("Temperature = ");
  Serial.print(bmp.readTemperature());
  Serial.println(" *C");
}
