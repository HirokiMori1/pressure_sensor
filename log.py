#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import serial
from time import sleep
import time
import csv

s = serial.Serial("/dev/ttyACM0", 9600)

sleep(1.0)

if __name__ == '__main__':
    with open('data.csv','a') as f:
        writer = csv.writer(f,lineterminator="\n")
        writer.writerow(['time','pressure[hPa]','temperature[℃]','humidity[%]'])

    t1 = time.time()
    while(True):
        data = s.readline().rstrip("\n").split(",")
        #print(data)
        temperature = data[0]
        pressure = data[1]
        humidity = data[2]
        
        print(temperature, pressure, humidity)
        print(time.time() - t1)

        with open('data.csv','a') as f:
            writer = csv.writer(f,lineterminator="\n")
            writer.writerow([str(time.time()-t1),pressure,temperature,humidity])

        if(time.time() - t1 > 3600):
            break

        sleep(5.0)

    print("finish")

