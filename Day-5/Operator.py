'''
Operators -> Arithmetic Operator - +, -, *, /, //, **, %
          -> Assignment operator - =, +=, -=, *=, %=, //=, /=
          -> Conditional operator - ==, !=, >, < <, >=, <=
          -> Logical operator - and, or, not 
          -> Member operator - in, not in
          -> Identity operator - is, is not
'''

x=11
y=30

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(y/x)
print("floor",y//x)
print("mod",y%x)
print(y**x)

x+=4
print(x)

check = "abc"
Check = "ABC"
CHECK = "abc"

print(check==Check)
print(check==CHECK)
print(check!=Check)

dict_1 = {"stock": [10,20,33], "products": "fruits", "sales": 30991}
print("stock" in dict_1)  
print("fruits" in dict_1)  # search for keys only
print("fruits" in dict_1.values())


'''
Memory Management -> Two primary types of memory allocation are stack memory and heap memory.
                    Stack memory is a region of memory that operates in a Last-In-First-Out (LIFO) 
                    manner. It is used for storing local variables, function arguments, and control
                    information such as return addresses. The allocation and deallocation of stack 
                    memory are managed automatically by the compiler, making it a temporary memory 
                    allocation scheme. 
                    Stack memory allocation is faster due to its contiguous nature.
                    Stack memory is generally smaller compared to heap memory
                    
                    Heap memory is a region of memory used for dynamic memory allocation. Unlike
                    stack memory, heap memory does not follow any specific order and is managed 
                    manually by the programmer. It is used for storing objects and data structures 
                    that require dynamic lifetimes.
'''

x=5
y=10
z=5

'''
Each time we declare a variable 2 farmes are created Global and local frame
x,y,z are stored in global frame and the number 5,10 are stored in local frames whose memory 
reference is stored in x,y and z
Global frame uses Stack memory and local frames uses Heap memory
'''

print(id(x))
print(id(y))
print(id(z))

print(x is y)
print(y is z)
print(x is z)

a =["Mano", 26]
b =["Mano", 76]
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))

'''As Primitive data types are immutable having same values will result in same memory locations.
In Non-primitive data types like list and tuple having same values will result in same memory 
location if they contain primitive values in  them.'''
