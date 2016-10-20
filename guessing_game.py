''' Guessing game that allows a player 10 tries to guess a number between 0 and 100. 
'''

from random import randint

def guess_number():
    secret_number = randint(0,100)
    guess = - 1
    count = 0

    # While the user's guess doesn't match the secret number and the user has tried less then 10 times: 
    # 1. if guess is less then secret number, tell the user that their guess is low
    # 2. if guess is more then the secret number, tell the user that their guess is high
    while (secret_number != guess and count < 10):
      count += 1
      guess = int(raw_input("Please guess a number between 0 and 100: "))
      if (guess < secret_number):
        print "Your guess is low"
      elif (guess > secret_number):
        print "Your guess is high"
    # if the secret number is equal to the user's guess, tell the user that they won. 
    # if the user hit 10 tries, tell the user that they lost. 
    if (secret_number == guess):
      print "You guessed right! You won!"
    else:
      print "You ran out of tries. You lost."


if __name__ == "__main__":
  guess_number()
 