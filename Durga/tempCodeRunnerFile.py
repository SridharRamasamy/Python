put("Enter the number of rows:"))
for i in range(n):
    print(((i)*" "),end =" ")     # # This will just print the front spaces and the printing of next for loop will be continued in the same line as we are using end=" "
    for j in range(n-i):
        print(chr(64+n-j), end =" ")
    print()