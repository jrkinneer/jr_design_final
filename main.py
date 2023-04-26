import cv2 as cv
import matplotlib.pyplot as plt
import serial as serial
import time

#define find laser spot function
def find_laser(threshold_a, threshold_b, img, dim):
    #holds all coords suspected to be part of the laser
    spot = []
    
    #loops through image
    for y in range(dim[0]):
        for x in range(dim[1]):
            temp = img[y,x]
            a = temp[1]
            b = temp[2]
            #if pixel is bright enough its coordinates are added to the spot list
            if (a > threshold_a and b > threshold_b):
                coord = [y,x]
                spot.append(coord)
    
    return spot

#calculates average of all coordinates in the spot so that the center can be sent to the arduino
def find_center(spot):
    center = [0,0]
    sum_x = 0
    sum_y = 0
    for cordinate in spot:
        sum_x += cordinate[1]
        sum_y += cordinate[0]
    length = len(spot)
    center[0] = sum_y/length
    center[1] = sum_x/length
    
    return center
    
#establish serial connection
ser = serial.Serial('COM4')
      
#start infinite while loop
while(1):
    res = ser.read()
#look for serial input signaling image was captured
    if (res == "0x30"):
        #load in image
        IMG_PATH = r"C:\Users\jrkin\Downloads\laser.png" #need to change this path for actual use
        original = cv.imread(IMG_PATH)
        hsv = cv.cvtColor(original, cv.COLOR_BGR2HSV)
        dim = hsv.shape
        
        thresh_a = 250
        thresh_b = 200
        
        spot = []
        #runs find_laser
        while (1):
            spot = find_laser(thresh_a, thresh_b, hsv, dim)
            #if list of spot coordinates is small enough loop is broke
            if (len(spot) < 100):
                break
            else:
                #if list is too long, threshold values are increased to 
                    #try and isolate the laser spots
                if (thresh_a < 255):
                    thresh_a += 1
                if (thresh_b < 255):
                    thresh_b += 5
        
        #finds center of the laser
        center = find_center(spot)
        
        ser.write("some indicator")
        time.sleep(.01)
        ser.write(center)