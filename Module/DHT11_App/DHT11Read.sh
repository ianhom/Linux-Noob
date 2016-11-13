#!/bin/bash

modprobe dht11 gpio=203

gcc DHT11TempApp.c -o dht11AppTemp
gcc DHT11HumidityApp.c -o dht11AppHumitidy

./dht11AppHumitidy
./dht11AppTemp

rmmod dht11
