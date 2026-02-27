# Source - https://stackoverflow.com/a
# Posted by Mahsa Hassankashi, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-18, License - CC BY-SA 4.0
#your_port_name
from serial.tools import list_ports
import serial, csv, time, sys, os

ard_port = None

ports = list_ports.comports()
for port in ports:
    if "USB-enhet" in str(port):
        ard_port = str(port)[0:4]

txt_dir = f"{os.getcwd()}\python_code\data.txt"
print(txt_dir)
if ard_port == None:  ard_port = "COM5"

baudrate = 115200 #Baudrate for arduino
ser = serial.Serial(ard_port,baudrate,timeout=0.001)

while True:
    data = ser.read(1)
    data += ser.read(ser.inWaiting())
    data = str(data)[2:-1]
    if data != "":
        with open(txt_dir, "a") as f:
            f.write(f"{data}\n")
    sys.stdout.flush()

