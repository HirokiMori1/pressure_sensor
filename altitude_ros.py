#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import rospy
import serial
import time

from std_msgs.msg import Float32


class Altitude():
    def __init__(self):
        self.pub = rospy.Publisher("/altitude", Float32, queue_size=10)
        self.s = serial.Serial("/dev/ttyACM0", 9600)

        self.pressure = 0.0;
        self.temperature = 0.0;

    #気圧、気温データ取得
    def get_pressure(self):
        data = self.s.readline().rstrip("\n").split(",")
        
        self.temperature = float(data[0])
        self.pressure = float(data[1])
    
    def publish_altitude(self):
        self.get_pressure()

        altitude = Float32()

        altitude.data = (((1013.25/(self.pressure+0.0001))**(1/5.257)-1)*(self.temperature+273.15))/0.0065

        print(altitude.data)

        self.pub.publish(altitude)

if __name__ == "__main__":
    rospy.init_node("get_altitude")
    altitude = Altitude()

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        altitude.publish_altitude()
        rate.sleep()
    rospy.spin()
