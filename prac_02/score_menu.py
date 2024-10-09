"""Program to get score, print result and show stars"""


MENU = """
G - get valid score (must be 0 - 100 inclusive)
P - print result
S - show stars
Q - quit 
"""

def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Your score of {score} is {determine_category(score)}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print("Menu")
        choice = input(">>> ").upper()
    print("Farewell")



def get_valid_score():
    score = int(input("Score: "))
    while score == "":
        print("Invalid score")
        score = input("Name: ")
    return score

def determine_category(score):
    if score < 0 or score > 100:
        category = "Invalid score"
    elif score >= 90:
        category = "Excellent"
    elif score >= 50:
        category = "Passable"
    else:
        category = "Bad"
    return category


main()