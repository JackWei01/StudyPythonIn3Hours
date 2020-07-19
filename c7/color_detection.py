import  cv2
import  numpy as np


path = '../Resources/lambo.PNG'


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def empty(para1):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow("TrackBars",640,240)
# 首个数值表示预设值 第二个是范围的边界值 从零开始
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)#Hue [0-179]
cv2.createTrackbar("Hue max","TrackBars",33,179,empty)#Hue [0-179]
cv2.createTrackbar("Sat min","TrackBars",167,255,empty)#Hue [0-179]
cv2.createTrackbar("Sat max","TrackBars",255,255,empty)#Hue [0-179]
cv2.createTrackbar("Val min","TrackBars",63,255,empty)#Hue [0-179]
cv2.createTrackbar("Val max","TrackBars",255,255,empty)#Hue [0-179]




img = cv2.imread(path)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")

    print(h_min, h_max,s_min, s_max, v_min, v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(img_hsv,lower,upper)

    img_result = cv2.bitwise_and(img,img,mask=mask)

    # cv2.imshow('img',img)
    # cv2.imshow('img HSV',img_hsv)
    # cv2.imshow('img HSV',img_hsv)
    # cv2.imshow('MASK',mask)
    # cv2.imshow('img result',img_result)
    img_output = stackImages(0.6,([img,img_hsv],[mask,img_result]))

    cv2.imshow('ouput',img_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break







    # cv2.imshow('Track',img)




