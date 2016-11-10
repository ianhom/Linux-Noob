#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import datetime

while True:
    os.system("modprobe dht11 gpio=203");
    os.system("clear");
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "This is a python app for DHT11!";
    now = datetime.datetime.now();
    print now.strftime('%Y-%m-%d %H:%M:%S');
    print

    f = open("/sys/devices/platform/dht11/iio:device0/in_humidityrelative_input","r");
    humi = f.readline(2);
    f.close()

    f = open("/sys/devices/platform/dht11/iio:device0/in_temp_input","r");
    temp = f.readline(2);
    f.close()

    print "Temp: %s Celsius\nHumi: %s%%" % (temp,humi)

    print "\n**Please press Ctrl+C to exit**"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    os.system("rmmod dht11");
    time.sleep(1);
