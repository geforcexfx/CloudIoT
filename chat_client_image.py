# chat_client.py

import sys, socket, select
import numpy as np
import ntplib
import dlib
from operator import pos
import pyinotify
import cv2
import sys
#import datetime
import time
import os
from datetime import datetime
global data1
data1 = ""
global filenum
filenum = 0
global found
found = True
img_counter = 0
cascade_path = "haarcascade_frontalface_default.xml"
predictor_path= "shape_predictor_68_face_landmarks.dat"
count = 0
#shared = {"Foo":"Bar", "Parrot":"Dead"}
def distance(x,y):
    return np.sqrt(np.sum((x-y)**2))

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascade_path)

# create the landmark predictor
predictor = dlib.shape_predictor(predictor_path)

def face_rec():
    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    timestr = timestr + '.jpg'
    face_rec.image_path = '/home/cody/project/'+data1
    print face_rec.image_path
    # Read the image
    image = cv2.imread(face_rec.image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(100, 100),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
    face_rec.face_features = None
    face_rec.face_num = faces
    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
       	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

       	detected_landmarks = predictor(image, dlib_rect).parts()

        landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])

        # copying the image so we can see side-by-side
       	image_copy = image.copy()
        #save facial feature numbers according to x and y cordinate
        nose27 = np.array((landmarks[27,0],landmarks[27,1]))
       	nose30 = np.array((landmarks[30,0],landmarks[30,1]))
        mouth51 = np.array((landmarks[51,0],landmarks[51,1]))
       	mouth57 = np.array((landmarks[57,0],landmarks[57,1]))
        mouthedge54 = np.array((landmarks[54,0],landmarks[54,1]))
       	mouthedge48 = np.array((landmarks[48,0],landmarks[48,1]))
        lefteye39 = np.array((landmarks[39,0],landmarks[39,1]))
       	lefteye36 = np.array((landmarks[36,0],landmarks[36,1]))

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
        #to normalize the number, devide by h

       	face_rec.face_feature= np.array(( dist_nose/h, dist_mouth/h, dist_mouthedg/h, dist_leye/h, dist_reye/h, dist_lface/h, distwface/h))

        for idx, point in enumerate(landmarks):
            pos = (point[0, 0], point[0, 1])
            cv2.putText(image_copy, str(idx), pos,
               	        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                       	fontScale=0.4,
                        color=(0, 0, 255))

            # draw points on the landmark positions
       	    cv2.circle(image_copy, pos, 3, color=(0, 255, 255))
            cv2.imwrite(timestr,image)

def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

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

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            if sock == s:
                # incoming message from remote server, s
                global data1
		data1 = sock.recv(4096)
                # print data1

                if not data1 :
                            print '\nDisconnected from chat server'
                            sys.exit()
                else :
                    print "Data is: ", data1[0], " ", data1
                    if data1[0] == 'o':
                        time_start = time.time()
			ts = datetime.utcnow()
			sys.stdout.flush()
			face_rec()
			print (face_rec.image_path)
                        cuong = np.array((42.0/187, 23.0/187, 56.0089278598/187, 25.079872408/187, 23.0217288664/187, 126.015872016/187, 156.012819986/187))
                        
			if len(face_rec.face_num)<0.5:
				print "no face"
			else:
                        	match1 = distance(face_rec.face_feature,cuong)
				match = np.linalg.norm(face_rec.face_feature-cuong)			
        	                print match
				print match1
                        	if match < 0.07:
	                            print "it's Cuong"
        	                else:
                	            print "Someone else!"
				time_end = time.time()
				time_done = (time_end-time_start)*1000
				print "finish time: "
				print time_done
				s.send("hs: {}".format(ts))
				
                    elif data1[0] == 'f':
			time_start = time.time()
			global found
			global filenum	
                        
			face_rec()
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
				print "no face!"
			else:
				str1= str(face_rec.face_feature).replace('\n','')
				str2= str1.replace(']','')
                        	filew = open("person_{}.txt".format(filenum),"w+")
                        	print str2
				filew.write(str2)
                        	found = True
		    elif data1[0] == 't':
			time_start_t=time.time()
			print "process t"
			lst_feature = []
			face_rec()
			if len(face_rec.face_num)<0.5:
				print "no face"
			else: 

				for file in os.listdir("/home/cody/"):
    					if file.endswith(".txt"):
        					ret = open(file, 'r').readlines()
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
                   		 
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())

