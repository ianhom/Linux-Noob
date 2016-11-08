#!/bin/bash

modprobe dht11 gpio=203

./dht11AppHumitidy
./dht11AppTemp

rmmod dht11
