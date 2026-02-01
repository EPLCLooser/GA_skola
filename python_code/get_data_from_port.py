# Lucas Norrflod
# Takes information from arduino through USB-port and writes it in a txt file

from serial.tools import list_ports
import serial, sys, os

ports = list_ports.comports()
for port in ports:
    print(port)
    if "USB-enhet" in str(port):
        ard_port = str(port)[0:4]

txt_dir = os.getcwd() + "\\data.txt"
baudrate = 115200 # Baudrate of arduino

try:
    with open(txt_dir, "x") as f:
      pass
except FileExistsError:
   print("You are about to delete all data in data.txt, are you sure?\n[y] [n]")
   inp = input()
   if inp != "y":
      exit()
   pass

with open(txt_dir, "w") as f:
    f.write("") 

ser = serial.Serial(ard_port,baudrate,timeout=0.001)

while True:
    data = ser.read(1)
    data += ser.read(ser.inWaiting())
    data = str(data)[2:-1]
    if data != "":
        with open(txt_dir, "w") as f:
            f.write(data)
    sys.stdout.flush()
