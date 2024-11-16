"""
Lists - Combination of data types
      - Should have a square bracket
"""

list_1 = ["Mano", 23, True, 78.09, None, False]
print(list_1)
print(type(list_1))

num_list = [2, 3, 4, 5, 6]
print(num_list[2])

fruit_list = ["apple", "orange", "Banana"]
print((fruit_list)[-1])  #backward indexing 


# Nested lists

nlist = [1,2,3,["a","b","c","d","e","f","g","h"],7,8,9]
print(nlist[3][2])  # c

nlist = [1,2,3,["a","b","c","d",["e","f"],"g","h"],7,8,9]
print(nlist[3][4][1]) # f

# Method will always have ".methodname(xyz)"; dedicated for a particular class/data type

# Append Method - adds one element by the end of the list

fruit_list = ["apple", "orange", "Banana"]
fruit_list.append("ice apple")
print(fruit_list)

# Extend Method - adds multiple element by the end of the list

fruit_list.extend(["watermelon","dates","dragon fruit"])
print(fruit_list)

# insert element in the middle of the list

fruit_list.insert(3,"berry") # .insert(index,"name"/number)
print(fruit_list)