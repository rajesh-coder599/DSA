#if-else statement

#nesting
i = int(input("enter a random number: "))
j=4
if(i==j):
    print("you guess it right")
    k=int(input("guess again: "))
    random=7
    if(k==random):
        print("you made a wining streek")
    else:
        print("try again")
else:
    print("try again")
#leader
a=float(input("enter your overall percentage: "))
if a>=90:
    print("exelent")
elif a>=70:
    print("good")
elif a>=50:
    print("fair")
else:
    print("bad")

temp=float(input("enter temperature: "))
if temp>50:
    print("extremly hot")
elif temp<=50 and temp>=25:
    print("hot")
elif temp<=24 and temp>=10:
    print("cold")
else:
    print("extremly cold")


#Ternery operator
age = int(input("enter your age: "))
result = "eligible" if age>=18 else "not eligible"
print(result)