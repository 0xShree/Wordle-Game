"""
Simple command line based Wordle Game in python

Wordle is a word game. Player has 6 attempts to guess 5 letter word

After each attempt a clue is showed.
'G' means character is in the word and in the exact position
'Y' means character is in the word and not the in exact position
'-' means character is not the word
"""
import random

word_list = []
word_file = open("word_list.txt")

for word in word_file:
    word_list.append(word.strip())

def checkWord(picked_word, guess_word):
    index = 0
    clue = ""
    for letter in guess_word:
        if letter == picked_word[index]:
            clue += "G"
        elif letter in picked_word:
            clue += "Y"
        else:
            clue += "-"

        # Replacing with dummy character to not to check other letter
        picked_word = picked_word.replace(letter, '0', 1) 
        index += 1
    print(clue)
    return clue == "GGGGG"

if __name__ == "__main__":
    picked_word = random.choice(word_list)
    num_of_guesses = 0
    guessed_correctly = False

    while num_of_guesses < 6 and not guessed_correctly:
        guess_word = input("Input a 5-letter word and press enter: ").upper()
        print("Your guess", guess_word)
        num_of_guesses += 1

        guessed_correctly = checkWord(picked_word, guess_word)

    if guessed_correctly:
        print("Congratulations! You guessed the correct word in", num_of_guesses, "time")
    else:
        print("You have used up your guesses... the correct word is", picked_word)
