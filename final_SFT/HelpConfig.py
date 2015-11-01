__author__ = 'Yas'
from Tkinter import *
from PIL import Image, ImageTk
'''
This is the help class f of the system.
'''
root = Tk()
root.title("Help")
root.geometry("700x280+50+50")
imageFile = "logo4.jpg"
logo = ImageTk.PhotoImage(Image.open(imageFile))
w1 = Label(root, image=logo).pack(side="top")
explanation1 = """In this Window using main option user can do following:\n\nUser must do this part at the beginning. In this part user assign value for system username,\n password and should provide database user name and password.And also if user intend\n to use  enrollment predicton part then he should entherthe no of previous subject that related \n to his subject.If he feels that the system is hacked of forget the new values then he can\n restore the password and usernams to the previous valuesall those values are write\n in database as well as text file for the protection as encripted text """
w2 = Label(root,
           justify=LEFT,
           font=("Purisa", 12),
           text=explanation1).pack(side="top")

root.mainloop()
