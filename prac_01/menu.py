name = input("Enter your name: ")
MENU = """H - Hello
G - Goodbye
Q - Quit"""
print(MENU)
choice = input (">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid option")
    print(MENU)
    choice = input (">>>").upper()
print("Finished")