'''
Sets -> Non-Primitive data type
     -> Curly Brackets {}
     -> Immutable
     -> has no index
     -> has unique elements
     -> only tuple is applicable here as nested as tuple is also immutable
     -> Sets inside a set is not allowed
     -> Elements in set can't be changed as no indexing
     -> Adding of elements is random is nature
'''
set1 = {}
print(type(set1)) # will give us dictionary

# To declare an empty Set
set2 = set()
print(type(set2)) # will give us set

# Unique elements
set3 = {32,87,54,22,98,39,32,15,15}
print(set3) # will give us unique elements

set4 ={10,32,17,53,20,19,True,71,"you", (10,65,84)} # tuple inside a set
print(set4)

help(set)

# Addition in Set, Addition of element happens one at a time
set4.add("new Element")
print(set4) # order is changed

# Deleting in Set happens one at a time
set4.discard(10)
print(set4)

# Merging in Set
print("New Merge Set - ",set4.union(set3)) 

# Update is modification in Set 
set4.update(set3) 
print(set4)  

# Frozenset -> helps in making the set ordered and does't accepts the methods like add or discard
fset = {10,11,8,65,10,54,32,8,34,11,76}
y=frozenset(fset)
print(y)