'''
def f1():
    def f2():
        print("f2 called...")
    def f3():
        print("f3 called...")
    return f2,f3

f1()[0]()
'''
'''
def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

def div(x,y):
    print(x/y)

x= int(input("enter number x : "))
y= int(input("enter number y : "))
choice = input("Enter Choice (+,-,/,*) : ")
i={"+":add,"-":sub,"*":mul,"/":div}
i.get(choice)(x,y)
'''
'''
if choice == "+":
    add(x,y)
elif choice == "-":
    sub(x,y)
elif choice == "*":
    mul(x,y)
elif choice == "/":
    div(x,y)
else:
    print("Invalid operation")
'''
'''
def calc(x,choice,y):
    print(eval(x+choice+y))

x= input("enter number x : ")
y= input("enter number y : ")
choice = input("Enter Choice (+,-,/,*) : ")
calc(x,choice,y)
'''
'''
def calc(x,choice,y):
    print(eval(x+choice+y))
x=input("enter number x:")
y=input("enter number y:")
choice=input("enter choice (+,-,*,/) :")
calc(x,choice,y)
'''
'''
x=int(input("enter number x :"))
y=int(input("enter number y :"))
choice=input("enter choice (+,-,*,/):")
i={"+":add,"-":sub,"*":mul,"/":div}
i.get(choice)(x,y)
'''
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):c
    print(x*y)
def div(x,y):
    print(x/y)


def calc(x,choice,y):
    print(eval(x+choice+y))
x=input("enter number x:")
y=input("enter number y:")
choice=input("enter choice (+,-,*,/):")
calc(x,choice,y)
