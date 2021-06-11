#This is a guess game for people to provide answers
#STILL DON'T UNDERSTAND WHY THE break does not work.
#You only get it right if the first guess is correct
#Otherwise the loop keeps running without end. Why? No idea!
import random
number = random.randint(0,10)

guess = int (input("I am thinking of a number from 0 to 10. Enter a Guess: "))

while True:
    if guess == number:
        break

    else:
        int (input("Nope. Try again: "))

print("You got it right! I was thinking of", number)

