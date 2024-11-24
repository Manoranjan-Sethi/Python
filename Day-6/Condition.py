# 1. Divisible by a number

num=121

if num%11==0:
    print("Number is divisible by 11")
else:
    print("Number is not divisible by 11")

# 2. odd or even numbers

num = 128
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

# 3. Find last digit

num = 555
if num%10==0:
    print("Last digit is 0")
else:
    print("Last digit is not 0")

# 4. last alphabet of string is vowel letter or not

str = "water"

vowel_letter = "aeiou"
if  str[-1] in vowel_letter:
    print("Vowel letter is present")
else:
    print("Vowel letter is not present")

# 5. If without Else
if  str[-1] in vowel_letter:
    print("Vowel letter is present")
'''OR'''
if  str[-1] in vowel_letter:
    print("Vowel letter is present")
else:()

'''Taking Input form User'''

x = input("Enter your string to check: ") 
a=int(input("Enter yout number: ")) # string will convert into integer

vowel_letter = "aeiou"
if  x [-1] in vowel_letter:
    print("Vowel letter is present")
else:
    print("Vowel letter is not present")