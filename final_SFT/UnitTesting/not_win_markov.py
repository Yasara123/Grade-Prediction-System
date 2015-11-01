__author__ = 'Yas'
from Tkinter import *
from ttk import Frame, Button, Style
from Tkinter import Tk
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import os


import ctypes
def getNoSubs():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[4]

master = Tk()
master.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(master, image=img).grid(row=0, column=3)
master.title("Enrolment Suggestions")
Label(master,background='#8A002E',foreground="white", text="Enter Student Name:").grid(row=1)
if int(getNoSubs())==2:
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub1 CA:").grid(row=2)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub1 WE:").grid(row=3)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub2 CA:").grid(row=4)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub2 WE:").grid(row=5)
if int(getNoSubs())==1:
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub CA:").grid(row=2)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub WE:").grid(row=3)
if int(getNoSubs())==3:
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub1 CA:").grid(row=2)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub1 WE:").grid(row=3)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub2 CA:").grid(row=4)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub2 WE:").grid(row=5)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub3 CA:").grid(row=6)
    Label(master,background='#8A002E',foreground="white", text="Enter Marks of Sub3 WE:").grid(row=7)

Label(master,background='#8A002E',foreground="white", text="Enter as P or F(in capital letters) ").grid(row=8)
if int(getNoSubs())==1:
    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
if int(getNoSubs())==2:
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)
if int(getNoSubs())==3:
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    e7 = Entry(master)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)
    e6.grid(row=6, column=1)
    e7.grid(row=7, column=1)

def model2(student,S1_CA,S2_CA,S1_WE,S2_WE):
    marks=[]
    if S1_CA=="P":
        marks.append(0)
    elif S1_CA=="F" :marks.append(1)
    if S1_WE=="P":
        marks.append(2)
    elif S1_WE=="F" :marks.append(3)
    if S2_CA=="P":
        marks.append(4)
    elif S2_CA=="F" :marks.append(5)
    if S2_WE=="P":
        marks.append(6)
    elif S2_WE=="F" :marks.append(7)
    print  marks
    import Not_Algo4_HiddenMarkovModel2
    val=Not_Algo4_HiddenMarkovModel2.f(marks)
    return val
def model3(student,S1_CA,S2_CA,S3_CA,S1_WE,S2_WE,S3_WE):
    marks=[]
    if S1_CA=="P":
        marks.append(0)
    elif S1_CA=="F" :marks.append(1)
    if S1_WE=="P":
        marks.append(2)
    elif S1_WE=="F" :marks.append(3)
    if S2_CA=="P":
        marks.append(4)
    elif S2_CA=="F" :marks.append(5)
    if S2_WE=="P":
        marks.append(6)
    elif S2_WE=="F" :marks.append(7)
    if S3_CA=="P":
        marks.append(8)
    elif S2_CA=="F" :marks.append(9)
    if S3_WE=="P":
        marks.append(10)
    elif S2_WE=="F" :marks.append(11)
    print  marks
    import Not_Algo4_HiddenMarkovModel2
    val=Not_Algo4_HiddenMarkovModel2.f(marks)
    return val

def model1(student,S1_CA,S1_WE):
    marks=[]
    if S1_CA=="P":
        marks.append(0)
    elif S1_CA=="F" :marks.append(1)
    if S1_WE=="P":
        marks.append(2)
    elif S1_WE=="F" :marks.append(3)
    import Not_Algo4_HiddenMarkovModel2
    val=Not_Algo4_HiddenMarkovModel2.f(marks)
    return val

def predict():
    student = e1.get()
    if int(getNoSubs())==1:
        S1_CA= e2.get()
        S1_WE= e3.get()
        val=model1(student,S1_CA,S1_WE)
    if int(getNoSubs())==2:
        S1_CA= e2.get()
        S1_WE= e3.get()
        S2_CA= e4.get()
        S2_WE= e5.get()
        val=model2(student,S1_CA,S2_CA,S1_WE,S2_WE)
    if int(getNoSubs())==3:
        S1_CA= e2.get()
        S1_WE= e3.get()
        S2_CA= e4.get()
        S2_WE= e5.get()
        S3_CA= e6.get()
        S3_WE= e7.get()
        val=model3(student,S1_CA,S2_CA,S3_CA,S1_WE,S2_WE,S3_WE)
    print val
    con=""
    if val>50.0:
        con="Approved"
    else:
        con="Not Sufficient Requirenment"
    window = Tk()
    window.configure(background='#8A002E')
    window.title('Margov Prediction')
    window.geometry('300x250') # Size 200, 200
    frame = Frame(window,background='#8A002E')
    frame.pack()
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=student+"'s predicted sucess:").grid(row=0, column=0)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=val).grid(row=0, column=1)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text="%").grid(row=0, column=2)
    Label(frame,background='#8A002E', text=con,fg="red",font=("Helvetica", 24)).grid(row=1, column=0)
    Button(frame, text='Quit', command=window.quit).grid(row=2, column=2, sticky=W, pady=4)
#----------------------------------------
def back():
   master.withdraw()
   os.system('python win_HomeWindow.py')

#----------------------------------------
Button(master, text='Back', command=back).grid(row=9, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=9, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=predict).grid(row=9, column=2, sticky=W, pady=4)
mainloop( )

