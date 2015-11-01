__author__ = 'Yas'
from Tkinter import *
import matplotlib.pyplot as plt
import Tkinter as tk
from PIL import Image, ImageTk
import os

class HomeWindow():
    def __init__(self, root):
        self.root = root
        self.root.title('Home Page')

        # pick an image file you have .bmp  .jpg  .gif.  .png
        # load the file and covert it to a Tkinter image object
        self.imageFile = "logo3.jpg"
        self.image1 = ImageTk.PhotoImage(Image.open(self.imageFile))

        # get the image size
        self.w = self.image1.width()
        self.h = self.image1.height()

        # position coordinates of root 'upper left corner'
        self.x = 0
        self.y = 10

        # make the root window the size of the image
        root.geometry("%dx%d+%d+%d" % (self.w, self.h, self.x, self.y))

        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(self.root, image=self.image1)
        self.panel1.pack(fill='both', expand='yes')

        # put a button on the image panel to test it
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red",text='Help',command= self.helloCallBack7)
        self.button6.pack(side=BOTTOM,pady=5)
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red", text='Exit App',command=root.quit())
        self.button6.pack(side=BOTTOM,pady=5)
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red",text='Back',command= self.helloCallBack6)
        self.button6.pack(side=BOTTOM,pady=5)
        self.button2 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red", text='Lecture Progress',command= self.helloCallBack5)
        self.button2.pack(side=BOTTOM,pady=5)
        self.button3 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red", text='Enrollment Approval',command= self.helloCallBack4)
        self.button3.pack(side=BOTTOM,pady=5)
        self.button4 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red", text='Student Datat',command= self.helloCallBack3)
        self.button4.pack(side=BOTTOM,pady=5)
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=2,foreground="dark red",text='Show Bach Result',command= self.helloCallBack1)
        self.button6.pack(side=BOTTOM,pady=5)

    #set actions to the buttons
    def helloCallBack1(self):
        self.root.withdraw()
        os.system('python win_Batch.py')
    def helloCallBack3(self):
        self.root.withdraw()
        os.system('python win_StudentData.py')
    def helloCallBack4(self):
        self.root.withdraw()
        os.system('python win1_Mac.py')
    def helloCallBack5(self):
        self.root.withdraw()
        os.system('python win_feedBack.py')
    def helloCallBack6(self):
        self.root.withdraw()
        os.system('python win_HomeWin1.py')
    def helloCallBack7(self):
        self.root.withdraw()
        os.system('python win_Help.py')

root = tk.Tk()
my_gui = HomeWindow(root)
root.mainloop()
