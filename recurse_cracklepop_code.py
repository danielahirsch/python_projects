'''
Program that prints out the numbers 1 to 100 (inclusive). 
If the number is divisible by 3, print Crackle instead of the number. 
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop.
'''
from random import randint

def divisible_number(): 
divisible_number = randint(0,100)

if (divisible_number / 3 == int):
  print "Crackle"
elif (divisible_number / 5 == int):
  print "Pop"
elif (divisible_number / 3 == int and divisible_number / 5 == int): 
  print "CracklePop" 
else: 
  print(divisible_number) 

if __name__ == "__main__":
  divisible_number()