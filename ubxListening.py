import joblib
import datetime
import time
import json
import serial
from ubx import UBXManager

filename = f'ubxPacket_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}'
obj_id_to_attrs = {}

def obj_to_dict(obj):
    try:
        attrs = obj_id_to_attrs[obj._id]
    except KeyError:
        attrs = obj_id_to_attrs[obj._id] = [k for k in obj.Fields.__dict__.keys() if not k.startswith('__')]
    return {attr: getattr(obj, attr, default='No Data') for attr in attrs}

def my_onUBX(obj):
    timestamp = time.time() - timestamp_start

    print(timestamp, obj)

    try:
        with open(filename + '.log','wb') as f:
            f.write(obj.serialize())
    except TypeError:
        print('obj.serialize() TypeError')
    
    with open(filename + '.txt','a') as f:
        f.write(f'{timestamp}, {json.dumps(obj_to_dict(obj), default=str)}\n')

    all_recved.append(
        (timestamp, obj)
    )

    # if obj._id == 0x07:
    #     print(obj.summary())
    #     # print(obj.magDec)
    #     # print(obj.velNED_m)
    # else:
    #     print(f'obj._id: {obj._id}')
def my_onUBXError(msgClass, msgId, errMsg):
    print(msgClass, msgId, errMsg)

# def my_onUBXError(msgClass, msgId, errMsg):
#     with open('errorPacket.txt','a') as f:
#         f.write(f'Class:{msgClass},ID:{msgId}\n')

if __name__ == '__main__':
    ser = serial.Serial('COM11', 115200, timeout=None)
    manager = UBXManager(ser, debug=True, eofTimeout=3.)

    manager.onUBX = my_onUBX
    manager.onUBXError = my_onUBXError

    timestamp_start = time.time()
    all_recved = []
    manager.start()

    try:
        while True:
            time.sleep(1.)
    except KeyboardInterrupt:
        print('KeyboardInterrupt detected. Shutdown...')
    finally:
        manager.shutdown()
        joblib.dump(all_recved, filename + '.pkl')