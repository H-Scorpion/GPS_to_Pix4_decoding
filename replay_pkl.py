import time
import serial
import joblib
from calGps import calGps

# filename ='./gpsData/demoGps.pkl'
# filename ='./gpsData/ubxPacket_20210901-165743.pkl'
filename ='fakeGps.pkl'

all_objs = joblib.load(filename)

with open('./ComPort.txt','r') as f:
    comPort = f.read()

ser = serial.Serial(comPort, 115200, timeout=None)

timestamp_start = time.time()

for timestamp, obj in all_objs:

    while (time.time() - timestamp_start) < timestamp:
        time.sleep(0.001)
        
        

    # try:
    #     correctedObj = calGps(obj)
    #     if correctedObj._id == 7:
    #         serialized = correctedObj.serialize()
    #     else:
    #         serialized = b''
    # except TypeError:
    #     continue
    # else:
        
    #     ser.write(serialized)
    #     print(timestamp, 'sent:', len(serialized))

    try: 
        if obj._id ==7:
            serialized = obj.serialize()
            ser.write(serialized)
            print(timestamp, 'sent:', len(serialized))
            print(obj)
    except TabError:
        continue
