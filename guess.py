import random

number=random.randrange(1,50)
guess = int(input("guess a number between 1 to 50:\n"))

while guess != number:
    if guess < number:
        print("you need to guess higher.Try again")
        guess = int(input("\nguess a number between 1 to 50:\n"))
    else:
        print("you need to guess lower. Try again")
        guess = int(input("guess a number between 1 to 50:\n"))
print("you guessed the number correctly!")