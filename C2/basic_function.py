import cv2
import numpy as np

img = cv2.imread('../Resources/lena.png')
kernel = np.ones((5, 5), np.uint8) #定义内核 矩阵


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)#高斯模糊
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('Gray img', imgGray)
cv2.imshow('Blur img', imgBlur)
cv2.imshow('Canny img', imgCanny)
cv2.imshow('Dilation img', imgDilation)
cv2.imshow('Eroded img', imgEroded)


cv2.waitKey(0)
