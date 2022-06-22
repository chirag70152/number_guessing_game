import random
import sys

num = int(random.random()*10)


print("guess the  number(between 1 to 10) in 3 guesses")
print("")

guess1 = int(input("Enter your first guess: "))
if guess1 == num:
    print("Hurray! correct answer in first guess.")
    print("your number: ", guess1)
    print("Answer: ", num)
    print()
    print("Thanks for playing")
    sys.exit()
elif guess1 > num:
    print("Sorry this number is greater than the answer. Try another chance")
else:
    print("Sorry this number is shorter than the answer. Try another chance")


guess2 = int(input("Enter your second guess: "))
if guess2 == num:
    print("Hurray! correct answer in second guess.")
    print("your number: ", guess2)
    print("Answer: ", num)
    print()
    print("Thanks for playing")
    sys.exit()
elif guess2 > num:
    print("Sorry this number is greater than the answer. Try another chance")
else:
    print("Sorry this number is shorter than the answer. Try another chance")


guess3 = int(input("Enter your last guess: "))
if guess3 == num:
    print("Hurray! correct answer in last guess.")
    print("your number: ", guess3)
    print("Answer: ", num)
    print()
    print("Thanks for playing")
    sys.exit()
elif guess3 > num:
    print("Sorry this number is greater than the answer.")
    print("The correct answer was", num)
    print("Better luck next time.")
    print()
    print("Thanks for playing")
else:
    print("Sorry this number is shorter than the answer.")
    print("The correct answer was", num)
    print("better luck next time.")
    print()
    print("Thanks for playing")


