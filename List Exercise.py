
# x = [110,12,500,1300]
# let the first element of list is largest
# largest = x[0]

# for i in range(1,len(x)):
#     if x[i]>largest:
#         largest = x[i]
# print(largest)
#find the largest element from the List without using any List function
#Find Second largest element from the list without using any  List function

#take a no as input and check whether the no is present in our given list or not...
# If present Print "Found" else "not found"
'''
x = [1,345,645,7,345,34]
num = int(input("Enter no : ")) 
'''
'''
for i in range(len(x)):
    if num==x[i]:
        print("Found")
        break
else:
    print("Not Found")    
'''
'''
if num in x:
    print("Found")
else:
    print("Not Found")
'''
'''
for i in range(len(x)):
    if x[i]-num==0:
        print("Found")
        break
else:
    print("Not Found")  
'''

# temp = input("Enter Temp in C or F")
# if temp.endswith("C"):
#     temp = int(temp[:-1])
#     print(temp)
#     res = (temp*9/5)+32
#     print(f"{res} F")
# elif temp.endswith("F"):
#     temp = int(temp[:-1])
#     res = (temp-32)*5/9
#     print(f"{res} C")

#Sort the List in Ascending Order without using sort function .
x = [1,-10,20,100,500,0]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            # swapping->exchanging the value of variables
            x[i],x[j]=x[j],x[i]

print(x)
