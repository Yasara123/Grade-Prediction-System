__author__ = 'Yas'
__author__ = 'Yas'
import numpy as np
from sklearn import hmm
import unittest
from Tkinter import *
from ttk import Frame, Button, Style
from Tkinter import Tk
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import os

def f(marks,prb):
    if len(marks)!=1:
      print "Error"
    else:
      #states = ["A+","A","A-", "B+","B","B-","C+","C","C-", "F"]
      states = ["A","B","C", "F"]
      n_states = len(states)
      #observations = ["OOP-A", "OOP-B", "OOP-C","OOP-F"]
      observations = ["Sub1:A+","Sub1:A","Sub1:A-", "Sub1:B+", "Sub1:B", "Sub1:B-", "Sub1:C+", "Sub1:C", "Sub1:C_","Sub1:F"]
      n_observations = len(observations)
      start_probability = np.array([0.25, 0.25,0.25, 0.25])
      #transition_probability = np.array([[0.2,0.2,0.1, 0.1,0.1,0.1,0.075,0.075, 0.025,0.025],[0.2,0.2,0.2,0.1,0.075,0.075,0.05,0.05, 0.025,0.025],[0.1,0.2,0.2,0.2,0.075,0.075,0.05,0.05, 0.025,0.025],[0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.05, 0.025,0.025],[0.05,0.075,0.1,0.2,0.2,0.2,0.075,0.05, 0.025,0.025],[0.05,0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.025,0.025],[ 0.025,0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.05,0.025],[ 0.025,0.025,0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.05],[0.025,0.025,0.05,0.1,0.2,0.2,0.2,0.075,0.075,0.05 ],[0.2,0.2,0.1, 0.1,0.1,0.1,0.075,0.075, 0.025,0.025]])
      transition_probability = np.array([[0.4, 0.3,0.2, 0.1],[0.3, 0.4,0.2, 0.1],[0.1, 0.3,0.4, 0.2],[0.1, 0.2,0.3, 0.4]])

      #emission_probability = np.array([[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1],[0.1, 0.1,0.1, 0.1,0.1,0.1, 0.1,0.1, 0.1,0.1]])
      #emission_probability=np.array([[0.2,0.2,0.1, 0.1,0.1,0.1,0.075,0.075, 0.025,0.025],[0.2,0.2,0.2,0.1,0.075,0.075,0.05,0.05, 0.025,0.025],[0.1,0.2,0.2,0.2,0.075,0.075,0.05,0.05, 0.025,0.025],[0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.05, 0.025,0.025],[0.05,0.075,0.1,0.2,0.2,0.2,0.075,0.05, 0.025,0.025],[0.05,0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.025,0.025],[ 0.025,0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.05,0.025],[ 0.025,0.025,0.075,0.1,0.2,0.2,0.2,0.075,0.05,0.05],[0.025,0.025,0.05,0.1,0.2,0.2,0.2,0.075,0.075,0.05 ],[0.2,0.2,0.1, 0.1,0.1,0.1,0.075,0.075, 0.025,0.025]])
      #emission_probability=np.array([[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25],[0.25,0.25,0.25, 0.25]])

      #emission_probability=np.array([[0.2,0.2,0.1, 0.1,0.1,0.1,0.075,0.075, 0.025,0.025],[0.2,0.2,0.2,0.1,0.075,0.075,0.05,0.05, 0.025,0.025],[0.2,0.2,0.1, 0.1,0.1,0.1,0.075,0.075, 0.025,0.025],[0.1,0.075,0.075,0.05,0.05, 0.025,0.025,0.2,0.2,0.2]])
      #emission_probability = np.array([[0.4, 0.2,0.2, 0.2],[0.4, 0.2,0.2, 0.2],[0.4, 0.2,0.2, 0.2],[0.4, 0.2,0.2, 0.2]])
      emission_probability = np.array(prb)
      model = hmm.MultinomialHMM(n_components=n_states)
      model._set_startprob(start_probability)
      model._set_transmat(transition_probability)
      model._set_emissionprob(emission_probability)
      bob_says = marks
      #bob_says=[0]
      logprob, pred = model.decode(bob_says, algorithm="viterbi")

      print "Previous Exam Result:", ", ".join(map(lambda x: observations[x], bob_says))
      print "Predicted Software Engineering Result:", ", ".join(map(lambda x: states[x], pred))
      if (pred[0]!=3)&(pred[0]!=2):
            con="Student Approved"
      else:con="Not Sufficient Requirenment"
    window = Tk()
    window.configure(background='#8A002E')
    window.title('Margov Prediction')
    window.geometry('450x200') # Size 200, 200
    frame = Frame(window,background='#8A002E')
    frame.pack()
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text="Student's predicted success:").grid(row=0, column=0)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=map(lambda x: states[x], pred)).grid(row=0, column=1)

    Label(frame,background='#8A002E', text=con,fg="red",font=("Helvetica", 24)).grid(row=1, column=0)
    Button(frame, text='Quit', command=window.quit).grid(row=2, column=2, sticky=W, pady=4)
    return pred[0]


