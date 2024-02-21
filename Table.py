
def mulitplicationTable(a):
    for i in range(1,11):
        print(f"{i} * {a} = {a*i}")

def additionTable(b):
    for i in range(1,11):
        print(f"{i} + {b} = {b+i}")

def subtractionTable(c):
    for i in range(1,11):
        print(f"{c} - {i} = {c-i}")

num = int(input("Enter your number:"))
mulitplicationTable(num)
print("===================")
additionTable(num)
print("===================")
subtractionTable(num)


def summa(name, className, sub, reg):
    print(sub)
    print(reg)
    print(name)
    print(className)

summa("raja", "class1", "math", 1)
summa(reg=1, sub="math", className="class1", name="raja")
summa("raja", "class1", sub="math", reg=1)

print("=======")

def multiplicationTable(b):
    for i in range(1,11):
        print(f"{b} * {i} = {b*i}")

def additionTable(h):
    for i in range(1,11):
        print(f"{h} + {i}= {h+i}")

def subtractionTable(p):
    for j in range(1,11):
        print(f"{j} - {p} = {p-j}")

number= int(input("enter your number:"))
subtractionTable(number)


def prince_of_mollywood(name,movies,movielist,sno):
    print(sno)
    print(name)
    print(movies)
    print(movielist)

prince_of_mollywood(sno=1,name="dulquarSalmon", movies="charlie",movielist=3)

