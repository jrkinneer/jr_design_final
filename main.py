import cv2 as cv
import matplotlib.pyplot as plt

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
    
            
#start infinite while loop

#look for serial input signaling image was captured

#if 
