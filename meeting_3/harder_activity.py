import random as rand
three_in_a_row = False
num_in_a_row = 0

while not three_in_a_row:
    guess = input("Guess heads or tails:")
    coin_flip = rand.randint(0, 1)
    if coin_flip == 0:
        print("The coin landed on heads.")
    else:
        print("The coin landed on tails.")
    if guess == "heads" and coin_flip == 0:
        num_in_a_row += 1
        print(f"You guessed correctly!, you have {num_in_a_row} in a row")
    elif guess == "tails" and coin_flip == 1:
        num_in_a_row += 1
        print(f"You guessed correctly!, you have {num_in_a_row} in a row")

    else:
        print("Sorry, you guessed incorrectly.")
        num_in_a_row = 0
    
    if num_in_a_row == 3:
        three_in_a_row = True
        print("Congratulations! You got three in a row!")