import cv2
import numpy as np
import math
from PIL import Image

def jarak(a, b): # calculate distance between 2 points
    return math.sqrt(((b[0] - a[0]) * (b[0] - a[0])) +\
                     ((b[1] - a[1]) * (b[1] - a[1])))

def findBiggest(faces): # find biggest face
    biggest = (0,0,0,0) # set biggest face
    maxArea = 0 # set max area
    for (x,y,w,h) in faces: 
        area = w * h # calculate area
        if area > maxArea: # if area is bigger than max area
            biggest = (x,y,w,h) # set biggest face
            maxArea = area # set max area
    return biggest

def faceAlignment(img):
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_frontalface_default.xml") # load face detector
    eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_eye.xml") # load eye detector
    face_coordinate = face_detector.detectMultiScale(img) # detect face
    eyes = eye_detector.detectMultiScale(img) # detect eyes

    if (len(eyes) > 1): # if eyes detected
        if (len(eyes) > 2): # if more than 2 eyes detected
            ab = abs(eyes[0][1] - eyes[1][1]) # calculate distance between eyes
            bc = abs(eyes[1][1] - eyes[2][1]) 
            ac = abs(eyes[0][1] - eyes[2][1])
            if (ab < bc and ab < ac): # if eyes 1 and 2 are the closest
                eyes = np.delete(eyes, 2, 0) # delete eyes 3
            elif (bc < ab and bc < ac): # if eyes 2 and 3 are the closest
                eyes = np.delete(eyes, 0, 0) # delete eyes 1
            else:
                eyes = np.delete(eyes, 1, 0) # delete eyes 2
        
        eye_1 = eyes[0] # set eye 1
        eye_2 = eyes[1] # set eye 2

        if eye_1[0] < eye_2[0]: # if eye 1 is on the left
            lEye = eye_1 # set left eye
            rEye = eye_2 # set right eye
        else:
            lEye = eye_2 # set left eye
            rEye = eye_1 # set right eye

        rEye_center = (rEye[0] + int(rEye[2] / 2), rEye[1] + int(rEye[3] / 2)) # calculate right eye center
        lEye_center = (lEye[0] + int(lEye[2] / 2), lEye[1] + int(lEye[3] / 2)) # calculate left eye center
        rEye_x = rEye_center[0] # get right eye x
        rEye_y = rEye_center[1] # get right eye y
        lEye_x = lEye_center[0] # get left eye x
        lEye_y = lEye_center[1] # get left eye y

        if lEye_y > rEye_y: # if left eye is on the top
            proyeksi = (rEye_x, lEye_y) # set proyeksi
            dir = -1 #rotate image clockwise
        else:
            proyeksi = (lEye_x, rEye_y) # set proyeksi
            dir = 1 #rotate image counterclockwise

        a = jarak(lEye_center, proyeksi) # calculate distance between left eye and proyeksi
        b = jarak(rEye_center, lEye_center) # calculate distance between right eye and left eye
        c = jarak(rEye_center, proyeksi) # calculate distance between right eye and proyeksi
        cos = (b*b + c*c - a*a)/(2*b*c) # calculate cos
        sudut = (np.arccos(cos) *180) / np.pi # calculate angle

        if dir == -1: # if rotate image clockwise
            sudut = 90 - sudut # calculate angle
        else:
            angle = -(90-sudut) # calculate angle
        img = Image.fromarray(img) # convert image to PIL image
        img = np.array(img.rotate(dir * sudut)) # rotate image

    if len(face_coordinate) > 0: # if face detected
        face_x, face_y, face_w, face_h = findBiggest(face_coordinate) # get face coordinate
        img = img[face_y:face_y + face_h, face_x:face_x + face_w] # crop face


    img = cv2.resize(img, (256,256)) # resize image

    return img