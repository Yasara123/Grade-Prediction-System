__author__ = 'Yas'
__author__ = 'Yas'
import numpy as np
from sklearn import hmm
import unittest
from Tkinter import *

def f(marks,prb):
    if len(marks)!=2:
      print "Error"
    else:
      print "hidden"
      states = ["A", "B","C", "F"]
      n_states = len(states)
      observations = ["Sub1:A+","Sub1:A","Sub1:A-", "Sub1:B+", "Sub1:B", "Sub1:B-", "Sub1:C+", "Sub1:C", "Sub1:C_","Sub1:F","Sub2:A+","Sub2:A","Sub2:A-", "Sub2:B+", "Sub2:B", "Sub2:B-", "Sub2:C+", "Sub2:C", "Sub2:C_","Sub2:F"]
      #observations = ["OOP-A", "OOP-B", "OOP-C","OOP-D"]
      n_observations = len(observations)
      start_probability = np.array([0.25, 0.25,0.25, 0.25])
      transition_probability = np.array([[0.4, 0.3,0.2, 0.1],[0.3, 0.4,0.2, 0.1],[0.1, 0.3,0.4, 0.2],[0.1, 0.2,0.3, 0.4]])
      #emission_probability = np.array([[0.2, 0.1,0.1, 0.1,0.2, 0.1,0.1, 0.1],[0.2, 0.1,0.1, 0.1,0.2, 0.1,0.1, 0.1],[0.2, 0.1,0.1, 0.1,0.2, 0.1,0.1, 0.1],[0.2, 0.1,0.1, 0.1,0.2, 0.1,0.1, 0.1]])
      #emission_probability = np.array([[0.4, 0.2,0.2, 0.2],[0.4, 0.2,0.2, 0.2],[0.4, 0.2,0.2, 0.2],[0.4, 0.2,0.2, 0.2]])
      emission_probability = np.array(prb)
      model = hmm.MultinomialHMM(n_components=n_states)
      model._set_startprob(start_probability)
      model._set_transmat(transition_probability)
      model._set_emissionprob(emission_probability)
      bob_says = marks
      logprob, pred = model.decode(bob_says, algorithm="viterbi")
      val1=0
      val2=0
      totval=0
      if(pred[0]==0):
          val1=85
      if(pred[0]==1):
          val1=65
      if(pred[0]==2):
          val1=47.5
      if(pred[0]==3):
          val1=20
      if(pred[1]==0):
          val2=85
      if(pred[1]==1):
          val2=65
      if(pred[1]==2):
          val2=47.5
      if(pred[1]==3):
          val2=20

      totval=(val1+val2)/2

      if (totval>70):
          gr=0
      elif (totval>55):
          gr=1
      elif (totval>40):
          gr=2
      else:
          gr=3


      print "Previous Exam Result:", ", ".join(map(lambda x: observations[x], bob_says))
      print "Predicted Software Engineering Result:", ", ".join(map(lambda x: states[x], pred))
      if (pred[0]!=3)&(pred[1]!=3)&(pred[0]!=2)&(pred[1]!=2):
            con="Student Approved"
      else:con="Not Sufficient Requirenment"
    window = Tk()
    window.configure(background='#8A002E')
    window.title('Margov Prediction')
    window.geometry('450x200') # Size 200, 200
    frame = Frame(window,background='#8A002E')
    frame.pack()
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text="Student's predicted success:").grid(row=0, column=0)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=", ".join(map(lambda x: states[x], pred))).grid(row=0, column=1)
    Label(frame,background='#8A002E', text=con,fg="red",font=("Helvetica", 24)).grid(row=1, column=0)
    Button(frame, text='Quit', command=window.quit).grid(row=2, column=2, sticky=W, pady=4)
    return gr

