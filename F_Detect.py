#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:08:50 2018

@author: user
"""

import cv2
import os
from Detector import Detection
from Detector import Recognizer

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cap.set(3,640)
cap.set(4,480)
def passMe():
    pass

d = Detection()
r = Recognizer()

cv2.createTrackbar("F","frame", 0, 1, passMe)
cv2.createTrackbar("E","frame", 0, 1, passMe)
cv2.createTrackbar("M","frame", 0, 1, passMe)

while 1:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    t = cv2.getTrackbarPos('F', 'frame')
    c = cv2.getTrackbarPos('E', 'frame')
    s = cv2.getTrackbarPos('M', 'frame')
    
    if t > 0:
        frame = d.detect_face(gray, frame)
    if c > 0:
        frame = d.detect_eyes(gray, frame)
    if s > 0:
        frame = d.detect_smile(gray, frame)
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(33) == ord('a'):
        r.recognize_face(cap)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break
        
cap.release()
cv2.destroyAllWindows()