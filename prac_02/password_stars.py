"""password check program"""

def main():
   password = get_password()
   print_stars(password)

def get_password():
    password = input("enter a password: ")
    while len (password) < 8:
        print("invalid password")
        password = input("enter a password: ")
    return password

def print_stars(password):
    print("*" * len(password))

main()
