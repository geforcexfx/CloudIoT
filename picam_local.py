import picamera
import picamera.array
from picamera.array import PiRGBArray, PiArrayOutput
from picamera import PiCamera
import time
import cv2
import sys, socket, select
import numpy as np

import dlib
from operator import pos
import pyinotify
import cv2
import sys
import datetime
import time
import os
# initialize the camera and grab a reference to the raw camera capture
global filenum
filenum = 0
global found
found = True
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
def distance(x,y):
    return np.sqrt(np.sum((x-y)**2))

time.sleep(0.1)
img_counter = 0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
predictor_path= "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
def face_rec(img):

    image = img
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(100, 100),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
    face_rec.face_feature=None
    
    face_rec.face_num = faces
    print("Found {0} faces!".format(len(faces)))
    if len(faces)<0.5:
        print "face please!"
    else :
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

            detected_landmarks = predictor(image.copy(), dlib_rect).parts()

            landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])

            # copying the image so we can see side-by-side
            image_copy = image.copy()
            #print landmarks[1,0]
            nose27 = np.array((landmarks[27,0],landmarks[27,1]))
            nose30 = np.array((landmarks[30,0],landmarks[30,1]))
            mouth51 = np.array((landmarks[51,0],landmarks[51,1]))
            mouth57 = np.array((landmarks[57,0],landmarks[57,1]))
            mouthedge54 = np.array((landmarks[54,0],landmarks[54,1]))
            mouthedge48 = np.array((landmarks[48,0],landmarks[48,1]))
            lefteye39 = np.array((landmarks[39,0],landmarks[39,1]))
            lefteye36 = np.array((landmarks[36,0],landmarks[36,1]))
            #print lefteye36
            righteye45 = np.array((landmarks[45,0],landmarks[45,1]))
            righteye42 = np.array((landmarks[42,0],landmarks[42,1]))
            facelength27 = np.array((landmarks[27,0],landmarks[27,1]))
            facelength8 = np.array((landmarks[8,0],landmarks[8,1]))
            facewidth0 = np.array((landmarks[0,0],landmarks[0,1]))
            facewidth16 = np.array((landmarks[16,0],landmarks[16,1]))
            dist_nose = distance(nose27,nose30)

            dist_mouth = distance(mouth51,mouth57)
            dist_mouthedg = distance(mouthedge54,mouthedge48)
            dist_leye = distance(lefteye39,lefteye36)
            dist_reye = distance(righteye45,righteye42)
            dist_lface = distance(facelength27, facelength8)
            distwface = distance(facewidth16, facewidth0)

            face_rec.face_feature= np.array(( dist_nose/h, dist_mouth/h, dist_mouthedg/h, dist_leye/h, dist_reye/h, dist_lface/h, distwface/h))
          
            print face_rec.face_feature
            #to normalize the number, devide by 187


            for idx, point in enumerate(landmarks):
                pos = (point[0, 0], point[0, 1])

    # annotate the positions
                cv2.putText(image_copy, str(idx), pos,
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.4,
                            color=(0, 0, 255))

    # draw points on the landmark positions
                cv2.circle(image_copy, pos, 3, color=(0, 255, 255))
   

print 'starting capture'

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    rawCapture.flush()
    image = frame.array
        # show the frame
    cv2.imshow("Frame", image)
    k = cv2.waitKey(1)
    rawCapture.truncate(0)

    if k%256 == 27:
        break
    
    elif k%256 == 32:
        time_start = time.time()    
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
        print("Found {0} faces!".format(len(faces)))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #image = rawCapture.array
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        time_end = time.time()
        time_done = (time_end-time_start)*1000
        cv2.putText(image,str(time_done),(10,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        print time_done
        cv2.imwrite(img_name, image)
        img_counter += 1

    elif k%256 == 99:
        time_start = time.time()
        print 'this is process'
        
        face_rec(image)
        
        cuong = np.array((42.0/187, 23.0/187, 56.0089278598/187, 25.079872408/187, 23.0217288664/187, 126.015872016/187, 156.012819986/187))
        match = np.linalg.norm(face_rec.face_feature-cuong)         
        print match
        
        if match < 0.07:
            print "it's Cuong"
        else:
            print "Someone else!"
        time_end = time.time()
        time_done = (time_end-time_start)*1000
        print "finish time: "
        print time_done
    
    elif k%256 == 100:
        time_start = time.time()
        global found
        global filenum	
        
        face_rec(image)
        print len(face_rec.face_num)
        if len(face_rec.face_num) < 0.5:
                found = False
                print "Face please!!!"
        else:
                found = True
        while found:

            name = './person_{}.txt'.format(filenum)
            if os.path.isfile(name):
                print "Found file ", name
                found = True;
                filenum = filenum+1

            else:
                found = False
                print "Not found ", name
        if len(face_rec.face_num)<0.5:
            print "no face"
        else: 
            #print face_rec.face_feature
            str1 = str(face_rec.face_feature).replace('\n','')
            str2 = str1.replace(']','')
            filew = open("person_{}.txt".format(filenum),"w+")
            
            filew.write(str2)
            found = True
    #elif c=="i":
    elif k%256 ==101:
        time_start_t=time.time()
        print "process t"
        lst_feature = []
        face_rec(image)
        if len(face_rec.face_num) < 0.5:
            print "face please!"
        else :
            for file in os.listdir("/home/pi/Desktop"):
                    if file.endswith(".txt"):
                            print(os.path.join("/home/pi/Desktop", file))
                            ret = open(file, 'r').readlines()
                            
                            print ret
                            print type(ret)
                            
                            N=len(ret)
                            for i in range(0,N):
                                    w=ret[i].split()
                                    l1=w[1:8]
                                    list1=[float(x) for x in l1]
                                    result = np.array(list1)
                                    lst_feature.append(result)
            sum_feature=np.sum(lst_feature, axis = 0)
            average = sum_feature/len(lst_feature)
            avr_dist = distance(face_rec.face_feature,average)
            print "avr_dist: "
            print avr_dist
            if avr_dist<0.07:
                    print "it's Cuong"
            else:
                    print "someone else"


            time_end_t= time.time()
            time_done_t= (time_end_t-time_start_t)*1000
            
            print "time finish: "
            print time_done_t	

cv2.destroyAllWindows()
