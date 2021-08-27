import serial

ser = serial.Serial('COM11', 9600, timeout=None)

try:
    while True:
        s = ser.read(128)
        print(s)
except KeyboardInterrupt:
    ser.close()
