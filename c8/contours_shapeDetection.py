import  cv2
import  numpy as np

path = '../Resources/shapes.png'

def getContours(img):
    countours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)

        if area> 500: #设置面积条件 以舍掉可能潜在的噪声
            cv2.drawContours(img_countours, cnt, -1, (255, 0, 0), 3)
            # 曲线周长
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            # 角点
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))# apporx的元素个数 及未知图像对应的交点个数,但不一定全是顶点！！！
            print(approx)

            objectCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objectCor == 3:
                object_type = 'Tri'
            elif objectCor == 4:
                aspRatio = w/float(h)#定义长宽比 区分矩形和正方形 注意要转为float 否则两个整数出发必时整数
                if aspRatio > 0.95 and aspRatio <1.05:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif objectCor > 4:
                object_type = 'Circle'
            else:
                object_type = "None"

            cv2.rectangle(img_countours,(x,y),(x+w,y+h),(0,200,200),2)
            cv2.putText(img_countours,object_type,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),2)
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

img = cv2.imread(path)
img_countours = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,img_countours,imgBlank]))

# cv2.imshow('original', img)
# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)
cv2.imshow('Stack img', imgStack)

cv2.waitKey(0)