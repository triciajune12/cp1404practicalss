"""
Write a program that reads a string from the user and then produces a table of the letters of the alphabet
in alphabetical order

Word Occurrences
Estimate: 10 minutes
Actual:   8 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    try:
        word_to_count[word] += 1

    except KeyError:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
