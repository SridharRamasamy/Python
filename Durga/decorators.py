# # # # # Video No : 116
# # # # # Decorators
# # # # # ----------------------------------------------------------------
# # # What is decorator
# # # How to define decorator functions?
# # # How to use decorator functions?
# # # What is decorator chaining concept?
# # # How you can invoke a function with and without a decorator function?
# # # # # ----------------------------------------------------------------





# # # # # Generators
# # # # # ----------------------------------------------------------------
# # # # # Power generator will start automatically/ manually whenever the power gone in order to generate electricity
# # # # # Python generator 
# # # # # ----------------------------------------------------------------
# # # # # Python generator - is a function,
# # # # # It will generate a sequence of values without storing the values
# # # # # Internally Python Generator is going to use a (special keyword = Yield) to generate values
# # # # # ((Range, set, list, tuple )- TO store the sequence of values) --> These are not generators
# # # # # ----------------------------------------------------------------------------------------------
# # # # #  Traditional collections [] vs Generator () --> Memory issue
# # # # # ----------------------------------------------------------------------------------------------
# g = [x for x in range(10)]   # # # # List comprehension concept
# print(g) 
# print(type(g))         # # # # #  TypeError: 'list' object is not an iterator
# print(next(g))
 
# l = [x for x in range(1000)]   # # # # List comprehension concept - 1000 objects created, Memory allocated then only it goes to nex line for printing
# print(l)
# print(type(l))

# # # In our home: Rice is required( 1year = 12 bags of rice required) -1) Am i going to store by purchasing it single hand(Traditional collections) or 2) Am i going to purchase only one bag and purchase the next after the completion of 1st bag?(Generators)
# l = [x for x in range(1000000000000000000000000000)]   # # # # List comprehension concept - System will restart/Hang - Memory wont be available(Memory issues) & It will take huge time
# print(l)                                                 # # # # No memory issues will come with generator. (But memory issue will come in case of list)
# # # If we are trying to apply comprehension concept for the tuple, then we will get generator --> Comprehension concept not applicable for tuple
# #  In Traditional collections -->  All objects will be created in the beginning only
# #  In Generators--> No object will be created at the beginning. ON demand objects will be created
# # # # # ----------------------------------------------------------------------------------------------

# l = (x for x in range(10))  
# print(l)
# print(next(l)) 
# print(next(l)) 
# print(next(l)) 
# print(next(l)) 
# print(next(l)) 
# print(next(l)) 
# print(next(l)) 
# print(next(l)) 

# l = (x for x in range(10))  
# print(l)
# while True:
#     print(next(l))  
# # # # # Compile or Runtime issue - Since its a interpretor, it is a Runtime issue
# # # Generator logically will exsist. Only when wwe start accessing the data then only, it will generate the values.
# # # # # ----------------------------------------------------------------------------------------------
# # # Eg: Wanna make my kid MBBS
# # # Option 1: Buy books only for LKG --> If you want to get the values one by one --> go for Generators
# # # Option 1: Buy books till MBBS
# # # # # ----------------------------------------------------------------------------------------------
# # # # Write a generator function to generate values A, B and C
# def mygen():
#     # yield "A", "B", "C"               # # # <class generator>-- for yield keyword ....... The diff btw normal & generator function is the keyword "yield"
#     return "A", "B", "C"                  # # # <class tuple> -- for return keyword
# g = mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))                        # # # After 3 times we cannot use next() as there are only 3 yields in the function
# # # # # ----------------------------------------------------------------------------------------------
# def mygen():
#     yield "A", "B", "C"               # # # <class generator>-- for yield keyword ....... The diff btw normal & generator function is the keyword "yield"
#     # return "A", "B", "C"                  # # # <class tuple> -- for return keyword
# g = mygen()
# print(type(g))
# for x in g:
#     print(x)              # # # We are not asking to print beyond the limit, we just want to print till the value available in g
# # # # # ----------------------------------------------------------------------------------------------
# # # Write a generator function to write first n Natural numbers?
# def first_n_values_generator(n):
#     x=1
#     while x<=n:
#         yield x
#         x+=1
# values = first_n_values_generator(1000000)
# for x in values:
#     print(x)
# # # # # ----------------------------------------------------------------------------------------------
# # # Write a generator function to generate values for count down based on given max value?
# import time
# def countdown_generator(max_value):
#     print("Starting countdown in seconds...")
#     while max_value > 0:
#         yield max_value
#         max_value = max_value - 1
# n = int(input("Enter max value from where countdown should start..."))
# values = countdown_generator(n)
# for x in values:
#     print (x) 
#     time.sleep(1)
# # # # # ----------------------------------------------------------------------------------------------
# # # Write a generator function to generate fibonacci numbers?
# # # The next number is the sum of previous two numbers(0,1,1,2,3,5,8,13...)
# import time
# def fib():
#     a, b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b   # # # we shouldnot define a & b in next lines.
# g = fib()
# for x in g:
#     print(x)
#     time.sleep(1)

# # # # # ----------------------------------------------------------------------------------------------
# # # Write a generator function to generate fibonacci numbers less than 100?
# import time
# def fib():
#     a, b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b   # # # we shouldnot define a & b in next lines.
# g = fib()
# for x in g:
#     if x > 100:
#         break
#     print(x)
#     time.sleep(1)

# # # # # ----------------------------------------------------------------------------------------------
# # # Write a generator function to generate first 5 fibonacci numbers?
# def fib():
#     a, b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b   # # # we shouldnot define a & b in next lines.
# g = fib()
# count = 1
# n = int(input("How many fibonacci numbers are required:"))
# for x in g:
#     if count > n:
#         break
#     print(x)
#     count = count +1
   

# # # # # ----------------------------------------------------------------------------------------------
# # Write a generator function to generate fibonacci numbers btw 25 and 75?
# def fib():
#     a, b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b   # # # we shouldnot define a & b in next lines.
# g = fib()
# for x in g:
#     if x>=25 and x<=75:
#         print(x)
#     if x > 75:
#         break
# # # # # ----------------------------------------------------------------------------------------------
# # # # #  Traditional collections [] vs Generator () --> Performance issue
# # # # # ----------------------------------------------------------------------------------------------
# import random
# names = ["Sridhar", "Sasi", "Elakkiya", "Pravin", "Kavin"]
# subjects = ["Python", "Django", "Datascience", "Cloud", "Devops"]
# def people_list(num_of_people):
#     result = []
#     for i in range(num_of_people):
#         person  = {                                 # # # # Dictionary creation & add this person objects to the result
#             "id": i,
#             "name" : random.choice(names),
#             "subject" : random.choice(subjects)
#             } 
#         result.append(person)
#     return result
# people = people_list(3)
# print(people)
# # # # # ----------------------------------------------------------------------------------------------
# import random
# import time
# names = ["Sridhar", "Sasi", "Elakkiya", "Pravin", "Kavin"]
# subjects = ["Python", "Django", "Datascience", "Cloud", "Devops"]
# def people_list(num_of_people):
#     result = []
#     for i in range(num_of_people):
#         person  = {                                 # # # # Dictionary creation & add this person objects to the result
#             "id": i,
#             "name" : random.choice(names),
#             "subject" : random.choice(subjects)
#             } 
#         result.append(person)
#     return result 
# t1 = time.process_time()
# people = people_list(10000000)
# t2 = time.process_time()
# print("The time taken by list", t2-t1)
# # # # # # ----------------------------------------------------------------------------------------------
# # # # # # Generators
# # # # # # The time taken by list 28.21875
# # # # # # The time taken by generator 2.8125
# # # # # # # ----------------------------------------------------------------------------------------------
# import random
# import time
# names = ["Sridhar", "Sasi", "Elakkiya", "Pravin", "Kavin"]
# subjects = ["Python", "Django", "Datascience", "Cloud", "Devops"]
# def people_list(num_of_people):
#     for i in range(num_of_people):
#         person  = {                                 # # # # Dictionary creation & add this person objects to the result
#             "id": i,
#             "name" : random.choice(names),
#             "subject" : random.choice(subjects)
#             } 
#         yield person
# t3 = time.process_time()
# people = people_list(10000000)
# t4 = time.process_time()
# print("The time taken by generator", t4-t3)     # # #  The time taken will be less in Generator when compared  with List

# # # # # # ----------------------------------------------------------------------------------------------
# import random
# import time
# names = ["Sridhar", "Sasi", "Elakkiya", "Pravin", "Kavin"]
# subjects = ["Python", "Django", "Datascience", "Cloud", "Devops"]
# def people_list(num_of_people):
#     result = []
#     for i in range(num_of_people):
#         person  = {                                 # # # # Dictionary creation & add this person objects to the result
#             "id": i,
#             "name" : random.choice(names),
#             "subject" : random.choice(subjects)
#             } 
#         result.append(person)
#     return result 
# t1 = time.process_time()
# people = people_list(1000)
# print (people)
# t2 = time.process_time()
# print("The time taken by list", t2-t1)
# # # # # # ----------------------------------------------------------------------------------------------
# # # # # # Generators
# # # # # # # ----------------------------------------------------------------------------------------------
# import random
# import time
# names = ["Sridhar", "Sasi", "Elakkiya", "Pravin", "Kavin"]
# subjects = ["Python", "Django", "Datascience", "Cloud", "Devops"]
# def people_list(num_of_people):
#     for i in range(num_of_people):
#         person  = {                                 # # # # Dictionary creation & add this person objects to the result
#             "id": i,
#             "name" : random.choice(names),
#             "subject" : random.choice(subjects)
#             } 
#         yield person
# t1 = time.process_time()
# people = people_list(1000)
# for x in people:
#     print (next(people))
# t2 = time.process_time()
# print("The time taken by generator", t2-t1)     # # #  The time taken will be less in Generator when compared  with List

# # # # # # ----------------------------------------------------------------------------------------------
# # # # # #  Advantages of Generators:
# # # Memorywise & Performancewise generators are recommended to use when compared with traditional collections
# # # If we want to handle huge data like lakhs of employee records from DB, etc. Better to go for generators concept.
# # # Web scraping & Crawling area - Generators are preferred - I will give 1 lakh website(Visit the website one by one and provide the required data)

# # # # # #  Limitations of Generators:
# # # 1. Data wont be stored. Whenever you required you can execute and take, but I wont store the data
# # # 2. We cannot access the particular element.
# # # # # # ----------------------------------------------------------------------------------------------
# # # How to convert Generatot to list:
# def first_n_numbers_generator(n):
#     i =1
#     while i <= n:
#         yield i
#         i = i + 1
# g = first_n_numbers_generator(10)
# l = list(g)                  # # # Conversion of generators to list
# print(l)
# # # # # # ----------------------------------------------------------------------------------------------
# # # What is the difference between decorator and generator?
# # # Decorator - Always going to take Some input function and generate output function with extended capability without modifying the input function
# # # Gednerator - A function To generate a sequence of values
# # #
# # #
# # #
# # #
# # #

# # # # # # ----------------------------------------------------------------------------------------------
# # # # # #  Exception Handling:
# # # If something goes wrong, how you can handle the situation
# # # Alternate way to continue
# # # # # # ----------------------------------------------------------------------------------------------
# # # In any programming 2 types of error:
# # # 1. Syntax error(not related to exception handling)  --> Mistake by programmer (Once all syntax errors are correct then only the program execution will be started by PVM)
# # 2. Logical error/Runtime error/Exceptions - While executing the program something goes wrong because of user input/ Programming logic/memory problem/etc... 
# # # # # # ----------------------------------------------------------------------------------------------
# x = 10
# y = 0
# print(x/y)    # # # ZeroDivisionError
# print(10/"ten") # # # TypeError
# # # # # # ----------------------------------------------------------------------------------------------
# # # In Java: Compiler - For Syntax checking & Interpreter - For Execution
# # # In Python : PVM will do both syntax check & execution
# # # # # # ----------------------------------------------------------------------------------------------
# # # 1. What is an exception?
# # # 2. What is the purpose of exception handling?
# # # 3. What is the meaning of exception handling?
# # # # # # ----------------------------------------------------------------------------------------------
# # # 1. What is an exception?
# # # You are attending offline/direct class @6AM. You have to travel 40km. Catch bus at 5AM. Wakeup @4:30AM. Keep alarm min@2AM
# # # Now class going on. After 10 mins, he starts sleeping(Unwanted/unexpected event happens which disturbs the normal flow of the program) 
# # # This Unwanted/unexpected event = Exception
# # # 5:30 the person started - Tyre punctured exception, which disturbs the normal flow of the program.
# # # -- FileNotFoundError  - Program to read the data from the remote file locating at london. At runtime, the remote file is not available. -->FileNotFoundError
# # # -- EOFerror(EOFError is short for "End-of-Line Error." This error occurs when Python has reached the end of user input without receiving any input), ZeroDivisionError
# # # # # # ----------------------------------------------------------------------------------------------
# # # DB server - Eg: Max 10 connections only will be supported by this DB server. 
# # # The person opening the DB connection has to close the DB connection, otherwise, it will be like one DB connection is open without use(or wasted).
# # # What if all the 10 persons opened and exited without closing. Then the DB will get wasted.
# # # # # # ----------------------------------------------------------------------------------------------





# # # 2. What is the purpose of exception handling?
# # # # # # ----------------------------------------------------------------------------------------------
# # Abnormal termination --> If the program terminates in the middle only 
# # # # # # -------------------
# # # print("statement-1")
# # # print(10/0)        # # # ZeroDivisionError: division by zero
# # # print("statement-3")
# # # # # # -------------------
# # # print("statement-1")  # # # Opening DB connection
# # # print(10/0)        # # # Read Data    --> Abnormal termination
# # # print("statement-3") # # # Closing DB connection
# # # We shouldnot miss/lost anything. We shouldnot block our resources. I want graceful ternmination.
# # # # # # ----------------------------------------------------------------------------------------------
# # Normal Termination --> If the all the statements are executed and comes to the end of the program


# # # 3. What is the meaning of exception handling?
# # # # # # ----------------------------------------------------------------------------------------------
# # # If something goes wrong, we should have alternative way to continue rest of the program normally
# # # We have to define some alternative way to continue rest of the program normally.
# # # Defining this alternative way = exception handling
# # # # # # ----------------------------------------------------------------------------------------------
# # # Experts will think of all the exceptions and define the alternative way accordingly.
# # # # # # ----------------------------------------------------------------------------------------------
# try:
#     read date from remote file locating at london(main code)
# except FileNotFoundError:
#     use local file(alternative)
# Continue rest of the program normally.
# # # # # # ----------------------------------------------------------------------------------------------

# # # Default exception handling in python
# # # # # # -----------------------------
# # #  Every exception is an Object. For every exception, the corresponding classes are available.
# # #  ZeroDivisionError --> Its a class name. For this class, Object will be created
# # # print("statement-1")
# # # print(10/0)        # # # ZeroDivisionError: division by zero --> PVM will check whether the coresponding Except block(Handling code) is available or Not
# # # print("statement-3")                                          --> If Handling code is not available, then the program will terminate(Abnormal Termination) and stopped by printing exception information to the console.
# # # # # # ----------------------------------------------------------------------------------------------



# # # Exception Hierarchy
# # # # # # -----------------------------
# # # TypeError, ValueError, ZeroDivisionError, AttributeError, IndexError, KeyError...
# # # Every exception in python is a class. 
# # # All these exceptions classes are child classes of BaseException(Parent class), either directly(Single inheritance) or Indirectly(Multi level inheritance). Hence baseException is considered as root of Python exception Hierarchy.
# # # Inheritance relation between the classes.
# # # # # # -----------------------------
# # # BaseException is the child class of Object
# # # BaseException --> Exception (AttributeError, ArithmeticError(Zerodivison, FloatingPoint, Overflow), EOFError, NameError, LookupError(Index, Key), OSError(FileNotFound, InteruptedError, PermissionError, TimeOut), TypeError, ValueError)
# # # BaseException --> SystemExit
# # # BaseException --> GeneratorExit
# # # BaseException --> KeyBoardInterrupt 
# # # # # # -----------------------------
# # # ZerodivisonError - PVM creates (e) exception object for this particular class(ZeroDivisonError Class)


# # # Customized exception handling by using try-except:
# # # # # # -------------------------------------------
# # # print("statement-1")
# # # print(10/0)                   # # # Abnormal termination/Non-Graceful termination without try-except:
# # # print("statement-3")                                          
# # # # # # -------------------------------------------
# # # The code which raises an exception is called Risky code --> Inside the try block
# # # The code which raises an exception is called Risky code --> Inside the try block
# # # # # # -------------------------------------------
# # # try:
# # #     risky code(main flow)
# # # except:
# # #     Handling code(alternative flow)
# # # # # # # -------------------------------------------
print("statement-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("statement-3")  
