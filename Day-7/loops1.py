# For Loops

set1={10,11,12,13,14,15,16,17, "apple", 98, "tiger"}
print("Set")
for i in set1:
    print(i)

list1 = [1,2,3,4,5,6,7,8]
print("List")
for i in list1:
    print(i)

dict1 = {"name": "Mano", "age": 26, "hobby": "singing"}
print("Dict Keys")
for i in dict1:
    print(i)

print("Dict values")
for i in dict1.values():
    print(i)

print("Dict Items")
for i in dict1.items():
    print(i)

str="Hello There"
print("String")
for i in str:
    print(i) # output in single line

'''
i/p-list_str=["apple","cat","mouse","banana"]
o/p-["e","t","e","a"]
'''
list_str=["apple","cat","mouse","banana"]
ans =[] # to append to list
for words in list_str:
    ans.append(words[-1])
print(ans) 

dict1 ={} # to append to dictionary 
for i in list_str:
    dict1[i] = i[-1]
print(dict1)

'''
find sq root of all values of dictionary
dict2={"val1": 12 , "val22" : 23, "val3" : 78}
'''
dict2={"val1": 12 , "val22" : 23, "val3" : 78}
list2=[]
for i in dict2.values():
    list2.append(i**2)
print(list2)

# Reverse string
str11 = "ball"
strRev=str11[::-1]
revStr=""
for i in strRev:
    revStr+=i
print(revStr)

# write a python program that accepts a string and calculate the number of digits in it.

str14=input("Enter your Digits : ")
count=0
for i in str14:
    if i.isdigit()==True:
        count+=1
print(count)

# write a python program that print the number of days for the month entered by user.

month = input("Enter Month : ")
list31=["January","March","May","July","August","October","December"]
list30=["April","June","September","November"]


if month.title() in list30: 
    print(f"{month} month has 30 days")
elif month.title() in list31:
    print(f"{month} month has 31 days")
elif month.title()=="February":
    print(f"{month} has 28 days")
else:
    print(f"{month} not a valid month")


