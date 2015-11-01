__author__ = 'Yas'
from Tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Help")
root.geometry("800x300+50+50")
imageFile = "logo4.jpg"
logo = ImageTk.PhotoImage(Image.open(imageFile))
w1 = Label(root, image=logo).pack(side="top")
explanation1 = """In this Window using main option user can do following:\n\n(1)-Make Warnings: This shows the students details who are in very poor predicted grades\n(2)-Show Bach Result:This shows the progess of all student in the bach and all predicted results at the final exam\n(3)-Student Data:This shows the current progress of particular student and his predicted result at the exam\n(4)-Enrollment Approval:This shows the whether student has a minimum requirenment to enroll his subject by \nconsidering upto 3 subject\n(5)-Lecture Progress:This shows the mean value of student result at each lecture"""
w2 = Label(root,
           justify=LEFT,
           font=("Purisa", 12),
           text=explanation1).pack(side="top")

root.mainloop()
