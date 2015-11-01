__author__ = 'Yas'
import numpy as np
from sklearn import hmm
import unittest

def f(marks):
    if len(marks)!=4:
      print "Error"
    else:
      states = ["pass", "fail"]
      n_states = len(states)
      observations = ["OOP CA Passed", "OOP CA Failed", "OOP Exam Passed","OOP Exam Failed","OOSD CA Passed", "OOSD CA Failed", "OOSD Exam Passed","OOSD Exam Failed"]
      n_observations = len(observations)
      start_probability = np.array([0.5, 0.5])
      transition_probability = np.array([[0.7, 0.3],[0.3, 0.7]])
      emission_probability = np.array([ [0.0, 0.0, 0.1,0.1,0.1, 0.1, 0.4,0.2],[0.0, 0.05, 0.1,0.2,0.1, 0.1, 0.05,0.4]])
      model = hmm.MultinomialHMM(n_components=n_states)
      model._set_startprob(start_probability)
      model._set_transmat(transition_probability)
      model._set_emissionprob(emission_probability)
      bob_says = marks
      logprob, pred = model.decode(bob_says, algorithm="viterbi")
      prob=0
      if pred[0]==0:
        prob=prob+1

      if pred[1]==0:
        prob=prob+1

      if pred[2]==0:
        prob=prob+1

      if pred[3]==0:
        prob=prob+1

      print "Persentage of Passing : ",float((float(prob)/4)*float(100)),"%"
      print "Previous Exam Result:", ", ".join(map(lambda x: observations[x], bob_says))
      print "Predicted Software Engineering Result:", ", ".join(map(lambda x: states[x], pred))
    return float((float(prob)/4)*float(100))

#unit testing
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(f([0,2,4,6]), 100.0)
        self.assertEqual(f([1,2,4,6]), 50.0)
        self.assertEqual(f([1,3,5,7]), 0.0)