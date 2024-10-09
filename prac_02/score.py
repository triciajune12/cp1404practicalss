"""
program to determine score status
"""


import random

def main():
    score = get_score()
    random_score = random.randint(1, 100)
    print(f"Your score of {score} is {determine_category(score)}")
    print(f"Your score of {random_score} is {determine_category(random_score)}")


def get_score():
    score = int(input("Enter score: "))
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








