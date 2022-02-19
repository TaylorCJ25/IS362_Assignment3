# **Assignment 3** # Pandas Series ## This python file contains a numpy array with 7 values, the first being 55 and
# 120 as suggested, to test the codes effectiveness.

import numpy as np

miles = np.array([])
for x in range(7):
   inp = int(input("Enter reading for day "+str(x+1)+": "))
   miles = np.append(miles,inp)

miles[1:] -= miles[:-1].copy()
for mile in range(len(miles)):
   print("Day "+str(mile+1)+": ",miles[mile],"miles")