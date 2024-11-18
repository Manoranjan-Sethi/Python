"""
Lists - Non-Primitive data type
      - Combination of data types
      - Should have a square bracket []
      - Mutable
"""
help(list)

list_1 = ["Mano", 23, True, 78.09, None, False]
print(list_1)
print(type(list_1))

num_list = [42, 13, 64, 95, 36]
print(num_list[2])

# Sorting a list descending i.e. z-a
num_list.sort(reverse=True)
print(num_list)

# Sorting a list
num_list.sort() # default a-z
print(num_list)

num_list.pop()
print(num_list)

# Delete a particular element with index
num_list.pop(1) # .pop(index)
print(num_list)

# Remove a particular element with index
num_list.remove(42)
print(num_list)


fruit_list = ["apple", "orange", "Banana"]
print((fruit_list)[-1])  #backward indexing 


# Nested lists

nlist = [1,2,3,["a","b","c","d","e","f","g","h"],7,8,9]
print(nlist[3][2])  # c

nlist = [1,2,3,["a","b","c","d",["e","f"],"g","h"],7,8,9]
print(nlist[3][4][1]) # f

# Method will always have ".methodName(xyz)"; dedicated for a particular class/data type

# Append Method - adds one element at the end of the list

fruit_list = ["apple", "orange", "Banana"]
fruit_list.append("ice apple")
print(fruit_list)

fruit_list.append([12,45,32])
print(fruit_list)  # adds a new nested list

# Extend Method - adds multiple element at the end of the list

fruit_list.extend(["watermelon","dates","dragon fruit"])
print(fruit_list)

# insert element in the middle of the list

fruit_list.insert(3,"berry") # .insert(index where we want to insert,what we want to insert
print(fruit_list)

# Identifying index position of an element
print(fruit_list.index("dates"))
print(fruit_list.index("ice apple"))

# Count of any specific object
print(fruit_list.count("Banana")) 

# Copy of a list
fruit_list_Copy = fruit_list.copy()
print(fruit_list_Copy)

# Wiping the entire object
fruit_list.clear()
print(fruit_list)

# Reversing a list
num_list.reverse()
print(num_list)

fruit_list_Copy.reverse()
print(fruit_list_Copy)


# Sorting alphabets
newL = ["apple", "orange", "b anana"]
newL.sort()
print(newL)