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
            account_sid = 'Your_twilio_account_sid'
            auth_token = 'Your_twilio_auth_token'
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_='Your_twilio_phone_number',body='Somebody is trying to use your Laptop....Hurry Up!!!!',to='Your_phone_number')
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
