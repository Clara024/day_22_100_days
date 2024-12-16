print("Guess the number game!!")

import random

number = random.randint (1,1000)
counter =0
while True:
  counter += 1

  #Get user input
  guess = int (input("What is your guess?"))

  if guess == number:
    print("You are correct!!. It took you",counter,"time(s) to get it")
    counter +=1
    break
  elif guess > number:
      print("Your guess is too high.Try again")
  else:
    break