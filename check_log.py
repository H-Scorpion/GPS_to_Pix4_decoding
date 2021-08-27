import time
import joblib

with open('UBX.log', 'rb') as f:
    all_logs = f.read()

print('all_logs len=', len(all_logs))

all_objs = joblib.load('ubxPacket_20210827-194754.pkl')
timestamp_start = time.time()

for timestamp, obj in all_objs:

    # while (time.time() - timestamp_start) < timestamp:
    #     time.sleep(0.001)

    try:
        serialized = obj.serialize()
    except TypeError:
        serialized = b''
        exist = False
    else:
        exist = serialized in all_logs

    print(timestamp, len(serialized), exist)

    if len(serialized) == 0:
        print(obj)