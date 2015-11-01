__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import tkMessageBox as box
from PIL import Image, ImageTk
import base64
#--------------------------------------
Er="null"
class Example():
    def onError(self):
        box.showerror("Error", "Could not Upadate")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Upadate Sucessfully")

#--------------------------------------
master = Tk()
master.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(master, image=img).grid(row=0, column=3)
master.wm_title("Enter Data")
Label(master,background='#8A002E',foreground="white", text="Enter Student Index to be Delete:").grid(row=1)

Label(master,background='#8A002E',foreground="white", text="Module code:").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)

e4 = Entry(master)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

e4.grid(row=3, column=1)
tem=[]
def getUserNm():
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
    return tem[2]
#get password
def getPass():
    return tem[3]

def plot():
    Er="null"
    student = e1.get()
    TestNo = e2.get()
    code = e4.get()
    user=getUserNm()
    pas=getPass()
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "DELETE FROM %s WHERE StudentName= '%s'" % (code,student)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       Er="not null"
       #Rollback in case there is any error
       db.rollback()
       print "Error: unable to update data"
       Example().onError()

    if Er=="null":
     Example().onInfo()

    # disconnect from server
    db.close()
def Back():
   import os
   master.withdraw()
   os.system('python win_HomeEdit.py')

Button(master, text='Back', command=Back).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=plot).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
