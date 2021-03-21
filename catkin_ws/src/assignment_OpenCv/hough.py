import cv2
import numpy as np
img = cv2.imread('test1.jpg')
print(img.shape)
crop_img = img[int(478*2/3-50):int(478)][1:int(638)]
#kernel = np.ones((3,3),np.float32)/9
#img1 = cv2.filter2D(crop_img,-1,kernel)
img1 = cv2.GaussianBlur(crop_img,(9,9),0)			#change filter type
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#img1 = cv2.GaussianBlur(gray,(5,5),0)			#change filter type
edges = cv2.Canny(gray,40,80,apertureSize = 3)
#cv2.imshow('1', edges)
#cv2.waitKey(0)
minLineLength = 10
maxLineGap = 1
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
print(lines)

try:
	for x1,y1,x2,y2 in lines[0]:
		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
except:
	print("An exception occurred") 

cv2.imwrite('houghlines5.jpg',img)

cv2.imshow('1', edges)
cv2.waitKey(0)
