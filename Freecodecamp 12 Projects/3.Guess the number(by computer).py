# # # Project 3
# # # Guess the secret number
# # # We can generate a secret number........ Let the computer guess it
import random
def computer_guess(x):
    low =1
    high = x 
    feedback = ""   # Just initialized....
    while feedback != "c" and low != high :
        guess = random.randint(low, high)      
        feedback = input ( f"Is {guess} too high (H), too low (L), or correct (C)??)".lower())  # C != c, H!=h 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats, you have gueesed the number, {guess}, correctly!")        
computer_guess(99)

# # or

def computer_guess(low, high):
    feedback = ""   # Just initialized....
    while feedback != "c" and low != high:      # # In while loop mostly the condition will be given as not matching/failing case, so that we can get into the loop and make it pass
        guess = random.randint(low, high)      
        feedback = input ( f"Is {guess} too high (H), too low (L), or correct (C)??)".lower())  # C != c, H!=h 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats, you have gueesed the number, {guess}, correctly!")        
computer_guess(1,99)

# # or

import random
def computer_guess(x):
    low =1
    high = x 
    feedback = ""   # Just initialized....     
    while feedback != "c" :
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low  # which is equal to high also low = high 
        guess = random.randint(low, high) 
        feedback = input ( f"Is {guess} too high (H), too low (L), or correct (C)??)".lower())  # C != c, H!=h        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats, you have gueesed the number {guess} correctly!")        
computer_guess(2345)
