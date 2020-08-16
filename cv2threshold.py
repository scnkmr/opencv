import cv2
import numpy as np

img=cv2.imread("my.jpg",1)
th,t=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
cv2.imshow("original",img)
cv2.imshow("image",t)
cv2.waitKey(0)
cv2.destroyAllWindows()
