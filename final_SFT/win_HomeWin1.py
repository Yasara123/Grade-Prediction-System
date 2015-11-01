__author__ = 'Yas'
from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk
import os
'''
This is the main window of the system and this have maily 3 functional options. They are:
 (1)---Data analyzing => Which is the main funtion window of the system.
 (2)---Data Manipulation => Which is the enter, Delete , Update function of the system
 (3)---Configuration => Which is the passwords and username handling of the system and also marcov model configuration of the system
'''
class MainWindow():
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
        self.x = 300
        self.y = 20

        # make the root window the size of the image
        self.root.geometry("%dx%d+%d+%d" % (self.w,self.h, self.x, self.y))

        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(self.root, image=self.image1)
        self.panel1.pack(fill='both', expand='yes')

		#Button Set of the GUI
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=8,foreground="dark red",text='Help',command= self.helloCallBack7)
        self.button6.pack(side=BOTTOM,pady=5)
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=8,foreground="dark red", text='Exit App',command=self.root.quit())
        self.button6.pack(side=BOTTOM,pady=5)
        self.button6 = tk.Button(self.panel1,width=20,borderwidth=8,foreground="dark red",text='Configurations',command= self.helloCallBack6)
        self.button6.pack(side=BOTTOM,pady=5)
        self.button2 = tk.Button(self.panel1,width=20,borderwidth=8,foreground="dark red", text='Data Manupulation',command= self.helloCallBack5)
        self.button2.pack(side=BOTTOM,pady=5)
        self.button3 = tk.Button(self.panel1,width=20,borderwidth=8,foreground="dark red", text='Grade Anlyzing',command= self.helloCallBack4)
        self.button3.pack(side=BOTTOM,pady=5)
        self.button6.pack(side=BOTTOM,pady=5)

    #set actions to the buttons
    def helloCallBack4(self):
        self.root.withdraw()
        os.system('python win_HomeWindow.py')
    def helloCallBack5(self):
        self.root.withdraw()
        os.system('python win_HomeEdit.py')
    def helloCallBack6(self):
        self.root.withdraw()
        os.system('python win_HomeConfig.py')
    def helloCallBack7(self):
        self.root.withdraw()
        os.system('python win_Help.py')
# runs the class

root = Tk()
my_gui = MainWindow(root)
root.mainloop()