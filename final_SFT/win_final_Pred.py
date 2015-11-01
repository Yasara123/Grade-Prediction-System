__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import  Button
from Tkinter import Tk
import matplotlib.pyplot as plt
import tkMessageBox as box
from PIL import Image, ImageTk
import os
from Tkinter import *
import MySQLdb
from ttk import  Button
from Tkinter import Tk
import matplotlib.pyplot as plt
import tkMessageBox as box
from PIL import Image, ImageTk
import os
import matplotlib.pyplot as pl
'''
Password of the database is read from the file
this class combine the alll prection functions in weighted regression. When looking at the actual data by unit testung intergrated
weights are assigned. This gives the final prediction
'''
#--------------------------------------
Er="null"
class Example():
    def onError(self):
        box.showerror("Error", "Could not Upadate")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Predictions Completed")

#--------------------------------------
master = Tk()
master.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(master, image=img).grid(row=0, column=3)
master.wm_title("Final Exam Result")

Label(master,background='#8A002E',foreground="white", text="Enter Module Code:").grid(row=1)
Label(master,background='#8A002E',foreground="white", text="Enter Year:").grid(row=2)
Label(master,background='#8A002E',foreground="white", text="Test No:").grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
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

def curv(student,TestNo,code):
    import Algo3_crvFitWin
    val=Algo3_crvFitWin.f(student,TestNo,code,"2")
    return val
def ExMov(student,TestNo,code):
    import Algo1_WegMovWin
    val=Algo1_WegMovWin.f(student,TestNo,code,"2")
    return val
def ExWeg(student,TestNo,code):
    import Algo2_WegAvgWin
    val=Algo2_WegAvgWin.f(student,TestNo,code,"2")
    return val
grd=""
predValue=[]
def predict(student,TestNo,code):
    clear(student,code)
    val1=curv(student,TestNo,code)
    #print val1
    val2=ExMov(student,TestNo,code)
    #print val2
    val3=ExWeg(student,TestNo,code)
   # print val3
    #by assuming weights are 3,2,1
    fVal=int(((int(val2)*1)+(int(val3)*1)+(int(val1)*0.85))/3)
    WritePred(student,fVal,code)
    clear(student,code)
    if fVal>=84:
       grd="A+"
    if (fVal>=75)&(fVal<=84):
       grd="A"
    if (fVal>=70)&(fVal<=74):
       grd="A-"
    if (fVal>=65)&(fVal<=69):
       grd="B+"
    if (fVal>=60)&(fVal<=64):
       grd="B"
    if (fVal>=55)&(fVal<=59):
       grd="B-"
    if (fVal>=50)&(fVal<=54):
       grd="C+"
    if (fVal>=45)&(fVal<=49):
       grd="C"
    if (fVal>=40)&(fVal<=44):
       grd="C-"
    if (fVal>=35)&(fVal<=39):
       grd="D"
    if (fVal<=34):
       grd="F"
    predValue.append(grd)
    return 0
def plot():
    Er="null"
    code = e1.get()
    year = e2.get()
    TestNo=e3.get()
    user=getUserNm()
    pas=getPass()
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql1 = "SELECT StudentName FROM %s" %(code)
    cursor.execute(sql1)
    results = cursor.fetchall()
    for list in results:
        for x in list:
            predict(x,int(TestNo),code)
    Example().onInfo()
    val=[]
    xv=[]
    yv=[]
    for x in range(0,len(predValue)):
            xv.append(x)
            yv.append(30)
            if predValue[x]=="A+":
               val.append(84)
            if predValue[x]=="A":
               val.append(75)
            if predValue[x]=="A-":
               val.append(70)
            if predValue[x]=="B+":
               val.append(65)
            if predValue[x]=="B":
               val.append(60)
            if predValue[x]=="B-":
               val.append(55)
            if predValue[x]=="C+":
               val.append(50)
            if predValue[x]=="C":
               val.append(45)
            if predValue[x]=="C-":
               val.append(40)
            if predValue[x]=="D":
               val.append(35)
            if predValue[x]=="F":
               val.append(30)
    #xval=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
    pl.plot(xv, val,'b')
    y=[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]
    pl.plot(yv,'r')
    plt.legend(["Predicted Grades", "Grade F"], loc='lower right')
    pl.ylim(0,100)
    pl.xlim(1,len(xv))
    pl.show()
#----------------------------------
def WritePred(student,fVal,code):
    user=getUserNm()
    pas=getPass()
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql1 = "UPDATE %s SET pred = '%s' WHERE StudentName = '%s'" % (str(code),int(fVal),student)
    try:
       # Execute the SQL command
       cursor.execute(sql1)
       # Commit your changes in the database
       db.commit()
    except:
       Er="not null"
       #Rollback in case there is any error
       db.rollback()
       print "Error: unable to update data"
       Example().onError()

#----------------------------------
def clear(student,code):
    user=getUserNm()
    pas=getPass()
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql1 = "UPDATE %s SET pred = NULL WHERE StudentName = '%s'" % (str(code),student)
    try:
       # Execute the SQL command
       cursor.execute(sql1)
       # Commit your changes in the database
       db.commit()
    except:
       Er="not null"
       #Rollback in case there is any error
       db.rollback()
       print "Error: unable to update data"
       Example().onError()


#----------------------------------------
def back():
   master.withdraw()
   os.system('python win_Batch.py')

#----------------------------------------
Button(master, text='Back', command=back).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='View', command=plot).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
