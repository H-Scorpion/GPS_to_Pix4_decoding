import time
import serial
from ubx import UBXManager


def my_onUBX(obj):
    # print(obj.serialize())
    if obj._id == 0x07:
        print(obj.summary())
        # print(obj.magDec)
        # print(obj.velNED_m)
    else:
        print(f'obj._id: {obj._id}')
# def my_onUBXError(msgClass, msgId, errMsg):
#     print()

if __name__ == '__main__':
    ser = serial.Serial('COM11', 115200, timeout=None)
    manager = UBXManager(ser, debug=False, eofTimeout=3.)

    manager.onUBX = my_onUBX

    manager.start()

    try:
        while True:
            time.sleep(1.)
    except KeyboardInterrupt:
        print('KeyboardInterrupt detected. Shutdown...')
    finally:
        manager.shutdown()