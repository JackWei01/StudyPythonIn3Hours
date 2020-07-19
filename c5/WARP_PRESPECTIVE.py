import cv2
import numpy  as np


img = cv2.imread('../Resources/cards.jpg')

pts1 = np.float32([[110,221],[288,188],[154,474],[350,439]])

width,height = 250,350
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

martix = cv2.getPerspectiveTransform(pts1,pts2)


imgOutput= cv2.warpPerspective(img,martix,(width,height))

cv2.imshow("Image Output", imgOutput)

cv2.imshow("Image", img)



cv2.waitKey(0)