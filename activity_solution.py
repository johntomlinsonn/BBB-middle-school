import random as rand

random_number = rand.randint(1, 100)
guess = None
num_attempts = 0
while guess != random_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Too low! ")
    elif guess > random_number:
        print("Too high! ")
    num_attempts += 1

print(f"Congratulations! You've guessed the number {random_number} in {num_attempts} attempts.")