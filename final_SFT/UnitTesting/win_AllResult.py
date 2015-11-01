__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import  Button
from Tkinter import Tk
import matplotlib.pyplot as plt
import tkMessageBox as box
from PIL import Image, ImageTk
import os
import  numpy
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
master.wm_title("All Students Result")

Label(master,background='#8A002E',foreground="white", text="Enter Module Code:").grid(row=1)
Label(master,background='#8A002E',foreground="white", text="Enter Year:").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
std=[]
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
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

def plot():
    Er="null"
    code = e1.get()
    year = e2.get()
    user=getUserNm()
    pas=getPass()
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(numpy.arange(1,15,1.0))
    ax.set_yticks(numpy.arange(0,110.,5.0))
    # Open database connection
    db = MySQLdb.connect("localhost",user,pas,"marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "SELECT StudentName FROM %s "% (code)
    cursor.execute(sql)
    results = cursor.fetchall()
    noStd=len(results)
    sql1 = "SELECT * FROM %s "%(code)+ " WHERE StudentName= '%s'" % (results[0])
    cursor.execute(sql1)
    results2 = cursor.fetchall()
    i=0
    for list in results2:
        for x in list:
            if x is not None:
             i=i+1
    noTest=i-1
    test=[]
    no=[]
    for y in range(1, (noTest+1)):
        no.append(y)
    for x in range(0, (noStd)):
        sql1 = "SELECT * FROM %s "%(code)+" WHERE StudentName= '%s'" % (results[x])
        cursor.execute(sql1)
        results2 = cursor.fetchall()
        row = results2[0]
        aStudentName= row[0]
        std.append(aStudentName)
        for y in range(1, (noTest+1)):
            test.append(int(row[y]))
        plt.plot(no, test)
        test=[]

    plt.axis([1, 15, 0, 110])

    #plt.scatter(no,tot)
    plt.ylabel('Marks 100%')
    plt.xlabel('Test Number')
    plt.title('All Bach Result')
    plt.legend(std, loc='lower right')
    plt.grid()
    plt.show()
    return 0
#----------------------------------------
def back():
   master.withdraw()
   os.system('python win_Batch.py')



Button(master, text='Back', command=back).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='View Individual Graph', command=plot).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
