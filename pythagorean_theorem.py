""" 
Pythagorean theorem for the relationship of the lengths of the 
three sides of a right triangle:
a2 + b2 = c2

The program accepts values for a and b and
then calculates the solution of c. 

"""
import math

def pythaTheorem(a, b):
  print("This program computes Pythagorean Theorem: ")
  c = math.sqrt(a * a + b * b)
  print("The value for 'c' is: ", c)

pythaTheorem(6, 11)
pythaTheorem(3, 5)
pythaTheorem(12, 22)