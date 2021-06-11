#Task 2: Create a guess game with the names of the colors.
# At each round, pick a random color from a list and let the user try to guess it.
# When he does, ask if he wants to play again. Keep playing until the user types "no".
import random
colors = ["black", "white", "yellow", "blue", "green", "red", "turquoise", "grey"]

while True:
    color = colors[random.randint(0, len(colors)-1)]
    guess = input("I am thinking of a color, can you guess it: ")
    while True:
        if (color == guess.lower()):
            break
        else:
            guess = input("Nope. Try again: ")
    print("You guessed it! I was thinking of", color)

    play_again = input("Let's play again? Type 'no' to quit. ")

    if play_again.lower() == "no":
        break

print("It was fun! Thanks for playing!!!")
