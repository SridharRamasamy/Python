def calc(a,b):
    sum = a+b
    diff = a-b
    return [sum,diff]     # # #List packing happens
x,y = calc(180,10)       # # # List unpacking happens
print("The sum", x)
print("The diff",y)
t=calc(30,10)
print(type(t))