MIN_LENGTH = 10
password = input("Enter a password: ")
while len(password) <= MIN_LENGTH:
    print(len(password) * "*")
else:
    print("Invalid password")
    password = input("Enter a password: ")