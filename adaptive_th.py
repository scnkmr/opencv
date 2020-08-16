import cv2
import numpy as np
img=cv2.imread("my.jpg",0)
adt=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("Original",img)
cv2.imshow("threshold",adt)
cv2.waitKey(0)
cv2.destroyAllWindows()
