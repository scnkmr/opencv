import cv2
import numpy as np
img1=cv2.imread("my.jpg",1)
img2=cv2.imread("my2.jpg",1)
rows,cols,channels=img2.shape
#print(rows)
cv2.imshow("image",img2+img1)
cv2.waitKey()
cv2.destroyAllWindows()
