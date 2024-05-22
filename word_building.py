import time
import nltk

# Download the word list from nltk
nltk.download('words')
from nltk.corpus import words
word_list = set(words.words())

def get_score(previous_word, current_word):
    # Find the longest common substring at the end of previous_word that matches the start or the reverse of the start of current_word
    max_len = min(len(previous_word), len(current_word))
    normal_score = 0
    reverse_score = 0
    # Flag to check if the current word starts with the last or the reverse of the last substring of the previous word
    follows_basic_rule = False

    # Check for direct substring match
    for i in range(max_len, 0, -1):
        if previous_word.endswith(current_word[:i]):
            normal_score = i
            follows_basic_rule = True
            break


    # Check for reverse substring match
    for i in range(max_len, 0, -1):
        if previous_word.endswith(current_word[:i][::-1]):
            reverse_score = 2 * i if i != 1 else 1  # Double points for reverse match
            follows_basic_rule = True
            break

    return 0.5 if follows_basic_rule and len(current_word) < 4 else max(normal_score, reverse_score)

print("Enter any word to start the game:")
previous_word = input().lower()
used_words = set([previous_word])  # Start with the first word in the set

score = 0
start_time = time.time()  # Record the start time of the game

while True:
    # Check if 60 seconds have passed
    if time.time() - start_time > 60:
        print("Time's up! Game Over!")
        break

    print("Enter the word: ")
    current_word = input().lower()

    # Validate if the word is in the dictionary
    if current_word not in word_list:
        print("Invalid word! Game Over!")
        break

    # Validate if the word is already used
    if current_word in used_words:
        print("Repeated word! Game Over!")
        break

    # Calculate the score for the move
    substring_score = get_score(previous_word, current_word)
    if substring_score == 0:
        print("Word does not start with any substring or its reverse of the previous word! Game Over!")
        break

    previous_word = current_word
    used_words.add(current_word)  # Add the current word to the set of used words
    score += substring_score  # Increment score based on the rule
    print(f"Current Score: {score}")

print(f"Final Score: {score}")
