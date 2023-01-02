from tkinter import *
from playsound import playsound
import os
from datetime import datetime;

root = Tk()
root.iconbitmap('P2GO_desk.ico')
# Gray Colors #B3B4BE  , #E07229, #8C6F60, #BFAB8E, #8F9B9A
root.configure(background='#F6EBF2') #"white"

color_Title = '#900C3F'#0E6A70'
color_IM_Labels = '#F71B1B'  #'#8C6F60' #
color_Buttons = '#0D47A1'  #'#BFAB8E'
color_Exit = '#900C3F'
# root.configure(background='#E8D5D0') #"white"
# color_Title = '#5D0347'#0E6A70'
# color_IM_Labels = '#8E026C' #'#F71B1B'
# color_Buttons = '#A40C64' #'#0D47A1'
# color_Exit = '#5D0347'
def function1():
    os.system("python createDataBase.py")

def function2():
    os.system("python captureRecord.py")
    # pass


def function3():
    import shutil
    if os.path.exists('./dataset'):
        shutil.rmtree('./dataset')

def function4():
    os.system("python Training.py")


def function5():
    os.system("python Detect.py")

def function6():
    os.system("python Attendance.py")


def function7():
    os.system("Attendance.csv")


def function8():
    os.system("python AboutUs.py")
7

def function9():
    root.destroy()


root.title(" ATTENDANCE SYSTEM")

Label(root, text="AUTOMATIC ATTENDANCE SYSTEM USING FACE RECOGNITION",font=("times new roman",20),fg="white",bg=color_Title,height=2).grid(row=0,rowspan=2,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="USERS ENROLMENT ",font=("times new roman",20),fg="white",bg=color_IM_Labels,height=1).grid(row=3,rowspan=2,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create Database/Reset Data",font=("times new roman",20),bg=color_Buttons,fg='white',command=function1).grid(row=5,column=0, columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Capture Samples of New Users",font=("times new roman",20),bg=color_Buttons,fg='white',command=function2).grid(row=5,column=2, columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Delete Previous Samples",font=("times new roman",20),bg=color_Buttons,fg='white',command=function3).grid(row=7,column=0, columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Train Model for new FACES",font=("times new roman",20),bg=color_Buttons,fg='white',command=function4).grid(row=7,column=2, columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Label(root, text="Recognize Person and Mark their Attendance",font=("times new roman",20),fg="white",bg=color_IM_Labels,height=1).grid(row=8,rowspan = 1,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Recognize Faces",font=("times new roman",20),bg=color_Buttons,fg='white',command=function5).grid(row=9,column =0, columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="Mark Attendance",font=("times new roman",20),bg=color_Buttons,fg='white',command=function6).grid(row=9,column=2, columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="View Attendance in CSV",font=("times new roman",20),bg=color_Buttons,fg='white',command=function7).grid(row=10,column =0, columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="About Us",font=("times new roman",20),bg=color_Buttons,fg='white',command=function8).grid(row=10,column=2, columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg=color_Exit,fg="white",command=function9).grid(row=14,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
