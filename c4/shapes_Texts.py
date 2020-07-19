import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# print(img)
# img[200:300, 100:300] = 255, 0, 0
cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 255), 3)

cv2.rectangle(img, (img.shape[0]//2-50, img.shape[1]//2-50), (img.shape[0]//2+50, img.shape[1]//2+50),(255,0,0),2)
# img = cv2.imread('../Resources/lambo.PNG')

cv2.circle(img,(img.shape[0]//2,img.shape[1]//2),50,(255,255,0),1)

cv2.putText(img,'OpenCV GOLD',(50,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
cv2.imshow('img', img)

cv2.waitKey(0)