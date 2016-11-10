#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import datetime

while True:
    os.system("modprobe dht11 gpio=203");  # Load the driver of DHT11
    os.system("clear");
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "This is a python app for DHT11!";
    now = datetime.datetime.now();
    print now.strftime('%Y-%m-%d %H:%M:%S');
    print

    # Read the humi value
    f = open("/sys/devices/platform/dht11/iio:device0/in_humidityrelative_input","r");
    humi = f.readline(2);
    f.close()

    # Read the temp value
    f = open("/sys/devices/platform/dht11/iio:device0/in_temp_input","r");
    temp = f.readline(2);
    f.close()

    print "Temp: %s°C\nHumi: %s%%" % (temp,humi)

    print "\n**Please press Ctrl+C to exit**"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    os.system("rmmod dht11");  # Remove the driver of DHT11
    time.sleep(1);
