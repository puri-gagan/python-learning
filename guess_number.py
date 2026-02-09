import random

number = random.randint(1, 100)   # random number between 1 and 100
chances = 3

print("I have chosen a number between 1 and 100.")
print("You have", chances, "chances to guess it.")

for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Hint: The number is GREATER than your guess.")
    else:
        print("Hint: The number is SMALLER than your guess.")

else:
    print("Sorry, you've used all your chances.")
    print("The correct number was:", number)
