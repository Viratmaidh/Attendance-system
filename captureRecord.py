import cv2
import numpy as np 
import sqlite3
import os
import playsound
import tkinter
from tkinter import messagebox
from tkinter import *

uname =""
conn = sqlite3.connect('database.db')

if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c = conn.cursor()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  if faces is ():
    return None

  for (x, y, w, h) in faces:
    cropped_face = img[y:y + h, x:x + w]

  return cropped_face


cap = cv2.VideoCapture(1)

root=Tk()
root.configure(background="white")
# -------------------------------------------
def getInput1():
  global uname
  inputValue = textBox.get("1.0","end-1c")
  if inputValue != "":
    uname = inputValue
  else:
    print('Please enter the name. it is mandatory')
    root.withdraw()
    messagebox.showwarning("Warning", "Please enter the name. It is mandatory field...")
    exit()
  print(inputValue)
  root.destroy()

L1 = Label(root, text = 'Enter Your Name : ',font=("times new roman",12))
L1.pack()
textBox = Text(root, height=1, width = 20,font=("times new roman",12),bg="Pink",fg='Red')
textBox.pack()
textBox.focus()
buttonSave = Button(root, height = 1, width = 10,font=("times new roman",12), text = "Save", command = lambda:getInput1())
buttonSave.pack()
# buttonQuit = Button(root, height = 1, width = 10,font=("times new roman",12), text = "Exit", command = lambda:quit())
# buttonQuit.pack()
mainloop()
# -------------------------------------------
# uname = input("Enter your name: ")
c.execute('INSERT INTO users1 (name) VALUES (?)', (uname,))
uid = c.lastrowid
count = 0
while True:
  ret, frame = cap.read()
  # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  # for (x,y,w,h) in faces:
  #   sampleNum = sampleNum+1
  #   cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
  #   cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
  #   cv2.waitKey(100)
  # cv2.imshow('img',img)
  # cv2.waitKey(1);
  # if sampleNum >= 20:
  # break
  if face_extractor(frame) is not None:
    count += 1
    face = cv2.resize(face_extractor(frame), (150, 150))
    # face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    file_name_path = 'DataSet/User.'+str(uid)+"."+str(count)+'.jpg'
    # file_name_path1 = 'DataSet/frame'+str(count)+'.jpg'

    cv2.imwrite(file_name_path, face)
    # cv2.imwrite(file_name_path1,frame)

    cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
    cv2.imshow('Face Cropper', face)
  else:
    print("Face not Found")
    pass
  if cv2.waitKey(1) == 13 or count == 20:
    break

print("\nSamples captured successfully...")
# playsound.playsound('sound.mp3')

cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()