import numpy as np
import cv2
import os
import time
class Detection:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        self.smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
        
    def detect_face(self,gray,frame):
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        return frame
    def detect_eyes(self,gray, frame):
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+int(h/2), x:x+w]
            roi_color = frame[y:y+int(h/2), x:x+w]
            eyes = self.eyes_cascade.detectMultiScale(roi_gray, 1.02, 30)
            for (ex, ey, ew, eh) in eyes[:2]:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        return frame
    
    def detect_smile(self,gray, frame):
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y+int(h/2):y+h, x:x+w]
            roi_color = frame[y+int(h/2):y+h, x:x+w]
            smile = self.smile_cascade.detectMultiScale(roi_gray, 1.07, 45)
            for (sx,sy,sw,sh) in smile[:1]:
                cv2.rectangle(roi_color,(sx,sy), (sx+sw, sy+sh), (0,0,255),4)
                break
        return frame

class Recognizer:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        self.smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
        
    def recognize_face(self,cap):
        name = str(input('Type the name: '))
        path = '/Users/user/Desktop/FaceRecognation/'+name+'/'
        os.makedirs(path)
        i = 0
        while i < 20:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                sub_face = gray[y:y+h, x:x+w]
                FaceFileName = name + "/face_" + str(i) + ".jpg"
                cv2.imwrite(FaceFileName, sub_face)
                time.sleep(0.3)
            i+=1