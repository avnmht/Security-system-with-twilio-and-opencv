import cv2,time
from twilio.rest import Client 
video=cv2.VideoCapture(0)
a=1
b=3
while True:
    a=a + 1
    check,frame=video.read()
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    if faces is not None:
        if b>0:
            account_sid = 'ACbcea9c59574a613760875bfa4835cb79'
            auth_token = 'e2bb8c32fda4c3ead9440e2003643341'
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_='+15104220161',body='Somebody is trying to use your Laptop....Hurry Up!!!!',to='+917799549112')
            print(message.sid)
            b=b-1
        for x,y,w,h in faces:
            imgs=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            
    cv2.imshow('capturing', imgs)
    key=cv2.waitKey(1)
    
    if key==ord('q'):
        break
    faces=None
print(a)
video.release()
cv2.destroyAllWindows()
