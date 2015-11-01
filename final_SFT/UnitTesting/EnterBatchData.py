__author__ = 'Yas'
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
Label(master,background='#8A002E',foreground="white", text="Enter Test Number:").grid(row=1)
Label(master,background='#8A002E',foreground="white", text="Year:").grid(row=2)
Label(master,background='#8A002E',foreground="white", text="Module code:").grid(row=3)
Label(master,background='#8A002E',foreground="white", text="Test Weight:").grid(row=4)

e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)


e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
tem=[]
def getUserNm():
  with open('Config.txt','r') as f:
    for line in f:
        for word in line.split():
           tem.append(word)
           print
    return tem[2]
#get password
def getPass():
    return tem[3]

sub=[]
def getSub():
  with open('marks.txt','r') as f:
    for line in f:
        for word in line.split():
           sub.append(word)
def plot():
    Er="null"
    TestNo = e2.get()
    marks = e3.get()
    code = e4.get()
    weig=e5.get()
    user=getUserNm()
    pas=getPass()
    getSub()
    print code,TestNo,marks
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    j=0
    for i in range(0,len(sub)/2):
        if int(TestNo)==1:
            print "ok"
            sql = "UPDATE %s SET Test1 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==2:
            sql = "UPDATE %s SET Test2 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==3:
            sql = "UPDATE %s SET Test3 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==4:
            sql = "UPDATE %s SET Test4 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==5:
            sql = "UPDATE %s SET Test5 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==6:
            sql = "UPDATE %s SET Test6 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==7:
            sql = "UPDATE %s SET Test7 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==8:
            sql = "UPDATE %s SET Test8 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==9:
            sql = "UPDATE %s SET Test9 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==10:
            sql = "UPDATE %s SET Test10 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==11:
            sql = "UPDATE %s SET Test11 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==12:
            sql = "UPDATE %s SET Test12 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==13:
            sql = "UPDATE %s SET Test13 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==14:
            sql = "UPDATE %s SET Test14 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)==15:
            sql = "UPDATE %s SET Test15 = '%d'"% (code,int(sub[j+1]))+" WHERE StudentName = '%s'"% (str(sub[j]))
        if int(TestNo)>15:
            print "Error: Maximum test numbers"
        j=j+2
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
        if int(TestNo)==1:
            sql1="UPDATE weights SET Test1 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==2:
                sql1="UPDATE weights SET Test2 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==3:
                sql1="UPDATE weights SET Test3 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==4:
                sql1="UPDATE weights SET Test4 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==5:
                sql1="UPDATE weights SET Test5 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==6:
                sql1="UPDATE weights SET Test6 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==7:
                sql1="UPDATE weights SET Test7 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==8:
                sql1="UPDATE weights SET Test8 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==9:
                sql1="UPDATE weights SET Test9 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==10:
               sql1="UPDATE weights SET Test10 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==11:
                sql1="UPDATE weights SET Test11 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==12:
                sql1="UPDATE weights SET Test12 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==13:
                sql1="UPDATE weights SET Test13 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==14:
                sql1="UPDATE weights SET Test14 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)==15:
                sql1="UPDATE weights SET Test15 = '%d'"% (int(weig))+" WHERE Subject = '%s'"% (str(code))
        if int(TestNo)>15:
                print "Error: Maximum test numbers"
        cursor.execute(sql1)
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
