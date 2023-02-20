# # # Project 1
# # # madlib
# # # string concatenation
# youtuber = "DigitalSridhar"

# print("subscribe to" + youtuber)
# print(f"subscribe to {youtuber}")  # cleanest way for string concatenation
# print("subscribe to {}".format(youtuber))

# adj = input("Adjective: ")
# verb1 = input ("Verb: ")
# verb2 = input ("Verb: ")
# famous_person = input ("Famous person: ")
# madlib =f"Computer programming is so {adj}! It makes me so excited all the time because \
#           I love to  {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
# print (madlib)
# madlib =f"Computer programming is so {adj}! It makes me so excited all the time because \
# I love to  {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"          
# print (madlib)

# /*********************************************************************************************************************************************/



# # # Project 2
# # # Guess the secret number
# # # Make the computer to generate a secret number........ for us to guess
# import random
# def guess():
#     random_number = random.randint(1,10)
#     guess = 13467             # Because the user should not enter any value between 1 and 10 
#     while guess != random_number :        
#         guess = int(input(f'Guess a number between 1 and 10 :'))
#         if guess < random_number :
#             print("Sorry, You guessed a lower number")
#         elif guess > random_number :
#             print("Sorry, You guessed a Higher number")
#         elif guess == random_number :
#             print(f"Congrats, You guessed the right number {guess} correctly")
# guess()

# # or 

# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0                    # Just initialized....Because the user should not enter any value between 1 and x, so i take 0
#     while guess != random_number :        
#         guess = int(input(f'Guess a number between 1 and {x} :'))
#         if guess < random_number :
#             print("Sorry, You guessed a lower number")
#         elif guess > random_number :
#             print("Sorry, You guessed a Higher number")
#         elif guess == random_number :
#             print(f"Congrats, You guessed the right number {guess} correctly")
# guess(5)

# # or 

# def guess(x):
#     random_number = random.randint(x,100)
#     guess = 0                    # Just initialized....Because the user should not enter any value between 1 and x, so i take 0
#     while guess != random_number :        
#         guess = int(input(f'Guess a number between {x} and 100 :'))
#         if guess < random_number :
#             print("Sorry, You guessed a lower number")
#         elif guess > random_number :
#             print("Sorry, You guessed a Higher number")
#         elif guess == random_number :
#             print(f"Congrats, You guessed the right number {guess} correctly")
# guess(90)

# /*********************************************************************************************************************************************/

# # # # Project 3
# # # # Guess the secret number
# # # # We can generate a secret number........ Let the computer guess it
# import random
# def computer_guess(x):
#     low =1
#     high = x 
#     feedback = ""   # Just initialized....
#     while feedback != "c" and low != high :
#         guess = random.randint(low, high)      
#         feedback = input ( f"Is {guess} too high (H), too low (L), or correct (C)??)".lower())  # C != c, H!=h 
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f"Congrats, you have gueesed the number, {guess}, correctly!")        
# computer_guess(99)

# or

# import random
# def computer_guess(x):
#     low =1
#     high = x 
#     feedback = ""   # Just initialized....     
#     while feedback != "c" :
#         if low != high :
#             guess = random.randint(low, high)
#         else :
#             guess = low  # which is equal to high also low = high 
#         guess = random.randint(low, high) 
#         feedback = input ( f"Is {guess} too high (H), too low (L), or correct (C)??)".lower())  # C != c, H!=h        
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f"Congrats, you have gueesed the number {guess} correctly!")        
# computer_guess(2345)

# /************************************************************************************************************************************************************************************************/

# # Project 4:
# # Rock paper scissors 
# import random
# def play():
#     user = input (" 'r' for rock, 'p' for paper, 's' for scissors : ")
#     Computer = random.choice(['r','p','s'])
#     if user == Computer:   #  r > s, s > p, p > r
#         return 'tie'
#     if is_win(user,Computer): 
#         return 'Your Won'
#     if is_loss(user,Computer): 
#         return 'Your Loss'

# def is_win(player, opponent):
#     # return True if player wins
#     #  r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#         return True

# def is_loss(player, opponent):
#     # return True if player wins
#     #  r > s, s > p, p > r
#     if (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's') or (player == 'r' and opponent == 'p'):
#         return True
# print(play())

# or

# import random
# def play():
#     user = input (" What's your choice? \n 'r' for rock, 'p' for paper, 's' for scissors : ")
#     Computer = random.choice(['r','p','s'])
#     if user == Computer:   #  r > s, s > p, p > r
#         return 'tie'
#     if is_win(user,Computer): 
#         return 'Your Won'
#     else : 
#         return 'Your Loss'

# def is_win(player, opponent):
#     # return True if player wins
#     #  r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#         return True
# print(play())


# /************************************************************************************************************************************************************************************************/
