# Read GPS obj data and save as pkl file
# Can replay GPS obj Data in replay_pkl.py 
# to emulate GPS signal for mission planner

import joblib
import datetime
import time
import json
import serial
from ubx import UBXManager

filename = f'./gpsData/ubxPacket_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}'
obj_id_to_attrs = {}

def obj_to_dict(obj):
    try:
        attrs = obj_id_to_attrs[obj._id]
    except KeyError:
        attrs = obj_id_to_attrs[obj._id] = [k for k in obj.Fields.__dict__.keys() if not k.startswith('__')]
    return {attr: getattr(obj, attr, 'No Data') for attr in attrs}


def my_onUBX(obj):
    timestamp = time.time() - timestamp_start

    print(timestamp, obj)

    try:
        with open(filename + '.log','ab') as f:
            f.write(obj.serialize())
    except TypeError:
        print('obj.serialize() TypeError')

    with open(filename + '.txt','a') as f:
        f.write(f'{timestamp}, {json.dumps(obj_to_dict(obj), default=str)}\n')
    
    all_recv.append(
        (timestamp, obj)
    )


def my_onUBXError(msgClass, msgId, errMsg):
    print(msgClass, msgId, errMsg)


if __name__ == '__main__':
    with open('./ComPort.txt','r') as f:
        comPort = f.read()
    ser = serial.Serial(comPort, 115200, timeout=None)
    manager = UBXManager(ser, debug=True, eofTimeout=3.)

    manager.onUBX = my_onUBX
    manager.onUBXError = my_onUBXError

    timestamp_start = time.time()
    all_recv = []
    manager.start()

    try:
        while True:
            time.sleep(1.)
    except KeyboardInterrupt:
        print('KeyboardInterrupt detected. Shutdown...')
    finally:
        manager.shutdown()
        joblib.dump(all_recv, filename + '.pkl')