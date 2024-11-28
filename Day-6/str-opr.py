str_1="Hey, are you there?"

print(str_1[-1])

str_1.upper()
print(str_1)

str_1.lower()
print(str_1)

x_list=str_1.split(" ")
print(x_list)

str_1.replace("Hey,","Hello")
print(str_1)

list_1=["I","love","to","eat","apples"]
listJoin=(" ").join(list_1)
print(listJoin)

str_2="I love to play badminton"
print(str_2.endswith("ton"))
print(str_2.endswith("badminton"))
print(str_2.endswith("I love"))

print("123456".isdigit())

print("1234"*5)

''' 
Email validation check:

if email add is valid by first checking if its not empty
Then check if it contains an "@" symbol
finally check if it ends .com or .in
'''
email = "example@gmail.com"

if not email:
    print("Invalid: Email is empty.")

elif "@" not in email:
    print("Invalid: Email must contain an '@' symbol.")

elif email.endswith(".com") or email.endswith(".in"):
    print("Valid email address.")
else:
    print("Invalid: Email must end with '.com' or '.in'.")



