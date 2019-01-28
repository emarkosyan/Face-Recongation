# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
c = cv2.VideoCapture(0)

def cam(x):
  pass


while(True):
    cv2.createTrackbar("Grayscale", "frame", 0, 255, cam)
    cv2.createTrackbar("Red", "frame", 0, 255, cam)
    cv2.createTrackbar("Blur","frame", 0, 100, cam)
    cv2.createTrackbar("Text","frame", 0, 1, cam)
    cv2.createTrackbar("Intensity", "frame", 0, 255, cam)
    cv2.createTrackbar("Trasholding", "frame", 0, 255, cam)
    
    ret, frame = c.read()
    
    if(cv2.getTrackbarPos("Grayscale","frame") > 0):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if(cv2.getTrackbarPos("Red","frame") > 1):
        b,g,r = cv2.split(frame)
        r_eq=cv2.equalizeHist(r)
        frame = cv2.merge((b,g,r_eq))
    cv2.imshow("frame",frame)
    
    if(cv2.getTrackbarPos("Intensity","frame") > 0):
        x = cv2.getTrackbarPos("Intensity","frame")
        frame[frame > 255-x]=255
        frame[frame != 255]+=x
    
    if(cv2.getTrackbarPos("Trasholding","frame") > 0):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,3)
    
    if (cv2.getTrackbarPos("Blur","frame") != 0):
        frame = cv2.GaussianBlur(frame,(5, 5),0)
        
    if(cv2.getTrackbarPos("Text","frame") == 1):
        frame = cv2.putText(frame,"Track 4 pressed", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break
c.release()
cv2.destroyAllWindows()