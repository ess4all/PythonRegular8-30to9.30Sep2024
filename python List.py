Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#List - List is Python's ordered and mutable data collection
#ordered - indexing
#mutable - changable - update,insert,delete
x = [1,34.45,"hey",True]
type(x)
<class 'list'>
x
[1, 34.45, 'hey', True]
x.append(99)#it will insert value at the end of the list
x
[1, 34.45, 'hey', True, 99]
x.append(8)
x
[1, 34.45, 'hey', True, 99, 8]
x.insert(0,-10)
x
[-10, 1, 34.45, 'hey', True, 99, 8]
x
[-10, 1, 34.45, 'hey', True, 99, 8]
x[0]="Hello"
x
['Hello', 1, 34.45, 'hey', True, 99, 8]
x
['Hello', 1, 34.45, 'hey', True, 99, 8]
x.pop()#it will remove then last value
8
x
['Hello', 1, 34.45, 'hey', True, 99]
x.pop(0)#remove by index
'Hello'
x
[1, 34.45, 'hey', True, 99]
x = "hello how are you"
x.count(" ")
3
x = ['Hello', 1, 34.45, 'hey', True, 99, 8]
x.remove("Hello")
x
[1, 34.45, 'hey', True, 99, 8]
del x[-1]
x
[1, 34.45, 'hey', True, 99]
x = [1,2,3,-10,3,34,0]
x.sort()#ascending order
x
[-10, 0, 1, 2, 3, 3, 34]
x.sort(reverse=True)#descending order
x
[34, 3, 3, 2, 1, 0, -10]
sum(x)
33
len(x)
7
