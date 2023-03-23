# # # *****************************************************************************************************************************
# # # *****************************************************************************************************************************
# # # session - 54  ***************************************************************************************************************
# # # *****************************************************************************************************************************
# # # *****************************************************************************************************************************
# # # Functions: To avoid code repitition, Readability is down (Function - A group of repeatedly used statements)
# # # DRY Principle - Don't Repeat yourself
# # # If any code repeatedly needed, then group the repeated code into a unit(Function) and call the unit any number of times
# # # Functions 
# #           - 1. Builtin/Inbuilt/Predefined functions   - id(), print(), input(), eval(), len()
# #           - 2. User defined functions                 - calc()
# #           - 3. Defining a function and calling a function (Write once & Use any number of times)
# #           - 4. Functions vs Methods 
# #           - 5. Functions should be defined before calling functions


# # # ----------------------------------------------------------------------------------------
# a = 20
# b = 10
# print("The Sum:", a+b)
# print("The Difference:", a-b)
# print("The Product:", a*b)
# print("The Dividend:", a/b)

# a = 200
# b = 100
# print("The Sum:", a+b)
# print("The Difference:", a-b)
# print("The Product:", a*b)
# print("The Dividend:", a/b)

# a = 200
# b = 100
# print("The Sum:", a+b)
# print("The Difference:", a-b)
# print("The Product:", a*b)
# print("The Dividend:", a/b)
# # # ----------------------------------------------------------------------------------------
# def calc(b,a):
#     print("The Sum:", a+b)
#     print("The Difference:", a-b)
#     print("The Product:", a*b)
#     print("The Dividend:", a/b)
# calc(10,20)
# calc(100,200)
# calc(1000,2000)
# # # ----------------------------------------------------------------------------------------
# # # Functions 
# #           - 1. Builtin/Inbuilt/Predefined functions   - id(), print(), input(), eval(), len()
# #           - 2. User defined functions                 - calc()

# # - User defined functions:
# # # ----------------------------------------------------------------------------------------
# def function_name(parameters):
#     '''doc string'''
#     business logic
#     business logic
#     return value
# def(mandatory) &  parameter, return, docstring(optional)  

# # # Methods - Functions defined within the class is called methods  - 
# # # Functions - Functions defined within the class is called methods  - Functional programming concept
# # # ForLoop cannot replace functions concept as functions can be called from any part of the code(At different places).
# # # While calling the functions, the argument has to be passed correctly.
# # # ----------------------------------------------------------------------------------------
# # # Write the fucntion to take the number as a argument and print its square value:
# def squareit(a):
#     print("The square value of {} is {}".format(a, a*a))
# squareit(4)
# def squareit(a):
#     return a*a
# result = squareit(4)
# print("The square value is:", result)
# # # ----------------------------------------------------------------------------------------
# def validate(mobile_number):
#     if len(mobile_number) == 10:
#         return True
#     else:
#         return False
# mobile_number = input("Enter mobile number: ")
# result = validate(mobile_number)
# if result == True:
#     write this number to a file/database(instead of Print)
# # # ----------------------------------------------------------------------------------------
# x = 10
# print(id(x)) 
# print(print(x))         # # # ---print(x) just prints and it will not return any value to the second print. 
# # # if return is not mentioned inside the function, then None will be returned.
# # # ----------------------------------------------------------------------------------------
# def show(sequence):
#     for x in sequence:
#         print(x)
# show('rekha')
# show(range(1,5))
# # show(1,5)                 # This is not possible
# # # ----------------------------------------------------------------------------------------
# # Write a function to find the factorial of given number?? 5! = 5*4*3*2*1
# def fact(n):
#     result = 1            
#     while n>1:
#         result = result*n
#         n = n-1
#     return result
# print(fact(5))
# for i in range(1,11):
#     print("The factorial of {} is: {}".format(i,fact(i)))
# for i in range(1,11):
#     print("The factorial of {} is: {}".format(i,fact(i)))
# # # ----------------------------------------------------------------------------------------
# def fact(n):
#     result = 1
#     while n>1:
#         result = result*n
#         n = n-1
#     print("The factorial of {} is: {}".format(n,result))
# print(fact(5))
# for i in range(1,11):
#     fact(i)
# # # ----------------------------------------------------------------------------------------
# # # A function can have multiple return values*********************
# def calc(a,b):
#     sum = a+b
#     diff = a-b
#     return sum,diff     # # #Tuple packing happens
# x,y = calc(180,10)       # # # Tuple unpacking happens
# print("The sum", x)
# print("The diff",y)
# t=calc(30,10)
# print(type(t))
# # # ----------------------------------------------------------------------------------------
# # A function can have multiple return values*********************
# def calc(a,b):
#     sum = a+b
#     diff = a-b
#     return [sum,diff]     # # #List packing happens
# x,y = calc(180,10)       # # # List unpacking happens
# print("The sum", x)
# print("The diff",y)
# t=calc(30,10)
# print(type(t))
# # # ----------------------------------------------------------------------------------------
# def calc(a,b):
#     sum = a+b
#     diff = a-b
#     mul = a*b
#     div =a/b
#     return sum,diff, mul,div     # # # tuple packing happens
# t = calc(180,10)       # # # tuple unpacking happens
# for x in t:
#     print(x)
# print(type(t))
# # # ----------------------------------------------------------------------------------------



# # # -------------
# # # *****************************************************************************************************************************
# # # *****************************************************************************************************************************
# # # session - 55  ***************************************************************************************************************
# # # *****************************************************************************************************************************
# # # *****************************************************************************************************************************
# # # -------------
# # # Types of arguments/parameters:
# # # -------------
# # # Formal parameters & Actual arguments
# # # 4 types of arguments: 
# # # # # 1. Positional arguments  - While calling the function
# # # # # 2. Keyword arguments     - While calling the function
# # # # # 3. Default arguments     - While declaring/defining the function
# # # # # 4. Variable Length arguments


# # # # # 1. Positional arguments
# # # -----------------------------
# def sub(a,b):
#     print(a-b)
# sub(10,20)     # # #  Positional arguments
# sub(20,10)
# # # The number of arguments must be Matched
# # # The Order of arguments is important, the result may be changed if we change the order


# # # # # 2. Keyword arguments
# # # -----------------------------
# # # We have to pass the values by keyword ie by parameter name
# def sub(a,b):
#     print(a-b)
# sub(a=10,b=20)     # # #  Keyword arguments
# sub(a=20,b=10)
# # # The number of arguments must be Matched
# # # The Order of arguments is not important. But the argument name should be same(a&b)
# # # Note: Both positional arguments and keyword arguments can be used simultaneously like sub(10,b=20) (First positional argument & Keyword argument has to be used) 
# # # The number of arguments must be Matched sub(a=10,20)   # # # Syntax error
# # # ---------------------------------------------------------------------------------------------------------
# def sub(a,b,c,d,e):
#     print(a-b)
# sub(d=10,20,30,40,50)     # # #  Order of arguments is wrong - SyntaxError: positional argument follows keyword argument
# # sub(10,20,30,50,d=40)     # # #  Order of arguments is wrong - TypeError: sub() got multiple values for argument 'd'
# # sub(10,20,30,d=40,50)       # # #  Order of arguments is wrong - Syntax Error = Positional arguments follows keyword arguments
# # sub(10,20,30,d=40, e=50)       # # #  Right - Once the keyword arguments starts, the following remaining has to be also keyword argumants only 
# # sub(10,20,30,e=50, d=40)       # # #  Right - Once the keyword arguments starts, the following remaining has to be also keyword argumants only 
# # # ---------------------------------------------------------------------------------------------------------
# # # # Find which one is the incorrect way of calling the function
# def wish(name, msg):
#     print("Hello {} {}".format(name, msg)
# # wish(Sasi, Happy birthday)
# # wish(name=Sasi, Happy birthday)
# # wish(Sasi,msg=Happy birthday)
# # wish(name=Sasi,msg=Happy birthday)
# # wish(NAME=Sasi,msg=Happy birthday)
# # # Positional argument follows keyword argument, but keyword argument won't follow Positional Argument 
# # # ---------------------------------------------------------------------------------------------------------




# # # # # 3. Default arguments
# # # ---------------------------------------------------------------------------------------------------------
# # If user doesnot provide any value, the default value will be considered
# # Default arguments should be last arguments. After default arguments we cannot take general/ Non-Default arguments
# # # ---------------------------------------------------------------------------------------------------------
# def wish(name = "Guest", msg):       # # # SyntaxError: non-default argument follows default argument
#     print("Hello {} {}".format(name, msg))
# wish(HappyBirthday)  
# # # ---------------------------------------------------------------------------------------------------------
# def wish(msg="Good Morning", name = "Guest"):       
#     print("Hello {} {}".format(name, msg))
# wish(msg="Good Afternoon", name = "Sridhar")                        # # #  NameError: name 'HappyBirthday' is not defined
# # # ---------------------------------------------------------------------------------------------------------
# def wish(msg, name = "Guest"):       
#     print("Hello {} {}".format(name, msg))
# wish("Good Afternoon")                        # # #  NameError: name 'HappyBirthday' is not defined
# # # ---------------------------------------------------------------------------------------------------------
# # After default arguments we cannot take non-default arguments...
