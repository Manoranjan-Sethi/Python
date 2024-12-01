# Break

list_1=[10,20,30,40,50]

for i in list_1:
    if i==40:
        break
    print(i)
    print("Hello")

print("End")

# Continue (Skip)

list_1=[10,20,30,40,50]

for i in list_1:
    if i==40:
        continue
    print(i)
    print("Hello")

print("End")

# Pass -> helps to bypass syntax errors

x=12
if x==10:
    pass

