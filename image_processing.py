import cv2 as cv
import matplotlib.pyplot as plt

#IMG_PATH = r"C:\Users\jrkin\Downloads\nedubla.jpg"
IMG_PATH = r"C:\Users\jrkin\Downloads\laser3.png"
original = cv.imread(IMG_PATH)
convertedArray = cv.cvtColor(original, cv.COLOR_BGR2RGB)
hsv = cv.cvtColor(original, cv.COLOR_BGR2HSV)
dim = hsv.shape

laser = []
#asdlfkja test
for y in range(dim[0]):
    for x in range(dim[1]):
        temp = hsv[y,x]
        a = temp[1]
        b = temp[2]
        if (a > 250 and b > 215):
            coord = [y,x]
            laser.append(coord)

print(dim[0]," ", dim[1])
print(laser)

plt.imshow(hsv)
plt.show()

#print(cv.minMaxLoc(original))

# green = convertedArray[:,:,1]
# print(cv.minMaxLoc(green))
# plt.imshow(green)
# plt.show()
# cv.imshow('green', green)
# cv.waitKey(0)
# cv.destroyAllWindows()

#max by rgb to grayscale
# gray = cv.cvtColor(convertedArray, cv.COLOR_RGB2GRAY)
# print(cv.minMaxLoc(gray))
# plt.imshow(gray)
# plt.show()
# cv.imshow('gray', gray)
# cv.waitKey(0)
# cv.destroyAllWindows()
