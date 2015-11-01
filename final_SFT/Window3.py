__author__ = 'Yas'
from Tkinter import *
import MySQLdb
from ttk import Frame, Button, Style
from Tkinter import Tk
import matplotlib.pyplot as plt
import tkMessageBox as box
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
Label(master, text="Enter Module Code:").grid(row=0)
Label(master, text="Enter Year:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def plot():
    Er="null"
    code = e1.get()
    year = e2.get()
    # Open database connection
    db = MySQLdb.connect("localhost","root","sri","marks" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "SELECT StudentName FROM %s "% (code)
    cursor.execute(sql)
    results = cursor.fetchall()
    noStd=len(results)
    sql1 =  "SELECT * FROM cs2202 \
           WHERE StudentName= '%s'" % (results[0])
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
        sql1 = "SELECT * FROM cs2202 WHERE StudentName= '%s'" % (results[x])
        cursor.execute(sql1)
        results2 = cursor.fetchall()
        row = results2[0]
        aStudentName= row[0]
        for y in range(1, (noTest+1)):
            test.append(int(row[y]))
        plt.plot(no, test)
        test=[]
    plt.axis([1, 12, 0, 100])
    plt.ylabel('Marks 100%')
    plt.xlabel('Test Number')
    plt.title('All Bach Result')
    plt.show()
    return 0




Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=plot).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
