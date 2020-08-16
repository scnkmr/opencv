import cv2
csd=cv2.CascadeClassifier(r"C:\Users\abc\numpy\frontalFace10/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while(True):
    fa,frame=cap.read()
    imgray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=csd.detectMultiScale(imgray,1.05,9)
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Videos Rock",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
