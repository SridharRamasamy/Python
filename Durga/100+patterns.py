# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 1  
# # # end attribute -  print() - will default breaks the current line and initiate the next line, to avoid this end attribute is used inside print
# # # To print the * n numner of times
# n = int(input("Enter n Value:"))
# for i in range(n):
#     print ("*")          # # # print() - will default breaks the current line and initiate the next line, to avoid this end attribute is used inside print

# n = int(input("Enter n Value:"))
# for i in range(n):
#     print ("*", end=" ")

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 2  
# # # To print square pattern with * symbols
# # # * * *
# # # * * *
# # # * * *
# # # 
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print ("*" * i)

# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print ("*" * (i+1))
    
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print ("*" * n)

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 3  
# # # To print square pattern with the given fixed digit
# # # 5 5 5 5 5
# # # 5 5 5 5 5
# # # 5 5 5 5 5
# # # 5 5 5 5 5
# # # 5 5 5 5 5
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print ((str(n)+" ") * n)

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 4 
# # To print square pattern with the given fixed digit in every row
# # 1 1 1 1 1
# # 2 2 2 2 2
# # 3 3 3 3 3
# # 4 4 4 4 4 
# # 5 5 5 5 5
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print ((str(i+1)+" ") * n)

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 5 
# # To print square pattern with fixed alphabet symbol
# # A A A A A
# # A A A A A
# # A A A A A
# # A A A A A
# # A A A A A
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print (("A") * n)

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 6 
# # To print square pattern with fixed alphabet symbols
# # A A A A A
# # B B B B B
# # C C C C C
# # D D D D D
# # E E E E E
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print (chr(65+i) * n)     # # # By using the unicode values. If you know unicode value get the corresponding alphabet with chr() function
 
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 7 
# # To print square pattern with digits
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# n = int(input("Enter the number of rows:"))
# for i in range(n):                                    # # # (n) here for number of rows
#     for j in range(n):                                # # # (n) here for number of columns
#         print(str(j+1), end=" ")
#     print()          # # # in order to go to the next blank line 
 
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 8 
# # To print square pattern with alphabet in dictionary order
# # A B C D E
# # A B C D E
# # A B C D E
# # A B C D E
# # A B C D E
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n):
#         print(chr(65+j), end=" ")
#     print()          # # # in order to go to the next blank line 
 
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 9 
# # To print square pattern with digits in descending order
# # 5 5 5 5 5
# # 4 4 4 4 4 
# # 3 3 3 3 3 
# # 2 2 2 2 2 
# # 1 1 1 1 1
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print((str(n-i) + " ")* n)
 
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 10 
# # To print square pattern with alphabets in reverse of dictionary order
# # E E E E E
# # D D D D D
# # C C C C C
# # B B B B B
# # A A A A A
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print((chr(64+n-i) + " ")* n)
 
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 11 
# # To print square pattern with digits descending order
# # 5 4 3 2 1     # # # Within the row, the symbol is changing --> Means nested loop is must required
# # 5 4 3 2 1
# # 5 4 3 2 1
# # 5 4 3 2 1
# # 5 4 3 2 1
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n):
#         print((str(n-j) + " "), end =" ")
#     print()
 
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 12 
# # To print square pattern with alphabets in reverse of dictionary order
# # E D C B A     # # # Within the row, the symbol is changing --> Means nested loop is must required
# # E D C B A 
# # E D C B A 
# # E D C B A 
# # E D C B A 
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n):
#         print((chr(64+n-j) + " "), end =" ")
#     print()

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 13 
# # To print the right angle triangle with * symbols 
# # *
# # * *
# # * * *
# # First way
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# # Second way
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print ("* " * (i+1))
# # # -------------------------------------------------------------------------------------------------------------
# # # My Own experimental patterns:
# # * ** *** **** 
# # * ** *** **** 
# # * ** *** **** 
# # * ** *** **** 
# # n = int(input("Enter number of rows:"))
# # for i in range(n):
# #     for j in range(n):
# #         print ((("*")*(j+1)), end =" " )
# #     print()
 
     
# # * * * * 
# # ** ** ** **         
# # *** *** *** ***     
# # **** **** **** **** 
# # n = int(input("Enter number of rows:"))
# # for i in range(n):
# #     for j in range(n):
# #         print ((("*")*(i+1)), end =" " )
# #     print()

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 14
# # To print the right angle triangle with fixed digit in every row
# # 1
# # 2 2
# # 3 3 3
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print((i+1), end=" ")
#     print()
        
# # Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print((str(i+1)+ " ")*(i+1))
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 15
# # To print the right angle triangle with fixed digit alphabet symbol
# # A
# # B B
# # C C C
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end=" ")
#     print()

# Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print((chr(i+65)+ " ")*(i+1))
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 16
# # To print the right angle triangle with digits in ascending order every row
# # 1
# # 1 2
# # 1 2 3
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print(str(j+1), end=" ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 17
# # To print the right angle triangle with alphabet symbols in dictionary order in every row
# # A
# # A B
# # A B C
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(j+65), end=" ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 18
# # To print the right angle triangle with digits in descending order in dictionary order in every row
# # 5
# # 5 4
# # 5 4 3
# # 5 4 3 2
# # 5 4 3 2 1
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print((str(n-j)), end= " ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 19
# # To print the right angle triangle with alphabet symbols in reverse of dictionary order in every row
# # E
# # E D
# # E D C
# # E D C B
# # E D C B A
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print((chr(64+n-j)), end= " ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 20
# # To print the inverted right angle triangle with * symbols
# # * * * * *
# # * * * * 
# # * * * 
# # * * 
# # * 
# # # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end= " ")
#     print()

# # Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print("* " * (n-i))

# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 21
# # To print the inverted right angle triangle with * symbols
# # * * * * *
# # * * * * 
# # * * * 
# # * * 
# # * 
# # # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print((i+1), end =" ")
#     print()

# # # Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print((str(i+1)+ " " )*(n-i))
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 22
# # To print the inverted right angle triangle with fixed  alphabet symbol in every row
# # A A A A A 
# # B B B B  
# # C C C
# # D D 
# # E 
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(65+i), end =" ")
#     print()
# # Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print(((chr(65+i)+" ")*(n-i)))
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 23
# # To print the inverted right angle triangle pattern with  fixed digit in every row
# # 5 5 5 5 5
# # 4 4 4 4 
# # 3 3 3
# # 2 2 
# # 1
# # # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(str(n-i), end =" ")
#     print()
# # Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print(((str(n-i)+" ")*(n-i)))
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 24
# # To print the inverted right angle triangle with fixed  alphabet symbol in every row
# # E E E E E 
# # D D D D 
# # C C C
# # B B
# # A
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(64+n-i), end =" ")
#     print()
# # Second way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     print(((chr(64+n-i)+" ")*(n-i)))
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 25
# # To print the inverted right angle triangle pattern with digits in ascending order in every row
# # 1 2 3 4 5
# # 1 2 3 4
# # 1 2 3 
# # 1 2 
# # 1
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(str(j+1), end =" ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 26
# # To print the inverted right angle triangle with alphabet symbol in dictionary order in every row
# # A B C D E
# # A B C D 
# # A B C 
# # A B 
# # A 
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(65+j), end =" ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 27
# # To print the inverted right angle triangle pattern with digits in decending order in every row
# # 5 4 3 2 1
# # 5 4 3 2 
# # 5 4 3
# # 5 4 
# # 5
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(str(n-j), end =" ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 28
# # To print the inverted right angle triangle with alphabet symbol in reverse order of dictionary order in every row
# # E D C B A
# # E D C B 
# # E D C 
# # E D 
# # E
# # First way:
# n = int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(64+n-j), end =" ")
#     print()
# # # -------------------------------------------------------------------------------------------------------------
# # # Pattern - 29
# # To print pyramid pattern with * symbol
# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *
n = int(input("Enter the number of rows:"))
for i in range(n):
    print(((n-i-1)*" ")+("*"*(i+1)))
# # # Number of spaces in every row: n-i-1
# # # How many times * to be print: i+1
