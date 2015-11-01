__author__ = 'Yas'
from Tkinter import *
import matplotlib.pyplot as plt
import Tkinter as tk
from PIL import Image, ImageTk
import os
'''
This is the class for Read the backups from the database.
Password of the database is read from the file
'''
root = tk.Tk()
root.title('Home Page')

# pick an image file you have .bmp  .jpg  .gif.  .png
# load the file and covert it to a Tkinter image object
imageFile = "logo3.jpg"
image1 = ImageTk.PhotoImage(Image.open(imageFile))

# get the image size
w = image1.width()
h = image1.height()

# position coordinates of root 'upper left corner'
x = 300
y = 20

# make the root window the size of the image
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# root has no image argument, so use a label as a panel
panel1 = tk.Label(root, image=image1)
panel1.pack(fill='both', expand='yes')
#set actions to the buttons

def helloCallBack5():
    root.withdraw()
    os.system('python ReadBackUps.py')
def helloCallBack6():
    root.withdraw()
    os.system('python Config.py')
def helloCallBack7():
    root.withdraw()
    os.system('python win_Help.py')
def helloCallBack3():
    root.withdraw()
    os.system('python win_HomeWin1.py')

# put a button on the image panel to test it
button3 = tk.Button(panel1,width=20,borderwidth=10,foreground="dark red", text='Back',command= helloCallBack3)
button3.pack(side=BOTTOM,pady=5)
button6 = tk.Button(panel1,width=20,borderwidth=10,foreground="dark red",text='Help',command= helloCallBack7)
button6.pack(side=BOTTOM,pady=5)
button6 = tk.Button(panel1,width=20,borderwidth=10,foreground="dark red", text='Exit App',command=root.quit())
button6.pack(side=BOTTOM,pady=5)
button6 = tk.Button(panel1,width=20,borderwidth=10,foreground="dark red",text='Edit System Passwords',command= helloCallBack6)
button6.pack(side=BOTTOM,pady=5)
button2 = tk.Button(panel1,width=20,borderwidth=10,foreground="dark red", text='Read Backups',command= helloCallBack5)
button2.pack(side=BOTTOM,pady=5)

button6.pack(side=BOTTOM,pady=5)

mainloop( )

