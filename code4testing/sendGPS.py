import serial
import time
import threading

exit_event = threading.Event()

def serSend():
    ser = serial.Serial('COM11',115200, timeout=0.1)
    while True:
        print('send:This is data for test')
        ser.write('This is data for test'.encode())
        time.sleep(1)
        if exit_event.is_set():
            break
    print('send thread terminated...')


if __name__ == '__main__':
    t = threading.Thread(target=serSend)
    t.start()

    ser = serial.Serial('COM12',115200, timeout=0.1)
    try:
        while True:
            msg = ser.read(100)
            print(msg)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('KeyboardInterrupt...')
        exit_event.set()
        t.join()
        print('recv thread terminated...')
        

