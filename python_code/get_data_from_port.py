# Source - https://stackoverflow.com/a
# Posted by Mahsa Hassankashi, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-18, License - CC BY-SA 4.0
#your_port_name
from serial.tools import list_ports
import serial, csv, time, sys

ports = list_ports.comports()
for port in ports:
    print(port)
    if "USB-enhet" in str(port):
        ard_port = str(port)[0:4]


baudrate = 9600 #115200
ser = serial.Serial(ard_port,baudrate,timeout=0.001)

while True:
    data = ser.read(1)
    data += ser.read(ser.inWaiting())
    data = str(data)[2:-1]
    if data != "":
        print(data)
    sys.stdout.flush()