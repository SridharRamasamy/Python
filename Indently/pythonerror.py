# # # 1. Attribute error:
# # Scenario:1
# number = 10
# number.append(10)
# # Scenario:2
# class Apple:
#     .....
# apple = Apple()
# apple.run()



# # # 2. Assertion error:
# has_connection: bool = False
# assert has_connection, "No Connection..."


# # # 3. ModuleNotFoundError
# if the module is not imported


# # # 4. SyntaxError:
# print("Hello"):

# # # 5. TypeError:
# Syntax is correct but the operation cannot be performed by Python
# print("Hello" + 10)   # # -- Datatype error

# # # 6. IndexError:
# numbers = [1, 2, 3]
# print(numbers[3])


# # # 7. NameError:    
# # # If the variable is not defined:  
# def do():
#     x = 10
# print(x) # #- x is not a global variable


# # # 8. RecursionError: 
# def func():
#     func()    # # # Previous line repeated 996 more times
# func()


# # # 9. IndentationError: 


# # # 10. ValueError: 
# import math
# print(math.sqrt(-10))  # # # Sqrt of value 10
