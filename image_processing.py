import cv2 as cv
import matplotlib.pyplot as plt

def find_center(spot):
    # print(spot)
    center = [0,0]
    sum_x = 0
    sum_y = 0
    for cordinate in spot:
        print(cordinate[1], " ", cordinate[0])
        sum_x += cordinate[1]
        sum_y += cordinate[0]
    length = len(spot)
    center[0] = sum_y/length
    center[1] = sum_x/length
    
    return center

#IMG_PATH = r"C:\Users\jrkin\Downloads\nedubla.jpg"
IMG_PATH = r"C:\Users\jrkin\Downloads\laser3.png"
original = cv.imread(IMG_PATH)
convertedArray = cv.cvtColor(original, cv.COLOR_BGR2RGB)
hsv = cv.cvtColor(original, cv.COLOR_BGR2HSV)
dim = hsv.shape

laser = []

for y in range(dim[0]):
    for x in range(dim[1]):
        temp = hsv[y,x]
        a = temp[1]
        b = temp[2]
        if (a > 250 and b > 215):
            coord = [y,x]
            laser.append(coord)
print(len(laser))
# print(dim[0]," ", dim[1])
# print(laser)
# print("\n\n")
print(find_center(laser))
plt.imshow(hsv)
plt.show()
