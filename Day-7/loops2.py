'''
Range -> Syntax-> range(start,end+1,jumps)
we can access range via loops
'''
for i in range(1,11):
    print(f"The numbers are {i}")

# Table of 2
for i in range(2,21,2):
    print(i)

for i in range(1,11):
    print(f"2x{i}={2*i}")

'''
Enumerate -> helps in finding index position which prints the ans in the tuple where 1st item 
is index  and 2nd is object
'''
list_1 = [10,20,40,90,54]

for i in enumerate(list_1):
    print(i) # (index,list items)
    print(i[0]) # all the indexes
    print(i[1]) # all the items

'''
Zip -> helps to loop 2 or more iterative at the same time
'''

list_87 = [1,2,3,4]
list_88 = [9,8,5,7]

for i,j in zip(list_87,list_88):
    print(f"For list 87 values are {i},For list 87 values are {j}")

'''
listV=[1,3,4,5]
listY=[2,3,4,5]
o/p-[3,6,8,10]
'''
listV=[1,3,4,5]
listY=[2,3,4,5]
ansList =[]
for i,j in zip(listV,listY):
    ansList.append(i+j)

print(ansList)

# Calculate the cube of all the numbers from 1 to a given number

num=int(input("Enter the number till which the cube to be calculated: "))

for i in range(1,num+1):
    print(f"The cube of {i} is {i**3}")