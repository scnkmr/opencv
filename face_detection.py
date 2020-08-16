import cv2 as cv
csd=cv.CascadeClassifier(r"C:\Users\abc\numpy\frontalFace10/haarcascade_frontalface_default.xml")
img=cv.imread("my.jpg")
gimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face=csd.detectMultiScale(gimg,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in face:
    img1=cv.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),3)


cv.imshow("image",img1)
cv.waitKey(0)
cv.destroyAllWindows()
