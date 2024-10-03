#Conditional Statements
#  if Statement
# take a no as input and check whether a number is even or odd
# num = int(input("Enter No : "))
# # == ->equality operator
# if num%2==0:
#     print("even")
# else:
#     print("odd")

#Find largest b/w two nos
# num1 = int(input("Enter No1:"))
# num2 = int(input("Enter No2:"))

# if num1 > num2:
#     print(f"{num1} is largest")
# else:
#     print(f"{num2} is largest")

#Find Largest b/w three nos
'''
num1 = int(input("Enter No1:"))
num2 = int(input("Enter No2:"))
num3 = int(input("Enter No3:"))

# if num2 < num1 > num3:

if num1 > num2 and num1 > num3:
    print(f"{num1} is largest")
elif num2>num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")
'''
# Nested IF Statement
# Take value of side1,side2,side3 as input and if they form a traingle,
#which traingle is it - equilateral/isoceles/scalene
side1 = int(input("Enter Side1:"))
side2 = int(input("Enter Side2:"))
side3 = int(input("Enter Side3:"))

#Sum of two sides of Traingle is always greater than the 3rd side.
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    if side1 == side2 and side2==side3:
        print("Equilateral Traingle")
    elif side1==side2 or side2==side3 or side3==side1:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Sides are incompatible to form a traingle")