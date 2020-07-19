import cv2

img = cv2.imread('../Resources/lambo.PNG')
print(img.shape)#打印图片的宽高和通道数

# Resize img
img_resize = cv2.resize(img, (300, 200))
print(img_resize.shape)


#crop img OpenCV funcs Unused
img_cropped = img[0:200, 200:500]    #[height,width]

cv2.imshow('img', img)
cv2.imshow('img Resize', img_resize)
cv2.imshow('img Cropped', img_cropped)


cv2.waitKey(0)