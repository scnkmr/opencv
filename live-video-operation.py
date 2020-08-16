import numpy as np
import cv2
from matplotlib import pyplot as plt
'''img = cv2.imread("my.jpg",0)
cv2.imshow("My Pic",img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
cap=cv2.VideoCapture(0)

while(True):
    ret , frame = cap.read()
    cv2.circle(frame,(200,200),100,(5,5,255),10)
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    t,th = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
    adth=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

    cv2.imshow("frame", frame)
    cv2.imshow("threshold",th)
    cv2.imshow("adaptive threshold",adth)
    if cv2.waitKey(1)  & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
