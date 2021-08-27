import time
import serial
import joblib

all_objs = joblib.load('ubxPacket_20210827-194754.pkl')

ser = serial.Serial('COM11', 115200, timeout=None)

timestamp_start = time.time()

for timestamp, obj in all_objs:

    while (time.time() - timestamp_start) < timestamp:
        time.sleep(0.001)

    try:
        serialized = obj.serialize()
    except TypeError:
        continue
    else:
        ser.write(serialized)
        print(timestamp, 'sent:', len(serialized))
