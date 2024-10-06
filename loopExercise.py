#Find the sum of first 10 natural nos (1-10)
# result = 0
# for i in range(1,11):
#     result = result + i
# print(result)

#Find the sum of digits of number
#=> 128 -> 1+2+8 = 11
'''
x = int(input("Enter No : "))
res = 0
for i in range(len(str(x))):
    rem = x%10
    res = res+rem
    x = x//10
print(res)
'''
#print first 10 nos of fibonacci series
# 0 1 1 2 3 5 8 13.....
'''
first = 0
second= 1
print(first)
print(second)
for i in range(8):
    third = first + second
    print(third)
    first = second
    second = third
'''
#break and continue
#break statement is used to exit the loop
'''
for i in range(1,1000000000000):
    if i>10:
        break
    print(i)
'''
#Continue - it is used to skip the current iteration
'''
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
    print("********")
'''
'''
x = int(input("Enter No : "))
for i in range(1,11):
    print(f"{x}X{i} = {x*i}")
'''
#Take a number as input and check whether is prime or not
# 2,3,5,7,11,13,19.....
'''
x = int(input("Enter No : "))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
'''
#Nested For Loop

'''
for i in range(0,4):
    for j in range(1,4):
        print(i,j)

'''
'''
for i in range(1,4):
    for j in range(0,i):
        print(i,j)
'''
'''
*
**
***
****
*****
'''
x = 1
for i in range(1,6):
    for j in range(i):
       if x%2==0:
         print(0,end="")
       else:
          print(1,end="")
       x+=1
    print()#next line
'''
1
12
123
1234
12345

1
22
333
4444
55555

1
01
010
1010
10101
'''

















































































