'''
Created on 25/09/2017

@author: cody
?'''
from datetime import datetime
import ntplib
import picamera
import picamera.array
from picamera.array import PiRGBArray, PiArrayOutput
from picamera import PiCamera
import cv2
import sys, socket, select
#import pickle
#import pyinotify
#import datetime
import time
import numpy as np

import dlib
from operator import pos
import os
#cam = cv2.VideoCapture(0)

#cv2.namedWindow("test")
global x1
x1 = ntplib.NTPClient()
filenum=0
found = True
img_counter = 0
cascade_path = "haarcascade_frontalface_default.xml"
predictor_path= "shape_predictor_68_face_landmarks.dat"
count = 0
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
#shared = {"Foo":"Bar", "Parrot":"Dead"}
def distance(x,y):
    return np.sqrt(np.sum((x-y)**2))
time.sleep(0.1)
img_counter = 0
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascade_path)

# create the landmark predictor
predictor = dlib.shape_predictor(predictor_path)


from ftplib import FTP
ftp=FTP('euve249939.serverprofi24.net','cody','dragon?')
ftp.retrlines('LIST')
print "connected"

def ftpPush(filepathSource, filename, filepathDestination):
    ftp = FTP('euve249939.serverprofi24.net','cody','dragon?')
    ftp.cwd(filepathDestination)
    ftp.storbinary("STOR "+filename, open(filepathSource+filename, 'r'))
    #ftp.storlines("STOR "+filename, open(filepathSource+filename, 'r'))
    ftp.quit()

host = "euve249939.serverprofi24.net" # sys.argv[1]
port = 9009 # int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

    # connect to remote host
try :
    s.connect((host, port))

except :
    print 'Unable to connect'
    sys.exit()

print 'Connected to remote host. You can start sending messages'
sys.stdout.write('[Me] '); sys.stdout.flush()

path = '/home/pi/Desktop/'

print 'starting capture'

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    rawCapture.flush()
    image = frame.array
    #image = np.frombuffer(frame, dtype='uint8', count=640*480).reshape(480, 640)
    # show the frame
    cv2.imshow("Frame", image)
    k = cv2.waitKey(1)
    rawCapture.truncate(0)

    if k%256 == 27:
       
        break
    elif k%256 == 32:
       
        cv2.imwrite(img_name, image)
        print "SDcard : {} ms".format(time_save)
        print("{} written!".format(img_name))
        img_counter += 1
        try:
            tp = datetime.utcnow()
            s.send("hp: {}".format(tp))
        except ValueError:
            print "can't connect to time server"
        ftpPush(filepathSource=path, filename=img_name, filepathDestination='/project')
        s.send(img_name)
        timend = time.time()
        timefn = (timend - timst)*1000
        print timefn
        print("sent {}".format(img_name))
        
    elif k%256 == 100:
        timst = time.time()
       
        imgName = "face_rec_{}.jpg".format(img_counter)
        cv2.imwrite(imgName, image)
        print("{} written!".format(imgName))
        img_counter += 1
        ftpPush(filepathSource=path, filename=imgName, filepathDestination='/project')
        timend = time.time()
        timefn = (timend - timst)*1000
        print timefn
        print("sent {}".format(imgName))
        s.send(imgName)
    elif k%256 == 101:
        timst = time.time()
        img_name = "topencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, image)
        print("{} written!".format(img_name))
        img_counter += 1
        ftpPush(filepathSource=path, filename=img_name, filepathDestination='/project')
        timend = time.time()
        timefn = (timend - timst)*1000
        print timefn
        print("sent {}".format(img_name))
        s.send(img_name)

cam.release()

cv2.destroyAllWindows()
