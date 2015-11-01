__author__ = 'Yas'
import numpy as np
from sklearn import hmm
import unittest
from Tkinter import *
'''
This is the class for hidden marcov model which ralate to 3 previous subject  of the system.
This reads the calculated proberbility value in the text file at the configeration level
This is the class which create the model relationship
starting probabilities are assign to the state equal brobabilities Ex: [0.25, 0.25,0.25, 0.25]
Emmission proberbilities are assign more more gerneral way. It is if 2nd prediction is much closer of same to the second prediction
'''
def f(marks,prb):
    if len(marks)!=3:
      print "Error"
    else:
      states = ["A", "B","C", "F"]
      n_states = len(states)
      observations = ["sub1-A", "sub1-B", "sub1-C","sub1-D","sub2-A", "sub2-B", "sub2-C","sub2-D","sub3-A", "sub3-B", "sub3-C","sub3-D"]
      n_observations = len(observations)
      start_probability = np.array([0.25, 0.25,0.25, 0.25])
      transition_probability = np.array([[0.4, 0.3,0.2, 0.1],[0.3, 0.4,0.2, 0.1],[0.1, 0.3,0.4, 0.2],[0.1, 0.2,0.3, 0.4]])
      emission_probability = np.array(prb)
      model = hmm.MultinomialHMM(n_components=n_states)
      model._set_startprob(start_probability)
      model._set_transmat(transition_probability)
      model._set_emissionprob(emission_probability)
      bob_says = marks
      logprob, pred = model.decode(bob_says, algorithm="viterbi")

      print "Previous Exam Result:", ", ".join(map(lambda x: observations[x], bob_says))
      print "Predicted Software Engineering Result:", ", ".join(map(lambda x: states[x], pred))
      if (pred[0]!=3)&(pred[1]!=3)&(pred[0]!=2)&(pred[1]!=2)&(pred[2]!=3)&(pred[2]!=2):
            con="Student Approved"
      else:con="Not Sufficient Requirenment"
    window = Tk()
    window.configure(background='#8A002E')
    window.title('Margov Prediction')
    window.geometry('480x200') # Size 200, 200
    frame = Frame(window,background='#8A002E')
    frame.pack()
    def back():
        window.withdraw()
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text="Student's predicted success:").grid(row=0, column=0)
    Label(frame, background='#8A002E',font=("Helvetica", 14),foreground="white",text=", ".join(map(lambda x: states[x], pred))).grid(row=0, column=1)
    Label(frame,background='#8A002E', text=con,fg="red",font=("Helvetica", 20)).grid(row=1, column=0)
    Button(frame, text='Next', command=back).grid(row=2, column=2, sticky=W, pady=4)
    return 0
