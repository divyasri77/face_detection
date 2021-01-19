import cv2
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# for face detection
# img=cv2.imread('profile.jpg')
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# face=face_cascade.detectMultiScale(gray, 1.5, 7)
# for (x,y,w,h) in face:
#    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.imshow('img',img)
# cv2.waitkey(0)
cap=cv2.VideoCapture(0)
while True:
    _,img =cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    face=face_cascade.detectMultiScale(gray, 1.5, 7)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)

    k=cv2.waitKey(30)& 0xff
    if k==27:
        break
cv2.release()


