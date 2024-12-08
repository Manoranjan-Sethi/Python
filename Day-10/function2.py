# 1. write a program that accepts a string and couts the number of upper and lower case letters.

# Normal type
def upperLower(str):
    upperCounter=0
    lowerCounter=0
    for i in str:
        if i.isupper():
            upperCounter+=1
        elif i.islower():
            lowerCounter+=1
        else:
            pass

    print(f"The upper count is {upperCounter} and lower count is {lowerCounter}")

upperLower("This is APPOLO")

# using dictionary

def upperLower(str):
    dictString ={"upperCounter":0,"lowerCounter":0}
    for i in str:
        if i.isupper():
            dictString["upperCounter"]+=1
        elif i.islower():
            dictString["lowerCounter"]+=1
        else:
            pass

    print(f"The upper count is {dictString["upperCounter"]} and lower count is {dictString["lowerCounter"]}")

upperLower("This is APPOLO")

# 2. write a python function that takes a list and returns a new list with distinct elements
# i/p-> [1,2,3,3,4,4,78,78,5]
# o/p-> [1,2,3,4,78,5]

list1=[1,2,3,3,4,4,78,78,5]
uniqueList=[]
count=0

for i in list1:
    for j in list1:
        if i!=j+2:
            # uniqueList.append(j)
            print(j)
# print(uniqueList)