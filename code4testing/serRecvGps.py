import serial
import time

ser = serial.Serial('COM12',115200, timeout=0.1)
while True :
    msg = ser.read(100)
    print(msg)
    time.sleep(0.1)

