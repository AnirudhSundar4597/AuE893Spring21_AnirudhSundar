import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1 = cv.imread('test1.jpg')
img = cv.GaussianBlur(img1,(5,5),0)
#img = cv.GaussianBlur(img1,(4,4),0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

