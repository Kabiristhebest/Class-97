import random
print("Number Guessing game")
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")
while chances < 5:
    guess=int(input("Enter your guess: "))
    if guess == number:
        print("You won")
        break
    elif guess < number:
        print("You lose, YoUR GuESS was To0 Low, guess a number higher then",guess)
    else:
        print("You lose, Guess a number lower then", guess)
    chances += 1
if not chances < 5:
    print("The number is", number, "YOU LOST")
