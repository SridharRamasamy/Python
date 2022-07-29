# # #  vs code shortcuts
# # # Ctrl + P
# # # >Git:
# # # Ctrl + ~


# # # Basics of python
# # # Functions - Inbuilt functions & User defined functions
# # # Inbuilt Functions

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
# print("happy\nbirthday")                  # \ represents escape sequence
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
# print("your otp is" + str(otp))      #  Concatenation btw string & integers is not possible
# print(type(otp))                       #  Changing the type of a data or Data type is called type casting
# count = "20"
# print(int(count)+ 1)
# print(count+"1")
# number =30.9                           # leaves .9 as it is, it will just ignore   
# print(int(float(number))+1)
# # # # cmd python >>>try python here 


# # # # # Assignment 1:
# # # Print the following message:
# # # Dear Anand,
# # # You have 15 days of Leave Balance for this 
# # # Year(2021)

# name , leave_balance, year = "Anand", 15, 2021
# print("Dear "+name +",\nYou have " + str(leave_balance) + " days of Leave Balance for this \nYear(" + str(year) +")")


# # # # User Input
# name = input ("what is your name : ")
# print("Hello " + name)
# height = input ("what is your height : ")         # # Always the input will be taken as String
# print(type(height))
# print("Your height is " + height +" cms" )
# print("Your height is " + str(int(height)/2.54) +" inch tall" )
# print("Your height is " + str(int(int(height)/2.54)) +" inch tall" )
# height = float(input ("what is your height : ") )
# height_inches = "{:.2f}".format(height/2.54)
# print("Your height is " + str(height_inches) +" inch tall" )

# # # # # # Assignment 2
# # # # Get the user input like Name, email id and Phone number and print the information like this
# # # ************************
# # # Username : Sridhar
# # #  Email : srsr
# # #  Ph : ygy
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
