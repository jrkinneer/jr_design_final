#! /usr/bin/python
import serial
ser = serial.Serial('DSD TECH' , 9600)
print(ser.name)

ser_bytes = ser.readline()
print = ser_bytes