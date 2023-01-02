import cv2, numpy as np;
import time
import datetime
import sqlite3
# import os
# import sys
from playsound import playsound
import csv

conn = sqlite3.connect('database.db')
c = conn.cursor()
start=time.time()
period=2
# face_cas = cv2.CascadeClassifier('haarcascade_profileface.xml')
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('recognizer/trainingData.yml');

flag = 0;
id=0;
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    H,W = gray.shape
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id,conf=recognizer.predict(roi_gray)
        # if(conf < 50):
        print(id)
        sql ='select name from users1 where id ={}'.format(id)
        print(sql)
        c.execute(sql)
        # c.execute('INSERT INTO users1 (name) VALUES (?)', (id,))
        results = c.fetchall()
        for row in results:
            sName = row[0]
        # print(sName)

        with open("Attendance.csv", 'a') as csvfile:
            fieldName1 = ['ID','SName', 'InTime']
            writer = csv.DictWriter(csvfile, fieldnames=fieldName1)
            # writer.writeheader()
            start_Time = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
            writer.writerow({'ID': id, 'SName': sName, 'InTime': start_Time})

        cv2.putText(img,str(id)+"   "+str('%3.2f'%(conf)),(x,y-10),font,0.55,(120,255,120),2)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('Attendance',img);
    #cv2.imshow('gray',gray);
    # if flag == 10:
    #     playsound('transactionSound.mp3')
    #     print("Transaction Blocked")
    #     break;

    if time.time()>start+period:      # Single time write data in csv sile
        cv2.imshow('frame', img);
        # playsound('Sound.mp3')
        cv2.waitKey(400)
        cv2.putText(img, str(start_Time), (x-50,y+h+20), font, 0.55, (255, 255, 0), 2)
        cv2.imshow('Attendance', img);
        # playsound('Sound.mp3')
        cv2.waitKey(400)
        # break;
        # os.system("python Attendance.py")
        exit()
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;
cap.release();
cv2.destroyAllWindows();
