"""
Functions -> reusable block of code
Types -> build-in functions - print(), id(), type(), help()
      -> user defined functions
      -> anonymous functions - functions with no name
      -> recursive functions - function calling itself
"""
'''
-> User defined functions Syntax:
def functionName(parameter1, parameter2, ....):
    # block of code
    print()/return

# call the function with arguments
functionName(argument1, argument1, ....)
'''

# 1. Sum of two numbers

def sum1(a, b):
    return a+b

print(sum1(10, 20))

# user input for sum of two numbers

def sum2():
      a=int(input("Enter the first number to add: "))
      b=int(input("Enter the second number to add: "))
      print(a+b) 

sum2()

def subt(c,d):
    return c-d

# When 2 variables comes into reference/substitution called pass by value
# Here a and c from function sum1 and subt points to same memory location i.e. var1 as 68
def passByValue(var1,var2):
    z=sum1(var1,var2)       
    y=subt(var1,var2)
    print(z,y)

passByValue(68,34)

