import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "huckleberry", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon", "xigua", "yellow watermelon", "zucchini"]

# Get user input
user_input = input("Enter a word: ")

# Get the last letter of the input
last_letter = user_input[-1]

# Find words that start with the last letter
matching_words = [word for word in words if word[0] == last_letter]

# If there are no matching words, give an error message
if len(matching_words) == 0:
    print("There are no words that start with that letter.")
else:
    # Randomly choose a word from the matching words
    chosen_word = random.choice(matching_words)
    print("The chosen word is: " + chosen_word)
