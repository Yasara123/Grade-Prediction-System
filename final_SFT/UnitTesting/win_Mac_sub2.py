__author__ = 'Yas'
__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
import os
from PIL import Image, ImageTk

class Example():
    def onError(self):
        box.showerror("Error", "Error In Input Grade ")




mastert = Tk()
mastert.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(mastert, image=img).grid(row=0, column=3)
mastert.wm_title("System Login")
Label(mastert,background='#8A002E',foreground="white", text="Enter Subject 1 Grade:").grid(row=1)
Label(mastert,background='#8A002E',foreground="white", text="Enter Subject 2 Grade:").grid(row=2)

e1 = Entry(mastert)
e2 = Entry(mastert)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)


def Fun():
    subgrd = e1.get()
    subgrd2 = e2.get()
    obs=[]
    if (str(subgrd)=="A+"):
        obs.append(0)
    if (str(subgrd)=="A"):
        obs.append(1)
    if (str(subgrd)=="A-"):
        obs.append(2)
    if (str(subgrd)=="B+"):
        obs.append(3)
    if (str(subgrd)=="B"):
        obs.append(4)
    if (str(subgrd)=="B-"):
        obs.append(5)
    if (str(subgrd)=="C+"):
        obs.append(6)
    if (str(subgrd)=="C"):
        obs.append(7)
    if (str(subgrd)=="C-"):
        obs.append(8)
    if (str(subgrd)=="F"):
        obs.append(9)
    if (str(subgrd2)=="A+"):
        obs.append(10)
    if (str(subgrd2)=="A"):
        obs.append(11)
    if (str(subgrd2)=="A-"):
        obs.append(12)
    if (str(subgrd2)=="B+"):
        obs.append(13)
    if (str(subgrd2)=="B"):
        obs.append(14)
    if (str(subgrd2)=="B-"):
        obs.append(15)
    if (str(subgrd2)=="C+"):
        obs.append(16)
    if (str(subgrd2)=="C"):
        obs.append(17)
    if (str(subgrd2)=="C-"):
        obs.append(18)
    if (str(subgrd2)=="F"):
        obs.append(19)
    if (obs==[]): Example().onError()
    print obs
    mastert.withdraw()
    import ReadSub2
    #ReadSub2.getSub()
    #ReadSub2.getSub1()
    #ReadSub2.getSub2()
    #ReadSub2.fun1()
    #ReadSub2.fun2()
    ReadSub2.getprob2(obs)

Button(mastert, text='Quit', command=mastert.quit).grid(row=3, column=2, sticky=W, pady=4)
Button(mastert, text='Submit', command=Fun).grid(row=3, column=3, sticky=W, pady=4)
mainloop( )
