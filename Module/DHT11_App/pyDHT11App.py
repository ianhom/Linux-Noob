#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
This is a python program which realise temperatrue and humidity detecting for NanoPi NEO and M1.
Use the default driver and the DHT11 sensor must be connected to the NanoPi
'''

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

    # Print the value of Temperatrue and Humidity.
    print "Temp: %s°C\nHumi: %s%%" % (temp,humi);

    print "\n**Please press Ctrl+C to exit**"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    os.system("rmmod dht11");  # Remove the driver of DHT11
    
    # Update every 2 second
    time.sleep(2);
