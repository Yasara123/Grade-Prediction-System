__author__ = 'Yas'
from Tkinter import *
from ttk import Frame, Button, Style
from Tkinter import Tk
from Tkinter import *
import tkMessageBox



import ctypes

master = Tk()
Label(master, text="Enter Student Name:").grid(row=0)
Label(master, text="Enter Marks of Sub1 CA:").grid(row=1)
Label(master, text="Enter Marks of Sub1 WE:").grid(row=2)
Label(master, text="Enter Marks of Sub2 CA:").grid(row=3)
Label(master, text="Enter Marks of Sub2 WE:").grid(row=4)
Label(master, text="Enter as P or F(in capital letters) ").grid(row=5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

def model(student,S1_CA,S2_CA,S1_WE,S2_WE):
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
    import HiddenMarkovModel
    val=HiddenMarkovModel.f(marks)
    return val

def predict():
    student = e1.get()
    S1_CA= e2.get()
    S1_WE= e3.get()
    S2_CA= e4.get()
    S2_WE= e5.get()
    val=model(student,S1_CA,S2_CA,S1_WE,S2_WE)
    print val
    con=""
    if val>50.0:
        con="Approved"
    else:
        con="Not Sufficient Requirenment"
    window = Tk()
    window.title('Margov Prediction')
    window.geometry('300x150') # Size 200, 200
    frame = Frame(window)
    frame.pack()
    Label(frame, text=student+"'s predicted sucess:").grid(row=0, column=0)
    Label(frame, text=val).grid(row=0, column=1)
    Label(frame, text=con,fg="red",font=("Helvetica", 24)).grid(row=1, column=0)
    Button(frame, text='Quit', command=window.quit).grid(row=2, column=2, sticky=W, pady=4)

Button(master, text='Quit', command=master.quit).grid(row=7, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=predict).grid(row=7, column=2, sticky=W, pady=4)
mainloop( )

