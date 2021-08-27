# -*- coding: utf-8 -*-
import serial
import glob, json
import collections
import datetime
import numpy as np
from datetime import datetime

_ser1 = serial.Serial('COM11', baudrate=115200, timeout=1)   


fi_num = datetime.now().strftime("%H_%M_%S")
while True:
    rx_1 = _ser1.readline()#.decode('latin1')
    
    try:
        ti = datetime.now().strftime("%H:%M:%S")
        if(rx_1 != ' ' ):
            print('---Time---: ', ti)
            print('rx_1: ',rx_1)
            # print('decode: ',rx_1.decode('utf-8'))
            # with open('gps1_' + fi_num + '.txt', 'a') as fout:    
            #     json.dump({'time': [ti], 'rx_1': rx_1}, fout) 

         
            
    except ValueError:
        print('ValueError')