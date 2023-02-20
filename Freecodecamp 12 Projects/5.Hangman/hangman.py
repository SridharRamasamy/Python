import random
from words import list   # from words.py file import list variable 
print(list)
import string

def get_valid_word(list):
    word = random.choice(list)          # randomly choose something from the list
    while '-' in word or ' ' in word:    # until the statement is true, it will run the statements in the while loop
        word = random.choice(list) # randomly choose something from the list
    return(word)    

def hangman():
    word = get_valid_word(list)
    word_letters = set(word)               # letters we have guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                   # letters, what the user has guessed 
    
    # getting user input
    user_letter = input("Guess a letter: ").upper()

    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)    
    elif user_letter in used_letters:
        print("You have already used the letter, please try again")
    else:
        print("Invalid Character")

user_input = input('Type something:')
print(user_input)



or

import random
import string
list = ["computer", "Laptop", "Windows", "Desktop", ]

word = random.choice(list)          # randomly choose something from the list
print(word)

print("Guess the character: ")
guesses =''
turns_allowed = 3

while turns_allowed > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char)
        else:
            print("_")    
            failed += 1
    if failed == 0 :
        print("You win")     
        print (f"the word is {word}")
        break
    guess = input("Guess the character:")
    guesses += guess
        
