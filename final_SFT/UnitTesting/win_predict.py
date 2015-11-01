__author__ = 'Yas'

from Tkinter import *
from PIL import Image, ImageTk
import os

master = Tk()
master.configure(background='#8A002E')
img = ImageTk.PhotoImage(Image.open("logo4.jpg"))
imglabel = Label(master, image=img).grid(row=0, column=3)
master.wm_title("Result Prediction")

Label(master,background='#8A002E',foreground="white", text="Enter Student Index:").grid(row=1)
Label(master,background='#8A002E',foreground="white", text="Test No need to predict:").grid(row=2)
Label(master,background='#8A002E',foreground="white", text="Enter Module Code:").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

def curv(student,TestNo,code):
    import Algo3_crvFitWin
    val=Algo3_crvFitWin.f(student,TestNo,code,"1")
    return val
def ExMov(student,TestNo,code):
    import Algo1_WegMovWin
    val=Algo1_WegMovWin.f(student,TestNo,code,"1")
    return val
def ExWeg(student,TestNo,code):
    import Algo2_WegAvgWin
    val=Algo2_WegAvgWin.f(student,TestNo,code,"1")
    return val
grd=""
def predict():
    student = e1.get()
    TestNo= e2.get()
    code=e3.get()
    val1=curv(str(student),int(TestNo),str(code))
    print val1
    val2=ExMov(str(student),int(TestNo),str(code))
    print val2
    val3=ExWeg(str(student),int(TestNo),str(code))
    print val3
    #by assuming weights are 3,2,1
    fVal=int(((int(val2)*2)+(int(val3)*1)+(int(val1)*0.85))/4)
    print fVal

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

    window = Tk()
    window.configure(background='#8A002E')
    window.title('Prediction')
    window.geometry('350x150') # Size 200, 200
    frame = Frame(window,background='#8A002E')
    frame.pack()
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text="Student's predicted result:").grid(row=0, column=0)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=str(grd)).grid(row=0, column=1)
    Button(frame, text='Quit', command=window.quit).grid(row=4, column=2, sticky=W, pady=4)
#----------------------------------------
def back():
   master.withdraw()
   os.system('python win_StudentData.py')

#----------------------------------------
Button(master, text='Back', command=back).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=predict).grid(row=5, column=2, sticky=W, pady=4)
mainloop( )
