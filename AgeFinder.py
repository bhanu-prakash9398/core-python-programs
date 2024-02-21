
age = int(input("Enter your Age:"))
if age <= 5:
    print("Kid")
elif age > 6 and age <=10:
    print("Too young")
elif age > 10 and age <=20:
    print("young")
elif age > 20 and age <=30:
    print("Teen")
elif age > 30 and age <=50:
    print("Middle age")
elif age > 50 and age <=70:
    print("Old")
else:
    print("Death")
print("===========================")

# number finder
number=int(input("enter your number:"))
if number <=10000:
    print ("below ten thousand")
elif number >11000 and number <15000:
    print ("below 15000")
elif number>16000 and number <20000:
    print ("below 20000")
elif number>21000 and number <25000:
    print ("below 25000")
else:
    print("above 25000")