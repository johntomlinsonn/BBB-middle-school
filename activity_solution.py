import random as rand

target_number = rand.randint(1, 100)
guess = None
num_attempts = 0
while guess != target_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < target_number:
        print("Too low! ")
    elif guess > target_number:
        print("Too high! ")
    num_attempts += 1

print(f"Congratulations! You've guessed the number {target_number} in {num_attempts} attempts.")