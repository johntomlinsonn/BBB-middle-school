password = input("Enter the password: ")
num_of_attempts = 1

while password != "secret":
    password = input("Enter the password: ")
    num_of_attempts += 1

print("Access granted!")