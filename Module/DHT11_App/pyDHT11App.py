#!/usr/bin/python

import os

os.system("modprobe dht11 gpio=203");    # load driver of DHT11

print "This is a python app for DHT11!";

# Humidity read operation
f = open("/sys/devices/platform/dht11/iio:device0/in_humidityrelative_input","r");
humi = f.readline();
print "Humidity is ", humi;
f.close()

# Temp read operation
f = open("/sys/devices/platform/dht11/iio:device0/in_temp_input","r");
temp = f.readline();
print "Temp is ", temp;
f.close()

os.system("rmmod dht11");  # unload driver
