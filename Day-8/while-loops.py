'''
While loops 

Syntax->
while condition:
    block of code
    ...
    statement that make the condtion false.

Disadvantage of While
    -> Infinite looping
    -> Dont know the number of iteration
    -> Exit statement required to come out of loop
'''

x=10

while x<=15:
    print(x)
    x+=1


# Print sum of all the untill user enters the number 0

num=int(input("Enter the number : "))
sum=0
while num!=0:
    sum+=num
    num=int(input("Enter another number : "))  #exit statement
print(sum)

# for else and while else

list1=[10,20,80,60,18]

for i in list1:
    print(i)

else:
    print("Hello")  #else block is only going to run when the loop completes all of its iteration