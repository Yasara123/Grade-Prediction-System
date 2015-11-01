__author__ = 'Yas'
from Tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Help")
root.geometry("400x200+50+50")
imageFile = "logo4.jpg"
logo = ImageTk.PhotoImage(Image.open(imageFile))
w1 = Label(root, image=logo).pack(side="top")
explanation1 = """At the 1st login user can use Yas as a user name \nand sri as system password and username.\n after that he should configure it to new vales"""
w2 = Label(root,
           justify=LEFT,
           font=("Purisa", 12),
           text=explanation1).pack(side="top")

root.mainloop()
