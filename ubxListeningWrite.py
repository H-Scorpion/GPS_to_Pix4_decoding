import joblib
import datetime
import time
import json
import serial
from ubx import UBXManager


def my_onUBX(obj):
    print(obj)

    if obj._id == 0x07:
        print(obj.summary())
        # process obj
        obj.year = 2021

        data = obj.serialize()
        print(data)

        manager.send(data)

        # print(obj.magDec)
        # print(obj.velNED_m)
    else:
        print(f'obj._id: {obj._id}')

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

    manager.start()

    try:
        while True:
            time.sleep(1.)
    except KeyboardInterrupt:
        print('KeyboardInterrupt detected. Shutdown...')
    finally:
        manager.shutdown()