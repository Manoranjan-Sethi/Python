'''
Tuple - Non-Primitive data type
      - Combination of data types
      - Should have a circle bracket ()
      - immutable
'''

# empty tuple
tuple = ()
print(type(tuple))

# Single tuple
tup1 = (4,) # type is tuple
print(type(tup1))
tup2 = (8) # type is integer
print(type(tup2))

# More about tuple
help(tuple)

newTup = (10,21,65, "SOC", True, None, "Ops", 12,65)


# Slicing - extract multiple elements
# Slicing Syntax - tuple/list(start index, end index+1, jump->if needed)

print(newTup[1:4]) # 21, 65, 'SOC'
print(newTup)

# Slicing with Jump
tuple_1 = ( 20,30,40,80.1,26,71,30,46,30)
print(tuple_1[:5:2])  # (20, 40, 26)
print(tuple_1[2:6:3]) # (40,71)

# Backward Slicing -> tuple can't be reversed as there are no methods as lists, backward 
# slicing is the only way to reverse a tuple

print(tuple_1[-2:-5:-1]) # (46, 30, 71)

# reversing a complete tuple
print(tuple_1[::-1])

newTuple = (12,13,14,151,16,17,19,10)
print(newTuple[6:]) # (19, 10)
print(newTuple[-2:]) # (19, 10)
print(newTuple[:4]) # (12, 13, 14, 151)

'''
List -> []
     -> mutable data type
     -> slower

Tuple -> ()
      -> immutable data type
      -> faster
'''

