# # #  vs code shortcuts
# # # Ctrl + P
# # # >Git:
# # # Ctrl + ~
# ctrl + K + C
# ctrl + K + U  
# ctrl + F5



# # # Basics of python
# # # Type casting - example: converting a data type from integer type to String type
# # # String Handling
# # # Multiple assignments to a variable
# # # FMPL - Functions, Modules(Collection of functions), Package(Collection of modules), Libraries(Collection of Packages)
# # # Functions - Inbuilt functions & User defined functions
# # # Inbuilt Functions - print, input

# # # Variables
# import this


# name = "Abinaya"
# print ("hi " + name )
# name = "John"
# print ("hi " + name)
# name = "John"        # string  - Dynamically typed language (((No need mention the data type, like int price = "45" ))) 
# price = 45           # integer  - Starts with ( letter or _) Dont use capital letters in python
# Amount = 35.5        # float
# child = True        # Boolean 
# print (child)



# # # # string handling
# name = "John"
# name = 'John'
# name = '"John"'
# # # # inbuilt methods in strings - methods are Similar to functions
# print (name.upper())    # print() is a function & upper() is a method. Both will come with paranthesis    # method wil be called/invoked by .(dot)
# print (name.lower())      # search python string methods in google  https://www.w3schools.com/python/python_ref_string.asp
# message ="happy birthday"
# print (message.title())
# print(len(message))          #len string method  "returns" the length
# print(message.find("y"))      
# print(message.find("q"))
# print(message.count("p"))
# print(message.replace("p","w"))
# print(message.isalpha())      # only if everything is alphabet   
# print(message.isdigit())
# print (message.title() + name)  # string concatenation
# print (message.title() + " " + name)  # string concatenation
# print("happy\nbirthday")                  # \ represents escape sequence \n \t
# print("happy\tbirthday")                  # \ represents escape sequence
# print(message * 10)

# # # # Multiple assignments
# name , age , height = "john", 30, 178
# print(age)
# like = dislike = 100
# print (like * dislike)
# print(like)
# print (like / dislike)
# print (int(like / dislike))


# # # # Type casting
# otp = 13234
# print("your otp is" + str(otp))        #  Concatenation btw string & integers is not possible
# print(type(otp))                       #  Changing the type of a data or Data type is called type casting
# count = "20"
# print(int(count)+ 1)
# print(count+"1")
# number =30.9                           # leaves .9 as it is, it will just ignore   (it will not round off to 31, it will just leave .9)
# print(int(float(number))+1)
# # # # cmd python >>>try python here 


# # # # # Assignment 1:
# # # Print the following message:
# # # Dear Anand,
# # # You have 15 days of Leave Balance for this 
# # # Year(2021)

# name , leave_balance, year = "Anand", 15, 2021
# print("Dear "+name +",\nYou have " + str(leave_balance) + " days of Leave Balance for this \nYear(" + str(year) +")")


# # # User Input
# name = input ("what is your name : ")
# print("Hello " + name)
# height = str(input ("what is your height : ") )        # # Always the input will be taken as String
# print(type(height))
# print("Your height is " + height +" cms" )
# print(type(height))
# print("Your height is " + str((int(height)/2.54)) +" inch tall" )
# print("Your height is " + str(int(int(height)/2.54)) +" inch tall" )
# height = float(input ("what is your height : ") )
# height_inches = "{:.2f}".format(height/2.54)
# print("Your height is " + str(height_inches) +" inch tall" )

# # # # # # Assignment 2
# # # # Get the user input like Name, email id and Phone number and print the information like this
# # ************************
# # Username : Sridhar
# #  Email : srsr
# #  Ph : ygy
# # # *************************
# username = input("UserName : ")
# email = input("Email : ")
# phone = input("Ph :")
# print("*************************")
# print ("Username : " + username, "\n", "Email : " + email,"\n", "Ph : " + phone)
# print("*************************")



# # # # Math Operations
# a = 10
# b = 5
# a + b
# a - b
# a*b
# a/b   # gives output in float
# int(a/b)
# a/4
# b/2
# (a+b)*5
# a+b*5
# a = 10.9
# b = 10.1  
# c= 10.5
# d = -5.9
# print(round(a), round(b), round(c), abs(d), pow(d,3), a, a**3, max(a,b), min(a,b))
# # importing math module for various mathematical operations   https://www.w3schools.com/python/module_math.asp   https://docs.python.org/3/library/math.html
# a = 10.9
# import math
# print(math.ceil(a))   # rounds to te next integer
# print(math.floor(a))   # rounds to te next integer
# print(math.factorial(int(a)))
# a=5
# print(a%2)

# # # Assignment :3
# # Get a number n from user, compute and print the following values
# print(math.log2(16))
# print(math.cos(16))
# print(math.e**16)
# m = input("User input : ")
# n = int(m)
# print("1.", int(math.log2(n)), "\n", "2.", int(math.cos(n)), "\n","3.", int(math.e**n))







# # # Ifelse --True/False condition  ----Conditional Statements
# # # Relational operators --True/False will be the answer
# pwd_correct = False
# if pwd_correct
#     print("Logged in")
# else:
#     print ("logged out")
#     print ("Incorrect password")
#     print("Try again")
# print("Bye")

# n = 20
# if n>=10:
#     print ("The user input is greater than or equal to 20")
# else:
#     print ("The user input is less than 20")

# num = input ("please provide the number : ")        
# if int(num) % 10 == 0 :                               # the user provided input is always taken as string so it needs to be changed to integer
#     print (" The number yopu have entered is " + str(num) + "and it is exactly divisible by 10")
# else:
#      print (" The number yopu have entered is " + str(num) + "and it is not exactly divisible by 10")

# num = input ("please provide the number : ")        
# if ((int(num) % 10 == 0) and (int(num) % 5 == 0)):                               # the user provided input is always taken as string so it needs to be changed to integer
#     print (" The number yopu have entered is " + str(num) + " and it is exactly divisible by 10 and 5")
# elif int(num) % 10 != 0 and int(num) % 5 == 0:
#     print (" The number yopu have entered is " + str(num) + " and it is not exactly divisible by 10 but exactly divisble by 5")
# else:
#      print (" The number yopu have entered is " + str(num) + " and it is not exactly divisible by 10 and 5")

# score = 169
# if score >= 350:
#     print("India will win the game")
# elif score >= 250:
#     print("India might win the game")
# elif score >= 150:
#     print("Australia might win the game")
# else:
#     print("Australia will win the game")

# # # # nested if:
# # Check if the given number is a 3 digit even number
# m = input("Check the 3 digit even number :")
# n = int(m)
# if n % 2 == 0 :
#     if n >= 100 and n <=999:
#         print(" The given number" + str(n) + " is a 3 digit even number")
#     else:
#         print (" The given number" + str(n) + " is non 3 digit even number")
# else:
#     print (" The given number" + str(n) + " is an odd numner")

# # Check if th student name starts with S:
# name = input("Enter the student name :")
# if name[0] == 'S' or name[0] == 's':
#     print (" The given student name starts with S:")
# else:
#     print(" The given student name does not start with S:")


# # # # bitwise operators ( & and, | or, ~ not, ^ exor(exclusive or), << left shift, >> right shift  )
# # print ( 3&4, 3|4, 3^4 ,12<<1, 12<<2, 12>>1 )
# # print( 12<<1, 12<<2, 3 & 4)


# # # String slicing ----For strings - indexing & reverse(negative) indexing
# name = "Sasirekha"
# print( name[0] )
# print( name[0], name[3] )
# print( name[0:3] )
# print( name[:3] )
# print( name[3:] )
# print( name[2:6] )
# print( name[0:19:2] )      # [start:stop:step]
# print( name[0:19:3] )
# print( name[0:19:4] )
# print( name[-5:-2] )
# print( name[::-1] )           # reverse the string direction
# print( name[-3:-1] ) 
# print( name[2:-2] ) 

# x = slice(2,-2)
# print( name[x])

# # Assignment 4:
# # H
# # Ha
# # Hap
# # Happ
# # Happy
# # y
# # py
# # ppy
# # appy
# # Happy
# str ="Happy"
# print(str[0])
# print(str[0:2])
# print(str[0:3])
# print(str[0:4])
# print(str[0:5])
# print(str[-1])
# print(str[3:])
# print(str[2:])
# print(str[1:])
# print(str[0:])


# # # Lists           ----------Modify, append , insert, remove using del, remove using pop()
# cities = ["Chennai", "Trichy", "Madurai", "Coimbatore"]
# value = [2,34,535,24,234523,23452,2523,5]
# list3 = [ value, 213, 23233]
# print(cities[0], value[3], list3[2])
# cities[2] = "Namakkal"
# print(cities[2])
# cities.append("karur")
# print (cities)
# print(cities[4])
# cities.append("Tirupur")         # append will not return and we cannot get that in variable
# print (cities)
# cities.insert(3,"Tanjore")
# print (cities)
# del cities[1]
# print (cities)
# delete = cities.pop(2)        # pop will return and get that in variable
# cities.remove("karur")
# print (cities)
# cities.append("karur")
# print(cities)
# cities.append("karur")
# print(cities)  
# cities.insert(5, "bangalore")
# print(cities)
# cities.remove("karur")
# print(cities)
# print(sorted(cities))             # temporary sort
# print(cities)              
# print(sorted(value))
# cities.sort()
# print(cities)
# cities.reverse()
# print(cities)
# cities.reverse()
# print(cities)


# # # loop - to repeat aa set of code
# # # while loop

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# letter = ' '
# while not letter.isalpha():
#     letter = input("Enter an alphabet: ")
# print("You have entered " + letter)

# # # print 1 to 100
# num =1
# while num <= 100:
#     print(num)
#     num = num + 1
# print("You have reached 100")


# # # for loop
# for q in range(1, 100 +1):
#     print(q)
# else:
#     print("Bye da. It is working fine")
# for q in range(1, 101):
#     print(q)
# range(1, 10)
# print(list(range(1, 10)))
# print(list(range(1, 10, 2)))
# print(list(range(1, 10, 3)))
# print(list(range(50, 100)))
# print(list(range(100, 50)))
# print(list(range(100, 50, -2)))
# print(list(range(50, 100, -2)))
# print(list(range(50, 100, 2)))

# cities = ["Chennai", "Trichy", "Madurai", "Coimbatore"]
# for i in cities:
#     print(i)
# list = [2,3,4,5,6]
# for i in list:
#     print(i*i)



# # # # # Guess the number game with unlimited attempts
# import random
# num = random.randint(1,20)
# guess = int(input("Can you guess the number I am thinking? Its less than 20 : "))
# while num != guess:
#     if guess > num :
#         print("your have guessed a higher number")

#     guess = int(input("Guess again: "))
# print("Your won")


# # # # Guess the number game with only 4 attempts
# import random
# from urllib.request import HTTPBasicAuthHandler
# num = random.randint(1,20)
# attempt = 1
# guess = int(input("Can you guess the number I am thinking? Its less than 20 : "))
# while num != guess and attempt <= 4:
#     attempt += 1
#     if guess > num:
#         print("your have guessed a higher number")
#     else:
#         print("your have guessed a lower number")
#     guess = int(input("Guess again: "))    
# print("Your won")


# # # # Assignment 5:
# # # # Get input number n from users. Print all the factors of n
# num = int(input("Find the factor for the number: "))


# # # # Get a list of todo lists from the user and add it to a to_do list. Print the list.

# # # # Give an array of integers. Find a peak element in it. An array element is a peak if it is NOT smaller than its neighbours. 
# # # # For corner elements we need to consider only one neighbour eg: in [3,4,7,6,5] - 7 is a peak element

# # # #  Move all negative numbers to the end of the list. List = [3,4,5,-2,-1,8,0,-5,6]

