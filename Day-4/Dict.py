'''
Dictionary -> Declaration is done with {}
           -> combination of elements with Key Value Pair
           -> in Key - all primitive and tuple are accepted
                     - keys are Immutable and Unique
           -> in Value - all data types are accepted
                       - values are mutable
'''

dict1 = {"name":"Mano","age":26,"interest":"Cars","d":4}
print(type(dict1))
print(dict1)
print(dict1["name"])

# help(dict)

# Key overridden
dict1 = {"name":"Mano","age":26,"interest":"Cars","d":4,"name":"Onam"}
print(dict1)

# Editing in dictionary
dict3 = {"name":"Skur","age":21,"interest":"Cars"}
dict3["interest"]="Bikes"
print(dict3)

# Duplicate Values
dict4 = {"name":["Mano","Skur"],"age":26,"interest":["Cars","Cooking"]}
print(dict4)

# Tuple inside list
print(dict4.items()) # ([('name', ['Mano', 'Skur']), ('age', 26), ('interest', ['Cars', 'Cooking'])])

# Print all keys, values
print(dict4.keys())
print(dict4.values())

# add an element in dictionary
dict4["food"]="Dahiwada"
print(dict4)


# Removing key value
dict4.pop('interest')
print(dict4)

# Deleting last item
dict4.popitem() # will remove 'food': 'Dahiwada'
print(dict4)

# Merging/Updating 2 dictionaries
frutDict = {"fruit":"apple","food":"Paneer"}
dict4.update(frutDict)
print("Update",dict4)
