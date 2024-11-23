'''
Operators -> Arithmetic Operator - +, -, *, /, //, **, %
          -> Assignment operator - =, +=, -=, *=, %=, //=, /=
          -> Conditional operator - ==, !=, >, < <, >=, <=
          -> Logical operator - and, or, not 
          -> Member operator - in, not in
'''

x=11
y=30

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(y/x)
print("floor",y//x)
print("mod",y%x)
print(y**x)

x+=4
print(x)

check = "abc"
Check = "ABC"
CHECK = "abc"

print(check==Check)
print(check==CHECK)
print(check!=Check)

dict_1 = {"stock": [10,20,33], "products": "fruits", "sales": 30991}
print("stock" in dict_1)  
print("fruits" in dict_1)  # search for keys only
print("fruits" in dict_1.values())
