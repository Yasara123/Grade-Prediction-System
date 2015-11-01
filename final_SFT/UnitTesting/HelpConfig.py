__author__ = 'Yas'
__author__ = 'Yas'
from Tkinter import *
from PIL import Image, ImageTk
root = Tk()

imageFile = "logo4.jpg"
logo = ImageTk.PhotoImage(Image.open(imageFile))
w1 = Label(root, image=logo).pack(side="right")
explanation = """By using this software you can increase the marks of your students.For that following functions can be done:\nShow Student Progress:This function shows the all students progress by using grphs\nPredict Future Result:\nEnrollment Aproval:\nLecture process:"""
w2 = Label(root,
           justify=LEFT,
           padx = 10,
           text=explanation).pack(side="left")
root.mainloop()