cost_of_sandwich = 5

answer = int(input("How much money do you have?"))

if answer == 1000:
    print("You have exactly 1000 dollars!")
elif answer >= cost_of_sandwich:
    print("You can buy a sandwich!")
else:
    print("You can't buy anything.")

#test