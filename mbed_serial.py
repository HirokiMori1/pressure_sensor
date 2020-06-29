import serial
from time import sleep
import time
import csv

s = serial.Serial("/dev/ttyACM0", 9600)

sleep(1.0)

if __name__ == '__main__':
    pressures = []

    t1 = time.time()
    while(True):
        data = s.readline().rstrip("\n").split(",")
        #print(data)
        temperature = float(data[0])
        pressure = float(data[1])
        humidity = float(data[2])
        
        #print(temperature, pressure, humidity)
        pressures.append(pressure)

        if(time.time() - t1 > 60):
            break

        sleep(0.1)
    
    pressures.sort()

    print(pressures)

    with open('test.csv','a') as f:
        writer = csv.writer(f,lineterminator="\n")
    
        writer.writerow(pressures)