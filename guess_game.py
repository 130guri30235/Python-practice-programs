import random

a = random.randint(1, 100)
guess = 101
count = 0

while guess != a:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess > a:
        print("Guess is Higher")
    elif guess < a:
        print("Guess is Lower")
    else:
        print("Guess is done" ,a)

print("Number was:", a)
print("Attempts:", count)
