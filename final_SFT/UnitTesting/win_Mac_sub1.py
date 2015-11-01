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
Label(mastert,background='#8A002E',foreground="white", text="Enter Subject Grade:").grid(row=1)
e1 = Entry(mastert)
e1.grid(row=1, column=1)
def Fun():
    subgrd = e1.get()
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
    if (obs==[]): Example().onError()
    mastert.withdraw()
    import ReadSub1
    #ReadSub1.getSub()
    #ReadSub1.getSub1()
    #ReadSub1.fun1()
    ReadSub1.getprob(obs)




Button(mastert, text='Quit', command=mastert.quit).grid(row=3, column=2, sticky=W, pady=4)
Button(mastert, text='Submit', command=Fun).grid(row=3, column=3, sticky=W, pady=4)
mainloop( )
