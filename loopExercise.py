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

x = int(input("Enter No : "))
for i in range(1,11):
    print(f"{x}X{i} = {x*i}")
