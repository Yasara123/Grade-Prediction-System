__author__ = 'Yas'
from Tkinter import *
from ttk import Frame, Button, Style
from Tkinter import Tk
from Tkinter import *
import tkMessageBox



import ctypes

master = Tk()
Label(master, text="Enter Student Name:").grid(row=0)
Label(master, text="Test No need to predict:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def curv(student,TestNo):
    import crvFitWin
    val=crvFitWin.f(student,TestNo)
    return val
def ExMov(student,TestNo):
    import WegMovWin
    val=WegMovWin.f(student,TestNo)
    return val
def ExWeg(student,TestNo):
    import WegAvgWin
    val=WegAvgWin.f(student,TestNo)
    return val
def predict():
    student = e1.get()
    TestNo= e2.get()
    val1=curv(student,TestNo)
    print val1
    val2=ExMov(student,TestNo)
    print val2
    val3=ExWeg(student,TestNo)
    print val3
    #by assuming weights are 3,2,1
    fVal=int(((int(val1)*3)+(int(val2)*2)+(int(val3)*1))/6)
    print fVal
    window = Tk()
    window.title('Prediction')
    window.geometry('200x100') # Size 200, 200
    frame = Frame(window)
    frame.pack()
    Label(frame, text="Predicted value is:").grid(row=0, column=0)
    Label(frame, text=fVal).grid(row=0, column=1)
    Button(frame, text='Quit', command=window.quit).grid(row=2, column=2, sticky=W, pady=4)

Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=predict).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
