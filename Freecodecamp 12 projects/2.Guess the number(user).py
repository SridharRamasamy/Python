# # Project 2
# # Guess the secret number
# # Make the computer to generate a secret number........ for us to guess
import random
def guess():
    random_number = random.randint(1,10)
    guess = 13467             # Because the user should not enter any value between 1 and 10 
    while guess != random_number :        
        guess = int(input(f'Guess a number between 1 and 10 :'))
        if guess < random_number :
            print("Sorry, You guessed a lower number")
        elif guess > random_number :
            print("Sorry, You guessed a Higher number")
        elif guess == random_number :
            print(f"Congrats, You guessed the right number {guess} correctly")
guess()

# # or 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0                    # Just initialized....Because the user should not enter any value between 1 and x, so i take 0
    while guess != random_number :        
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number :
            print("Sorry, You guessed a lower number")
        elif guess > random_number :
            print("Sorry, You guessed a Higher number")
        elif guess == random_number :
            print(f"Congrats, You guessed the right number {guess} correctly")
guess(5)

# # or 

def guess(x):
    random_number = random.randint(x,100)
    guess = 0                    # Just initialized....Because the user should not enter any value between 1 and x, so i take 0
    while guess != random_number :        
        guess = int(input(f'Guess a number between {x} and 100 :'))
        if guess < random_number :
            print("Sorry, You guessed a lower number")
        elif guess > random_number :
            print("Sorry, You guessed a Higher number")
        elif guess == random_number :
            print(f"Congrats, You guessed the right number {guess} correctly")
guess(90)
