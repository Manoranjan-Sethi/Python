# 1. If a number is Prime Number 

num=int(input("Enter the number to check for Prime : "))
if num<2:
    print("Cannot check for this number")
else:
    for i in range(2,num):
        if num%i==0:
            print ("Not Prime Number")
            break
    else:
        print ("Prime Number")

# 2. Accept number from user and print prime number within the range

start=int(input("Enter the starting number for the range: "))
end=int(input("Enter the ending number for the range: "))

if start>end:
    print("This is not possible")
else:
    print(f"Prime Numbers between {start} and {end} are as follows:-")
    for num in range(start,end+1):
        if num<2:
            continue
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

# 3. Add 2 Lists

list_1 = [10,20,30,40]
list_2 = [50,60,70,80]

list_ans =[]
for i,j in zip(list_1,list_2): 
    list_ans.append(i+j)

print(list_ans)

"""
comprehension is a way of writing down the python programs within a single line while converting 
the output into the desired data type

Two types of comprehensions:
1. list
2. dict
"""
# syntax -> name=[ans for loop]
# Iteration
list_itr = [i for i in range(1,6)]
print(list_itr)

list_add=[i+j for i,j in zip(list_1,list_2)]
print(list_add)

# if statement with comprehension 
a = [i for i in range(2,30,3) if i%2==0]
print(a)

# 4. print all the numbers starting from 4 ending at 24 and in the reverse order but do not print 
# the numbers which are divisible by 4

ans2=[i for i in range(2,25) if i%4!=0]
ans2.reverse()
print(ans2)

"""
Comprehension if else
"""
# 5. Given list of string if the string is starting with a vowel print 1 else print 0

list_str1=["abc","xyz","efg","bad","good"]
ans3=[1 if i[0] in "aeiou" else 0 for i in list_str1]
print(ans3)
print(ans3.count(0)) # to count the number of 0s
