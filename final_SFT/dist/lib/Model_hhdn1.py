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
'''
This is the class for hidden marcov model which ralate to 1 previous subject  of the system.
This reads the calculated proberbility value in the text file at the configeration level
This is the class which create the model relationship
starting probabilities are assign to the state equal brobabilities Ex: [0.25, 0.25,0.25, 0.25]
Emmission proberbilities are assign more more gerneral way but for this  function transision proberbilities are not useful
'''
def f(marks,prb):
    if len(marks)!=1:
      print "Error"
    else:
      #states = ["A+","A","A-", "B+","B","B-","C+","C","C-", "F"]
      states = ["A","B","C", "F"]
      n_states = len(states)
      observations = ["Sub1:A+","Sub1:A","Sub1:A-", "Sub1:B+", "Sub1:B", "Sub1:B-", "Sub1:C+", "Sub1:C", "Sub1:C_","Sub1:F"]
      n_observations = len(observations)
      #Starting proberbilities
      start_probability = np.array([0.25, 0.25,0.25, 0.25])
      #Transision proberbilities
      transition_probability = np.array([[0.4, 0.3,0.2, 0.1],[0.3, 0.4,0.2, 0.1],[0.1, 0.3,0.4, 0.2],[0.1, 0.2,0.3, 0.4]])
      # Emission proberbilities are read from file
      emission_probability = np.array(prb)
      model = hmm.MultinomialHMM(n_components=n_states)
      model._set_startprob(start_probability)
      model._set_transmat(transition_probability)
      model._set_emissionprob(emission_probability)
      bob_says = marks
      #bob_says=[0]
      logprob, pred = model.decode(bob_says, algorithm="viterbi")
      # Display the result
      print "Previous Exam Result:", ", ".join(map(lambda x: observations[x], bob_says))
      print "Predicted Software Engineering Result:", ", ".join(map(lambda x: states[x], pred))
      '''
      If C and F values are not get as a predicted then student is displayed as approved
      '''
      if (pred[0]!=3)&(pred[0]!=2):
            con="Student Approved"
      else:con="Not Sufficient Requirement"
    # Create GUI


    window = Tk()
    window.configure(background='#8A002E')
    window.title('Margov Prediction')
    window.geometry('480x200') # Size 200, 200
    frame = Frame(window,background='#8A002E')
    frame.pack()
    def back():
        window.withdraw()

    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text="Student's predicted success:").grid(row=0, column=0)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=map(lambda x: states[x], pred)).grid(row=0, column=1)
    Label(frame,background='#8A002E', text=con,fg="red",font=("Helvetica", 20)).grid(row=1, column=0)
    Button(frame, text='Next', command=back).grid(row=2, column=2, sticky=W, pady=4)

    return pred[0]


