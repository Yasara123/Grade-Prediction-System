__author__ = 'Yas'
from Tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Help")
root.geometry("800x400+50+50")
imageFile = "logo4.jpg"
logo = ImageTk.PhotoImage(Image.open(imageFile))
w1 = Label(root, image=logo).pack(side="top")
explanation1 = """By using this software you can increase the marks of your students.For that following functions can be done:\nShow Student Progress:This function shows the all students progress by using grphs\n-Predict Future Result:\n-Enrollment Aproval:\n-Lecture process.etc"""
w2 = Label(root,
           justify=LEFT,
           font=("Purisa", 12),
           text=explanation1).pack(side="top")
explanation2 = """In this window have options\n(1)-Configurations:User must do this part at the begining. In this part user assign value for system username,\n password and should provide database user name and password.And also if user intend to use  enrollment \npredicton part then he should entherthe no of previous subject that related \n to his subject\n(2)-Data Manupulation: From this part user can add/delete/update database values and prediction configuration\n should be done here \n (3)-Grade Anlyzing: Other Functions are handdle by this option"""
w3 = Label(root,
           justify=LEFT,
           font=("Purisa", 12),
           text=explanation2).pack(side="top")
root.mainloop()