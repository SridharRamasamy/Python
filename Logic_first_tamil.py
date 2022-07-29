# #  vs code shortcuts
# # Ctrl + P
# # >Git:
# # Ctrl + ~


# # Basics of python
# # Functions - Inbuilt functions & User defined functions
# # Inbuilt Functions

# # Variables
name = "Abinaya"
print ("hi " + name )
name = "John"
print ("hi " + name)
name = "John"        # string  - Dynamically typed language (((No need mention the data type, like int price = "45" ))) 
price = 45           # integer  - Starts with ( letter or _) Dont use capital letters in python
Amount = 35.5        # float
child = True        # Boolean 
print (child)



# # # string handling
name = "John"
name = 'John'
name = '"John"'
# # # inbuilt methods in strings - methods are Similar to functions
print (name.upper())    # print() is a function & upper() is a method. Both will come with paranthesis    # method wil be called/invoked by .(dot)
print (name.lower())      # search python string methods in google  https://www.w3schools.com/python/python_ref_string.asp
message ="happy birthday"
print (message.title())
print(len(message))          #len string method  "returns" the length
print(message.find("y"))      
print(message.find("q"))
print(message.count("p"))
print(message.replace("p","w"))
print(message.isalpha())      # only if everything is alphabet   
print(message.isdigit())
print (message.title() + name)  # string concatenation
print (message.title() + " " + name)  # string concatenation
print("happy\nbirthday")                  # \ represents escape sequence
print("happy\tbirthday")                  # \ represents escape sequence
print(message * 10)
# # # Multiple assignments
name , age , height = "john", 30, 178
print(age)
like = dislike = 100
print (like * dislike)
print(like)
print (like / dislike)
print (int(like / dislike))
# # # Type casting
otp = 13234
print("your otp is" + str(otp))      #  Concatenation btw string & integers is not possible
print(type(otp))                       #  Changing the type of a data or Data type is called type casting
count = "20"
print(int(count)+ 1)
print(count+"1")
number =30.9                           # leaves .9 as it is, it will just ignore   
print(int(float(number))+1)
# # # cmd python >>>try python here 


# # # # Assignment 1:
# # Print the following message:
# # Dear Anand,
# # You have 15 days of Leave Balance for this 
# # Year(2021)

name , leave_balance, year = "Anand", 15, 2021
print("Dear "+name +",\nYou have " + str(leave_balance) + " days of Leave Balance for this \nYear(" + str(year) +")")