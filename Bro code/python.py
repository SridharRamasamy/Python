# # # https://www.youtube.com/watch?v=ivl5-snqul8
# # # recursion - A function that calls itself, from within,
                    # helps to visualize a complex problem into basic steps,
                    # which can be solved more easily & iteratively or recursively

# # ITERATIVE Approach                   
# def walk(steps):
#     for x in range(1, steps+1):
#         print("You take step  number{}".format(x))
# walk(20)
# # # # --------------------------------------------------------------------------------------------------------------------------------------
# # # RECURSIVE Approach 
# def walk(steps):
#     print("You take step  number{}".format(steps))    
#     walk(steps-1)          # # #  RecursionError: maximum recursion depth exceeded while calling a Python object
# walk(20)

# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps-1)
#     print("You take step  number{}".format(steps))    
# walk(100)

# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps-1)                                       # # #    [Previous line repeated 995 more times] - There is a limit in the number of freames in the call stack
#     print("You take step  number{}".format(steps))    # # #  RecursionError: maximum recursion depth exceeded in comparison
# walk(1000)
# # # # --------------------------------------------------------------------------------------------------------------------------------------
    
# # Finding the factorial of the number 5 
# # ITERATIVE Approach 
# def factorial(x):
#     result =1
#     if x>0:
#         for a in range(1, x+1):
#             result *= a
#         return result
# print(factorial(10))
                 