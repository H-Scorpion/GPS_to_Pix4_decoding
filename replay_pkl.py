import time
import serial
import joblib

# filename ='demoGps.pkl'
filename ='ubxPacket_20210901-165743.pkl'
all_objs = joblib.load('./gpsData/' + filename)

ser = serial.Serial('COM12', 115200, timeout=None)

timestamp_start = time.time()

for timestamp, obj in all_objs:

    while (time.time() - timestamp_start) < timestamp:
        time.sleep(0.001)
        
        

    try:
        if obj._id == 7:
            # for k,v in obj.items():
            #     if k != 'lon' and k!='lat':
            #         obj[k]=0
            # print(obj.Fields.__dict__.keys())
            obj.lon=obj.lon+5000000  # adding 1 for 10**-7degree
            obj.lat=obj.lat-5*10**7
            # print(obj)
            

        serialized = obj.serialize()
    except TypeError:
        continue
    else:
        ser.write(serialized)
        print(timestamp, 'sent:', len(serialized))
