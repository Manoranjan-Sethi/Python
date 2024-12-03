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

num=int(input("Enter the number to check for Prime : "))

if num<2:
    print("Cannot check for this number")
else:
    for i in range(2,num):
        for j in num:
            print(f"i={i},j={j}")


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
