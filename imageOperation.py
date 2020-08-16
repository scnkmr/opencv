import cv2
import numpy as np
img=cv2.imread("my.jpg",1)


watch=img[100:200,100:200]
img[25:125,25:125]=watch
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
