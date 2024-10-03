Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String
x = "Hey.....How are you?"
type(x)
<class 'str'>
x = 'Hey.....How are you?'
type(x)
<class 'str'>
x = '"Python" is a High Level Programming Language'
print(x)
"Python" is a High Level Programming Language
x = ""Python" is a High Level Programming Language""
SyntaxError: unterminated string literal (detected at line 1)
x = "\"Python\" is a High Level Programming Language""
SyntaxError: unterminated string literal (detected at line 1)
x = "\"Python\" is a High Level Programming Language"
#\ - escape character
print(x)
"Python" is a High Level Programming Language
x = "Python is a Programming Language.\nPython is General Purpose"
print(x)
Python is a Programming Language.
Python is General Purpose
#\n - next line
x = "hello\tPython"#\t - one tab space
print(x)
hello	Python
x = "Hello Python"
len(x)#it will return no of characters in a string including space also
12
len(x)
12
x = "Python"
x[0]#indexing
'P'
x[2]
't'
x[-1]
'n'
x[-2]
'o'
#Slicing - Extracting a sub String of Given String
x = "hello welcome to Python's Class"
x[0:5]
'hello'
x[0:5:1]
'hello'
x[0:5:2]
'hlo'
x[:5]#byt default it will starts from zero
'hello'
x[6:]#it will move to last
"welcome to Python's Class"
x[0:]
"hello welcome to Python's Class"
x[:]
"hello welcome to Python's Class"
x[::1]
"hello welcome to Python's Class"
x[::-1]#rightToLeft
"ssalC s'nohtyP ot emoclew olleh"
x[::-2]
'saCsnhy teolwolh'

x = "hello"
x[::-2]
'olh'
x
'hello'
x = "Welcome to PYTHON PRogramming"
#String formatting functions
x
'Welcome to PYTHON PRogramming'
x.lower()
'welcome to python programming'
x.upper()
'WELCOME TO PYTHON PROGRAMMING'
x.capitalize()#first character of String will be Capital
'Welcome to python programming'
x.title()
'Welcome To Python Programming'
x.swapcase()
'wELCOME TO python prOGRAMMING'
#String is immutable
print(x)
Welcome to PYTHON PRogramming

x = [1,2,3]
x.append(5)
x
[1, 2, 3, 5]
x
[1, 2, 3, 5]
x[0]=100
x
[100, 2, 3, 5]
x = "hello"
>>> x[0] = "H"
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    x[0] = "H"
TypeError: 'str' object does not support item assignment
>>> x
'hello'
>>> x[1:]
'ello'
>>> x
'hello'
>>> #String cannot be changed but can be overriden
>>> x
'hello'
>>> x[1:]
'ello'
>>> x = x[1:]
>>> x
'ello'
