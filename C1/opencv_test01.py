import cv2
import numpy as np


img = cv2.imread("../Resources/Lenna.png") #imread 读取图片

cv2.imshow("img_output", img) #显示图片

cv2.waitKey(1000)#延时函数 1000 表示 1000ms  设为零则无限延时


def main():
    pass


if __name__ == '__main__':
    main()



