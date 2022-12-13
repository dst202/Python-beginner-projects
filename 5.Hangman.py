#code to play hangman from words file with systems with limited lives

import random
from words import words
import string
#code to filter valid words from words list and to elimiate hypen and dash containing words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

#main code to execute hangman game

def hangman():

    word = get_valid_word(words)
    print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

#getting user input
    while len(word_letters)>0:

        #used letters
        print('You have used these letters :',' '.join(used_letters))
        #print word with guessd letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print ('current word:',' '.join(word_list))

        guess_letter = input("Enter a character :")
        if guess_letter in alphabet - used_letters:
            used_letters.add(guess_letter)
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
            elif guess_letter in used_letters:
                print("You have already used that letter")
            else:
                print("You entered invalid character.Please try again")



hangman()


