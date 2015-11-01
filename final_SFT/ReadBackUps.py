__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import base64
import tkMessageBox as box
from PIL import Image, ImageTk
import os
from Crypto.Cipher import AES
from Crypto import Random
'''
This is the class for Read the backups from the database.
Password of the database is read from the file
'''
class Example():
    def onError(self):
        box.showerror("Error", "Could not Upadate")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Upadate Sucessfully")


master = Tk()
master.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(master, image=img).grid(row=0, column=3)

master.wm_title("System Configuration")
Label(master,background='#8A002E',foreground="white", text="System UserName").grid(row=1, column=0)
Label(master,background='#8A002E',foreground="white", text="System Password:").grid(row=2, column=0)
Label(master,background='#8A002E',foreground="white", text="No of Related Subjects:").grid(row=3, column=0)
def getUserNm():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[2]
#get password
def getPass():
  tem=[]
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
  f.close()
  return tem[3]
t1=[]
t2=[]
t3=[]
def f():
    Er="null"
    user=getUserNm()
    pas=getPass()
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "SELECT UserName FROM users "
    cursor.execute(sql)
    results1 = cursor.fetchall()
    for list in results1:
        for x in list:
            t1.append(x)
    sql = "SELECT CAST(AES_DECRYPT(PassWord, 'sri') AS CHAR(50)) FROM users"
   # sql= "SELECT AES_DECRYPT(AES_ENCRYPT('%s','%s'),'%s') "
    cursor.execute(sql)
    results2 = cursor.fetchall()
    for list in results2:
        for x in list:
            t2.append(x)
    sql = "SELECT SNo FROM users"
    cursor.execute(sql)
    results3 = cursor.fetchall()
    for list in results3:
        for x in list:
            t3.append(x)
    db.close()

f()

def Help():
    master.withdraw()
    os.system('python HelpConfig.py')

def Back():
    master.withdraw()
    os.system('python win_HomeConfig.py')

Label(master,background='#8A002E',foreground="white", text=t1[0]).grid(row=1, column=1)
Label(master,background='#8A002E',foreground="white", text=t2[0]).grid(row=2, column=1)
Label(master,background='#8A002E',foreground="white", text=t3[0]).grid(row=3, column=1)
Button(master, text='Help', command=Help).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='Back', command=Back).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=W, pady=4)

mainloop( )
