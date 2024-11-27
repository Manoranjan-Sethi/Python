'''
1. Calculate electricity bill
0-100 charge - 7rs/unit
100-200 charge - 10rs/unit
200 - 16rs/unit
'''
units=int(input("Enter the unit : "))

if units>0 and units<=100:
    bill= units*7
    print("The amount is " ,bill)

elif units>100 and units<=200:
    bill=100*7+(units-100)*10
    print("The amount is " ,bill)

else:
    bill=100*7+100*10+(units-200)*16
    print("The amount is " ,bill)

# Code Optimisation

if units>0 and units<=100:
    bill= units*7

elif units>100 and units<=200:
    bill=100*7+(units-100)*10

else:
    bill=100*7+100*10+(units-200)*16

print("The amount is " ,bill)

'''
2. Road tax calculator:
vehicle price < 100000 -> 5% of vehicle price
between 100000 to 200000  ->10% of vehicle price
greater than 200000  —>12.5% of vehicle price
'''

price = int(input("Enter vehicle price :"))
if price<100000:
    amt=5/100*price

elif price>=100000 and price<200000:
    amt=10/100*price

else:
    amt=12.5/100*price

print("The road tax is " ,amt)

